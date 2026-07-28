#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import io
import json
import platform
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
from typing import Any, Callable

import jsonschema
import yaml
from jsonschema import Draft202012Validator
from yaml.tokens import AliasToken, AnchorToken

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "dist/QA-LIVRE-V-CH13-FORMATS.json"
SAFE_INTEGER_MAX = 9_007_199_254_740_991


class ExpectedFailureNotRaised(AssertionError):
    pass


def package_version(name: str) -> str:
    try:
        return version(name)
    except PackageNotFoundError:
        return "unknown"


def reject_duplicate_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate member: {key}")
        result[key] = value
    return result


def reject_constant(value: str) -> None:
    raise ValueError(f"non-finite number: {value}")


def strict_json_loads(text: str) -> Any:
    return json.loads(
        text,
        object_pairs_hook=reject_duplicate_pairs,
        parse_constant=reject_constant,
    )


def expect_raises(exc_type: type[BaseException], action: Callable[[], Any]) -> None:
    try:
        action()
    except exc_type:
        return
    raise ExpectedFailureNotRaised(f"{exc_type.__name__} was not raised")


def parse_jsonl(text: str) -> list[Any]:
    records: list[Any] = []
    for line_number, raw_line in enumerate(text.splitlines(), start=1):
        if not raw_line.strip():
            raise ValueError(f"blank line at record {line_number}")
        records.append(strict_json_loads(raw_line))
    return records


def formula_like(cell: str) -> bool:
    return bool(cell) and cell[0] in ("=", "+", "-", "@")


def canonical_json_bytes(value: Any) -> bytes:
    text = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    )
    return (text + "\n").encode("utf-8")


SCHEMA: dict[str, Any] = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://example.invalid/schemas/asteria-item-v1.schema.json",
    "type": "object",
    "additionalProperties": False,
    "required": ["format", "format_version", "id", "count"],
    "properties": {
        "format": {"const": "asteria-item"},
        "format_version": {"const": 1},
        "id": {"type": "string", "pattern": "^[a-z][a-z0-9]*(\\.[a-z][a-z0-9_-]*)+$"},
        "count": {
            "type": "integer",
            "minimum": 0,
            "maximum": SAFE_INTEGER_MAX,
        },
    },
}


CASES: list[tuple[str, Callable[[], None]]] = []


def case(name: str) -> Callable[[Callable[[], None]], Callable[[], None]]:
    def register(function: Callable[[], None]) -> Callable[[], None]:
        CASES.append((name, function))
        return function
    return register


@case("json.strict.valid")
def _() -> None:
    value = strict_json_loads('{"format":"asteria-item","format_version":1,"id":"item.iron"}')
    assert value["format_version"] == 1


@case("json.syntax.invalid")
def _() -> None:
    expect_raises(json.JSONDecodeError, lambda: strict_json_loads("{format:'asteria-item',}"))


@case("json.duplicate.rejected")
def _() -> None:
    expect_raises(ValueError, lambda: strict_json_loads('{"id":"a","id":"b"}'))


@case("json.nan.rejected")
def _() -> None:
    expect_raises(ValueError, lambda: strict_json_loads('{"weight":NaN}'))


@case("json.top_level_scalar.accepted")
def _() -> None:
    assert strict_json_loads("42") == 42


@case("json.concatenation.rejected")
def _() -> None:
    expect_raises(json.JSONDecodeError, lambda: strict_json_loads('{"a":1}{"b":2}'))


@case("schema.2020_12.valid")
def _() -> None:
    Draft202012Validator.check_schema(SCHEMA)
    Draft202012Validator(SCHEMA).validate(
        {"format": "asteria-item", "format_version": 1, "id": "item.iron", "count": 2}
    )


@case("schema.version_string.rejected")
def _() -> None:
    validator = Draft202012Validator(SCHEMA)
    expect_raises(
        jsonschema.ValidationError,
        lambda: validator.validate(
            {"format": "asteria-item", "format_version": "1", "id": "item.iron", "count": 2}
        ),
    )


@case("schema.additional_property.rejected")
def _() -> None:
    validator = Draft202012Validator(SCHEMA)
    expect_raises(
        jsonschema.ValidationError,
        lambda: validator.validate(
            {
                "format": "asteria-item",
                "format_version": 1,
                "id": "item.iron",
                "count": 2,
                "unknown": True,
            }
        ),
    )


@case("schema.unsafe_integer.rejected")
def _() -> None:
    validator = Draft202012Validator(SCHEMA)
    expect_raises(
        jsonschema.ValidationError,
        lambda: validator.validate(
            {
                "format": "asteria-item",
                "format_version": 1,
                "id": "item.iron",
                "count": SAFE_INTEGER_MAX + 1,
            }
        ),
    )


@case("jsonl.two_records")
def _() -> None:
    records = parse_jsonl('{"id":"a"}\n{"id":"b"}\n')
    assert [record["id"] for record in records] == ["a", "b"]


@case("jsonl.blank_line.rejected")
def _() -> None:
    expect_raises(ValueError, lambda: parse_jsonl('{"id":"a"}\n\n{"id":"b"}\n'))


@case("jsonl.pretty_print.rejected")
def _() -> None:
    expect_raises(json.JSONDecodeError, lambda: parse_jsonl('{\n  "id": "a"\n}\n'))


@case("jsonl.record_separator.rejected")
def _() -> None:
    # str.splitlines() recognizes U+001E as a boundary. The project profile still
    # rejects the record before JSON parsing because it creates an empty record.
    expect_raises(ValueError, lambda: parse_jsonl('\x1e{"id":"a"}\n'))


@case("csv.quoted_comma")
def _() -> None:
    rows = list(csv.reader(io.StringIO('id,name\r\nitem.iron,"Marteau, fer"\r\n', newline="")))
    assert rows[1] == ["item.iron", "Marteau, fer"]


@case("csv.multiline_record")
def _() -> None:
    rows = list(csv.reader(io.StringIO('id,note\r\nitem.note,"ligne 1\nligne 2"\r\n', newline="")))
    assert rows[1][1] == "ligne 1\nligne 2"


@case("csv.formula_prefix.detected")
def _() -> None:
    assert all(formula_like(value) for value in ("=1+1", "+SUM(A1:A2)", "-2+3", "@CMD"))
    assert not formula_like("item.safe")


@case("csv.none_is_ambiguous_empty_string")
def _() -> None:
    stream = io.StringIO(newline="")
    csv.writer(stream, lineterminator="\n").writerow([None, ""])
    assert stream.getvalue() == ",\n"


@case("yaml.safe_document")
def _() -> None:
    value = yaml.safe_load('enabled: true\nname: "Asteria"\n')
    assert value == {"enabled": True, "name": "Asteria"}


@case("yaml.quoted_yes_is_string")
def _() -> None:
    value = yaml.safe_load('enabled: "yes"\n')
    assert value["enabled"] == "yes" and isinstance(value["enabled"], str)


@case("yaml.custom_tag.rejected")
def _() -> None:
    expect_raises(
        yaml.constructor.ConstructorError,
        lambda: yaml.safe_load('value: !!python/object:module.Class {}\n'),
    )


@case("yaml.multidocument.detected")
def _() -> None:
    documents = list(yaml.safe_load_all('---\nid: a\n---\nid: b\n'))
    assert len(documents) == 2


@case("yaml.anchor_alias.detected")
def _() -> None:
    tokens = list(yaml.scan('base: &base\n  enabled: true\ncopy: *base\n'))
    assert any(isinstance(token, AnchorToken) for token in tokens)
    assert any(isinstance(token, AliasToken) for token in tokens)


@case("json.canonical_bytes_and_hash")
def _() -> None:
    payload = {"étiquette": "Asteria", "a": 1}
    encoded = canonical_json_bytes(payload)
    assert encoded == '{"a":1,"étiquette":"Asteria"}\n'.encode("utf-8")
    assert hashlib.sha256(encoded).hexdigest() == hashlib.sha256(canonical_json_bytes(payload)).hexdigest()


def main() -> int:
    if len(CASES) != 24:
        raise RuntimeError(f"Expected 24 fixture cases, found {len(CASES)}")

    results: list[dict[str, str]] = []
    failed = 0
    for name, action in CASES:
        try:
            action()
        except Exception as exc:  # report the exact bounded fixture failure
            failed += 1
            results.append({"name": name, "status": "failed", "detail": f"{type(exc).__name__}: {exc}"})
        else:
            results.append({"name": name, "status": "passed", "detail": ""})

    report = {
        "schema_version": 1,
        "scope": "temporary-local-format-fixtures",
        "python": platform.python_version(),
        "pyyaml": package_version("PyYAML"),
        "jsonschema": package_version("jsonschema"),
        "total": len(results),
        "passed": len(results) - failed,
        "failed": failed,
        "cases": results,
        "reservations": [
            "No Godot binary or project was loaded.",
            "No user, network, secret, archive or Companion Pack data was processed.",
            "The fixtures qualify only the recorded Python, PyYAML and jsonschema environment.",
        ],
    }
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"total": report["total"], "passed": report["passed"], "failed": report["failed"]}))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
