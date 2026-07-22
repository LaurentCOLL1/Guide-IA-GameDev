---
title: "Validation transversale et publication du Livre II"
id: "DOC-L2-QA-TRANSVERSE-PUBLICATION"
status: "complete"
version: "1.0.1"
lang: "fr-FR"
last-verified: "2026-07-22T10:22:13+02:00"
audit-level: "static-review+pdf-inspected"
validation-evidence: "Livre-II/QA/VALIDATION-PUBLICATION-LIVRE-II.yaml"
---

# Validation transversale et publication du Livre II

## 1. Périmètre

La campagne couvre les trente chapitres du Livre II, leurs rapports d’audit, les preuves QA disponibles, l’index du Livre, l’ordre de compilation, les liens et identifiants, les repères d’utilisation, les doublons, la chaîne Pandoc/XeLaTeX et le PDF complet de la collection à l’état de clôture du Livre II.

Les preuves YAML restent versionnées dans le dépôt mais sont exclues de `contents.txt`. Cette séparation évite de présenter au lecteur des pages de données techniques brutes et empêche qu’une preuve modifie le PDF qu’elle décrit. La preuve de publication contenant le nombre final de pages, l’empreinte SHA-256 et les identifiants GitHub Actions est conservée dans `Livre-II/QA/VALIDATION-PUBLICATION-LIVRE-II.yaml`.

## 2. Validation transversale

La validation confirme :

- trente chapitres déclarés et présents ;
- trente identifiants de chapitre uniques ;
- un rapport d’audit référencé et présent pour chaque chapitre, avec rapport groupé autorisé pour les chapitres 1 et 2 ;
- toutes les preuves finales présentes au dépôt contrôlées sans état `pending` ;
- trente chapitres du Livre II déclarés dans `contents.txt` ;
- preuves YAML conservées hors de l’ordre de compilation lecteur ;
- zéro erreur bloquante dans le validateur documentaire ;
- zéro doublon de titre, bloc significatif ou paragraphe long dans les chapitres ;
- zéro bloc sans repère d’utilisation ;
- zéro incohérence sémantique de contexte ;
- absence de métadonnée de niveau de raisonnement dans les chapitres publiés.

L’unique avertissement global reste l’absence de licence de collection.

## 3. Compilation Pandoc et XeLaTeX

La compilation utilise `build.sh`, `metadata.yaml`, `contents.txt`, le filtre Lua du dépôt, Pandoc et XeLaTeX. Les dépendances de publication comprennent les familles DejaVu, Latin Modern et le convertisseur SVG de `librsvg`.

Une première compilation a révélé deux dépendances manquantes (`lmodern.sty` et `rsvg-convert`). Elles ont été ajoutées au runner de publication. La compilation suivante a produit un PDF A4 lisible et extractible.

L’option LaTeX `openany` a été ajoutée à la classe `book`. Elle supprime les pages verso quasi vides qui conservaient un en-tête courant tronqué entre deux chapitres. Le nombre de ces pages parasites est passé de cinquante et une à zéro, hors dernière page normale de la table des matières.

Une inspection ultérieure a révélé que les preuves YAML des chapitres 14 à 30 étaient encore compilées comme du texte. Elles ont été retirées de l’ordre Pandoc sans être supprimées du dépôt.

## 4. Préflight PDF

Les contrôles ont confirmé :

- format A4 et rotation nulle ;
- PDF non chiffré et sans JavaScript ;
- absence d’erreur de syntaxe ou de flux selon `qpdf --check` ;
- texte extractible avec `pdftotext` ;
- polices DejaVu et Latin Modern incorporées, sous-ensemblées et associées à une table Unicode ;
- métadonnées de titre et d’auteur présentes ;
- empreinte SHA-256 enregistrée dans la preuve externe.

## 5. Inspection visuelle

L’inspection a couvert :

- la couverture et les premières pages de la table des matières ;
- des pages représentatives aux quarts, à la moitié et aux trois quarts du volume ;
- les trente ouvertures de chapitre du Livre II ainsi que son index ;
- des pages contenant du code dense, des listes et des explications structurées ;
- le rapport transversal, les audits de clôture et les dernières pages ;
- les index des Livres futurs.

Aucun texte rogné, chevauchement, tableau hors page, rotation incorrecte, glyphe manquant ou carré noir n’a été retenu. Les titres longs se replient dans les marges et les blocs de code observés restent lisibles.

## 6. Portes qualité

- [x] Q0 — intégrité, métadonnées et ordre de compilation ;
- [x] Q1 — conformité éditoriale et explication des blocs ;
- [x] Q2 — liens, identifiants, audits, preuves et frontières ;
- [x] Q3 — validation technique statique transversale ;
- [x] Q4 — sécurité documentaire et absence de secrets ;
- [x] Q5 — compilation Pandoc/XeLaTeX, préflight et inspection visuelle.

## 7. Décision

**Livre II accepté pour publication technique avec réserves globales de collection.**

Les réserves propres à la construction PDF de fin du Livre II sont closes. Le Livre III peut commencer selon son plan maître.

Deux réserves générales empêchent encore de qualifier la collection de publication officielle finale :

1. aucune licence globale n’est définie et `LICENSE.md` est absent ;
2. le PDF produit par la chaîne actuelle n’est pas balisé pour les lecteurs d’écran (`Tagged: no`).

Ces choix ne sont pas corrigés automatiquement : le premier exige une décision juridique du propriétaire, le second une évolution dédiée de la chaîne de publication et une validation d’accessibilité.

## 8. Réserves runtime

Cette campagne ne matérialise pas le Starter Kit et n’exécute pas Godot, GUT, les services IA, les scènes pédagogiques ou les procédures Windows/WSL décrites. Les niveaux `runtime-tested` restent attachés aux futures campagnes d’exécution sur les environnements concernés.
