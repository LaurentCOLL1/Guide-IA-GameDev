---
title: "Audit — ComfyUI Library"
id: "CP-AUDIT-PACK-06"
status: "complete"
version: "1.0.0"
audit-level: "runtime-tested-linux"
audit-date: "2026-07-30T11:20:49+02:00"
---

# Décision

Le Pack 6 est accepté dans son périmètre Linux x86_64 avec ComfyUI `v0.28.0`, CPython `3.12.13` et le profil CPU sans modèle.

## Périmètre comparé au plan maître

Le lot matérialise les workflows JSON, manifestes, listes de custom nodes, presets, scripts de lancement, modèles de dossiers, provenance, image légère et checksums prévus. Il ne modifie ni l’ordre des Packs ni les frontières des chapitres propriétaires.

## Contrôle anti-doublon

- la sélection de concepts reste au Livre III, chapitre 3 ;
- l’orchestration de lots reste au Livre III, chapitre 30 ;
- les files et caches de fournisseurs restent dans l’AI Library ;
- les benchmarks comparatifs restent réservés au Pack 8 ;
- aucun modèle ou custom node tiers n’est distribué.

## Preuves runtime

- workflow permanent : `Validate ComfyUI Library` ;
- run : `30529642016` ;
- artefact : `8754176422` ;
- digest : `sha256:19be52a44ab295a747cb4ed7655268058d27494572e83709455004bf5be145af` ;
- ComfyUI : `v0.28.0`, commit `700821e1364eaab0e8f21c538a2131719fec57bf` ;
- Python : `3.12.13` ;
- Torch : `2.13.0+cu130` ;
- 37 fichiers du Pack validés ;
- 12 tests Python réussis ;
- workflow `LoadImage → SaveImage` exécuté sans modèle ;
- base SQLite interne créée dans le workspace runtime ;
- PNG de `1565` octets, SHA-256 `868bc37be44cf32ae8cac9e55106bd2d16dc9161f6bea4e391e9c146e7603388` ;
- métadonnées `prompt` et `workflow` validées ;
- aucun modèle, custom node tiers ou PDF produit ;
- arbre Git propre après runtime.

## Réserves

Le workflow text-to-image, les modèles réels, les custom nodes tiers, le profil AMD/ZLUDA, Windows graphique, les performances, la qualité artistique, les droits d’exploitation des sorties, les exports, les releases et la licence globale ne sont pas validés.
