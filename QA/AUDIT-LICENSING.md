---
title: "Audit — Politique de licence globale"
id: "QA-AUDIT-GLOBAL-LICENSING"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
last-verified: "2026-07-30T18:26:37+02:00"
audit-level: "runtime-tested-linux"
license: "CC-BY-SA-4.0"
---

# Audit — Politique de licence globale

- **Statut :** reviewed
- **Décision :** licence multiple CC BY-SA 4.0 / MIT / CC0 1.0
- **Périmètre :** sources éditoriales, logiciel, ressources techniques, métadonnées, exports et archives

## Contrôles attendus

- textes et notices de licence présents ;
- matrice YAML analysable et identifiants SPDX autorisés ;
- aucune mention `À définir avant publication` ou `pending-global-license` dans les points de gouvernance contrôlés ;
- dix Packs reliés à la politique globale ;
- règles de contribution alignées sur la licence applicable ;
- prochaine action M8 mise à jour ;
- composants tiers explicitement exclus de toute relicence automatique.

La validation ne remplace pas une consultation juridique pour une publication commerciale à risque élevé.

## Résultat

La politique est structurée, les dix Packs sont reliés à la matrice et les anciens marqueurs de licence globale en attente sont retirés. Le workflow permanent a réussi sur Ubuntu 24.04 avec Python 3.12.13 : run `30561457478`, artefact `8767038421`, digest `sha256:bda4f6a33fda885a5ee2bc140c835a1af58a695d9399c5fd64cac099839371d9`.
