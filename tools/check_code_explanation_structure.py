#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKER = "<!-- qa:code-explanation -->"
STRUCTURED = "**Explication structurée du bloc :**"
LABELED = re.compile(r"^- \*\*([^*\n]+) :\*\*\s+\S")
HEADING = re.compile(r"^#{1,6}\s+")
SOLO = re.compile(r"^##\s+\d+\.\s+Modes? Solo et (?:Mode )?Studio\s*$", re.I)
BANNED = (
    "Le bloc présente une structure de référence et les relations explicites entre ses éléments.",
    "Le lecteur doit retrouver la structure, les clés ou la commande dans l’ordre montré, sans interpréter ce bloc de référence comme une preuve d’exécution runtime.",
    "L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.",
    "Le traitement suit l’ordre écrit dans le bloc ; aucune étape implicite ne doit être ajoutée entre les gardes, la préparation et le résultat montré.",
)


def number(path: Path) -> int | None:
    match = re.search(r"CHAPITRE-(\d+)-", path.name)
    return int(match.group(1)) if match else None


def end_of_explanation(lines: list[str], start: int) -> int:
    structured_seen = False
    for index in range(start, len(lines)):
        line = lines[index]
        stripped = line.strip()
        if not stripped:
            continue
        if stripped == STRUCTURED:
            structured_seen = True
            continue
        if structured_seen and (line.startswith("- **") or line.startswith("  ")):
            continue
        if structured_seen:
            return index
    return len(lines)


def check(path: Path) -> list[str]:
    chapter = number(path)
    if chapter is None or chapter < 17:
        return []
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    errors: list[str] = []
    for phrase in BANNED:
        if phrase in text:
            errors.append(f"{path.relative_to(ROOT)}: formulation générique interdite: {phrase}")
    for marker in [i for i, line in enumerate(lines) if line.strip() == MARKER]:
        start = marker + 1
        while start < len(lines) and not lines[start].strip():
            start += 1
        if start >= len(lines) or lines[start].strip() != STRUCTURED:
            errors.append(f"{path.relative_to(ROOT)}:{marker + 1}: rubrique structurée absente")
            continue
        end = end_of_explanation(lines, start)
        labels = [match.group(1) for line in lines[start + 1:end] if (match := LABELED.match(line))]
        minimum = 4 if chapter in {25, 26} else 1
        if len(labels) < minimum:
            errors.append(f"{path.relative_to(ROOT)}:{marker + 1}: {len(labels)} rubrique(s), minimum {minimum}")
        if len(labels) != len(set(labels)):
            errors.append(f"{path.relative_to(ROOT)}:{marker + 1}: rubriques dupliquées")
    for index, line in enumerate(lines):
        if not SOLO.match(line):
            continue
        end = next((i for i in range(index + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
        if any(re.match(r"^```|^~~~", value) for value in lines[index + 1:end]):
            errors.append(f"{path.relative_to(ROOT)}:{index + 1}: Solo/Studio doit rester en Markdown")
    return errors


def main() -> int:
    argparse.ArgumentParser().add_argument("--check", action="store_true")
    errors: list[str] = []
    for path in sorted(ROOT.glob("Livre-II/CHAPITRE-*.md")):
        errors.extend(check(path))
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Explications structurées, spécifiques et sans rubriques dupliquées.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
