#!/usr/bin/env python3
from pathlib import Path
import re
import sys

HEADING = "Synthèse opérationnelle pour Project Asteria"
errors = []
checked = 0
for path in sorted(Path("Livre-III").glob("CHAPITRE-*.md")):
    match = re.search(r"CHAPITRE-(\d+)-", path.name)
    if not match or int(match.group(1)) < 17:
        continue
    checked += 1
    text = path.read_text(encoding="utf-8")
    heading = re.search(r"(?m)^##(?:\s+\d+\.)?\s+Synthèse opérationnelle pour Project Asteria\s*$", text)
    if not heading:
        errors.append(f"{path}: section obligatoire absente")
        continue
    body = text[heading.end():]
    following = re.search(r"(?m)^##\s+", body)
    if following:
        body = body[:following.start()]
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", body) if len(p.strip()) >= 80]
    if len(paragraphs) < 2:
        errors.append(f"{path}: deux paragraphes substantiels minimum")
    if "Project Asteria" not in body:
        errors.append(f"{path}: Project Asteria absent du corps")
    if not any(token in body for token in ("porte", "acceptation", "bloquée", "bloque")):
        errors.append(f"{path}: condition d’acceptation ou de blocage absente")
if errors:
    print("Validation des synthèses Asteria : ÉCHEC", file=sys.stderr)
    for error in errors:
        print(f"- {error}", file=sys.stderr)
    sys.exit(1)
print(f"Validation des synthèses Asteria : SUCCÈS ({checked} chapitres contrôlés)")
