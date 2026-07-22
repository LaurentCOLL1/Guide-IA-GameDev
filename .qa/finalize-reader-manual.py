from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CH15 = ROOT / "Livre-II" / "CHAPITRE-15-Relations-sociales.md"
CH25 = ROOT / "Livre-II" / "CHAPITRE-25-Narration-quetes-codex-et-connaissances.md"
FILTER = ROOT / "filters" / "pdf-normalize.lua"
CONTINUITY = ROOT / "CONTINUITE-PROJET.md"
TIMESTAMP = "2026-07-22T12:34:00+02:00"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: attendu une occurrence, trouvé {count}")
    return text.replace(old, new, 1)


ch15 = CH15.read_text(encoding="utf-8")
ch15 = replace_once(
    ch15,
    "- [ ] Aucun PDF intermédiaire n’est produit.\n",
    "",
    "checklist PDF chapitre 15",
)
ch15 = replace_once(
    ch15,
    "## 34. Critères d’acceptation\n\nLe chapitre est acceptable au niveau documentaire lorsque :",
    "## 34. Critères de validation\n\nLa mise en œuvre respecte le contrat du chapitre lorsque :",
    "critères chapitre 15",
)
ch15 = replace_once(
    ch15,
    "12. le rapport d’audit post-création documente les réserves runtime.\n",
    "",
    "référence audit chapitre 15",
)
ch15, count = re.subn(
    r"\n## 35\. Tests à préparer\n.*?(?=\n## 36\. Réserves runtime\n)",
    "\n",
    ch15,
    count=1,
    flags=re.S,
)
if count != 1:
    raise RuntimeError("section Tests à préparer du chapitre 15 introuvable")
ch15 = replace_once(
    ch15,
    "Ce chapitre reste au niveau `static-review`.\n\n",
    "",
    "statut static-review chapitre 15",
)
ch15 = replace_once(
    ch15,
    "- la compilation PDF de fin de Livre.\n",
    "",
    "réserve PDF chapitre 15",
)
CH15.write_text(ch15, encoding="utf-8")

ch25 = CH25.read_text(encoding="utf-8")
ch25, count = re.subn(
    r"\n## 40\. Tests à préparer\n.*?(?=\n## 41\. Erreurs fréquentes et corrections\n)",
    "\n",
    ch25,
    count=1,
    flags=re.S,
)
if count != 1:
    raise RuntimeError("section Tests à préparer du chapitre 25 introuvable")
CH25.write_text(ch25, encoding="utf-8")

filter_text = FILTER.read_text(encoding="utf-8")
anchor = '  "reste donc au niveau static-review",\n'
if anchor not in filter_text:
    filter_text = filter_text.replace(
        '  "reste au niveau static-review",\n',
        '  "reste au niveau static-review",\n'
        '  "le statut reste static-review",\n'
        '  "reste donc static-review",\n',
        1,
    )
FILTER.write_text(filter_text, encoding="utf-8")

continuity = CONTINUITY.read_text(encoding="utf-8")
continuity = replace_once(
    continuity,
    'version: "3.30.3"',
    'version: "3.30.4"',
    "version continuité",
)
continuity, count = re.subn(
    r'^last-updated: ".*"$',
    f'last-updated: "{TIMESTAMP}"',
    continuity,
    count=1,
    flags=re.M,
)
if count != 1:
    raise RuntimeError("last-updated continuité introuvable")
entry = f"""### {TIMESTAMP} — version 3.30.4

- les derniers résidus de fabrication du manuel lecteur sont retirés des chapitres 15 et 25 ;
- les critères techniques du chapitre 15 sont conservés sous une formulation destinée au lecteur ;
- les sections obsolètes `Tests à préparer`, les statuts `static-review` visibles et les références au PDF intermédiaire sont exclus du manuel ;
- le filtre PDF reconnaît les variantes résiduelles de statut éditorial ;
- le plan maître enrichi du Livre III reste en version `1.1.0` et la prochaine action demeure son chapitre 1.

"""
anchor_journal = "## 27. Journal\n\n"
if anchor_journal not in continuity:
    raise RuntimeError("journal continuité introuvable")
continuity = continuity.replace(anchor_journal, anchor_journal + entry, 1)
CONTINUITY.write_text(continuity, encoding="utf-8")

for temporary in (
    ROOT / ".qa" / "l3-reader-validation-trigger.txt",
    Path(__file__),
):
    if temporary.exists():
        temporary.unlink()

print("Nettoyage sémantique final appliqué.")
