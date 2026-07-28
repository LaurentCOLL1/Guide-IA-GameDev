#!/usr/bin/env python3
"""Valide les fiches, matrices et liens profonds du Livre V."""
from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
CHAPTER_RE = re.compile(r"CHAPITRE-\d{2}-.+\.md$")
LINK_RE = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*$")
SOURCE_RE = re.compile(r"^\.\./Livre-(?:I|II|III|IV)/")
CARD_MARKER = "<!-- l5:card -->"
MATRIX_MARKER = "<!-- l5:matrix -->"


def slugify_heading(title: str) -> str:
    """Produit le fragment Markdown attendu par GitHub/Pandoc pour les titres du dépôt."""
    value = re.sub(r"`([^`]*)`", r"\1", title)
    value = re.sub(r"[*_~]", "", value).strip().casefold()
    value = re.sub(r"[^\w\s-]", "", value, flags=re.UNICODE)
    value = re.sub(r"[\s-]+", "-", value).strip("-")
    return value


def anchors(path: Path) -> set[str]:
    counts: Counter[str] = Counter()
    result: set[str] = set()
    in_fence = False
    fence_char = ""
    fence_length = 0
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        fence = re.match(r"^(`{3,}|~{3,})", stripped)
        if fence:
            token = fence.group(1)
            if not in_fence:
                in_fence = True
                fence_char = token[0]
                fence_length = len(token)
            elif token[0] == fence_char and len(token) >= fence_length:
                in_fence = False
            continue
        if in_fence:
            continue
        match = HEADING_RE.match(line)
        if not match:
            continue
        base = slugify_heading(match.group(1))
        if not base:
            continue
        index = counts[base]
        counts[base] += 1
        result.add(base if index == 0 else f"{base}-{index}")
    return result


def validate_chapter(path: Path) -> tuple[list[str], dict[str, int]]:
    rel = path.relative_to(ROOT).as_posix()
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    links = LINK_RE.findall(text)
    source_targets = [unquote(target.strip().split()[0].strip("<>")) for _, target in links if SOURCE_RE.match(target.strip())]
    fragment_targets = [target for target in source_targets if "#" in target]

    if 'document-format: "reference-cards"' not in text[:1200]:
        errors.append(f"{rel}: métadonnée document-format=reference-cards absente")
    if text.count(CARD_MARKER) < 4:
        errors.append(f"{rel}: moins de quatre fiches marquées")
    if text.count(CARD_MARKER) + text.count(MATRIX_MARKER) < 5:
        errors.append(f"{rel}: moins de cinq unités de consultation")
    if len(source_targets) < 6:
        errors.append(f"{rel}: moins de six renvois vers les Livres I à IV")
    if len(fragment_targets) < 2:
        errors.append(f"{rel}: moins de deux liens profonds vers des sous-sections")

    anchor_cache: dict[Path, set[str]] = {}
    for target in fragment_targets:
        relative_file, fragment = target.split("#", 1)
        resolved = (path.parent / relative_file).resolve()
        try:
            resolved.relative_to(ROOT)
        except ValueError:
            errors.append(f"{rel}: lien profond sortant du dépôt : {target}")
            continue
        if not resolved.is_file():
            errors.append(f"{rel}: fichier cible absent : {target}")
            continue
        if resolved not in anchor_cache:
            anchor_cache[resolved] = anchors(resolved)
        if fragment not in anchor_cache[resolved]:
            errors.append(f"{rel}: fragment introuvable : {target}")

    return errors, {
        "cards": text.count(CARD_MARKER),
        "matrices": text.count(MATRIX_MARKER),
        "links": len(links),
        "source_links": len(source_targets),
        "fragment_links": len(fragment_targets),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", required=True)
    parser.parse_args()

    chapters = sorted(path for path in (ROOT / "Livre-V").glob("CHAPITRE-*.md") if CHAPTER_RE.fullmatch(path.name))
    errors: list[str] = []
    totals: Counter[str] = Counter()
    for path in chapters:
        chapter_errors, metrics = validate_chapter(path)
        errors.extend(chapter_errors)
        totals.update(metrics)

    print(f"Chapitres du Livre V contrôlés : {len(chapters)}")
    print(f"Fiches marquées : {totals['cards']}")
    print(f"Matrices marquées : {totals['matrices']}")
    print(f"Liens internes : {totals['links']}")
    print(f"Renvois vers les Livres I à IV : {totals['source_links']}")
    print(f"Liens profonds vérifiés : {totals['fragment_links']}")
    print(f"Non-conformités : {len(errors)}")
    for error in errors:
        print(f"- {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
