---
title: "Audit — PDF balisé et accessibilité"
id: "QA-AUDIT-ACCESSIBLE-PDF"
status: "draft"
version: "0.2.0"
lang: "fr-FR"
last-verified: "2026-07-31T17:26:00+02:00"
audit-level: "implementation-pending-runtime"
license: "CC-BY-SA-4.0"
---

# Audit — PDF balisé et accessibilité

## Objectif

Produire un candidat PDF technique de la collection avec arbre de structure, langue de document, métadonnées de titre et d’auteur, ordre des 162 sources maîtrisé et diagnostic PDF/UA automatisé, sans dégrader la publication multiformat déjà qualifiée.

## Périmètre

- source unique définie par `contents.txt` ;
- construction Pandoc et LuaLaTeX avec TeX Live 2026 ;
- `\DocumentMetadata` placé avant `\documentclass` ;
- langue `fr-FR` et cible technique PDF/UA-1 ;
- images TeX Live et veraPDF épinglées par digest ;
- manifeste de taille et d’empreinte SHA-256 ;
- contrôles `qpdf`, `pdfinfo`, catalogue PDF et extraction textuelle ;
- diagnostic veraPDF `ua1` conservé intégralement ;
- inventaire indépendant des types de balises ;
- audit des alternatives textuelles dans les sources Markdown et HTML ;
- comparaison textuelle et visuelle avec le PDF classique ;
- validations documentaires et de licence du dépôt.

## Porte automatique

La qualification runtime doit vérifier :

- intégrité syntaxique avec `qpdf` ;
- valeur `Tagged: yes` exposée par `pdfinfo` ;
- présence de `/MarkInfo`, `/Marked true`, `/StructTreeRoot` et `/Lang` ;
- titre, auteur, nombre de pages et manifeste ;
- concordance exacte de la taille et du SHA-256 ;
- présence des 162 sources déclarées ;
- absence d’image destinée au lecteur sans alternative textuelle non vide ;
- présence et analyse du rapport veraPDF PDF/UA-1 ;
- inventaire des titres, listes, tableaux, figures, alternatives et liens dans l’arbre ;
- validations documentaires et de licence inchangées ;
- absence de sortie générée suivie par Git.

Une absence ou une impossibilité d’analyser le rapport veraPDF est bloquante. Une non-conformité veraPDF doit rester une réserve explicite à corriger ou à justifier ; elle ne peut pas être transformée en réussite PDF/UA.

## Référence multiformat

La même tête documentaire a franchi le workflow classique `Build Publication Formats`, run `30639518132`, artefact `8796952251`, digest `sha256:8127cd03415634c1a7c6f598f30babbe94628efac522bf437548c18606dec8be`.

La référence possède :

- 4 108 pages ;
- une extraction textuelle globale de 7 822 647 octets ;
- le SHA-256 textuel `c34985cb87d2de04a8a741bdb9b4222ace34e5e1cfae6e583473ce110a4279b9` ;
- cinq images avec une alternative non vide dans le HTML ;
- 579 tableaux avec au moins une cellule d’en-tête ;
- aucune rupture de niveau détectée dans la hiérarchie HTML.

Trente et une pages représentatives ont été comparées entre deux builds classiques verts. Les rendus à 110 dpi sont pixel-identiques et les extractions textuelles globales sont identiques, malgré des fichiers PDF non identiques octet pour octet. Cette stabilité constitue la référence de non-régression du candidat balisé ; elle ne prouve pas son accessibilité.

## Échantillon prévu pour le candidat balisé

L’inspection doit couvrir au minimum :

- couverture, table des matières et premières pages ;
- pages 921 à 925 pour des structures sociales et du code ;
- pages 3 649 à 3 652 et 3 660 pour les fiches et matrices ;
- pages 3 806, 3 894 et 3 895 pour tableaux et références ;
- pages 4 009 à 4 013 pour les index croisés ;
- pages 4 104 à 4 108 pour la fin de collection et les notices.

Les numéros du candidat peuvent différer si le balisage change la pagination. Dans ce cas, les mêmes contenus doivent être localisés par extraction textuelle plutôt que par numéro supposé.

## Contrôles humains requis

- ordre de lecture sur l’échantillon ;
- navigation et hiérarchie des titres ;
- pertinence des alternatives textuelles ;
- sémantique des tableaux et listes ;
- liens, notes, blocs de code, sorties terminal et formules ;
- comparaison visuelle avec le PDF classique ;
- comportement avec un lecteur d’écran réel.

Tout contrôle non exécuté reste nommé comme réserve. Une inspection par extraction textuelle ou arbre PDF ne doit pas être présentée comme un test de lecteur d’écran.

## Règle de revendication

La présence de balises et la réussite des contrôles machine ne suffisent pas à revendiquer une conformité PDF/UA complète. Le lot emploie uniquement la qualification :

```text
tagged-pdf-machine-checked-not-full-pdfua-conformance
```

Cette qualification exclut une certification d’accessibilité, une conformité exhaustive au protocole Matterhorn et une garantie d’interopérabilité avec tous les lecteurs d’écran.

## État actuel

La chaîne est implémentée et le PDF classique de référence est qualifié. La preuve du candidat balisé, son rapport veraPDF, son inventaire de structure et sa comparaison finale ne sont pas encore inscrits dans cet audit. Le statut reste `implementation-pending-runtime` jusqu’à lecture des artefacts du workflow et fermeture de la preuve QA.
