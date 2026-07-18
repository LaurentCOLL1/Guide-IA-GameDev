#!/usr/bin/env python3
"""Produce deterministic coverage metrics for usage-context markers."""

from __future__ import annotations

from collections import Counter
from pathlib import Path

from audit_contextes_utilisation import MARKER_RE, iter_markdown_files, parse_fences

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    files = iter_markdown_files()
    marker_counts: Counter[str] = Counter()
    fence_count = 0
    marked_fence_count = 0
    external_link_lines = 0
    web_marker_count = 0

    for path in files:
        lines = path.read_text(encoding="utf-8").splitlines()
        fences = parse_fences(lines)
        fence_count += len(fences)

        for line in lines:
            match = MARKER_RE.match(line.strip())
            if match:
                marker_counts[match.group(1)] += 1
                if match.group(1) == "WEB":
                    web_marker_count += 1
            if "http://" in line or "https://" in line:
                external_link_lines += 1

        for fence in fences:
            cursor = fence.start - 1
            while cursor >= 0 and not lines[cursor].strip():
                cursor -= 1
            if cursor >= 0 and MARKER_RE.match(lines[cursor].strip()):
                marked_fence_count += 1

    print("# Couverture des contextes d’utilisation")
    print()
    print(f"- Fichiers contrôlés : **{len(files)}**")
    print(f"- Blocs de code ou texte : **{fence_count}**")
    print(f"- Blocs précédés d’un repère : **{marked_fence_count}**")
    print(f"- Lignes contenant une URL externe : **{external_link_lines}**")
    print(f"- Repères [WEB] : **{web_marker_count}**")
    print(f"- Repères totaux : **{sum(marker_counts.values())}**")
    print()
    print("## Répartition des repères")
    print()
    for code in ("PS", "CMD", "WSL", "DCT", "DCK", "VSC", "WEB", "APP", "SORTIE", "LECTURE"):
        print(f"- [{code}] : **{marker_counts[code]}**")

    if marked_fence_count != fence_count:
        print()
        print("ERREUR : tous les blocs ne possèdent pas un repère.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
