---
title: "Audit du Livre II — Chapitre 26"
id: "DOC-L2-QA-AUDIT-CH26"
status: "complete"
version: "1.0.1"
chapter-id: "DOC-L2-CH26"
chapter-version: "1.0.1"
audit-level: "static-review"
audit-date: "2026-07-21T15:28:42+02:00"
last-verified: "2026-07-21T15:28:42+02:00"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit du chapitre 26 — Outils d’édition internes et pipelines de contenu

## 1. Porte de création

Le chapitre a été créé sur la branche dédiée `docs/livre-ii-ch26-outils-edition-pipelines` après clôture du chapitre 25, correction de la gouvernance GPT-5.6 Sol et vérification de l’absence de chapitre, branche ou pull request concurrente.

## 2. Résultats

- lignes finales : **2660** ;
- titres Markdown : **74** ;
- blocs de code ou de données : **71** ;
- marqueurs d’explication : **71** ;
- cas d’erreurs détaillés : **10** ;
- contre-exemples expliqués : **10** ;
- corrections expliquées : **10** ;
- doublons de titres : **0** ;
- paragraphes longs dupliqués : **0** ;
- blocs significatifs sans explication : **0** ;
- commandes de validation QA dans le chapitre lecteur : **0** ;
- instruction `Prochaine étape` dans le chapitre : **0** ;
- métadonnée ou en-tête de niveau de raisonnement dans le chapitre : **0** ;
- synthèse finale `Project Asteria` : **présente**.
- segments d’explication antérieurs conservés : **166** ;
- segments d’explication antérieurs perdus : **0** ;
- points pédagogiques complémentaires ajoutés : **304** ;
- sections Solo/Studio rendues en Markdown ordinaire : **oui**.

## 3. Complétude et frontières

Le chapitre couvre scripts `@tool`, plugins d’éditeur, docks, inspecteurs, annulation, validation structurée, importeurs versionnés, graphes de dépendances, sérialisation canonique, empreintes, manifestes, provenance, staging, transactions de fichiers, synchronisation de l’éditeur, IA consultative et exécution headless.

Les chapitres 14 à 25 restent propriétaires des états runtime. Le chapitre 26 produit et contrôle des définitions, catalogues, artefacts et reçus ; il ne devient pas une autorité de gameplay. Les tests automatisés systématiques restent au chapitre 27, la journalisation et la reproductibilité au chapitre 28, et l’automatisation Python à grande échelle au chapitre 29.

## 4. Revue statique

Les contrats `EditorPlugin`, `EditorInspectorPlugin`, `EditorImportPlugin`, `EditorUndoRedoManager`, `EditorFileSystem`, `ResourceSaver`, `@tool` et les options de ligne de commande Godot ont été relus contre la documentation stable officielle. Les exemples protègent les cycles de vie symétriques, l’annulation, la séparation source/artefact/cache, la déterminisme des empreintes, la promotion staged et l’absence d’autorité runtime.

Cette revue ne constitue pas une exécution du parseur GDScript ni une installation réelle du plugin dans Godot `4.7.1-stable`.

## 5. Explications pédagogiques



Les **71** blocs possèdent **71** marqueurs. Les explications antérieures ont été décomposées en **166** segments techniques conservés mot pour mot, puis regroupées sous des rubriques uniques et adaptées. Les libellés génériques sont interdits ; chaque point cite un champ, une fonction, une garde, un retour, un effet, un chemin ou une relation réellement visible dans le bloc. **304** segments complémentaires spécifiques ont été ajoutés à partir de la syntaxe et de la structure propres à chaque extrait.

## 6. Réserves

- parseur Godot 4.7.1 non exécuté ;
- plugin `EditorPlugin` non activé dans un projet matérialisé ;
- dock et inspecteur non instanciés ;
- annulation éditoriale non testée ;
- importeur personnalisé non enregistré ni exécuté ;
- transaction de fichiers et restauration non testées ;
- service IA local non appelé ;
- validation headless non exécutée sur le Starter Kit ;
- performances sur grand catalogue non mesurées ;
- aucun PDF construit.

## 7. Décision

Le chapitre 26 est **accepté au niveau `static-review`**, sous les réserves runtime et PDF de fin de Livre.
