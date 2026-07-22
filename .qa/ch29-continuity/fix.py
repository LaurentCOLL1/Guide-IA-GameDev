#!/usr/bin/env python3
from pathlib import Path

PATH = Path("CONTINUITE-PROJET.md")
STAMP = "2026-07-22T05:14:39+02:00"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one occurrence, found {count}")
    return text.replace(old, new, 1)


text = PATH.read_text(encoding="utf-8")
text = replace_once(text, 'version: "3.29.0"', 'version: "3.29.1"', "version")
text = replace_once(
    text,
    'last-updated: "2026-07-22T04:30:00+02:00"',
    f'last-updated: "{STAMP}"',
    "timestamp",
)
text = replace_once(
    text,
    '**En cours : 27 chapitres sur 30.**',
    '**En cours : 29 chapitres sur 30.**',
    "collection progress",
)
text = replace_once(
    text,
    '28. Journalisation, diagnostic et reproductibilité.',
    '28. Journalisation, diagnostic et reproductibilité — terminé au niveau `static-review`.',
    "chapter 28 status",
)
text = replace_once(
    text,
    '29. Automatisation Python et génération de données.',
    '29. Automatisation Python et génération de données — terminé au niveau `static-review`.',
    "chapter 29 status",
)
text = replace_once(
    text,
    'Chapitres 3 à 27 : **Élevée**.',
    'Chapitres 3 à 29 : **Élevée**.',
    "reasoning range",
)
text = replace_once(
    text,
    '- ne pas employer le calque `durée murale` ; utiliser `durée réelle (durée basée sur l’horloge système)` ;\n- ne pas employer les calques `temps mur`, `temps mural` ou `temps horloge` ; utiliser `temps basé sur l\'horloge système` ;',
    '- ne pas employer les calques `durée murale`, `temps mur`, `temps mural` ou `temps horloge` ; utiliser `durée réelle (durée de l’horloge système)` et `horloge système` selon le contexte ;',
    "terminology rule",
)
journal = f'''### {STAMP} — version 3.29.1\n\n- compteur supérieur du Livre II aligné sur 29 chapitres sur 30 ;\n- chapitres 28 et 29 marqués terminés au niveau `static-review` dans la liste de collection ;\n- plage des niveaux de production alignée sur les chapitres 3 à 29 ;\n- terminologie temporelle harmonisée sur `durée réelle (durée de l’horloge système)` et `horloge système` ;\n- aucune modification du chapitre 29, aucun test runtime revendiqué et aucun PDF construit.\n\n'''
text = replace_once(text, '## 27. Journal\n\n', '## 27. Journal\n\n' + journal, "journal")
PATH.write_text(text, encoding="utf-8")

assert '**En cours : 29 chapitres sur 30.**' in text
assert 'Chapitres 3 à 29 : **Élevée**.' in text
assert 'durée réelle (durée de l’horloge système)' in text
print("Continuity governance aligned to chapter 29.")
