from __future__ import annotations

import base64
import hashlib
import lzma
from pathlib import Path

TIMESTAMP = "2026-07-22T22:25:35+02:00"
CHAPTER = "Livre-III/CHAPITRE-04-Pipeline-Blender-et-organisation-des-fichiers.md"
CHAPTER_SHA256 = "9d8cce0ea1a4ff51405a45117b0843290321fb9108edb2f7325459271a69278b"
AUDIT_SHA256 = "6edc688a059bac1c1cc9b0bad766a9ca22fed74f739cb83b860abde4e5faf89b"
PROOF_SHA256 = "c5a0df832d4943a40ae0f13f9f4c40a0d9f191bac987978ff5fdf98702253cc1"


def replace_once(path: str, old: str, new: str) -> None:
    target = Path(path)
    content = target.read_text(encoding="utf-8")
    count = content.count(old)
    if count != 1:
        raise RuntimeError(f"{path}: motif attendu une fois, trouvé {count}: {old[:120]!r}")
    target.write_text(content.replace(old, new, 1), encoding="utf-8")


def sha256(path: str) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def materialize_chapter() -> None:
    parts = sorted(Path(".qa/ch04").glob("chapter.b85.*"))
    if [part.name for part in parts] != [
        "chapter.b85.00",
        "chapter.b85.01",
        "chapter.b85.02",
        "chapter.b85.03",
    ]:
        raise RuntimeError(f"paquet incomplet: {[part.name for part in parts]}")
    encoded = "".join(part.read_text(encoding="ascii") for part in parts)
    data = lzma.decompress(base64.b85decode(encoded.encode("ascii")))
    digest = hashlib.sha256(data).hexdigest()
    if digest != CHAPTER_SHA256:
        raise RuntimeError(f"empreinte chapitre inattendue: {digest}")
    Path(CHAPTER).write_bytes(data)

    checks = {
        CHAPTER: CHAPTER_SHA256,
        "Livre-III/QA/AUDIT-CHAPITRE-04.md": AUDIT_SHA256,
        "Livre-III/QA/VALIDATION-FINALE-CHAPITRE-04.yaml": PROOF_SHA256,
    }
    for path, expected in checks.items():
        actual = sha256(path)
        if actual != expected:
            raise RuntimeError(f"empreinte inattendue pour {path}: {actual} != {expected}")


def patch_index() -> None:
    replace_once("Livre-III/index.md", 'version: "1.2.0"', 'version: "1.3.0"')
    replace_once(
        "Livre-III/index.md",
        "3. [Références, concept art et ComfyUI](CHAPITRE-03-References-concept-art-et-ComfyUI.md)\n\n"
        "Les chapitres 4 à 30 seront ajoutés progressivement selon `plans/LIVRE-III-PLAN-MAITRE.md`.",
        "3. [Références, concept art et ComfyUI](CHAPITRE-03-References-concept-art-et-ComfyUI.md)\n"
        "4. [Pipeline Blender et organisation des fichiers](CHAPITRE-04-Pipeline-Blender-et-organisation-des-fichiers.md)\n\n"
        "Les chapitres 5 à 30 seront ajoutés progressivement selon `plans/LIVRE-III-PLAN-MAITRE.md`.",
    )


def patch_roadmap() -> None:
    replace_once(
        "ROADMAP.md",
        "- [x] Chapitre 3 — Références, concept art et ComfyUI.\n"
        "- [ ] Préproduction et direction artistique — 3 chapitres sur 5.",
        "- [x] Chapitre 3 — Références, concept art et ComfyUI.\n"
        "- [x] Chapitre 4 — Pipeline Blender et organisation des fichiers.\n"
        "- [ ] Préproduction et direction artistique — 4 chapitres sur 5.",
    )
    replace_once(
        "ROADMAP.md",
        "**Statut M4 : en cours — 3 chapitres rédigés, repérés et audités sur 30.**",
        "**Statut M4 : en cours — 4 chapitres rédigés, repérés et audités sur 30.**",
    )


def patch_contents() -> None:
    replace_once(
        "contents.txt",
        "Livre-III/CHAPITRE-03-References-concept-art-et-ComfyUI.md\nLivre-IV/index.md",
        "Livre-III/CHAPITRE-03-References-concept-art-et-ComfyUI.md\n"
        "Livre-III/CHAPITRE-04-Pipeline-Blender-et-organisation-des-fichiers.md\n"
        "Livre-IV/index.md",
    )


def patch_plan() -> None:
    replace_once("plans/LIVRE-III-PLAN-MAITRE.md", 'version: "1.1.3"', 'version: "1.1.4"')
    replace_once(
        "plans/LIVRE-III-PLAN-MAITRE.md",
        'last-updated: "2026-07-22T20:42:28+02:00"',
        f'last-updated: "{TIMESTAMP}"',
    )
    replace_once(
        "plans/LIVRE-III-PLAN-MAITRE.md",
        "> **Statut :** en cours — 3 chapitres sur 30",
        "> **Statut :** en cours — 4 chapitres sur 30",
    )
    replace_once(
        "plans/LIVRE-III-PLAN-MAITRE.md",
        "> **Progression :** chapitres 1, 2 et 3 rédigés, repérés et audités au niveau `static-review` ; chapitres 4 à 30 à produire.",
        "> **Progression :** chapitres 1 à 4 rédigés, repérés et audités au niveau `static-review` ; chapitres 5 à 30 à produire.",
    )


def patch_continuity() -> None:
    path = "CONTINUITE-PROJET.md"
    replace_once(path, 'version: "3.33.1"', 'version: "3.34.0"')
    replace_once(
        path,
        'last-updated: "2026-07-22T21:21:47+02:00"',
        f'last-updated: "{TIMESTAMP}"',
    )
    replace_once(path, "**En cours : 3 chapitres sur 30.**", "**En cours : 4 chapitres sur 30.**")
    replace_once(
        path,
        "3. Références, concept art et ComfyUI — terminé au niveau `static-review`.\n\n"
        "Les chapitres 4 à 30 restent définis dans `plans/LIVRE-III-PLAN-MAITRE.md`.",
        "3. Références, concept art et ComfyUI — terminé au niveau `static-review`.\n"
        "4. Pipeline Blender et organisation des fichiers — terminé au niveau `static-review`.\n\n"
        "Les chapitres 5 à 30 restent définis dans `plans/LIVRE-III-PLAN-MAITRE.md`.",
    )

    architecture = """### 11.29 Pipeline Blender et organisation des fichiers

- Blender `4.5 LTS` constitue la branche documentaire ; la version corrective réelle est épinglée dans le manifeste d’environnement ;
- le fichier `.blend` publié reste la source canonique 3D et ne se confond ni avec les caches, ni avec les exports, ni avec les livraisons ;
- unités métriques, échelle unitaire, face avant, axes, origine, pivot et transforms neutres forment un contrat vérifiable ;
- les collections distinguent travail, publication et validation ; seule la collection de publication alimente l’export ;
- Link conserve l’autorité de la bibliothèque, Append crée une copie locale, et Library Override encadre les adaptations autorisées ;
- les dépendances utilisent des chemins relatifs et une réouverture sur une autre machine fait partie de la porte de validation ;
- sources, travail, caches, staging, exports, livraisons et archives occupent des chemins distincts ;
- les versions approuvées sont immuables, les sauvegardes automatiques ne sont pas des versions publiées ;
- GLB ou glTF constitue le contrat d’échange explicite vers Godot ; l’import direct `.blend` reste une voie d’itération dépendante de Blender ;
- tout export cite source, preset, collection, empreinte et autorité de publication ;
- la scène Godot de calibration vérifie échelle, orientation, pivot et réimportation sans réparer silencieusement la source ;
- aucune exécution Blender, export, import Godot, réouverture multi-poste ou mesure n’est revendiquée avant matérialisation.
"""
    replace_once(
        path,
        "- le dossier consolidé transmet règles, sources modifiables, inconnues et rapport de sélection aux chapitres de production.\n\n"
        "## 24. Erreurs à ne pas reproduire",
        "- le dossier consolidé transmet règles, sources modifiables, inconnues et rapport de sélection aux chapitres de production.\n\n"
        + architecture
        + "\n## 24. Erreurs à ne pas reproduire",
    )

    errors = """- ne pas utiliser `Unit Scale` comme réparation d’une géométrie ou de transforms incohérents ;
- ne pas corriger une mauvaise échelle uniquement dans Godot ;
- ne pas exporter une collection dont le contrat de publication est ambigu ;
- ne pas versionner des chemins absolus vers des textures ou bibliothèques ;
- ne pas modifier une donnée liée comme si elle était possédée localement ;
- ne pas versionner caches, temporaires ou sauvegardes automatiques comme sources ;
- ne pas écraser une version approuvée ;
- ne pas livrer uniquement un `.blend` sans manifeste ni contrat d’échange ;
- ne pas supposer que des réglages d’export mémorisés remplacent un preset contrôlé ;
- ne pas déplacer le pivot après publication sans nouvelle version et nouvelle validation ;

"""
    replace_once(path, "- ne pas oublier la mise à jour de ce fichier.", errors + "- ne pas oublier la mise à jour de ce fichier.")

    replace_once(
        path,
        "- progression du Livre III : 3 chapitres sur 30 ;",
        "- progression du Livre III : 4 chapitres sur 30 ;",
    )
    replace_once(
        path,
        "- chapitre 3 du Livre III : version `1.0.0`, niveau `static-review` ;\n"
        "- Livre II : 30 chapitres sur 30, publication technique terminée ;",
        "- chapitre 3 du Livre III : version `1.0.0`, niveau `static-review` ;\n"
        "- chapitre 4 du Livre III : version `1.0.0`, niveau `static-review` ;\n"
        "- Livre II : 30 chapitres sur 30, publication technique terminée ;",
    )

    old_next = """## 26. Prochaine action

Le chapitre 3 du Livre III est rédigé, repéré et audité au niveau `static-review`. La chaîne de références et de concepts distingue les statuts, enregistre provenance et droits, versionne les workflows ComfyUI, manifeste modèles et dépendances, puis impose une sélection humaine. Aucun environnement ComfyUI, concept réel, benchmark ou test Godot n’est revendiqué comme exécuté.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-III/CHAPITRE-04-Pipeline-Blender-et-organisation-des-fichiers.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 4 qualifiera la version de Blender et les addons, puis fixera unités, axes, échelle, origines, collections, arborescence source/travail/cache/export/archive, formats d’échange et test aller-retour vers Godot. Il ne produira pas encore les assets définitifs.
"""
    new_next = """## 26. Prochaine action

Le chapitre 4 du Livre III est rédigé, repéré et audité au niveau `static-review`. Le pipeline fixe Blender `4.5 LTS`, la source canonique, les unités, axes, pivots, collections, bibliothèques, versions, chemins, exports glTF/GLB et la porte d’import Godot. Aucun template réel, asset de calibration, export, import, test multi-poste ou benchmark n’est revendiqué comme exécuté.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 5 établira les fiches d’assets, le registre de provenance, la matrice des licences, les statuts de blocage et les procédures de retrait ou remplacement. Il ne fournira pas d’avis juridique personnalisé.
"""
    replace_once(path, old_next, new_next)

    journal = f"""### {TIMESTAMP} — version 3.34.0

- chapitre 4 du Livre III créé, relu et audité au niveau `static-review` ;
- Blender `4.5 LTS` qualifié comme branche documentaire, sans version corrective inventée ;
- template, unités, axes, pivots, transforms, collections, bibliothèques liées et overrides documentés ;
- arborescence source, travail, cache, staging, export, livraison et archive définie ;
- conventions de noms, versions, sauvegardes, chemins relatifs et dépendances encadrées ;
- formats GLB, glTF séparé et import direct `.blend` comparés avec leurs limites ;
- asset de calibration, validateur Blender, contrat d’export, empreintes et scène Godot de validation documentés ;
- procédures Solo, Studio, réouverture multi-poste, migration, sécurité et checklists ajoutées ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA provisoire et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 5 — Provenance, licences et validation des assets, niveau Élevée ;
- aucune exécution Blender ou Godot et aucun PDF du Livre III construits.

"""
    replace_once(path, "## 27. Journal\n\n", "## 27. Journal\n\n" + journal)


def main() -> None:
    materialize_chapter()
    patch_index()
    patch_roadmap()
    patch_contents()
    patch_plan()
    patch_continuity()
    print("CH04_BATCH_APPLIED")


if __name__ == "__main__":
    main()
