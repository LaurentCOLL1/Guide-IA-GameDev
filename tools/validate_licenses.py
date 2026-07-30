#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

try:
    import yaml
except ImportError as exc:
    raise SystemExit("PyYAML is required") from exc

ALLOWED = {"CC-BY-SA-4.0", "MIT", "CC0-1.0"}
PACKS = [
    "Starter-Kit",
    "Project-Templates",
    "AI-Library",
    "Code-Library",
    "Database-Library",
    "ComfyUI-Library",
    "Documentation-Library",
    "Test-Benchmark-Library",
    "Production-Toolkit",
    "Knowledge-Base",
]
REQUIRED = [
    "LICENSE.md",
    "NOTICE.md",
    "LICENSES/MIT.txt",
    "LICENSES/CC-BY-SA-4.0.txt",
    "LICENSES/CC0-1.0.txt",
    "docs/licensing/README.md",
    "docs/licensing/LICENSE-MATRIX.yaml",
    "QA/AUDIT-LICENSING.md",
    "QA/VALIDATION-LICENSING.yaml",
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    errors: list[str] = []

    for rel in REQUIRED:
        if not (root / rel).is_file():
            errors.append(f"missing:{rel}")

    if not errors:
        matrix = yaml.safe_load(
            (root / "docs/licensing/LICENSE-MATRIX.yaml").read_text(encoding="utf-8")
        )
        if matrix.get("schema-version") != 1:
            errors.append("matrix:schema-version")
        licenses = {value.get("spdx") for value in matrix.get("licenses", {}).values()}
        if licenses != ALLOWED:
            errors.append(f"matrix:licenses:{sorted(licenses)}")
        if len(matrix.get("rules", [])) < 5:
            errors.append("matrix:rules")

    license_md = (
        (root / "LICENSE.md").read_text(encoding="utf-8")
        if (root / "LICENSE.md").exists()
        else ""
    )
    for token in ALLOWED:
        if token not in license_md:
            errors.append(f"license-md:{token}")

    mit = (
        (root / "LICENSES/MIT.txt").read_text(encoding="utf-8")
        if (root / "LICENSES/MIT.txt").exists()
        else ""
    )
    for marker in [
        "Permission is hereby granted",
        'THE SOFTWARE IS PROVIDED "AS IS"',
        "Copyright (c) 2026 Laurent Collin",
    ]:
        if marker not in mit:
            errors.append(f"mit:{marker[:20]}")

    for pack in PACKS:
        path = root / "Companion-Pack" / pack / "LICENSE-STATUS.md"
        if not path.is_file():
            errors.append(f"pack-license-missing:{pack}")
            continue
        text = path.read_text(encoding="utf-8")
        for token in ["LICENSE.md", "CC-BY-SA-4.0", "MIT"]:
            if token not in text:
                errors.append(f"pack-license:{pack}:{token}")
        if "pending-global-license" in text or "suspendue à la licence globale" in text:
            errors.append(f"pack-license-pending:{pack}")

    governed = [
        "README.md",
        "CONTRIBUTING.md",
        "metadata.yaml",
        "ROADMAP.md",
        "CONTINUITE-PROJET.md",
    ]
    combined = "\n".join(
        (root / path).read_text(encoding="utf-8")
        for path in governed
        if (root / path).exists()
    )
    for forbidden in [
        'license: "À définir avant publication"',
        "- [ ] Définir la licence globale du projet.",
    ]:
        if forbidden in combined:
            errors.append(f"governance-pending:{forbidden}")

    continuity = (root / "CONTINUITE-PROJET.md").read_text(encoding="utf-8")
    if "Produire les versions PDF, HTML et EPUB" not in continuity:
        errors.append("continuity-next-action")

    status = "success" if not errors else "failure"
    report = {
        "status": status,
        "errors": errors,
        "licenses": sorted(ALLOWED),
        "pack_license_files": len(PACKS),
        "required_files": len(REQUIRED),
    }
    print(json.dumps(report, ensure_ascii=False, sort_keys=True))
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(
            json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
