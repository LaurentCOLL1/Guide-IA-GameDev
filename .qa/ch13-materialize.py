#!/usr/bin/env python3
import hashlib
import json
import os
import re
import subprocess
from collections import Counter
from pathlib import Path

CHAPTER_PATH = Path("Livre-III/CHAPITRE-13-Architecture-batiments-et-kits-modulaires.md")
EXPECTED_CHAPTER_SHA = "fb9835f62e40f33091db48662ed16bb629002ca396b7e5972ce4767b6b3d54c9"
ANALYSIS_PATH = Path(".qa/ch13-analysis.json")

chapter = CHAPTER_PATH.read_text(encoding="utf-8")
if hashlib.sha256(chapter.encode("utf-8")).hexdigest() != EXPECTED_CHAPTER_SHA:
    raise RuntimeError("Empreinte du chapitre récupéré invalide.")

lines = chapter.splitlines()
headings = [line.strip() for line in lines if re.match(r"^#{1,6}\s+", line)]
fences = [index for index, line in enumerate(lines) if line.startswith("```")]
blocks = []
for index in range(0, len(fences) - 1, 2):
    blocks.append("\n".join(lines[fences[index] + 1:fences[index + 1]]).strip())
paragraphs = []
for part in re.split(r"\n\s*\n", chapter):
    normalized = " ".join(part.split())
    if len(normalized) >= 160 and not normalized.startswith(("```", "<!--", "|")):
        paragraphs.append(normalized)

def duplicate_count(values):
    return sum(count - 1 for count in Counter(values).values() if count > 1)

analysis = {
    "chapter_sha256": EXPECTED_CHAPTER_SHA,
    "lines": len(lines),
    "headings_count": len(headings),
    "headings": headings,
    "code_and_data_blocks": len(blocks),
    "code_explanation_markers": chapter.count("<!-- qa:code-explanation -->"),
    "structured_non_error_explanations": chapter.count("**Explication structurée du bloc :**"),
    "error_section_markers": chapter.count("<!-- qa:error-correction-section -->"),
    "faulty_explanations": chapter.count("**Pourquoi cet exemple est fautif :**"),
    "corrected_explanations": chapter.count("**Pourquoi la correction fonctionne :**"),
    "duplicate_headings": duplicate_count(headings),
    "duplicate_blocks": duplicate_count(blocks),
    "duplicate_long_paragraphs": duplicate_count(paragraphs),
}
ANALYSIS_PATH.write_text(json.dumps(analysis, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

subprocess.run(["git", "config", "user.name", "github-actions[bot]"], check=True)
subprocess.run(["git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com"], check=True)
subprocess.run(["git", "add", str(ANALYSIS_PATH)], check=True)
if subprocess.run(["git", "diff", "--cached", "--quiet"]).returncode != 0:
    subprocess.run(["git", "commit", "-m", "chore(ch13): relever la structure du chapitre récupéré"], check=True)
    subprocess.run(["git", "push", "origin", f"HEAD:{os.environ['HEAD_BRANCH']}"], check=True)
raise RuntimeError("Structure du chapitre 13 enregistrée ; génération QA différée.")
