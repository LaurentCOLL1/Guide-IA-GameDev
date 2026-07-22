#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import re

root = Path(".")
now = datetime.now(ZoneInfo("Europe/Paris")).replace(microsecond=0).isoformat()

# 1. Remove process-facing audit notices from reader chapters.
changed_chapters = 0
for path in sorted((root / "Livre-II").glob("CHAPITRE-*.md")):
    text = path.read_text(encoding="utf-8")
    updated = re.sub(r"^>.*Audit post-création.*\n?", "", text, flags=re.MULTILINE)
    updated = re.sub(r"^>.*Explications de code.*\n?", "", updated, flags=re.MULTILINE)
    updated = re.sub(r"\n{3,}", "\n\n", updated)
    if updated != text:
        path.write_text(updated, encoding="utf-8")
        changed_chapters += 1

# 2. Keep the reader index focused on the book, not the production process.
index_path = root / "Livre-II/index.md"
index = index_path.read_text(encoding="utf-8")
index = re.sub(r'^version:\s*"[^"]+"', 'version: "1.24.0"', index, count=1, flags=re.MULTILINE)
index = re.sub(
    r"\n## Audit post-création\n.*?(?=\n## Principes du Livre II\n)",
    "\n",
    index,
    flags=re.DOTALL,
)
index_path.write_text(index, encoding="utf-8")

# 3. Update continuity with a permanent reader-publication rule.
continuity_path = root / "CONTINUITE-PROJET.md"
continuity = continuity_path.read_text(encoding="utf-8")
continuity = re.sub(r'^version:\s*"[^"]+"', 'version: "3.30.2"', continuity, count=1, flags=re.MULTILINE)
continuity = re.sub(r'^last-updated:\s*"[^"]+"', f'last-updated: "{now}"', continuity, count=1, flags=re.MULTILINE)
pdf_rule = (
    "\n- l’ordre de compilation destiné au lecteur exclut tous les fichiers `QA/`, "
    "protocoles d’audit, audits de chapitres, preuves de validation et rapports de campagne ;\n"
    "- les métadonnées et mentions visibles décrivant la phase de conception ou l’audit "
    "restent dans le dépôt, mais ne doivent pas apparaître dans le manuel PDF vendu au lecteur ;"
)
anchor = "- autoriser une exception uniquement pour une modification directe de la chaîne PDF ou de la mise en page."
if pdf_rule.strip() not in continuity:
    if anchor not in continuity:
        raise RuntimeError("Ancre de politique PDF introuvable")
    continuity = continuity.replace(anchor, anchor + pdf_rule, 1)

journal_anchor = "## 27. Journal\n"
entry = f"""## 27. Journal

### {now} — version 3.30.2

- ordre de compilation lecteur nettoyé : protocoles, audits, preuves et rapports QA exclus du PDF ;
- mentions visibles d’audit et d’explication éditoriale retirées des en-têtes des trente chapitres du Livre II ;
- index du Livre II recentré sur le contenu du manuel, sans sections de gouvernance éditoriale ;
- pagination `plain` retenue pour éviter les en-têtes courants rognés ;
- fichiers QA conservés dans le dépôt comme preuves de conception et de validation ;
- reconstruction Pandoc/XeLaTeX et inspection visuelle du manuel lecteur requises avant le Livre III.
"""
if "version 3.30.2" not in continuity:
    continuity = continuity.replace(journal_anchor, entry, 1)
continuity_path.write_text(continuity, encoding="utf-8")

# 4. Remove the temporary script from the permanent branch diff.
Path(".qa/finalize-reader-manual.py").unlink(missing_ok=True)
print(f"chapters_cleaned={changed_chapters}")
