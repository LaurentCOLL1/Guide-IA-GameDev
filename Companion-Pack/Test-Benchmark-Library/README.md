---
title: "Companion Pack — Test & Benchmark Library"
id: "CP-PACK-08-TEST-BENCHMARK-LIBRARY"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
last-verified: "2026-07-30T14:03:39+02:00"
validation-status: "runtime-tested-linux"
redistribution-status: "global-policy-defined"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Test & Benchmark Library

> **Repères d’utilisation :** **[PS]** PowerShell, **[CMD]** Invite de commandes, **[WSL]** terminal Linux sous Windows, **[DCT]** terminal d’un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique, **[SORTIE]** résultat à comparer et **[LECTURE]** contenu à étudier.

Le Pack 8 centralise des tests fonctionnels, des charges synthétiques et des formats de mesure reproductibles. Il sépare explicitement la preuve d’exécution, la mesure locale et toute comparaison de performance.

## État qualifié

| Élément | État |
|---|---|
| fichiers du Pack | 73 validés |
| contrats versionnés | 6 |
| tests Python | 25 réussis |
| suite GDScript | réussie |
| benchmarks Python | CPU, mémoire et corpus exécutés séparément |
| scènes Godot | CPU, mémoire et proxy de rendu exécutés séparément |
| résultats de campagne | 6 résultats horodatés et validés |
| formats | JSON, CSV, YAML-compatible et Markdown |
| arbre Git | propre après suppression des artefacts runtime |

## Exécution Python séparée

> **[PS] PowerShell — Exécuter depuis la racine du dépôt :**

```powershell
$env:PYTHONPATH = ".\Companion-Pack\Test-Benchmark-Library\python\src"
python .\Companion-Pack\Test-Benchmark-Library\scripts\run_python_suite.py `
  --benchmark cpu `
  --output-dir .\dist\bench-cpu
```

Remplacer `cpu` par `memory`, `corpus` ou `all`.

## Tests Python

```powershell
$env:PYTHONPATH = ".\Companion-Pack\Test-Benchmark-Library\python\src"
python -m unittest discover `
  -s .\Companion-Pack\Test-Benchmark-Library\python\tests `
  -v
```

## Scènes Godot

Chaque scène s’exécute indépendamment :

```text
res://scenes/cpu_benchmark.tscn
res://scenes/memory_benchmark.tscn
res://scenes/render_proxy_benchmark.tscn
```

## Qualification obtenue

Le run `30540336088` a validé les 73 fichiers du Pack, 25 tests Python, la suite GDScript, trois benchmarks Python et trois scènes Godot exécutés séparément. Il a produit six résultats avec horodatage UTC, seed, paramètres, observations brutes, statistiques de dispersion et empreinte d’environnement.

Environnement : Ubuntu 24.04, CPython `3.12.13` et Godot `4.7.1.stable.official.a13da4feb`. Le proxy de rendu a utilisé Xvfb, `gl_compatibility` et Mesa llvmpipe ; il qualifie le protocole graphique virtuel, pas un GPU physique.

Artefact `8758417029`, digest `sha256:4c4aeeea49e3d9b1d7124bb2da119e0d4994d14250e1c9959754cf980cf18d42`. Le finaliseur de gouvernance a été exécuté par le run `30540978373`.

## Interprétation

Une mesure est liée au contrat, au commit, à la seed, au scénario, aux versions et à l’empreinte matérielle. Les résultats du runner hébergé prouvent que le protocole s’exécute ; ils ne décrivent pas les performances générales d’un PC, d’un GPU ou du projet final.

## Réserves

La qualification ne valide aucun Windows, GPU physique, Forward+, pilote AMD/ZLUDA, mobile, console, charge longue, performance produit, modèle IA réel, export, publication, release, licence globale ou redistribution autonome.
