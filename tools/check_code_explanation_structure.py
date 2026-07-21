#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKER = "<!-- qa:code-explanation -->"
STRUCTURED = "**Explication structurée du bloc :**"
ERROR_SECTION_MARKER = "<!-- qa:error-correction-section -->"
ERROR_INDEX_MARKER = "<!-- qa:error-correction-index -->"
LABELED = re.compile(r"^- \*\*([^*\n]+) :\*\*\s+\S")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
FENCE_RE = re.compile(r"^(?P<fence>`{3,}|~{3,})(?P<lang>.*)$")
SOLO = re.compile(r"^##\s+\d+\.\s+Modes? Solo et (?:Mode )?Studio\s*$", re.I)
ERROR_HEADING_RE = re.compile(
    r"(?:erreurs? fréquentes|anti[- ]patterns?|symptômes fréquents|"
    r"pièges(?: fréquents)?|mauvaises pratiques|problèmes fréquents|"
    r"diagnostics et corrections)",
    re.IGNORECASE,
)
SYMPTOM_RE = re.compile(
    r"\*\*(?:Symptôme(?:\s+ou\s+risque)?|Risque)\s*:\*\*",
    re.IGNORECASE,
)
EXAMPLE_KIND = (
    r"(?:exemple|structure|organisation|architecture|flux|formulation|ordre|"
    r"historique|chemin|dépendances?|arbre|lot|configuration|commande|code|"
    r"version|implémentation|approche|séquence|appel|script)"
)
FAULTY_RE = re.compile(
    EXAMPLE_KIND + r"[^\n]{0,100}(?:fautif|fautive|incorrect|incorrecte|à éviter|anti[- ]pattern)",
    re.IGNORECASE,
)
WHY_FAULTY_RE = re.compile(r"Pourquoi cet exemple est fautif", re.IGNORECASE)
CORRECTED_RE = re.compile(
    EXAMPLE_KIND + r"[^\n]{0,100}corrig(?:é|ée|és|ées)",
    re.IGNORECASE,
)
WHY_CORRECTED_RE = re.compile(r"Pourquoi la correction fonctionne", re.IGNORECASE)
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


def headings_outside_fences(lines: list[str]) -> list[tuple[int, int, str]]:
    headings: list[tuple[int, int, str]] = []
    in_fence = False
    fence_char = ""
    fence_length = 0

    for index, line in enumerate(lines):
        fence_match = FENCE_RE.match(line.strip())
        if fence_match:
            fence = fence_match.group("fence")
            if not in_fence:
                in_fence = True
                fence_char = fence[0]
                fence_length = len(fence)
            elif fence[0] == fence_char and len(fence) >= fence_length:
                in_fence = False
            continue
        if in_fence:
            continue
        match = HEADING_RE.match(line)
        if match:
            headings.append((index, len(match.group(1)), match.group(2).strip()))
    return headings


def check_error_correction_sections(path: Path, lines: list[str]) -> list[str]:
    """Applique la règle sémantique, indépendamment du titre exact de la section."""
    errors: list[str] = []
    headings = headings_outside_fences(lines)

    for position, (start, level, title) in enumerate(headings):
        if level < 2:
            continue
        end = len(lines)
        for next_start, next_level, _ in headings[position + 1:]:
            if next_level <= level:
                end = next_start
                break
        body = "\n".join(lines[start + 1:end])
        is_error_section = (
            ERROR_HEADING_RE.search(title) is not None
            or ERROR_SECTION_MARKER in body
            or ERROR_INDEX_MARKER in body
        )
        if not is_error_section:
            continue

        rel = path.relative_to(ROOT)
        if ERROR_INDEX_MARKER in body:
            continue
        if ERROR_SECTION_MARKER not in body:
            errors.append(
                f"{rel}:{start + 1}: section pédagogique d’erreurs sans marqueur détaillé ou d’index"
            )
            continue

        children = [
            (child_start, child_title)
            for child_start, child_level, child_title in headings[position + 1:]
            if child_start < end and child_level == level + 1
        ]
        if not children:
            errors.append(f"{rel}:{start + 1}: section détaillée sans sous-cas")
            continue

        for child_index, (child_start, child_title) in enumerate(children):
            child_end = children[child_index + 1][0] if child_index + 1 < len(children) else end
            child_body = "\n".join(lines[child_start + 1:child_end])
            checks = (
                ("symptôme ou risque", SYMPTOM_RE),
                ("exemple fautif", FAULTY_RE),
                ("Pourquoi cet exemple est fautif", WHY_FAULTY_RE),
                ("exemple corrigé", CORRECTED_RE),
                ("Pourquoi la correction fonctionne", WHY_CORRECTED_RE),
            )
            positions: list[int] = []
            missing: list[str] = []
            for label, pattern in checks:
                match = pattern.search(child_body)
                if match is None:
                    missing.append(label)
                else:
                    positions.append(match.start())
            if missing:
                errors.append(
                    f"{rel}:{child_start + 1}: cas « {child_title} » incomplet: "
                    + ", ".join(missing)
                )
                continue
            if positions != sorted(positions):
                errors.append(
                    f"{rel}:{child_start + 1}: cas « {child_title} » hors ordre; "
                    "attendu symptôme → exemple fautif → pourquoi fautif → "
                    "exemple corrigé → pourquoi la correction fonctionne"
                )
    return errors


def check(path: Path) -> list[str]:
    chapter = number(path)
    if chapter is None:
        return []
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    errors = check_error_correction_sections(path, lines) if chapter >= 17 else []

    if chapter < 17:
        return errors

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
        print("\n".join(errors))
        return 1
    print(
        "Explications structurées et règle sémantique des erreurs/corrections conformes."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
