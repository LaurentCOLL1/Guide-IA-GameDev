from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CH29 = ROOT / "Livre-II" / "CHAPITRE-29-Automatisation-Python-et-generation-de-donnees.md"
CONTINUITY = ROOT / "CONTINUITE-PROJET.md"
TIMESTAMP = "2026-07-22T12:45:00+02:00"

chapter = CH29.read_text(encoding="utf-8")
old = 'MARKER = "CONTINUITE-PROJET.md"'
new = 'MARKER = "pyproject.toml"'
if chapter.count(old) != 1:
    raise RuntimeError(f"Marqueur éditorial attendu une fois, trouvé {chapter.count(old)}")
chapter = chapter.replace(old, new, 1)
CH29.write_text(chapter, encoding="utf-8")

continuity = CONTINUITY.read_text(encoding="utf-8")
if continuity.count('version: "3.30.4"') != 1:
    raise RuntimeError("Version 3.30.4 de la continuité introuvable")
continuity = continuity.replace('version: "3.30.4"', 'version: "3.30.5"', 1)
continuity, count = re.subn(
    r'^last-updated: ".*"$',
    f'last-updated: "{TIMESTAMP}"',
    continuity,
    count=1,
    flags=re.M,
)
if count != 1:
    raise RuntimeError("last-updated introuvable")
entry = f"""### {TIMESTAMP} — version 3.30.5

- le dernier lien sémantique vers la fabrication éditoriale est retiré du manuel lecteur ;
- l’exemple Python du chapitre 29 utilise désormais `pyproject.toml` comme marqueur technique de racine ;
- le PDF lecteur doit être reconstruit et inspecté sur ce dernier état avant fusion ;
- le plan maître enrichi du Livre III reste en version `1.1.0`.

"""
anchor = "## 27. Journal\n\n"
if anchor not in continuity:
    raise RuntimeError("Journal de continuité introuvable")
continuity = continuity.replace(anchor, anchor + entry, 1)
CONTINUITY.write_text(continuity, encoding="utf-8")

for temporary in (
    ROOT / ".qa" / "final-reader-check.txt",
    Path(__file__),
):
    if temporary.exists():
        temporary.unlink()

print("Marqueur de racine du chapitre 29 remplacé par pyproject.toml.")
