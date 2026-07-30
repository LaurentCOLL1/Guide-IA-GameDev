---
title: "Audit — Test & Benchmark Library"
id: "CP-AUDIT-PACK-08"
status: "complete"
version: "1.0.0"
audit-level: "runtime-tested-linux"
audit-date: "2026-07-30T14:03:39+02:00"
lang: "fr-FR"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Décision

Le Pack 8 est accepté dans son périmètre Linux x86_64 pour les tests et mesures synthétiques reproductibles.

## Périmètre validé

- 73 fichiers du Pack et 6 contrats versionnés ;
- 25 tests Python et une suite GDScript ;
- trois benchmarks Python exécutés séparément ;
- trois scènes Godot exécutées séparément ;
- six résultats horodatés avec seeds, paramètres, observations brutes, variance, écart-type, coefficient de variation, p95 et p99 ;
- portes de comparaison compatibles et incompatibles ;
- campagne JSON, CSV et Markdown ;
- fixtures et corpus entièrement synthétiques ;
- arbre Git propre et absence de donnée privée détectée.

## Preuves runtime

- workflow permanent : `Validate Test Benchmark Library` ;
- run : `30540336088` ;
- artefact : `8758417029` ;
- digest : `sha256:4c4aeeea49e3d9b1d7124bb2da119e0d4994d14250e1c9959754cf980cf18d42` ;
- Ubuntu 24.04, Python `3.12.13`, Godot `4.7.1.stable.official.a13da4feb` ;
- archive Godot vérifiée par SHA-256 `c7ff14fd28472c8d4f193043de30278dcf7e5241a1dcf7566b02e27addaa33ba` ;
- Xvfb, renderer `gl_compatibility`, Mesa llvmpipe pour le proxy de rendu ;
- finaliseur de gouvernance : run `30540978373`.

## Décision de comparabilité

Les temps observés ne sont pas promus comme références universelles. Une comparaison automatique est refusée lorsque le contrat, la charge, la seed, l’implémentation, l’unité ou l’empreinte d’environnement diffère.

## Réserves

Aucun Windows, GPU physique, Forward+, pilote AMD/ZLUDA, mobile, console, charge longue, performance produit, modèle IA réel, export, publication, release, licence globale ou redistribution autonome n’est validé.
