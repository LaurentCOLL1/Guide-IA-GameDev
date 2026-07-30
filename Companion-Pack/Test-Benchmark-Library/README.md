---
title: "Companion Pack — Test & Benchmark Library"
id: "CP-PACK-08-TEST-BENCHMARK-LIBRARY"
status: "candidate"
version: "1.0.0"
lang: "fr-FR"
validation-status: "candidate"
redistribution-status: "pending-global-license"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Test & Benchmark Library

> **Repères d’utilisation :** **[PS]** PowerShell, **[CMD]** Invite de commandes, **[WSL]** terminal Linux sous Windows, **[DCT]** terminal d’un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique, **[SORTIE]** résultat à comparer et **[LECTURE]** contenu à étudier.

Le Pack 8 centralise des tests fonctionnels, des charges synthétiques et des formats de mesure reproductibles. Il sépare explicitement la preuve d’exécution, la mesure locale et toute comparaison de performance.

## Contenu

- trois benchmarks Python séparables : CPU, mémoire et corpus synthétique ;
- trois scènes Godot séparables : CPU, mémoire et proxy de rendu sous environnement graphique ;
- suites unitaires Python et GDScript ;
- contrats, seeds, fixtures et corpus synthétique ;
- observations brutes CSV, résumés JSON et manifestes YAML-compatible ;
- statistiques de répétition : moyenne, médiane, variance, écart-type, coefficient de variation, p95 et p99 ;
- comparaison refusée lorsque le contrat ou l’empreinte d’environnement diffère ;
- modèles de rapports et exemples uniquement illustratifs.

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

Le proxy de rendu mesure des intervalles de frame dans le renderer et l’affichage documentés. Une exécution Xvfb ou une carte non identifiée ne constitue pas un benchmark GPU physique.

## Interprétation

Une mesure est liée au contrat, au commit, à la seed, au scénario, aux versions et à l’empreinte matérielle. Les résultats d’un runner hébergé prouvent que le protocole s’exécute ; ils ne décrivent pas les performances générales d’un PC, d’un GPU ou du projet final.

## Réserves candidates

Aucun matériel Windows, GPU physique, pilote AMD/ZLUDA, Forward+, mobile, console, charge longue, performance produit, modèle IA réel, publication, export ou licence globale n’est encore qualifié.
