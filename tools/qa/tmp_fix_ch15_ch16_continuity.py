from pathlib import Path

path = Path("CONTINUITE-PROJET.md")
text = path.read_text(encoding="utf-8")

replacements = {
    'version: "3.17.2"': 'version: "3.17.3"',
    '- chapitre 15 : version `1.0.0` ;': '- chapitre 15 : version `1.1.0` ;',
    '- chapitre 16 : version `1.0.0` ;': '- chapitre 16 : version `1.1.0` ;',
    '- chapitre 15 : 44 blocs significatifs contrôlés, 44 explications détaillées ajoutées ;': '- chapitre 15 : 56 blocs de code ou données contrôlés, 56 explications détaillées présentes ;',
    '- chapitre 16 : 43 blocs significatifs contrôlés, 43 explications détaillées ajoutées ;': '- chapitre 16 : 67 blocs de code ou données contrôlés, 67 explications détaillées présentes ;',
}

for old, new in replacements.items():
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"expected exactly one occurrence of {old!r}, got {count}")
    text = text.replace(old, new, 1)

anchor = "## 27. Journal\n"
entry = """## 27. Journal

### 2026-07-20 — version 3.17.3

- correction post-fusion de la source de vérité de continuité ;
- versions courantes des chapitres 15 et 16 corrigées de `1.0.0` vers `1.1.0` ;
- comptage final corrigé à 56 blocs expliqués pour le chapitre 15 et 67 pour le chapitre 16 ;
- aucune modification du contenu technique des chapitres ;
- aucun PDF construit et aucun test runtime revendiqué.
"""
if text.count(anchor) != 1:
    raise RuntimeError("journal anchor missing or duplicated")
text = text.replace(anchor, entry, 1)

path.write_text(text, encoding="utf-8")
