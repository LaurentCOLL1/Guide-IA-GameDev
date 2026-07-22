#!/usr/bin/env python3
"""Produce deterministic coverage metrics for usage-context markers."""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path

from audit_contextes_utilisation import MARKER_RE, all_markdown_files, parse_fences

ROOT = Path(__file__).resolve().parents[1]


def group_for(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    if rel.startswith("Volume-0/"):
        return "Volume 0"
    if rel.startswith("Livre-I/"):
        return "Livre I"
    if rel.startswith("Livre-II/"):
        return "Livre II"
    if rel.startswith("Livre-III/"):
        return "Livre III"
    return "Racine"


def main() -> int:
    files = all_markdown_files()
    marker_counts: Counter[str] = Counter()
    group_files: Counter[str] = Counter()
    group_fences: Counter[str] = Counter()
    group_marked: Counter[str] = Counter()
    chapter_counts: defaultdict[str, Counter[str]] = defaultdict(Counter)
    fence_count = 0
    marked_fence_count = 0
    external_link_lines = 0

    for path in files:
        group = group_for(path)
        group_files[group] += 1
        lines = path.read_text(encoding="utf-8").splitlines()
        fences = parse_fences(lines)
        fence_count += len(fences)
        group_fences[group] += len(fences)

        for line in lines:
            match = MARKER_RE.match(line.strip())
            if match:
                code = match.group(1)
                marker_counts[code] += 1
                if path.name.startswith("CHAPITRE-"):
                    chapter_counts[path.relative_to(ROOT).as_posix()][code] += 1
            if "http://" in line or "https://" in line:
                external_link_lines += 1

        for fence in fences:
            cursor = fence.start - 1
            while cursor >= 0 and not lines[cursor].strip():
                cursor -= 1
            if cursor >= 0 and MARKER_RE.match(lines[cursor].strip()):
                marked_fence_count += 1
                group_marked[group] += 1

    print("# Couverture des contextes d’utilisation")
    print()
    print(f"- Fichiers contrôlés : **{len(files)}**")
    print(f"- Blocs de code ou texte : **{fence_count}**")
    print(f"- Blocs précédés d’un repère : **{marked_fence_count}**")
    print(f"- Lignes contenant une URL externe : **{external_link_lines}**")
    print(f"- Repères totaux : **{sum(marker_counts.values())}**")
    print()
    print("## Couverture par ensemble")
    print()
    for group in ("Volume 0", "Livre I", "Livre II", "Livre III", "Racine"):
        if group_files[group]:
            print(
                f"- {group} : **{group_files[group]} fichiers**, "
                f"**{group_marked[group]}/{group_fences[group]} blocs repérés**"
            )
    print()
    print("## Répartition des repères")
    print()
    for code in ("PS", "CMD", "WSL", "DCT", "DCK", "VSC", "WEB", "APP", "SORTIE", "LECTURE"):
        print(f"- [{code}] : **{marker_counts[code]}**")
    print()
    print("## Chapitres des Livres II et III")
    print()
    for path in sorted(chapter_counts):
        if not path.startswith(("Livre-II/", "Livre-III/")):
            continue
        values = chapter_counts[path]
        rendered = ", ".join(
            f"[{code}] {values[code]}"
            for code in ("PS", "CMD", "WSL", "DCT", "DCK", "VSC", "WEB", "APP", "SORTIE", "LECTURE")
            if values[code]
        )
        print(f"- `{path}` : {rendered}")

    if marked_fence_count != fence_count:
        print()
        print("ERREUR : tous les blocs ne possèdent pas un repère.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
