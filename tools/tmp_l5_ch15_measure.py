#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

chapter = Path("Livre-V/CHAPITRE-15-Bases-vectorielles-et-recherche-semantique.md")
text = chapter.read_text(encoding="utf-8")
links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)
source_links = [
    target for target in links
    if any(target.startswith(f"../Livre-{roman}/") for roman in ("I", "II", "III", "IV"))
]
report = {
    "lines": len(text.splitlines()),
    "headings": len(re.findall(r"^#{1,6}\s", text, flags=re.MULTILINE)),
    "cards": text.count("<!-- l5:card -->"),
    "matrices": text.count("<!-- l5:matrix -->"),
    "markdown_links": len(links),
    "source_book_links": len(source_links),
    "fragment_links": sum("#" in target for target in source_links),
    "official_links": sum(target.startswith("https://") for target in links),
    "fenced_blocks": len(re.findall(r"^```", text, flags=re.MULTILINE)) // 2,
    "chapter_sha256": hashlib.sha256(chapter.read_bytes()).hexdigest(),
}
Path("dist").mkdir(exist_ok=True)
Path("dist/QA-LIVRE-V-CH15-CHAPTER.json").write_text(
    json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(report, ensure_ascii=False))
