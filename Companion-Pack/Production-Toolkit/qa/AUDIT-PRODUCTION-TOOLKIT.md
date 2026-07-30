---
title: "Audit — Production Toolkit"
id: "CP-AUDIT-PACK-09"
status: "complete"
version: "1.0.0"
audit-level: "runtime-tested-linux"
audit-date: "2026-07-30T15:10:10+02:00"
lang: "fr-FR"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Décision

Le Pack 9 est accepté dans son périmètre Linux x86_64 pour des traitements non destructifs sur assets synthétiques.

## Périmètre validé

- 28 fichiers et neuf familles d’outils ;
- 29 tests Python ;
- dry-run sans création de sortie métier ;
- journaux JSON et codes de sortie ;
- conversions PPM vers PNG et WAV stéréo vers PCM mono ;
- validation OBJ, PNG et WAV ;
- renommage par copie avec collisions résolues ;
- catalogue JSON et CSV ;
- échec injecté, checkpoint partiel et reprise complète ;
- deux archives ZIP déterministes ;
- Blender OBJ vers GLB ;
- Godot : import et instanciation du GLB ;
- SHA-256 des sources inchangés ;
- arbre Git propre et aucune donnée privée détectée.

## Preuves runtime

- workflow : `Validate Production Toolkit` ;
- run : `30544978391` ;
- artefact : `8760345537` ;
- digest : `sha256:d48f12b2aff00e76dc82e06072deb994863dff43fcce7758faa762c914841359` ;
- Ubuntu 24.04 ;
- Python `3.12.13` ;
- Blender `4.0.2`, NumPy `1.26.4` ;
- Godot `4.7.1.stable.official.a13da4feb` ;
- finaliseur de gouvernance : run `30545689178`.

## Réserves

Aucun format propriétaire, bake complexe, compression GPU, rendu artistique, qualité perceptuelle, export de jeu, Windows, macOS, GPU physique, mobile, console, publication, release, licence globale ou redistribution autonome n’est qualifié.
