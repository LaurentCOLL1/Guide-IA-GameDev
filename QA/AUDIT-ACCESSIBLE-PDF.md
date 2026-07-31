---
title: "Audit — PDF balisé pour lecteurs d’écran"
id: "QA-AUDIT-ACCESSIBLE-PDF"
status: "candidate"
version: "0.1.0"
lang: "fr-FR"
last-verified: "2026-07-31T03:40:00+02:00"
audit-level: "implementation-ready"
license: "CC-BY-SA-4.0"
---

# Audit — PDF balisé pour lecteurs d’écran

## Objectif

Produire un livrable PDF séparé du PDF visuel historique, avec structure logique, langue française, titre documentaire, ordre de contenu balisé et déclaration PDF/UA-2. Le livrable reste un **candidat technique** tant que les contrôles machine et humains ne sont pas tous documentés.

## Chaîne candidate

- sources ordonnées par `contents.txt` ;
- normalisation éditoriale par `filters/pdf-normalize.lua` ;
- Pandoc et LuaLaTeX depuis une image versionnée ;
- TeX Live 2026 afin d’activer le balisage moderne de LaTeX ;
- profil demandé `PDF/UA-2` ;
- validation structurelle avec Poppler et qpdf ;
- validation PDF/UA-2 avec veraPDF ;
- artefact distinct `Guide-IA-GameDev-accessible.pdf` ;
- aucun remplacement du PDF XeLaTeX existant.

## Critères machine

- PDF déclaré balisé par `pdfinfo` ;
- présence de `StructTreeRoot`, `MarkInfo`, `Marked true`, langue `fr-FR` et affichage du titre ;
- titre et auteur extractibles ;
- manifeste cohérent avec les octets générés ;
- aucune image Markdown ou HTML sans alternative textuelle non vide ;
- validation veraPDF PDF/UA-2 sans échec machine ;
- dépôt propre après génération.

## Contrôles humains obligatoires avant toute revendication complète

- ordre de lecture sur un échantillon représentatif puis sur les structures complexes ;
- navigation par titres, listes, tableaux, liens, notes et code ;
- pertinence des alternatives textuelles ;
- compréhension de la langue et des symboles techniques ;
- essai avec au moins un lecteur d’écran et un lecteur PDF cible.

## Limites initiales

- veraPDF ne couvre que les exigences PDF/UA vérifiables automatiquement ;
- aucun certificat, label ou audit juridique d’accessibilité n’est produit ;
- aucun test utilisateur ou lecteur d’écran n’est encore inscrit comme réussi ;
- aucune release publique n’est créée dans ce lot.
