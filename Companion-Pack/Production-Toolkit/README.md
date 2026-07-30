---
title: "Companion Pack — Production Toolkit"
id: "CP-PACK-09-PRODUCTION-TOOLKIT"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
last-verified: "2026-07-30T15:10:10+02:00"
validation-status: "runtime-tested-linux"
redistribution-status: "pending-global-license"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Production Toolkit

> **Repères d’utilisation :** **[PS]** PowerShell, **[CMD]** Invite de commandes, **[WSL]** terminal Linux sous Windows, **[DCT]** terminal d’un conteneur, **[VSC]** Visual Studio Code, **[APP]** application graphique, **[SORTIE]** résultat à contrôler et **[LECTURE]** contenu à étudier.

Le Pack 9 fournit des outils non destructifs pour produire, convertir, valider, cataloguer, renommer et empaqueter des assets. Il sépare les sources, le workspace et les sorties, et rend chaque opération mutante explicite.

## État qualifié

| Élément | État |
|---|---|
| fichiers du Pack | 28 validés |
| familles d’outils | 9 |
| tests Python | 29 réussis |
| dry-run | sorties métier absentes |
| conversions | PPM vers PNG et WAV stéréo vers PCM mono |
| reprise | échec injecté puis checkpoint repris |
| packaging | deux ZIP de SHA-256 identique |
| Blender | OBJ synthétique exporté en GLB |
| Godot | GLB importé et instancié |
| sources | empreintes SHA-256 inchangées |

## Principes d’exploitation

- `--dry-run` décrit les opérations sans créer les sorties métier ;
- les commandes émettent des journaux JSON structurés et des codes de sortie stables ;
- les sources sont lues, jamais modifiées ;
- l’écrasement est refusé par défaut ;
- les traitements par lots utilisent un checkpoint lié à l’empreinte du plan ;
- les archives ZIP utilisent un ordre, une date et des permissions déterministes ;
- les fixtures sont synthétiques.

## Exemple

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

## Qualification obtenue

Le run `30544978391` a validé 28 fichiers, 29 tests Python, le dry-run de toutes les familles mutantes, trois assets convertis ou validés, un échec injecté suivi d’une reprise complète, deux archives déterministes, l’export OBJ vers GLB et l’import Godot.

Environnement : Ubuntu 24.04, CPython `3.12.13`, Blender `4.0.2`, NumPy `1.26.4` dans Blender et Godot `4.7.1.stable.official.a13da4feb`.

Artefact `8760345537`, digest `sha256:d48f12b2aff00e76dc82e06072deb994863dff43fcce7758faa762c914841359`. Finaliseur de gouvernance : run `30545689178`.

## Interprétation

La qualification démontre les contrats fonctionnels sur des assets synthétiques. Elle ne mesure ni la qualité artistique, ni la qualité audio perceptuelle, ni les performances générales d’un poste de production.

## Réserves

Aucun format propriétaire, bake complexe, compression GPU, rendu artistique, export de jeu, Windows, macOS, GPU physique, mobile, console, publication, release, licence globale ou redistribution autonome n’est validé.
