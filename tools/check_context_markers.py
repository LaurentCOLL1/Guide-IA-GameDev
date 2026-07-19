#!/usr/bin/env python3
"""Vérifie les repères d'utilisation sans modifier les documents."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKER_RE = re.compile(r"^> \*\*\[(PS|CMD|WSL|DCT|DCK|VSC|WEB|APP|SORTIE|LECTURE)\]")
FENCE_RE = re.compile(r"^(?P<fence>`{3,}|~{3,})(?P<lang>[^`]*)$")
L2_CHAPTER_RE = re.compile(r"Livre-II/CHAPITRE-\d{2}-.+\.md$")
AUDIT_DATE_RE = re.compile(r'^audit-date:\s*["\']?\d{4}-\d{2}-\d{2}["\']?\s*$')


def files() -> list[Path]:
    result: list[Path] = []
    for base in (ROOT / "Volume-0", ROOT / "Livre-I", ROOT / "Livre-II"):
        result.extend(sorted(base.rglob("*.md")))
    result.append(ROOT / "STYLE_GUIDE.md")
    return [path for path in result if path.is_file()]


def previous_nonempty(lines: list[str], index: int) -> int | None:
    index -= 1
    while index >= 0:
        if lines[index].strip():
            return index
        index -= 1
    return None


def check_file(path: Path) -> tuple[list[str], int]:
    rel = path.relative_to(ROOT).as_posix()
    lines = path.read_text(encoding="utf-8").splitlines()
    errors: list[str] = []
    controlled_blocks = 0
    inside = False
    fence_char = ""
    fence_len = 0

    for index, line in enumerate(lines):
        match = FENCE_RE.match(line.strip())
        if not match:
            continue
        fence = match.group("fence")
        lang = match.group("lang").strip()
        if inside:
            if fence[0] == fence_char and len(fence) >= fence_len and not lang:
                inside = False
            continue
        inside = True
        fence_char = fence[0]
        fence_len = len(fence)
        controlled_blocks += 1
        marker_index = previous_nonempty(lines, index)
        if marker_index is None or not MARKER_RE.match(lines[marker_index].strip()):
            errors.append(f"{rel}:{index + 1}: bloc `{lang or 'text'}` sans repère d’utilisation")

    if L2_CHAPTER_RE.fullmatch(rel):
        front = lines[:120]
        required_exact = (
            'audit-status: "complete"',
            'usage-context-standard: "DOC-V0-ANN-CONTEXTES"',
        )
        for expected in required_exact:
            if expected not in front:
                errors.append(f"{rel}: métadonnée absente ou incorrecte : {expected}")
        if not any(AUDIT_DATE_RE.fullmatch(line.strip()) for line in front):
            errors.append(f"{rel}: métadonnée audit-date absente ou invalide")
        if not any(line.startswith('audit-level: "') for line in front):
            errors.append(f"{rel}: métadonnée audit-level absente")
        if not any("Repères d’utilisation" in line for line in lines[:140]):
            errors.append(f"{rel}: légende des repères absente")

    return errors, controlled_blocks


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", required=True)
    parser.parse_args()

    errors: list[str] = []
    controlled_blocks = 0
    controlled_files = files()
    for path in controlled_files:
        file_errors, block_count = check_file(path)
        errors.extend(file_errors)
        controlled_blocks += block_count

    print(f"Fichiers contrôlés : {len(controlled_files)}")
    print(f"Blocs contrôlés : {controlled_blocks}")
    print(f"Non-conformités : {len(errors)}")
    for error in errors:
        print(f"- {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
