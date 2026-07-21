#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKER = "<!-- qa:code-explanation -->"
CHAPTER_GLOB = "Livre-II/CHAPITRE-*.md"
STRUCTURED = "**Explication structurée du bloc :**"
LABELED_BULLET = re.compile(r"^- \*\*[^*\n]+ :\*\*\s+\S")
HEADING = re.compile(r"^#{1,6}\s+")
SOLO_HEADING = re.compile(r"^##\s+\d+\.\s+Modes? Solo et (?:Mode )?Studio\s*$", re.I)


def chapter_number(path: Path) -> int | None:
    match = re.search(r"CHAPITRE-(\d+)-", path.name)
    return int(match.group(1)) if match else None


def explanation_end(lines: list[str], start: int) -> int:
    seen = False
    for index in range(start, len(lines)):
        line = lines[index]
        if line.strip():
            if seen and (
                HEADING.match(line)
                or line.startswith("> **[")
                or line.startswith("<!-- qa:")
                or line.startswith("**Exemple fautif")
                or line.startswith("**Exemple corrigé")
                or line.startswith("**Symptôme")
            ):
                return index
            seen = True
    return len(lines)


def check_file(path: Path) -> list[str]:
    number = chapter_number(path)
    if number is None or number < 17:
        return []
    lines = path.read_text(encoding="utf-8").splitlines()
    errors: list[str] = []
    marker_indexes = [i for i, line in enumerate(lines) if line.strip() == MARKER]
    for marker_index in marker_indexes:
        start = marker_index + 1
        while start < len(lines) and not lines[start].strip():
            start += 1
        if start >= len(lines) or lines[start].strip() != STRUCTURED:
            errors.append(f"{path.relative_to(ROOT)}:{marker_index + 1}: explication structurée absente")
            continue
        body_start = start + 1
        end = explanation_end(lines, body_start)
        bullets = [line for line in lines[body_start:end] if LABELED_BULLET.match(line)]
        minimum = 4 if number in {25, 26} else 1
        if len(bullets) < minimum:
            errors.append(
                f"{path.relative_to(ROOT)}:{marker_index + 1}: {len(bullets)} point(s) structuré(s), minimum {minimum}"
            )

    for index, line in enumerate(lines):
        if not SOLO_HEADING.match(line):
            continue
        end = len(lines)
        for probe in range(index + 1, len(lines)):
            if lines[probe].startswith("## "):
                end = probe
                break
        if any(re.match(r"^```|^~~~", value) for value in lines[index + 1:end]):
            errors.append(
                f"{path.relative_to(ROOT)}:{index + 1}: Solo/Studio doit rester en Markdown ordinaire"
            )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.parse_args()
    errors: list[str] = []
    for path in sorted(ROOT.glob(CHAPTER_GLOB)):
        errors.extend(check_file(path))
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Explications structurées conformes pour les chapitres 17 et suivants.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
