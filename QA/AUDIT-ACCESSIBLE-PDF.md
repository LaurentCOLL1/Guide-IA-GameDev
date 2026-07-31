---
title: "Audit — PDF balisé et accessibilité"
id: "QA-AUDIT-ACCESSIBLE-PDF"
status: "draft"
version: "0.1.0"
lang: "fr-FR"
last-verified: "2026-07-31T05:36:00+02:00"
audit-level: "implementation-pending-runtime"
license: "CC-BY-SA-4.0"
---

# Audit — PDF balisé et accessibilité

## Objectif

Produire un PDF technique de la collection avec arbre de structure, langue de document, métadonnées de titre et d’auteur, ordre de sources maîtrisé et diagnostic PDF/UA automatisé.

## Porte automatique

- construction avec LuaLaTeX et TeX Live 2026 ;
- `\DocumentMetadata` placé avant `\documentclass` ;
- cible déclarée PDF/UA-1 ;
- présence de `/MarkInfo`, `/Marked true`, `/StructTreeRoot` et `/Lang` ;
- titre, auteur, nombre de pages et manifeste contrôlés ;
- diagnostic veraPDF `ua1` conservé intégralement ;
- validations documentaires et de licence inchangées ;
- aucune sortie générée suivie par Git.

## Contrôles humains requis

- ordre de lecture sur un échantillon représentatif ;
- hiérarchie des titres ;
- pertinence des alternatives textuelles ;
- sémantique des tableaux et listes ;
- comportement avec lecteur d’écran ;
- vérification des liens, notes, blocs de code et formules.

## Règle de revendication

La présence de balises et la réussite des contrôles machine ne suffisent pas à revendiquer une conformité PDF/UA complète. Le lot emploie la qualification `tagged-pdf-machine-checked-not-full-pdfua-conformance` tant que les contrôles humains et les éventuelles corrections de veraPDF ne sont pas clos.

## Références de méthode

La chaîne suit l’interface `\DocumentMetadata` du projet LaTeX Tagged PDF et utilise le profil PDF/UA-1 de veraPDF. veraPDF ne couvre que les points contrôlables automatiquement ; le protocole Matterhorn distingue les vérifications machine et humaines.
