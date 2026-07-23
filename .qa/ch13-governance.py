#!/usr/bin/env python3
import hashlib
import os
from pathlib import Path

TIMESTAMP = "2026-07-23T14:35:47+02:00"
BASE_COMMIT = os.environ["BASE_COMMIT"]
CHAPTER_PATH = Path("Livre-III/CHAPITRE-13-Architecture-batiments-et-kits-modulaires.md")
AUDIT_PATH = Path("Livre-III/QA/AUDIT-CHAPITRE-13.md")
PROOF_PATH = Path("Livre-III/QA/VALIDATION-FINALE-CHAPITRE-13.yaml")
EXPECTED_CHAPTER_SHA = "fb9835f62e40f33091db48662ed16bb629002ca396b7e5972ce4767b6b3d54c9"
EXPECTED_AUDIT_SHA = "48defcdb19887a51643c87d3ad2aa02d37792c5d42409d1d9508b511d255af0e"

def replace_once(text: str, old: str, new: str, label: str) -> str:
    if text.count(old) != 1:
        raise RuntimeError(f"Remplacement {label} attendu une fois, trouvé {text.count(old)}.")
    return text.replace(old, new, 1)

if hashlib.sha256(CHAPTER_PATH.read_bytes()).hexdigest() != EXPECTED_CHAPTER_SHA:
    raise RuntimeError("Empreinte du chapitre 13 invalide avant gouvernance.")
if hashlib.sha256(AUDIT_PATH.read_bytes()).hexdigest() != EXPECTED_AUDIT_SHA:
    raise RuntimeError("Empreinte de l'audit reconstruit invalide avant gouvernance.")

proof = PROOF_PATH.read_text(encoding="utf-8")
proof = replace_once(
    proof,
    "validated-base-commit: BASE_COMMIT_PLACEHOLDER",
    f"validated-base-commit: {BASE_COMMIT}",
    "base de preuve",
)
PROOF_PATH.write_text(proof, encoding="utf-8")

continuity_path = Path("CONTINUITE-PROJET.md")
continuity = continuity_path.read_text(encoding="utf-8")
continuity = replace_once(continuity, 'version: "3.42.1"', 'version: "3.43.0"', "version continuité")
continuity = replace_once(
    continuity,
    'last-updated: "2026-07-23T14:07:25+02:00"',
    f'last-updated: "{TIMESTAMP}"',
    "date continuité",
)
old_collection = """### Livre III

**En cours : 9 chapitres sur 30.**

1. Préproduction et cahier des charges artistique — terminé au niveau `static-review`.
2. Direction artistique et bible visuelle — terminé au niveau `static-review`.
3. Références, concept art et ComfyUI — terminé au niveau `static-review`.
4. Pipeline Blender et organisation des fichiers — terminé au niveau `static-review`.
5. Provenance, licences et validation des assets — terminé au niveau `static-review`.
6. Création des humains — terminé au niveau `static-review`.
7. Création des humanoïdes — terminé au niveau `static-review`.
8. Création des animaux — terminé au niveau `static-review`.
9. Création des créatures — terminé au niveau `static-review`.

Les chapitres 10 à 30 restent définis dans `plans/LIVRE-III-PLAN-MAITRE.md`.
"""
new_collection = """### Livre III

**En cours : 13 chapitres sur 30.**

1. Préproduction et cahier des charges artistique — terminé au niveau `static-review`.
2. Direction artistique et bible visuelle — terminé au niveau `static-review`.
3. Références, concept art et ComfyUI — terminé au niveau `static-review`.
4. Pipeline Blender et organisation des fichiers — terminé au niveau `static-review`.
5. Provenance, licences et validation des assets — terminé au niveau `static-review`.
6. Création des humains — terminé au niveau `static-review`.
7. Création des humanoïdes — terminé au niveau `static-review`.
8. Création des animaux — terminé au niveau `static-review`.
9. Création des créatures — terminé au niveau `static-review`.
10. Visages, peau, yeux, cheveux et pilosité — terminé au niveau `static-review`.
11. Vêtements, armures et accessoires — terminé au niveau `static-review`.
12. Objets, équipements et armes — terminé au niveau `static-review`.
13. Architecture, bâtiments et kits modulaires — terminé au niveau `static-review`.

Les chapitres 14 à 30 restent définis dans `plans/LIVRE-III-PLAN-MAITRE.md`.
"""
continuity = replace_once(continuity, old_collection, new_collection, "synthèse collection Livre III")
continuity = replace_once(
    continuity,
    "- progression du Livre III : 12 chapitres sur 30 ;",
    "- progression du Livre III : 13 chapitres sur 30 ;",
    "progression courante",
)
continuity = replace_once(
    continuity,
    "- chapitre 12 du Livre III : version `1.0.0`, niveau `static-review` ;",
    "- chapitre 12 du Livre III : version `1.0.0`, niveau `static-review` ;\n- chapitre 13 du Livre III : version `1.0.0`, niveau `static-review` ;",
    "chapitre 13 état courant",
)
next_start = continuity.index("## 26. Prochaine action")
journal_start = continuity.index("## 27. Journal", next_start)
new_next = """## 26. Prochaine action

Le chapitre 13 du Livre III est rédigé, repéré et audité au niveau `static-review`. Le kit architectural couvre métriques humaines, grille, catalogue de modules, connecteurs, règles d’assemblage, murs, ouvertures, coins, transitions, sols, escaliers, toitures, intérieurs, pivots, snapping, tolérances, collisions, navigation, occlusion, états visuels de destruction, matériaux partagés, variantes, LOD, HLOD, export GLB, scènes Godot dérivées, `GridMap`, `MeshLibrary` et campagnes de validation. Aucun module, bâtiment, collision, navigation, occluder, matériau, atlas, LOD, HLOD, export, scène ou résultat runtime n’est revendiqué comme matérialisé.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-III/CHAPITRE-14-Terrains-paysages-et-mondes-ouverts.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 14 produira un terrain pilote, un découpage spatial, des raccords avec les bâtiments, des profils de streaming, des matériaux de terrain et une scène de benchmark, sans refaire les kits architecturaux du chapitre 13 ni déplacer la simulation écologique du Livre II.

"""
continuity = continuity[:next_start] + new_next + continuity[journal_start:]
journal_entry = f"""## 27. Journal

### {TIMESTAMP} — version 3.43.0

- chapitre 13 du Livre III récupéré avec son empreinte originale, relu et audité au niveau `static-review` ;
- audit QA reconstruit depuis le chapitre vérifié, le plan maître et le protocole après corruption du conteneur de transport temporaire ;
- kit pilote `AST-ARCH-KIT-WAYSTATION-001`, grille, modules, connecteurs, tolérances et porte de blockout à trois bâtiments documentés ;
- murs, ouvertures, coins, transitions, sols, escaliers, toitures, intérieurs et variantes encadrés ;
- rendu, collisions, navigation et occlusion séparés ; destruction limitée à une préparation visuelle ;
- scènes modulaires, `GridMap`, `MeshLibrary`, LOD de module et HLOD de bâtiment documentés ;
- métriques statiques : 2 381 lignes, 63 titres, 69 blocs significatifs, 49 explications structurées et dix diagnostics ;
- synthèse supérieure du Livre III corrigée de 9/30 à 13/30 pour rejoindre l’état courant et les preuves ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA provisoire et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 14 — Terrains, paysages et mondes ouverts, niveau Élevée ;
- aucun module, bâtiment, collision, navigation, occluder, matériau, atlas, LOD, HLOD, GLB, scène Godot, runtime ou PDF du Livre III produits.

"""
continuity = replace_once(continuity, "## 27. Journal\n\n", journal_entry, "journal continuité")
continuity_path.write_text(continuity, encoding="utf-8")

index_path = Path("Livre-III/index.md")
index = index_path.read_text(encoding="utf-8")
index = replace_once(index, 'version: "1.11.0"', 'version: "1.12.0"', "version index")
index = replace_once(
    index,
    "12. [Objets, équipements et armes](CHAPITRE-12-Objets-equipements-et-armes.md)\n\nLes chapitres 13 à 30",
    "12. [Objets, équipements et armes](CHAPITRE-12-Objets-equipements-et-armes.md)\n13. [Architecture, bâtiments et kits modulaires](CHAPITRE-13-Architecture-batiments-et-kits-modulaires.md)\n\nLes chapitres 14 à 30",
    "entrée index chapitre 13",
)
index_path.write_text(index, encoding="utf-8")

roadmap_path = Path("ROADMAP.md")
roadmap = roadmap_path.read_text(encoding="utf-8")
roadmap = replace_once(
    roadmap,
    "- [x] Chapitre 12 — Objets, équipements et armes.\n",
    "- [x] Chapitre 12 — Objets, équipements et armes.\n- [x] Chapitre 13 — Architecture, bâtiments et kits modulaires.\n",
    "roadmap chapitre 13",
)
roadmap = replace_once(
    roadmap,
    "**Statut M4 : en cours — 12 chapitres rédigés, repérés et audités sur 30.**",
    "**Statut M4 : en cours — 13 chapitres rédigés, repérés et audités sur 30.**",
    "statut M4",
)
roadmap_path.write_text(roadmap, encoding="utf-8")

contents_path = Path("contents.txt")
contents = contents_path.read_text(encoding="utf-8")
contents = replace_once(
    contents,
    "Livre-III/CHAPITRE-12-Objets-equipements-et-armes.md\nLivre-IV/index.md",
    "Livre-III/CHAPITRE-12-Objets-equipements-et-armes.md\nLivre-III/CHAPITRE-13-Architecture-batiments-et-kits-modulaires.md\nLivre-IV/index.md",
    "ordre lecteur chapitre 13",
)
contents_path.write_text(contents, encoding="utf-8")

plan_path = Path("plans/LIVRE-III-PLAN-MAITRE.md")
plan = plan_path.read_text(encoding="utf-8")
plan = replace_once(plan, 'version: "1.1.12"', 'version: "1.1.13"', "version plan")
plan = replace_once(
    plan,
    'last-updated: "2026-07-23T13:30:28+02:00"',
    f'last-updated: "{TIMESTAMP}"',
    "date plan",
)
plan = replace_once(
    plan,
    "> **Statut :** en cours — 12 chapitres sur 30",
    "> **Statut :** en cours — 13 chapitres sur 30",
    "statut plan",
)
plan_path.write_text(plan, encoding="utf-8")
