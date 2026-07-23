#!/usr/bin/env python3
import base64
import gzip
import hashlib
import os
from pathlib import Path

CREATED_AT = "2026-07-23T13:30:28+02:00"
EXPECTED_CHAPTER_SHA = "73905a954ffe28f11fb1e8f9350df80969829a9520cfa4bd98c2f9e620f960ac"
EXPECTED_AUDIT_SHA = "c8196c7ed13377c180011844cc1e269f7721328b3746d21ff708bdd39bb31856"
BASE_COMMIT = os.environ["BASE_COMMIT"]

chapter_path = Path("Livre-III/CHAPITRE-12-Objets-equipements-et-armes.md")
audit_path = Path("Livre-III/QA/AUDIT-CHAPITRE-12.md")
proof_path = Path("Livre-III/QA/VALIDATION-FINALE-CHAPITRE-12.yaml")

chapter_parts = [Path(f".qa/ch12-chapter-{index:02d}.txt") for index in range(1, 6)]
if all(path.is_file() for path in chapter_parts):
    encoded = "".join(path.read_text(encoding="utf-8").strip() for path in chapter_parts)
    chapter_path.write_bytes(gzip.decompress(base64.b64decode(encoded)))
    for path in chapter_parts:
        path.unlink()
elif any(path.is_file() for path in chapter_parts):
    missing = [str(path) for path in chapter_parts if not path.is_file()]
    raise RuntimeError("Fragments exacts du chapitre 12 incomplets : " + ", ".join(missing))

for target in (chapter_path, audit_path, proof_path):
    if not target.is_file():
        raise RuntimeError(f"Fichier du chapitre 12 absent : {target}")

if hashlib.sha256(chapter_path.read_bytes()).hexdigest() != EXPECTED_CHAPTER_SHA:
    raise RuntimeError("Empreinte du chapitre 12 invalide.")
if hashlib.sha256(audit_path.read_bytes()).hexdigest() != EXPECTED_AUDIT_SHA:
    raise RuntimeError("Empreinte de l'audit du chapitre 12 invalide.")

proof = proof_path.read_text(encoding="utf-8")
placeholder = "validated-base-commit: BASE_COMMIT_PLACEHOLDER"
replacement = f"validated-base-commit: {BASE_COMMIT}"
if placeholder not in proof:
    raise RuntimeError("Base provisoire de la preuve introuvable.")
proof_path.write_text(proof.replace(placeholder, replacement, 1), encoding="utf-8")

def replace_once(path: str, old: str, new: str) -> None:
    target = Path(path)
    text = target.read_text(encoding="utf-8")
    if old not in text:
        raise RuntimeError(f"Motif introuvable dans {path}: {old[:120]!r}")
    target.write_text(text.replace(old, new, 1), encoding="utf-8")

# Livre III index
replace_once("Livre-III/index.md", 'version: "1.10.0"', 'version: "1.11.0"')
replace_once(
    "Livre-III/index.md",
    "10. [Visages, peau, yeux, cheveux et pilosité](CHAPITRE-10-Visages-peau-yeux-cheveux-et-pilosite.md)\n"
    "11. [Vêtements, armures et accessoires](CHAPITRE-11-Vetements-armures-et-accessoires.md)\n\n"
    "Les chapitres 12 à 30 seront ajoutés progressivement selon `plans/LIVRE-III-PLAN-MAITRE.md`.",
    "10. [Visages, peau, yeux, cheveux et pilosité](CHAPITRE-10-Visages-peau-yeux-cheveux-et-pilosite.md)\n"
    "11. [Vêtements, armures et accessoires](CHAPITRE-11-Vetements-armures-et-accessoires.md)\n"
    "12. [Objets, équipements et armes](CHAPITRE-12-Objets-equipements-et-armes.md)\n\n"
    "Les chapitres 13 à 30 seront ajoutés progressivement selon `plans/LIVRE-III-PLAN-MAITRE.md`."
)

# Roadmap
replace_once(
    "ROADMAP.md",
    "- [x] Chapitre 11 — Vêtements, armures et accessoires.\n"
    "- [x] Préproduction et direction artistique — 5 chapitres sur 5.",
    "- [x] Chapitre 11 — Vêtements, armures et accessoires.\n"
    "- [x] Chapitre 12 — Objets, équipements et armes.\n"
    "- [x] Préproduction et direction artistique — 5 chapitres sur 5."
)
replace_once(
    "ROADMAP.md",
    "**Statut M4 : en cours — 11 chapitres rédigés, repérés et audités sur 30.**",
    "**Statut M4 : en cours — 12 chapitres rédigés, repérés et audités sur 30.**"
)

# Ordre de compilation
replace_once(
    "contents.txt",
    "Livre-III/CHAPITRE-11-Vetements-armures-et-accessoires.md\nLivre-IV/index.md",
    "Livre-III/CHAPITRE-11-Vetements-armures-et-accessoires.md\n"
    "Livre-III/CHAPITRE-12-Objets-equipements-et-armes.md\n"
    "Livre-IV/index.md"
)

# Plan maître
replace_once("plans/LIVRE-III-PLAN-MAITRE.md", 'version: "1.1.11"', 'version: "1.1.12"')
replace_once(
    "plans/LIVRE-III-PLAN-MAITRE.md",
    'last-updated: "2026-07-23T11:50:40+02:00"',
    f'last-updated: "{CREATED_AT}"'
)
replace_once(
    "plans/LIVRE-III-PLAN-MAITRE.md",
    "> **Statut :** en cours — 11 chapitres sur 30",
    "> **Statut :** en cours — 12 chapitres sur 30"
)
replace_once(
    "plans/LIVRE-III-PLAN-MAITRE.md",
    "> **Progression :** chapitres 1 à 11 rédigés, repérés et audités au niveau `static-review` ; chapitres 12 à 30 à produire.",
    "> **Progression :** chapitres 1 à 12 rédigés, repérés et audités au niveau `static-review` ; chapitres 13 à 30 à produire."
)

# Continuité
replace_once("CONTINUITE-PROJET.md", 'version: "3.41.1"', 'version: "3.42.0"')
replace_once(
    "CONTINUITE-PROJET.md",
    'last-updated: "2026-07-23T12:33:11+02:00"',
    f'last-updated: "{CREATED_AT}"'
)
replace_once(
    "CONTINUITE-PROJET.md",
    "- progression du Livre III : 11 chapitres sur 30 ;",
    "- progression du Livre III : 12 chapitres sur 30 ;"
)
replace_once(
    "CONTINUITE-PROJET.md",
    "- chapitre 11 du Livre III : version `1.0.0`, niveau `static-review` ;\n"
    "- Livre II : 30 chapitres sur 30, publication technique terminée ;",
    "- chapitre 11 du Livre III : version `1.0.0`, niveau `static-review` ;\n"
    "- chapitre 12 du Livre III : version `1.0.0`, niveau `static-review` ;\n"
    "- Livre II : 30 chapitres sur 30, publication technique terminée ;"
)

old_next = """Le chapitre 11 du Livre III est rédigé, repéré et audité au niveau `static-review`. Le système d’équipement visuel porté couvre kit pilote, layering, profils morphologiques, patrons, marges, topologie, skinning, rigidité, attaches, proxies de collision, simulation Blender qualifiée, conversion, clipping, masques corporels, matériaux, variantes, LOD, matrice de compatibilité, export GLB et scène Godot de validation. Aucun vêtement, armure, accessoire, patron, poids, simulation, collision, masque, atlas, LOD, export, scène ou résultat runtime n’est revendiqué comme matérialisé.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-III/CHAPITRE-12-Objets-equipements-et-armes.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 12 produira des objets, équipements et armes cohérents avec leur usage, leur échelle, leurs pivots, sockets, collisions, états visuels et LOD, sans refaire les vêtements portés du chapitre 11 ni déplacer les règles d’inventaire, de dégâts et de combat du Livre II."""

new_next = """Le chapitre 12 du Livre III est rédigé, repéré et audité au niveau `static-review`. La bibliothèque d’objets couvre fonctions observables, références dimensionnelles, ergonomie, échelle, axes, origines, pivots, prises, sockets de rangement et d’environnement, pièces mobiles, collisions d’interaction, physiques et d’impact, états visuels, variantes, LOD, export GLB et scènes Godot de validation. Aucun objet, outil, arme, pivot, socket, collision, matériau, atlas, LOD, export, scène ou résultat runtime n’est revendiqué comme matérialisé.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-III/CHAPITRE-13-Architecture-batiments-et-kits-modulaires.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 13 créera des kits architecturaux modulaires fondés sur une grille métrique, des règles d’assemblage, des pivots de snapping, des collisions, de la navigation, de l’occlusion et des LOD, sans refaire les objets individuels du chapitre 12 ni déplacer les règles de construction par le joueur du Livre II."""

replace_once("CONTINUITE-PROJET.md", old_next, new_next)

journal = f"""### {CREATED_AT} — version 3.42.0

- chapitre 12 du Livre III créé, relu et audité au niveau `static-review` ;
- bibliothèque pilote `AST-PROP-KIT-EXPLORER-001` encadrée par cinq objets aux contraintes distinctes ;
- fonctions observables, références dimensionnelles, ergonomie, échelle et gabarits documentés ;
- axes, origines, pivots, prises, sockets de rangement, environnement et émission encadrés ;
- pièces mobiles, silhouette, blockout, topologie, ombrage et matériaux provisoires préparés ;
- interaction, physique, impact et émission séparés en profils de collision distincts ;
- états visuels, variantes, dégradation, LOD et représentations fonctionnelles documentés ;
- export GLB, scènes Godot dérivées, validateur structurel et campagnes de mesure préparés ;
- dix erreurs fréquentes fournissent symptômes, exemples fautifs, corrections et explications directes ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA provisoire et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 13 — Architecture, bâtiments et kits modulaires, niveau Élevée ;
- aucun objet, outil, arme, pivot, socket, collision, matériau, atlas, LOD, export GLB, scène Godot, runtime ou PDF du Livre III produits.

"""
replace_once("CONTINUITE-PROJET.md", "## 27. Journal\n\n", "## 27. Journal\n\n" + journal)

print("Chapter 12 governance applied.")
