#!/usr/bin/env python3
import base64
import gzip
import hashlib
import json
from pathlib import Path

CREATED_AT = "2026-07-23T11:50:40+02:00"
EXPECTED_CHAPTER_SHA = "70862593df9ea757123d6285f1cecd12e621ed02ce48111723af6632c1e0a874"
EXPECTED_AUDIT_SHA = "939e775c3bfdb1c46398426ee14aa48262f3fe673a65433b1caa34571582a4af"

package_parts = [
    Path(".qa/ch11-package-01.txt"),
    Path(".qa/ch11-package-02.txt"),
    Path(".qa/ch11-package-03a.txt"),
    Path(".qa/ch11-package-03b.txt"),
    Path(".qa/ch11-package-04a.txt"),
    Path(".qa/ch11-package-04b.txt"),
]
missing_parts = [str(path) for path in package_parts if not path.is_file()]
if missing_parts:
    raise RuntimeError("Fragments documentaires du chapitre 11 absents : " + ", ".join(missing_parts))

encoded_package = "".join(path.read_text(encoding="utf-8").strip() for path in package_parts)
payload = json.loads(gzip.decompress(base64.b64decode(encoded_package)).decode("utf-8"))
chapter_text = payload["chapter"]
audit_text = payload["audit"]
proof_text = payload["proof"]

if hashlib.sha256(chapter_text.encode("utf-8")).hexdigest() != EXPECTED_CHAPTER_SHA:
    raise RuntimeError("Empreinte du chapitre 11 invalide.")
if hashlib.sha256(audit_text.encode("utf-8")).hexdigest() != EXPECTED_AUDIT_SHA:
    raise RuntimeError("Empreinte de l'audit du chapitre 11 invalide.")

targets = {
    Path("Livre-III/CHAPITRE-11-Vetements-armures-et-accessoires.md"): chapter_text,
    Path("Livre-III/QA/AUDIT-CHAPITRE-11.md"): audit_text,
    Path("Livre-III/QA/VALIDATION-FINALE-CHAPITRE-11.yaml"): proof_text,
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
        raise RuntimeError(f"Motif introuvable dans {path}: {old[:160]!r}")
    target.write_text(text.replace(old, new, 1), encoding="utf-8")


# Livre III index
replace_once("Livre-III/index.md", 'version: "1.9.0"', 'version: "1.10.0"')
replace_once(
    "Livre-III/index.md",
    "9. [Création des créatures](CHAPITRE-09-Creation-des-creatures.md)\n"
    "10. [Visages, peau, yeux, cheveux et pilosité](CHAPITRE-10-Visages-peau-yeux-cheveux-et-pilosite.md)\n\n"
    "Les chapitres 11 à 30 seront ajoutés progressivement selon `plans/LIVRE-III-PLAN-MAITRE.md`.",
    "9. [Création des créatures](CHAPITRE-09-Creation-des-creatures.md)\n"
    "10. [Visages, peau, yeux, cheveux et pilosité](CHAPITRE-10-Visages-peau-yeux-cheveux-et-pilosite.md)\n"
    "11. [Vêtements, armures et accessoires](CHAPITRE-11-Vetements-armures-et-accessoires.md)\n\n"
    "Les chapitres 12 à 30 seront ajoutés progressivement selon `plans/LIVRE-III-PLAN-MAITRE.md`.",
)

# Roadmap
replace_once(
    "ROADMAP.md",
    "- [x] Chapitre 10 — Visages, peau, yeux, cheveux et pilosité.\n"
    "- [x] Préproduction et direction artistique — 5 chapitres sur 5.",
    "- [x] Chapitre 10 — Visages, peau, yeux, cheveux et pilosité.\n"
    "- [x] Chapitre 11 — Vêtements, armures et accessoires.\n"
    "- [x] Préproduction et direction artistique — 5 chapitres sur 5.",
)
replace_once(
    "ROADMAP.md",
    "**Statut M4 : en cours — 10 chapitres rédigés, repérés et audités sur 30.**",
    "**Statut M4 : en cours — 11 chapitres rédigés, repérés et audités sur 30.**",
)

# Ordre de compilation
replace_once(
    "contents.txt",
    "Livre-III/CHAPITRE-10-Visages-peau-yeux-cheveux-et-pilosite.md\nLivre-IV/index.md",
    "Livre-III/CHAPITRE-10-Visages-peau-yeux-cheveux-et-pilosite.md\n"
    "Livre-III/CHAPITRE-11-Vetements-armures-et-accessoires.md\n"
    "Livre-IV/index.md",
)

# Plan maître
replace_once("plans/LIVRE-III-PLAN-MAITRE.md", 'version: "1.1.10"', 'version: "1.1.11"')
replace_once(
    "plans/LIVRE-III-PLAN-MAITRE.md",
    'last-updated: "2026-07-23T10:56:17+02:00"',
    f'last-updated: "{CREATED_AT}"',
)
replace_once(
    "plans/LIVRE-III-PLAN-MAITRE.md",
    "> **Statut :** en cours — 10 chapitres sur 30",
    "> **Statut :** en cours — 11 chapitres sur 30",
)
replace_once(
    "plans/LIVRE-III-PLAN-MAITRE.md",
    "> **Progression :** chapitres 1 à 10 rédigés, repérés et audités au niveau `static-review` ; chapitres 11 à 30 à produire.",
    "> **Progression :** chapitres 1 à 11 rédigés, repérés et audités au niveau `static-review` ; chapitres 12 à 30 à produire.",
)

# Continuité : métadonnées et état
replace_once("CONTINUITE-PROJET.md", 'version: "3.40.1"', 'version: "3.41.0"')
replace_once(
    "CONTINUITE-PROJET.md",
    'last-updated: "2026-07-23T11:14:44+02:00"',
    f'last-updated: "{CREATED_AT}"',
)
replace_once(
    "CONTINUITE-PROJET.md",
    "- progression du Livre III : 10 chapitres sur 30 ;",
    "- progression du Livre III : 11 chapitres sur 30 ;",
)
replace_once(
    "CONTINUITE-PROJET.md",
    "- chapitre 10 du Livre III : version `1.0.0`, niveau `static-review` ;\n"
    "- Livre II : 30 chapitres sur 30, publication technique terminée ;",
    "- chapitre 10 du Livre III : version `1.0.0`, niveau `static-review` ;\n"
    "- chapitre 11 du Livre III : version `1.0.0`, niveau `static-review` ;\n"
    "- Livre II : 30 chapitres sur 30, publication technique terminée ;",
)

old_next = """Le chapitre 10 du Livre III est rédigé, repéré et audité au niveau `static-review`. Le système de lookdev facial couvre références et consentement, repères anatomiques, topologie de déformation, sculpture par niveaux, asymétrie contrôlée, formes faciales de test, peau, diffusion sous-surface, yeux, bouche, dents, cheveux, barbe, sourcils, cils, pilosité, transparence, LOD, export GLB et scène Godot de validation. Aucune tête finale, texture, matériau, œil, dentition, solution capillaire, blendshape, export, scène ou mesure runtime n’est revendiqué comme matérialisé.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-III/CHAPITRE-11-Vetements-armures-et-accessoires.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 11 créera un système d’équipement visuel modulaire pour vêtements, armures et accessoires, compatible avec les morphologies, l’animation, les collisions et les LOD, sans refaire le lookdev facial du chapitre 10 ni déplacer les règles d’inventaire et d’équipement du Livre II."""

new_next = """Le chapitre 11 du Livre III est rédigé, repéré et audité au niveau `static-review`. Le système d’équipement visuel porté couvre kit pilote, layering, profils morphologiques, patrons, marges, topologie, skinning, rigidité, attaches, proxies de collision, simulation Blender qualifiée, conversion, clipping, masques corporels, matériaux, variantes, LOD, matrice de compatibilité, export GLB et scène Godot de validation. Aucun vêtement, armure, accessoire, patron, poids, simulation, collision, masque, atlas, LOD, export, scène ou résultat runtime n’est revendiqué comme matérialisé.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-III/CHAPITRE-12-Objets-equipements-et-armes.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 12 produira des objets, équipements et armes cohérents avec leur usage, leur échelle, leurs pivots, sockets, collisions, états visuels et LOD, sans refaire les vêtements portés du chapitre 11 ni déplacer les règles d’inventaire, de dégâts et de combat du Livre II."""
replace_once("CONTINUITE-PROJET.md", old_next, new_next)

journal = f"""### {CREATED_AT} — version 3.41.0

- chapitre 11 du Livre III créé, relu et audité au niveau `static-review` ;
- kit pilote `AST-WEAR-KIT-WARDEN-001` encadré par catégories de comportement et cas d’usage ;
- layering, conflits, prérequis, profils morphologiques et matrice de compatibilité documentés ;
- patrons, marges de mouvement, blockout, topologie, coutures et épaisseurs encadrés ;
- transfert de poids, skinning, rigidité locale, armures et attaches préparés ;
- proxies de collision, simulation Blender, conversion et frontière runtime Godot explicités ;
- clipping, masques corporels réversibles, matériaux, variantes et LOD documentés ;
- export GLB, scène Godot dérivée, validateur structurel et campagne de performance préparés ;
- dix erreurs fréquentes fournissent symptômes, exemples fautifs, corrections et explications directes ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA provisoire et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 12 — Objets, équipements et armes, niveau Élevée ;
- aucun vêtement, armure, accessoire, patron, skinning, simulation, collision, masque, atlas, LOD, export GLB, scène Godot, runtime ou PDF du Livre III produits.

"""
replace_once("CONTINUITE-PROJET.md", "## 27. Journal\n\n", "## 27. Journal\n\n" + journal)

print("Chapter 11 governance applied.")
