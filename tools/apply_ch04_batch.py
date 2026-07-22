from __future__ import annotations

from pathlib import Path

TIMESTAMP = "2026-07-22T22:37:42+02:00"
CHAPTER = "Livre-III/CHAPITRE-04-Pipeline-Blender-et-organisation-des-fichiers.md"


def replace_once(path: str, old: str, new: str) -> None:
    target = Path(path)
    content = target.read_text(encoding="utf-8")
    count = content.count(old)
    if count != 1:
        raise RuntimeError(f"{path}: motif attendu une fois, trouvé {count}: {old[:120]!r}")
    target.write_text(content.replace(old, new, 1), encoding="utf-8")


def verify_permanent_files() -> None:
    chapter = Path(CHAPTER).read_text(encoding="utf-8")
    required = (
        'id: "DOC-L3-CH04"',
        'version: "1.0.0"',
        'blender:\n    version: "5.2.0"',
        'audit-status: "complete"',
        '## 41. Références officielles vérifiées',
    )
    for marker in required:
        if marker not in chapter:
            raise RuntimeError(f"chapitre 4 incomplet: {marker!r}")
    if "__PLACEHOLDER__" in chapter or "Blender `4.5 LTS`" in chapter:
        raise RuntimeError("chapitre 4 obsolète ou non matérialisé")

    audit = Path("Livre-III/QA/AUDIT-CHAPITRE-04.md").read_text(encoding="utf-8")
    if "Blender `5.2.0`" not in audit or "1 578" not in audit:
        raise RuntimeError("audit du chapitre 4 non aligné")


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

- Blender `5.2.0` Stable constitue la référence documentaire ; toute mise à jour future repasse par une qualification et un asset pilote ;
- aucun add-on tiers n’est obligatoire pour le chemin de référence ; une extension future est qualifiée comme du code et une dépendance de production ;
- le fichier `.blend` reste la source canonique 3D et ne se confond ni avec les caches, ni avec les exports, ni avec les livraisons ;
- les scènes utilisent le système métrique avec une unité pour un mètre ; `Unit Scale` ne sert pas à réparer une géométrie incorrecte ;
- les assets orientés regardent vers `-Y` dans Blender et arrivent vers `+Z` dans Godot par la conversion glTF, sans parent correctif ;
- origines et pivots sont fonctionnels et ne changent pas après publication sans nouvelle version ;
- les collections distinguent géométrie, rig, sockets, guides et frontière `__EXPORT` unique ;
- Link conserve l’autorité de la bibliothèque, Append crée une copie locale, et Library Override encadre les adaptations autorisées ;
- les dépendances utilisent des chemins relatifs et une réouverture sur une autre machine fait partie de la porte runtime ;
- sources, travail, bibliothèques, caches, exports, livraisons et archives occupent des chemins distincts ;
- les versions approuvées sont immuables, les sauvegardes automatiques ne sont pas des versions publiées ;
- GLB constitue la livraison par défaut, glTF séparé répond aux besoins d’inspection, et l’import direct `.blend` reste une voie Solo dépendante de Blender ;
- tout export cite source, preset, collection, empreinte et autorité de publication ;
- le cube d’un mètre vérifie échelle, orientation, pivot, marqueurs et réimportation dans Godot ;
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

    errors = """- ne pas utiliser `Unit Scale` comme réparation d’une géométrie incorrecte ;
- ne pas ajouter un parent tourné à 90 degrés pour masquer une mauvaise convention d’axes ;
- ne pas appliquer toutes les transformations sans examiner rigs, contraintes et hiérarchies ;
- ne pas exporter une sélection manuelle lorsque la collection `__EXPORT` est le contrat ;
- ne pas versionner des chemins personnels absolus vers des textures ou bibliothèques ;
- ne pas modifier une donnée liée comme si elle était possédée localement ;
- ne pas versionner caches, temporaires ou sauvegardes automatiques comme sources ;
- ne pas écraser une version approuvée ;
- ne pas livrer uniquement un `.blend` en Studio sans GLB contrôlé et manifeste ;
- ne pas installer automatiquement un add-on inconnu ;
- ne pas déplacer le pivot après publication sans nouvelle version et validation ;

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

Le chapitre 4 du Livre III est rédigé, repéré et audité au niveau `static-review`. Le pipeline fixe Blender `5.2.0` Stable, les unités, axes, pivots, collections, bibliothèques, versions, chemins, exports GLB/glTF et la porte d’import Godot. Aucun template réel, cube pilote, export, import, test multi-poste ou benchmark n’est revendiqué comme exécuté.

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
- Blender `5.2.0` Stable qualifié comme référence documentaire, sans add-on tiers obligatoire ;
- template, unités, axes, pivots, transformations, collections, bibliothèques liées et overrides documentés ;
- arborescence source, travail, bibliothèque, cache, export, livraison et archive définie ;
- conventions de noms, versions, sauvegardes, chemins relatifs et dépendances encadrées ;
- formats GLB, glTF séparé et import direct `.blend` comparés avec leurs limites ;
- cube d’un mètre, validateur Blender, exporteur GLB, empreintes et contrôle Godot documentés ;
- procédures Solo, Studio, réouverture multi-poste, sécurité et checklists ajoutées ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA provisoire et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 5 — Provenance, licences et validation des assets, niveau Élevée ;
- aucune exécution Blender ou Godot et aucun PDF du Livre III construits.

"""
    replace_once(path, "## 27. Journal\n\n", "## 27. Journal\n\n" + journal)


def cleanup_temporary_files() -> None:
    for part in Path(".qa/ch04").glob("chapter.b85.*"):
        part.unlink()
    qa_dir = Path(".qa/ch04")
    if qa_dir.exists() and not any(qa_dir.iterdir()):
        qa_dir.rmdir()
    qa_root = Path(".qa")
    if qa_root.exists() and not any(qa_root.iterdir()):
        qa_root.rmdir()
    Path("tools/apply_ch04_batch.py").unlink(missing_ok=True)
    Path(".github/workflows/ch04-apply-governance.yml").unlink(missing_ok=True)


def main() -> None:
    verify_permanent_files()
    patch_index()
    patch_roadmap()
    patch_contents()
    patch_plan()
    patch_continuity()
    cleanup_temporary_files()
    print("CH04_GOVERNANCE_APPLIED")


if __name__ == "__main__":
    main()
