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


timestamp = datetime.now(ZoneInfo("Europe/Paris")).isoformat(timespec="seconds")

# CONTINUITE-PROJET.md
path = Path("CONTINUITE-PROJET.md")
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'version: "3.35.1"', 'version: "3.36.0"', "version continuité")
text = re.sub(
    r'last-updated: "[^"]+"',
    f'last-updated: "{timestamp}"',
    text,
    count=1,
)
text = replace_once(
    text,
    "**En cours : 5 chapitres sur 30.**",
    "**En cours : 6 chapitres sur 30.**",
    "progression Livre III",
)
text = replace_once(
    text,
    "5. Provenance, licences et validation des assets — terminé au niveau `static-review`.\n\n"
    "Les chapitres 6 à 30 restent définis dans `plans/LIVRE-III-PLAN-MAITRE.md`.",
    "5. Provenance, licences et validation des assets — terminé au niveau `static-review`.\n"
    "6. Création des humains — terminé au niveau `static-review`.\n\n"
    "Les chapitres 7 à 30 restent définis dans `plans/LIVRE-III-PLAN-MAITRE.md`.",
    "liste Livre III",
)
next_action = f'''## 26. Prochaine action

Le chapitre 6 du Livre III est rédigé, repéré et audité au niveau `static-review`. La base humaine documentaire couvre références anatomiques, proportions, topologie de déformation, modules, variantes morphologiques, préparation UV et matériaux, budgets LOD et scène Godot de validation. Aucun maillage, rig, export, scène ou résultat runtime n’est revendiqué comme matérialisé.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-III/CHAPITRE-07-Creation-des-humanoides.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 7 adaptera le contrat de la base humaine à des espèces humanoïdes distinctes, en documentant les écarts anatomiques, profils de rig, compatibilités d’équipement, variations culturelles et tests de silhouette sans produire les créatures non humanoïdes du chapitre 9.

'''
text, count = re.subn(
    r"## 26\. Prochaine action\n.*?(?=## 27\. Journal\n)",
    next_action,
    text,
    count=1,
    flags=re.S,
)
if count != 1:
    raise RuntimeError(f"section prochaine action: attendu 1 remplacement, trouvé {count}")

journal = f'''### {timestamp} — version 3.36.0

- chapitre 6 du Livre III créé, relu et audité au niveau `static-review` ;
- références anatomiques, proportions métriques, pose de construction et base neutre documentées ;
- topologie des épaules, coudes, hanches, genoux, mains et pieds encadrée ;
- modules, variantes morphologiques et séparation avec les données de gameplay définis ;
- préparation UV, matériaux, rig futur, export GLB et import Godot documentée ;
- budgets provisoires, profils LOD, scène de poses et protocole de mesure définis sans résultat runtime inventé ;
- dix erreurs fréquentes fournissent exemples fautifs, corrections et explications directes ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA provisoire et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 7 — Création des humanoïdes, niveau Élevée ;
- aucun maillage humain, rig, animation, export GLB, scène Godot, runtime ou PDF du Livre III produits.

'''
marker = "## 27. Journal\n\n"
text = replace_once(text, marker, marker + journal, "journal continuité")
path.write_text(text, encoding="utf-8")

# Livre-III/index.md
path = Path("Livre-III/index.md")
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'version: "1.4.0"', 'version: "1.5.0"', "version index")
text = replace_once(
    text,
    "5. [Provenance, licences et validation des assets](CHAPITRE-05-Provenance-licences-et-validation-des-assets.md)\n\n"
    "Les chapitres 6 à 30 seront ajoutés progressivement selon `plans/LIVRE-III-PLAN-MAITRE.md`.",
    "5. [Provenance, licences et validation des assets](CHAPITRE-05-Provenance-licences-et-validation-des-assets.md)\n"
    "6. [Création des humains](CHAPITRE-06-Creation-des-humains.md)\n\n"
    "Les chapitres 7 à 30 seront ajoutés progressivement selon `plans/LIVRE-III-PLAN-MAITRE.md`.",
    "index chapitre 6",
)
path.write_text(text, encoding="utf-8")

# ROADMAP.md
path = Path("ROADMAP.md")
text = path.read_text(encoding="utf-8")
text = replace_once(
    text,
    "- [x] Chapitre 5 — Provenance, licences et validation des assets.\n"
    "- [x] Préproduction et direction artistique — 5 chapitres sur 5.",
    "- [x] Chapitre 5 — Provenance, licences et validation des assets.\n"
    "- [x] Chapitre 6 — Création des humains.\n"
    "- [x] Préproduction et direction artistique — 5 chapitres sur 5.",
    "roadmap chapitre 6",
)
text = replace_once(
    text,
    "**Statut M4 : en cours — 5 chapitres rédigés, repérés et audités sur 30.**",
    "**Statut M4 : en cours — 6 chapitres rédigés, repérés et audités sur 30.**",
    "statut M4",
)
path.write_text(text, encoding="utf-8")

# contents.txt
path = Path("contents.txt")
text = path.read_text(encoding="utf-8")
text = replace_once(
    text,
    "Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md\n"
    "Livre-IV/index.md",
    "Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md\n"
    "Livre-III/CHAPITRE-06-Creation-des-humains.md\n"
    "Livre-IV/index.md",
    "ordre lecteur chapitre 6",
)
path.write_text(text, encoding="utf-8")

# plans/LIVRE-III-PLAN-MAITRE.md
path = Path("plans/LIVRE-III-PLAN-MAITRE.md")
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'version: "1.1.5"', 'version: "1.1.6"', "version plan")
text = re.sub(
    r'last-updated: "[^"]+"',
    f'last-updated: "{timestamp}"',
    text,
    count=1,
)
text = replace_once(
    text,
    "> **Statut :** en cours — 5 chapitres sur 30",
    "> **Statut :** en cours — 6 chapitres sur 30",
    "statut plan",
)
text = replace_once(
    text,
    "> **Progression :** chapitres 1 à 5 rédigés, repérés et audités au niveau `static-review` ; chapitres 6 à 30 à produire.",
    "> **Progression :** chapitres 1 à 6 rédigés, repérés et audités au niveau `static-review` ; chapitres 7 à 30 à produire.",
    "progression plan",
)
path.write_text(text, encoding="utf-8")

print(timestamp)
