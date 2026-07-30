---
title: "Companion Pack — Production Toolkit"
id: "CP-PACK-09-PRODUCTION-TOOLKIT"
status: "candidate"
version: "1.0.0"
lang: "fr-FR"
validation-status: "candidate-runtime"
redistribution-status: "pending-global-license"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Production Toolkit

> **Repères d’utilisation :** **[PS]** PowerShell, **[CMD]** Invite de commandes, **[WSL]** terminal Linux sous Windows, **[DCT]** terminal d’un conteneur, **[VSC]** Visual Studio Code, **[APP]** application graphique, **[SORTIE]** résultat à contrôler et **[LECTURE]** contenu à étudier.

Le Pack 9 fournit des outils non destructifs pour produire, convertir, valider, cataloguer, renommer et empaqueter des assets. Le candidat sépare les sources, le workspace et les sorties, et rend les opérations mutantes explicites.

## Principes

- `--dry-run` décrit les opérations sans créer les sorties métier ;
- chaque CLI émet des journaux JSON structurés et un code de sortie stable ;
- les sources sont lues, jamais modifiées ;
- les traitements par lots utilisent un checkpoint et peuvent reprendre après échec ;
- les archives ZIP sont déterministes ;
- les fixtures sont synthétiques et générées localement ;
- Blender et Godot sont qualifiés uniquement sur les versions exécutées par la CI.

## Commandes principales

```powershell
$env:PYTHONPATH = ".\Companion-Pack\Production-Toolkit\python\src"
python .\Companion-Pack\Production-Toolkit\scripts\toolkit_cli.py generate `
  --output .\dist\production-fixtures
python .\Companion-Pack\Production-Toolkit\scripts\toolkit_cli.py batch `
  --plan .\Companion-Pack\Production-Toolkit\fixtures\plans\pipeline.json `
  --source-root .\Companion-Pack\Production-Toolkit\fixtures `
  --workspace .\dist\production-workspace `
  --dry-run
```

## Qualification attendue

Le workflow permanent doit exécuter les tests Python, démontrer le dry-run, injecter un échec puis reprendre, convertir texture et audio, exporter un GLB avec Blender, l’importer avec Godot, produire deux archives identiques et vérifier que les empreintes des sources restent inchangées.

## Frontières

Le candidat ne revendique aucune conversion de formats propriétaires, aucun rendu artistique, aucun bake complexe, aucune compression GPU, aucune qualité audio perceptuelle, aucun export de jeu, aucun traitement de données utilisateur et aucune publication.
