#!/usr/bin/env python3
import base64
import gzip
import hashlib
import json
from pathlib import Path

CREATED_AT = "2026-07-23T10:56:17+02:00"
EXPECTED_CHAPTER_SHA = "a39df80e5f6a37d9290f87464f02b5804d0193b262db3c6209560cc10e3e375c"
EXPECTED_AUDIT_SHA = "cf9a9fa649b59b07c7a70b1193fa1340291cbf9a18ce6b02e268bdc88e082a7e"

package_parts = [Path(f".qa/ch10-package-{index:02d}.txt") for index in range(1, 10)]
missing_parts = [str(path) for path in package_parts if not path.is_file()]
if missing_parts:
    raise RuntimeError("Fragments documentaires du chapitre 10 absents : " + ", ".join(missing_parts))

encoded_package = "".join(
    path.read_text(encoding="utf-8").strip()
    for path in package_parts
)
payload = json.loads(
    gzip.decompress(base64.b64decode(encoded_package)).decode("utf-8")
)
chapter_text = payload["chapter"]
audit_text = payload["audit"]
proof_text = payload["proof"].replace(
    "validated-base-commit: 379de646f8939d3e63e8964c35f6552ae1947081",
    "validated-base-commit: ec43d99f2baa7fa1210be172664b1820b23aa7ea",
    1,
)

if hashlib.sha256(chapter_text.encode("utf-8")).hexdigest() != EXPECTED_CHAPTER_SHA:
    raise RuntimeError("Empreinte du chapitre 10 invalide.")
if hashlib.sha256(audit_text.encode("utf-8")).hexdigest() != EXPECTED_AUDIT_SHA:
    raise RuntimeError("Empreinte de l'audit du chapitre 10 invalide.")

targets = {
    Path("Livre-III/CHAPITRE-10-Visages-peau-yeux-cheveux-et-pilosite.md"): chapter_text,
    Path("Livre-III/QA/AUDIT-CHAPITRE-10.md"): audit_text,
    Path("Livre-III/QA/VALIDATION-FINALE-CHAPITRE-10.yaml"): proof_text,
}
for target, content in targets.items():
    if target.exists():
        raise RuntimeError(f"Le fichier cible existe déjà: {target}")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")

for package_part in package_parts:
    package_part.unlink()

def replace_once(path: str, old: str, new: str) -> None:
    target = Path(path)
    text = target.read_text(encoding="utf-8")
    if old not in text:
        raise RuntimeError(f"Motif introuvable dans {path}: {old[:120]!r}")
    target.write_text(text.replace(old, new, 1), encoding="utf-8")

# Livre III index
replace_once(
    "Livre-III/index.md",
    'version: "1.8.0"',
    'version: "1.9.0"',
)
replace_once(
    "Livre-III/index.md",
    "8. [Création des animaux](CHAPITRE-08-Creation-des-animaux.md)\n"
    "9. [Création des créatures](CHAPITRE-09-Creation-des-creatures.md)\n\n"
    "Les chapitres 10 à 30 seront ajoutés progressivement selon `plans/LIVRE-III-PLAN-MAITRE.md`.",
    "8. [Création des animaux](CHAPITRE-08-Creation-des-animaux.md)\n"
    "9. [Création des créatures](CHAPITRE-09-Creation-des-creatures.md)\n"
    "10. [Visages, peau, yeux, cheveux et pilosité](CHAPITRE-10-Visages-peau-yeux-cheveux-et-pilosite.md)\n\n"
    "Les chapitres 11 à 30 seront ajoutés progressivement selon `plans/LIVRE-III-PLAN-MAITRE.md`.",
)

# Roadmap
replace_once(
    "ROADMAP.md",
    "- [x] Chapitre 9 — Création des créatures.\n"
    "- [x] Préproduction et direction artistique — 5 chapitres sur 5.",
    "- [x] Chapitre 9 — Création des créatures.\n"
    "- [x] Chapitre 10 — Visages, peau, yeux, cheveux et pilosité.\n"
    "- [x] Préproduction et direction artistique — 5 chapitres sur 5.",
)
replace_once(
    "ROADMAP.md",
    "**Statut M4 : en cours — 9 chapitres rédigés, repérés et audités sur 30.**",
    "**Statut M4 : en cours — 10 chapitres rédigés, repérés et audités sur 30.**",
)

# Ordre de compilation
replace_once(
    "contents.txt",
    "Livre-III/CHAPITRE-09-Creation-des-creatures.md\nLivre-IV/index.md",
    "Livre-III/CHAPITRE-09-Creation-des-creatures.md\n"
    "Livre-III/CHAPITRE-10-Visages-peau-yeux-cheveux-et-pilosite.md\n"
    "Livre-IV/index.md",
)

# Plan maître
replace_once(
    "plans/LIVRE-III-PLAN-MAITRE.md",
    'version: "1.1.9"',
    'version: "1.1.10"',
)
replace_once(
    "plans/LIVRE-III-PLAN-MAITRE.md",
    'last-updated: "2026-07-23T09:06:37+02:00"',
    f'last-updated: "{CREATED_AT}"',
)
replace_once(
    "plans/LIVRE-III-PLAN-MAITRE.md",
    "> **Statut :** en cours — 9 chapitres sur 30",
    "> **Statut :** en cours — 10 chapitres sur 30",
)
replace_once(
    "plans/LIVRE-III-PLAN-MAITRE.md",
    "> **Progression :** chapitres 1 à 9 rédigés, repérés et audités au niveau `static-review` ; chapitres 10 à 30 à produire.",
    "> **Progression :** chapitres 1 à 10 rédigés, repérés et audités au niveau `static-review` ; chapitres 11 à 30 à produire.",
)

# Continuité : métadonnées et état
replace_once(
    "CONTINUITE-PROJET.md",
    'version: "3.39.1"',
    'version: "3.40.0"',
)
replace_once(
    "CONTINUITE-PROJET.md",
    'last-updated: "2026-07-23T09:48:12+02:00"',
    f'last-updated: "{CREATED_AT}"',
)
replace_once(
    "CONTINUITE-PROJET.md",
    "- progression du Livre III : 9 chapitres sur 30 ;",
    "- progression du Livre III : 10 chapitres sur 30 ;",
)
replace_once(
    "CONTINUITE-PROJET.md",
    "- chapitre 9 du Livre III : version `1.0.0`, niveau `static-review` ;\n"
    "- Livre II : 30 chapitres sur 30, publication technique terminée ;",
    "- chapitre 9 du Livre III : version `1.0.0`, niveau `static-review` ;\n"
    "- chapitre 10 du Livre III : version `1.0.0`, niveau `static-review` ;\n"
    "- Livre II : 30 chapitres sur 30, publication technique terminée ;",
)

old_next = """Le chapitre 9 du Livre III est rédigé, repéré et audité au niveau `static-review`. Le système de création des créatures couvre brief fonctionnel, analogues qualifiés, niveaux de spéculation, masses, appuis, silhouettes, blockout métrique, anatomie inventée, topologie, profil de rig, sockets, proxies de collision, zones de lisibilité, poses d’action, variantes, LOD, export GLB et scène Godot de validation. Aucun concept final, modèle, rig, collision, socket, export, scène ou résultat runtime n’est revendiqué comme matérialisé.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-III/CHAPITRE-10-Visages-peau-yeux-cheveux-et-pilosite.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 10 approfondira le lookdev de gros plan des visages, de la peau, des yeux, des cheveux et de la pilosité, sans refaire les contrats anatomiques, de rig ou de collision du chapitre 9 ni anticiper l’animation faciale complète du chapitre 27."""

new_next = """Le chapitre 10 du Livre III est rédigé, repéré et audité au niveau `static-review`. Le système de lookdev facial couvre références et consentement, repères anatomiques, topologie de déformation, sculpture par niveaux, asymétrie contrôlée, formes faciales de test, peau, diffusion sous-surface, yeux, bouche, dents, cheveux, barbe, sourcils, cils, pilosité, transparence, LOD, export GLB et scène Godot de validation. Aucune tête finale, texture, matériau, œil, dentition, solution capillaire, blendshape, export, scène ou mesure runtime n’est revendiqué comme matérialisé.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-III/CHAPITRE-11-Vetements-armures-et-accessoires.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 11 créera un système d’équipement visuel modulaire pour vêtements, armures et accessoires, compatible avec les morphologies, l’animation, les collisions et les LOD, sans refaire le lookdev facial du chapitre 10 ni déplacer les règles d’inventaire et d’équipement du Livre II."""

replace_once("CONTINUITE-PROJET.md", old_next, new_next)

journal = f"""### {CREATED_AT} — version 3.40.0

- chapitre 10 du Livre III créé, relu et audité au niveau `static-review` ;
- tête pilote `AST-CHR-FACE-PILOT-001` encadrée par un brief de gros plan et des caméras de référence ;
- provenance, consentement, diversité des références et risques de perspective documentés ;
- repères anatomiques, topologie, sculpture primaire-secondaire-tertiaire et asymétrie contrôlée encadrés ;
- profils de peau, diffusion sous-surface, œil, bouche, dents et intersections préparés ;
- cheveux, hair cards, groom, sourcils, cils, barbe, duvet, transparence et overdraw documentés ;
- formes faciales limitées aux tests de déformation, sans visèmes ni timings du chapitre 27 ;
- LOD, export GLB, scène Godot dérivée, validateur structurel et campagne de performance documentés ;
- dix erreurs fréquentes fournissent symptômes, exemples fautifs, corrections et explications directes ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA provisoire et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 11 — Vêtements, armures et accessoires, niveau Élevée ;
- aucune tête, texture, matériau, œil, dentition, solution capillaire, blendshape, export GLB, scène Godot, runtime ou PDF du Livre III produits.

"""
replace_once(
    "CONTINUITE-PROJET.md",
    "## 27. Journal\n\n",
    "## 27. Journal\n\n" + journal,
)

print("Chapter 10 governance applied.")
