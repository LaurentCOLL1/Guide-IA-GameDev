from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path
import re

PACK = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md",
    "VERSION",
    "manifest.json",
    "DEPENDENCIES.json",
    "PROVENANCE.json",
    "LICENSE-STATUS.md",
    "pyproject.toml",
    "src/asteria_ai/contracts.py",
    "src/asteria_ai/client.py",
    "src/asteria_ai/mock_server.py",
    "godot-example/project.godot",
    "godot-example/tests/run_tests.gd",
    "qa/AUDIT-AI-LIBRARY.md",
    "qa/VALIDATION-AI-LIBRARY.yaml",
]

SECRET_PATTERNS = [
    re.compile(r"(?i)sk-[A-Za-z0-9]{20,}"),
    re.compile(r"(?i)(api[_-]?key|token|secret)\s*[:=]\s*['\"][^'\"]{8,}"),
]


def validate() -> dict:
    errors: list[str] = []
    source_files = sorted(path for path in PACK.rglob("*") if path.is_file())

    for relative in REQUIRED:
        if not (PACK / relative).is_file():
            errors.append(f"missing:{relative}")

    for relative in ["manifest.json", "DEPENDENCIES.json", "PROVENANCE.json"]:
        try:
            json.loads((PACK / relative).read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"json:{relative}:{exc}")

    pyproject = (PACK / "pyproject.toml").read_text(encoding="utf-8")
    if "dependencies = []" not in pyproject:
        errors.append("pyproject:third-party-dependencies")

    for path in source_files:
        raw = path.read_bytes()
        if b"\x00" in raw:
            errors.append(f"binary:{path.relative_to(PACK)}")
            continue
        text = raw.decode("utf-8")
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                errors.append(f"secret-pattern:{path.relative_to(PACK)}")
        if path.suffix == ".py":
            try:
                ast.parse(text, filename=str(path))
            except SyntaxError as exc:
                errors.append(f"python-syntax:{path.relative_to(PACK)}:{exc.lineno}")

    config = (PACK / "src/asteria_ai/config.py").read_text(encoding="utf-8")
    for expected in ["127.0.0.1:11434", "127.0.0.1:8080", "allow_remote"]:
        if expected not in config:
            errors.append(f"config-marker:{expected}")

    report = {
        "status": "success" if not errors else "failure",
        "pack": "CP-PACK-03-AI-LIBRARY",
        "source_files": len(source_files),
        "third_party_python_dependencies": 0,
        "errors": errors,
    }
    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--report")
    args = parser.parse_args()
    report = validate()
    if args.report:
        target = Path(args.report)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(
        f"AI_LIBRARY_STATIC: {report['status'].upper()} "
        f"({report['source_files']} files)"
    )
    for error in report["errors"]:
        print(error)
    return 0 if report["status"] == "success" else 1


if __name__ == "__main__":
    raise SystemExit(main())
