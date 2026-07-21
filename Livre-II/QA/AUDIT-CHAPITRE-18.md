---
title: "Audit du Livre II — Chapitre 18"
id: "DOC-L2-QA-AUDIT-CH18"
status: "complete"
version: "1.0.1"
chapter-id: "DOC-L2-CH18"
chapter-version: "1.0.1"
audit-level: "static-review"
audit-date: "2026-07-21T17:35:51+02:00"
last-verified: "2026-07-21T17:35:51+02:00"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit du chapitre 18 — Combat

## 1. Porte de brouillon

Le premier état permanent du chapitre a conservé `status: draft`, `version: 0.9.0`, `audit-status: pending` et `audit-level: not-audited`. La présente version `1.0.0` résulte d’une seconde lecture distincte, de corrections techniques et d’un contrôle documentaire séparé.

## 2. Résultats

- lignes finales : **3957** ;
- titres Markdown : **74** ;
- blocs de code ou de données : **67** ;
- marqueurs d’explication : **67** ;
- cas d’erreurs détaillés : **14** ;
- contre-exemples expliqués : **14** ;
- corrections expliquées : **14** ;
- liens vers la documentation officielle Godot : **20** ;
- doublons de titres : **0** ;
- blocs significatifs sans explication : **0** ;
- longs paragraphes dupliqués : **0** ;
- instruction `Prochaine étape` dans le chapitre : **0**.

## 3. Complétude et frontières

Le chapitre couvre les commandes typées, l’affrontement, les participants, les côtés, l’initiative, les cibles, la portée, la ligne de vue, le toucher, les dégâts, la défense, les résistances, la garde, les états, les événements, l’historique, les budgets, la simulation hors écran et la sauvegarde.

Les responsabilités restent séparées :

- les agents et les contrôleurs choisissent une demande ;
- `CombatService` valide et résout l’impact ;
- `CharacterRuntimeState` conserve santé, endurance et état de vie ;
- `CombatantState` conserve initiative, côté, garde et états temporaires ;
- la présentation consomme les événements sans recalculer l’issue ;
- les compétences, objets, économie, politique et narration restent autorités de leurs règles.

## 4. Corrections issues de la seconde lecture

La seconde lecture a notamment :

1. ajouté les côtés opposés et une politique explicite de tir allié ;
2. supprimé le départage fondé sur `hash()` au profit d’un ordre lexical stable ;
3. corrigé l’initialisation du RNG afin d’enregistrer un `state` réellement produit après la graine ;
4. séparé la graine et l’état 64 bits en mots de 32 bits pour éviter une perte de précision JSON ;
5. ajouté des copies détachées profondes pour affrontements, participants, états et événements ;
6. rendu la file de commandes défensive et bornée ;
7. matérialisé les ports manquants, la fabrique d’affrontement et l’unité de commit ;
8. enregistré l’historique candidat avant le commit et émis les événements seulement après succès ;
9. complété les branches `ATTACK`, `GUARD`, `WAIT` et `DISENGAGE` ;
10. complété le codec strict de sauvegarde et distingué un document vide valide d’un échec de décodage ;
11. validé toutes les références, séquences, bornes et doublons avant remplacement du dépôt ;
12. empêché toute mutation directe depuis l’agent, le raycast, l’animation ou les données de conception.

## 5. Revue du code et des données

Les extraits ont été relus statiquement pour vérifier :

- les types et signatures ;
- les valeurs de retour et refus contrôlés ;
- les limites de tableaux, files et historiques ;
- les ordres canoniques ;
- la monotonie des ticks et séquences ;
- les copies défensives ;
- les candidats préparés avant commit ;
- la persistance limitée à l’état autoritaire ;
- l’absence de `Node`, de `Resource` partagée et de cache dans les snapshots.

Cette revue ne constitue pas une exécution du parseur GDScript.

## 6. Contextes d’utilisation

Les 67 blocs portent un contexte explicite ou sont des sorties de référence. Les repères principaux sont :

- `[VSC]` : **31** ;
- `[LECTURE]` : **36** ;
- `[APP]` : **1**.

La différence entre le nombre de repères et de blocs vient des consignes d’interface qui ne contiennent pas nécessairement un bloc clôturé.

## 7. Sources

Les API moteur sont reliées aux pages officielles Godot 4.7 concernant notamment `Resource`, `RefCounted`, `RandomNumberGenerator`, `PhysicsDirectSpaceState3D`, `PhysicsRayQueryParameters3D`, `Dictionary`, `Array`, `StringName`, `Vector3`, `JSON`, `Error`, `Engine`, `Performance` et les signaux.

La version de référence du projet reste Godot `4.7.1-stable`.

## 8. Clôture éditoriale

La dernière section est une synthèse opérationnelle des décisions retenues pour `Project Asteria`. Elle ne contient ni chemin du chapitre suivant, ni niveau GPT futur, ni instruction de production. Ces informations restent dans `CONTINUITE-PROJET.md`.

## 9. Explications pédagogiques


Les **67** blocs possèdent **67** marqueurs. Les explications antérieures ont été décomposées en **217** segments techniques conservés mot pour mot, puis regroupées sous des rubriques uniques et adaptées. Les libellés génériques sont interdits ; chaque point cite un champ, une fonction, une garde, un retour, un effet, un chemin ou une relation réellement visible dans le bloc.

## 9. Réserves

- le parseur Godot n’a pas été exécuté ;
- la scène de démonstration n’a pas été instanciée ;
- les signaux, commandes et commits multi-dépôts n’ont pas été exécutés ;
- les raycasts et collisions n’ont pas été testés dans une scène 3D ;
- les performances de l’ordonnanceur n’ont pas été mesurées ;
- la restauration de sauvegarde n’a pas été exécutée ;
- le replay multiplateforme n’a pas été vérifié ;
- aucun PDF n’a été construit.

## 10. Décision

Le chapitre 18 est **accepté au niveau `static-review`**, sous les réserves runtime et PDF indiquées ci-dessus.
