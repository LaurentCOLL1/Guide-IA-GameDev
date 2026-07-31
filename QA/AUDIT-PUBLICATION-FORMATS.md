---
title: "Audit — Formats de publication PDF HTML EPUB"
id: "QA-AUDIT-PUBLICATION-FORMATS"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
last-verified: "2026-07-30T23:04:00+02:00"
audit-level: "runtime-tested-linux"
license: "CC-BY-SA-4.0"
---

# Audit — Formats de publication PDF HTML EPUB

## Périmètre

- source unique définie par `contents.txt` ;
- métadonnées communes dans `metadata.yaml` ;
- PDF A4 produit avec Pandoc et XeLaTeX ;
- HTML autonome produit avec ressources embarquées ;
- EPUB 3 produit par Pandoc ;
- manifeste de sortie avec tailles et SHA-256 ;
- validation structurelle des trois formats ;
- intégration des notices de licence ;
- génération sous Linux dans GitHub Actions.

## Critères attendus

- les trois fichiers sont non vides et dépassent le seuil minimal ;
- le PDF contient le titre et l'auteur et possède un nombre de pages cohérent ;
- le HTML contient une table des matières, le titre et la licence, sans chemin local absolu ;
- l'EPUB place `mimetype` en première entrée, fournit le conteneur et le paquet OPF, et déclare la licence ;
- le manifeste correspond aux octets générés ;
- les validations documentaires et de licence restent vertes ;
- le dépôt reste propre après génération ;
- les artefacts sont marqués comme builds techniques, non comme release officielle.

## Réserves

- aucune conformité EPUBCheck complète n'est encore revendiquée ;
- aucune inspection visuelle exhaustive du HTML ou de l'EPUB n'est encore revendiquée ;
- aucun PDF balisé pour lecteur d'écran n'est produit dans ce lot ;
- aucune identité byte pour byte inter-plateformes ou inter-versions d'outils n'est revendiquée ;
- aucune publication publique, release ou archive définitive n'est créée.


## Résultat qualifié

Le run `30582855712` a construit et validé 162 sources sous Ubuntu 24.04 avec Python 3.12.13 et Pandoc 3.1.3 : PDF de 4 108 pages, HTML autonome et EPUB 3. L'artefact `8775425907` porte le digest `sha256:d5d3d548b133e1e6cc12e7d2809e27c3e7166f5dfb131e0e817c4de39426e9e6`. Les pages PDF 1 et 2 ont été rendues et inspectées visuellement : couverture et table des matières lisibles, sans chevauchement ni glyphe cassé.
