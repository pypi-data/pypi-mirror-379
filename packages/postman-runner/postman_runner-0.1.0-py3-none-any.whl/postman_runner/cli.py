from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

from .collection_parser import find_request, list_request_names, load_collection
from .environment import apply_environment, apply_environment_to_data, load_environment
from .executor import DEFAULT_TIMEOUT, execute_request
from .models import BodySpecification, RequestPayload
from .test_runner import execute_tests, render_results


def main(argv: Optional[list[str]] = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.list:
        if not args.collection:
            parser.error("--list requires --collection")
        collection = load_collection(args.collection)
        for name in list_request_names(collection):
            print(name)
        return 0

    environment_variables: Dict[str, str] = {}
    environment_path = _determine_environment_path(args.environment, args.collection)
    if environment_path:
        environment_variables = load_environment(environment_path)
        print(f"Using environment: {environment_path.name}")

    payload: RequestPayload
    if args.inline or args.inline_file:
        if args.collection or args.request_name:
            parser.error("--inline/--inline-file cannot be combined with --collection/--request-name")
        payload = _load_inline_payload(args.inline, args.inline_file)
    else:
        if not args.collection or not args.request_name:
            parser.error("--collection and --request-name are required unless using --inline or --inline-file")
        collection = load_collection(args.collection)
        try:
            payload = find_request(collection, args.request_name)
        except KeyError as exc:
            available = list_request_names(collection)
            message = f"{exc}. Available requests: {', '.join(available)}" if available else str(exc)
            raise SystemExit(message) from exc

    payload = apply_environment(payload, environment_variables)

    additional_assertions: Dict[str, Any] = {}
    if args.assert_json:
        try:
            additional_assertions = json.loads(args.assert_json.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise SystemExit(f"Could not parse assertion file: {exc}") from exc
        if not isinstance(additional_assertions, dict):
            raise SystemExit("Assertion JSON must be an object of key/value pairs")
        additional_assertions = apply_environment_to_data(additional_assertions, environment_variables)

    merged_assertions = dict(payload.assertions)
    merged_assertions.update(additional_assertions)

    response = execute_request(payload, timeout=args.timeout)

    print(f"Status: {response.status_code}")
    print("Headers:")
    for header, value in response.headers.items():
        print(f"  {header}: {value}")
    print("Body:")
    print(response.text)

    if merged_assertions:
        results, passed = execute_tests(response, merged_assertions)
        print(render_results(results))
        return 0 if passed else 1

    return 0


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Local Postman collection runner")
    parser.add_argument("--collection", type=Path, help="Path to Postman collection (JSON)")
    parser.add_argument("--request-name", help="Name of the request to execute")
    parser.add_argument("--inline", help="Inline JSON payload describing the request")
    parser.add_argument("--inline-file", type=Path, help="Path to JSON file describing the request")
    parser.add_argument("--assert-json", type=Path, help="Path to JSON file containing extra assertions")
    parser.add_argument(
        "--environment",
        type=Path,
        help=(
            "Path to a Postman environment file or directory containing environment files. "
            "If omitted, environment files in the collection directory are discovered automatically."
        ),
    )
    parser.add_argument("--timeout", type=float, default=DEFAULT_TIMEOUT, help="Request timeout in seconds")
    parser.add_argument("--list", action="store_true", help="List requests available in the collection")
    return parser


def _determine_environment_path(environment: Optional[Path], collection: Optional[Path]) -> Optional[Path]:
    if environment:
        if not environment.exists():
            raise SystemExit(f"Environment path '{environment}' does not exist")
        if environment.is_file():
            return environment
        if environment.is_dir():
            candidates = _list_environment_files(environment)
            selected = _prompt_environment_selection(candidates, allow_skip=False)
            if selected is None:
                raise SystemExit("No environment selected")
            return selected
        raise SystemExit(f"Environment path '{environment}' must be a file or directory")

    if collection:
        candidates = _list_environment_files(collection.parent)
        return _prompt_environment_selection(candidates, allow_skip=True)

    return None


def _list_environment_files(directory: Path) -> List[Path]:
    if not directory.exists() or not directory.is_dir():
        return []

    patterns = ["*.postman_environment.json", "*environment*.json"]
    results: List[Path] = []
    seen = set()
    for pattern in patterns:
        for candidate in sorted(directory.glob(pattern)):
            if candidate.is_file() and candidate not in seen:
                results.append(candidate)
                seen.add(candidate)
    return results


def _prompt_environment_selection(candidates: List[Path], allow_skip: bool) -> Optional[Path]:
    if not candidates:
        if not allow_skip:
            raise SystemExit("No environment files found")
        if not sys.stdin.isatty():
            return None
        response = input("Enter path to environment file (press Enter to skip): ").strip()
        if not response:
            return None
        candidate = Path(response).expanduser()
        if not candidate.exists() or not candidate.is_file():
            raise SystemExit(f"Environment file '{candidate}' not found or is not a file")
        return candidate

    if len(candidates) == 1:
        return candidates[0]

    if not sys.stdin.isatty():
        raise SystemExit("Multiple environment files found. Re-run with --environment to select one.")

    print("Available environments:")
    for index, candidate in enumerate(candidates, start=1):
        print(f"  {index}. {candidate.name}")

    while True:
        prompt = f"Select environment [1-{len(candidates)}]"
        if allow_skip:
            prompt += " (press Enter to skip)"
        prompt += ": "
        selection = input(prompt).strip()
        if not selection:
            if allow_skip:
                return None
            selection = "1"
        try:
            index = int(selection)
        except ValueError:
            print("Invalid selection. Please enter a number.")
            continue
        if 1 <= index <= len(candidates):
            return candidates[index - 1]
        print("Selection out of range. Try again.")


def _load_inline_payload(inline: Optional[str], inline_file: Optional[Path]) -> RequestPayload:
    source: Dict[str, Any]
    if inline_file:
        try:
            source = json.loads(inline_file.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise SystemExit(f"Could not parse inline file: {exc}") from exc
    else:
        if not inline:
            raise SystemExit("Inline JSON string is empty")
        try:
            source = json.loads(inline)
        except json.JSONDecodeError as exc:
            raise SystemExit(f"Could not parse inline JSON: {exc}") from exc
    return _inline_dict_to_payload(source)


def _inline_dict_to_payload(data: Dict[str, Any]) -> RequestPayload:
    required = {"url", "method"}
    missing = required - data.keys()
    if missing:
        raise SystemExit(f"Inline request is missing keys: {', '.join(sorted(missing))}")

    headers = {str(key): str(value) for key, value in data.get("headers", {}).items()}
    body_spec = BodySpecification()
    raw_body: Optional[str] = None

    if "body" in data and data["body"] is not None:
        body_spec.mode = "raw"
        if isinstance(data["body"], (dict, list)):
            raw_body = json.dumps(data["body"])
            if not _has_header(headers, "content-type"):
                headers["Content-Type"] = "application/json"
        else:
            raw_body = str(data["body"])
        body_spec.raw = raw_body

    assertions = data.get("assertions", {})
    if assertions and not isinstance(assertions, dict):
        raise SystemExit("Inline assertions must be a dictionary of key/value pairs")

    return RequestPayload(
        name=data.get("name", "inline"),
        method=str(data["method"]).upper(),
        url=str(data["url"]),
        headers=headers,
        body=body_spec,
        assertions=assertions or {},
    )


def _has_header(headers: Dict[str, str], name: str) -> bool:
    name_lower = name.lower()
    return any(key.lower() == name_lower for key in headers)


if __name__ == "__main__":
    sys.exit(main())
