#!/usr/bin/env python3
from pathlib import Path
import re

VALIDATED_HEAD = "bbfced8c7792c98938c5c3e989e14fd22d9e47d8"
CHAPTER_RUN = "29855954911"
CONTEXT_RUN = "29855954936"
ARTIFACT_ID = "8505270544"
ARTIFACT_DIGEST = "sha256:d0a0b1d6b63ffb37588c7aeb0e26a780b23a116553e7db24b156b78c1bc3e826"


def replace_once(text: str, pattern: str, replacement: str) -> str:
    updated, count = re.subn(pattern, replacement, text, count=1, flags=re.MULTILINE)
    if count != 1:
        raise SystemExit(f"Remplacement attendu une fois, obtenu {count}: {pattern}")
    return updated


for number in range(17, 27):
    path = Path(f"Livre-II/QA/VALIDATION-FINALE-CHAPITRE-{number}.yaml")
    text = path.read_text(encoding="utf-8")
    text = replace_once(text, r"^status:\s*.*$", "status: complete")
    text = replace_once(
        text,
        r"^validated-head-commit:\s*.*$",
        f"validated-head-commit: {VALIDATED_HEAD}",
    )
    text = replace_once(text, r"^  blocking-errors:\s*.*$", "  blocking-errors: 0")
    text = replace_once(text, r"^  warnings:\s*.*$", "  warnings: 0")
    text = replace_once(
        text,
        r"(^  validate-chapters-without-pdf:\n    run-id:)\s*.*$",
        rf"\1 {CHAPTER_RUN}",
    )
    text = replace_once(
        text,
        r"(^  validate-chapters-without-pdf:\n    run-id:.*\n    conclusion:)\s*.*$",
        r"\1 success",
    )
    text = replace_once(
        text,
        r"(^  validate-usage-contexts:\n    run-id:)\s*.*$",
        rf"\1 {CONTEXT_RUN}",
    )
    text = replace_once(
        text,
        r"(^  validate-usage-contexts:\n    run-id:.*\n    conclusion:)\s*.*$",
        r"\1 success",
    )
    text = replace_once(text, r"(^  artifact:\n    id:)\s*.*$", rf"\1 {ARTIFACT_ID}")
    text = replace_once(
        text,
        r"(^  artifact:\n(?:    .*\n)*?    digest:)\s*.*$",
        rf"\1 {ARTIFACT_DIGEST}",
    )
    text = replace_once(
        text,
        r"(^evidence-closure:\n  commit:)\s*.*$",
        rf"\1 {VALIDATED_HEAD}",
    )
    text = replace_once(
        text,
        r"(^evidence-closure:\n  commit:.*\n  conclusion:)\s*.*$",
        r"\1 success",
    )
    path.write_text(text, encoding="utf-8")
    print(f"preuve chapitre {number} fermée")
