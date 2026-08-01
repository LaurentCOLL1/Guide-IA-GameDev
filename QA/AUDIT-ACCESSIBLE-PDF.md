---
title: "Audit — PDF balisé et accessibilité"
id: "QA-AUDIT-ACCESSIBLE-PDF"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
last-verified: "2026-08-01T06:49:00+02:00"
audit-level: "runtime-tested-linux"
license: "CC-BY-SA-4.0"
---

# Audit — PDF balisé et accessibilité

## Objectif

Produire un candidat PDF technique de la collection avec arbre de structure, langue de document, métadonnées de titre et d’auteur, ordre des 162 sources maîtrisé et diagnostic PDF/UA automatisé, sans dégrader la publication multiformat déjà qualifiée.

## Périmètre qualifié

- source unique définie par `contents.txt` ;
- construction Pandoc 3.10 et LuaHBTeX 1.24.0 avec TeX Live 2026 ;
- `\DocumentMetadata` placé avant `\documentclass` ;
- langue `fr-FR` et cible technique PDF/UA-1 ;
- images TeX Live et veraPDF épinglées par digest ;
- manifeste de taille et d’empreinte SHA-256 ;
- contrôles `qpdf`, `pdfinfo`, catalogue PDF et extraction textuelle ;
- diagnostic veraPDF `ua1` conservé intégralement ;
- inventaire indépendant des types de balises avec pypdf 5.9.0 ;
- audit des alternatives textuelles dans les sources Markdown et HTML ;
- comparaison textuelle et visuelle avec le PDF classique ;
- validations documentaires et de licence du dépôt.

## Résultat runtime

Le workflow `Build Accessible Tagged PDF`, run `30684329205`, a réussi sous Ubuntu 24.04 sur la tête `9f7f4feb3e5808d68057f67ba336e068d3a0a0c2`.

Artefacts conservés :

- `guide-ia-gamedev-accessible-tagged-pdf` — identifiant `8813427010`, digest `sha256:fe3f4c844b5d3e14afe2d01ca070b11d8f215aa92563c79f502d410c4d7bc861` ;
- `guide-ia-gamedev-accessible-pdf-diagnostics` — identifiant `8813426329`, digest `sha256:57e86c3de2ffd3bf31a51a97417077456a30fd923029f6bd32e2e5efaf1cfde3`.

Le candidat possède :

- 4 214 pages A4 ;
- 28 766 695 octets ;
- SHA-256 `629ed5231627b84ea1832ffea9a60a403d3818b785949dbc3c2425ddac33159b` ;
- `Tagged: yes`, `/Marked true`, `/StructTreeRoot` et langue `fr-FR` ;
- titre, auteur, dates et préférence d’affichage du titre ;
- manifeste concordant avec les octets générés ;
- statut `technical-tagged-pdf-not-official-release`.

Le PDF est ouvert par PyMuPDF, n’est pas chiffré, n’est pas assimilé à un document numérisé et ne contient pas de formulaire XFA.

## Diagnostic PDF/UA machine

veraPDF 1.30.2 a exécuté le profil `PDF/UA-1 validation profile` et a terminé normalement :

- fichier analysé : 28 766 695 octets ;
- résultat machine : conforme au profil ;
- règles réussies : 106 ;
- règles échouées : 0 ;
- contrôles réussis : 20 644 277 ;
- contrôles échoués : 0 ;
- erreur de lecture, exception veraPDF ou tâche échouée : 0.

Cette réussite porte uniquement sur les points vérifiables par veraPDF. Elle ne constitue ni une certification, ni une preuve exhaustive du protocole Matterhorn, ni un test de lecteur d’écran réel.

## Préflight qpdf

`qpdf --check` termine avec le code `3`, qualifié `success-with-reservations`, et le marqueur `operation succeeded with warnings`. Cinq dictionnaires signalent une clé `/Group` dupliquée, aux objets `8860`, `8865`, `8870`, `8875` et `8880` ; la dernière occurrence remplace la précédente.

Ces avertissements sont conservés intégralement dans `qpdf-check.txt` et `qpdf-validation.json`. Ils ne sont ni masqués ni reclassés comme exécution propre. Tout autre code de sortie ou toute absence du marqueur de réussite reste bloquant.

## Inventaire de structure

L’inventaire indépendant confirme :

- un nœud `/Document` ;
- 387 347 éléments `/StructElem` ;
- 187 096 références de contenu marqué `/MCR` ;
- 3 402 références d’objets `/OBJR` ;
- 160 balises de chapitre reliées à `/H1` ;
- 4 802 sections, 2 363 sous-sections et 13 sous-sous-sections ;
- 579 tableaux, 1 633 cellules d’en-tête et 15 758 cellules de données ;
- 4 896 listes non ordonnées, 229 listes ordonnées et 28 926 éléments de liste dans les balises personnalisées et leur `RoleMap` ;
- 5 figures, toutes avec une alternative non vide, et aucune figure à alternative vide ;
- 2 978 liens ;
- 70 553 lignes de code et 5 809 blocs verbatim repérés par leurs balises personnalisées ;
- 254 175 objets indirects visités.

Les cinq alternatives de figures sont `Statut`, `Documentation`, `Moteur`, `3D` et `IA locale`. Leur présence ne prouve pas à elle seule leur pertinence éditoriale dans tous les lecteurs.

## Alternatives dans les sources

L’audit des 162 sources, après exclusion des exemples placés dans les blocs ou spans de code, trouve cinq images destinées au lecteur dans `README.md`. Toutes disposent d’une alternative textuelle non vide. Aucun fichier source manquant et aucune alternative vide ne sont signalés.

## Non-régression multiformat

La même tête `9f7f4feb3e5808d68057f67ba336e068d3a0a0c2` a franchi le workflow `Build Publication Formats`, run `30684329206`, artefact `8813421114`, digest `sha256:e47f97c7a44c3fbc8ec3cccf4298769ae4d0c3f63751ddbce889f8255f77399f`.

Le PDF classique de référence conserve 4 108 pages. Le candidat balisé possède 106 pages supplémentaires en raison des différences de composition LuaLaTeX et de retours à la ligne. Aucune identité de pagination ou d’octets entre les deux moteurs n’est revendiquée.

## Inspection humaine représentative

Le candidat a été rendu avec Poppler à 100 et 130 dpi. L’échantillon inspecté couvre :

- pages 1 à 8 — couverture et table des matières ;
- pages 143 à 150 — fin du sommaire, cinq figures, présentation, listes et tableaux ;
- pages 556 et 1 401 — ouvertures de chapitre et listes ;
- page 3 018 — code, liens et synthèse opérationnelle ;
- pages 3 784 et 3 995 — fiches, tableaux et réserves ;
- pages 4 151 et 4 153 — sources et index croisés ;
- pages 4 206 à 4 214 — licences, notices et fin du volume.

Le texte extrait des pages 145, 146, 556, 3 018, 3 995, 4 151, 4 206, 4 213 et 4 214 suit l’ordre visuel attendu. Les cinq alternatives apparaissent dans l’extraction de la page 145. Les pages échantillonnées ne présentent pas de texte coupé, chevauchement, carré noir, glyphe cassé ou lien visiblement désorganisé.

Les ouvertures et contenus correspondants du PDF classique ont été localisés par leur texte plutôt que par numéro supposé. Les différences observées relèvent de la composition, des retours à la ligne, du style des listes et de la pagination ; aucune perte de contenu évidente n’est constatée dans l’échantillon.

## Validations du dépôt

Sur le run final :

- 162 sources déclarées ;
- 159 identifiants uniques ;
- zéro erreur et zéro avertissement dans la validation légère des chapitres ;
- validation des licences réussie pour `CC-BY-SA-4.0`, `MIT` et `CC0-1.0` ;
- dix fichiers de licence du Companion Pack reliés à la politique globale ;
- arbre Git propre après les validations ;
- sommes de contrôle enregistrées ;
- aucune sortie générée suivie par Git.

## Réserves

- aucun test avec NVDA, JAWS, VoiceOver, Orca ou autre lecteur d’écran réel n’a été exécuté ;
- aucune inspection manuelle exhaustive des 4 214 pages ou des 387 347 éléments structurés n’est revendiquée ;
- l’ordre de lecture, la hiérarchie, les listes, les tableaux, les notes, le code et les formules ne sont contrôlés humainement que sur un échantillon ;
- les cinq avertissements qpdf sur les clés `/Group` dupliquées restent ouverts ;
- aucune certification PDF/UA, conformité Matterhorn exhaustive ou interopérabilité universelle n’est revendiquée ;
- aucune identité byte pour byte entre systèmes, versions d’outils ou moteurs TeX n’est revendiquée ;
- le candidat reste un build technique, pas une release publique officielle.

## Qualification retenue

La seule qualification autorisée pour ce lot est :

```text
tagged-pdf-machine-checked-not-full-pdfua-conformance
```

Dans ce périmètre borné, le lot est accepté au niveau `runtime-tested-linux`. Les contrôles humains non exécutés et les avertissements qpdf restent visibles dans la preuve finale.
