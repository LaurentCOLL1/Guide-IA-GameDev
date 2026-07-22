from __future__ import annotations

import re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: attendu 1 occurrence, trouvé {count}")
    return text.replace(old, new, 1)


path = Path("CONTINUITE-PROJET.md")
text = path.read_text(encoding="utf-8")
timestamp = datetime.now(ZoneInfo("Europe/Paris")).isoformat(timespec="seconds")

text = replace_once(text, 'version: "3.36.1"', 'version: "3.36.2"', "version continuité")
text = re.sub(
    r'last-updated: "[^"]+"',
    f'last-updated: "{timestamp}"',
    text,
    count=1,
)
text = replace_once(
    text,
    "- progression du Livre III : 5 chapitres sur 30 ;",
    "- progression du Livre III : 6 chapitres sur 30 ;",
    "progression de l'état courant",
)
text = replace_once(
    text,
    "- chapitre 5 du Livre III : version `1.0.0`, niveau `static-review` ;\n"
    "- Livre II : 30 chapitres sur 30, publication technique terminée ;",
    "- chapitre 5 du Livre III : version `1.0.0`, niveau `static-review` ;\n"
    "- chapitre 6 du Livre III : version `1.0.0`, niveau `static-review` ;\n"
    "- Livre II : 30 chapitres sur 30, publication technique terminée ;",
    "entrée chapitre 6 de l'état courant",
)

journal = f'''### {timestamp} — version 3.36.2

- correction de cohérence de la section `État courant` après la fusion du chapitre 6 ;
- progression du Livre III alignée de 5 à 6 chapitres sur 30 ;
- chapitre 6 ajouté à la liste des versions courantes en `1.0.0`, niveau `static-review` ;
- prochaine action, preuve QA, empreintes et périmètre documentaire inchangés ;
- aucun asset, runtime ou PDF produit par cette correction de gouvernance.

'''
marker = "## 27. Journal\n\n"
text = replace_once(text, marker, marker + journal, "journal continuité")
path.write_text(text, encoding="utf-8")
print(timestamp)

# runner-trigger
