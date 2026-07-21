---
title: "Audit du Livre II — Chapitre 25"
id: "DOC-L2-QA-AUDIT-CH25"
status: "complete"
version: "1.0.2"
chapter-id: "DOC-L2-CH25"
chapter-version: "1.0.2"
audit-level: "static-review"
audit-date: "2026-07-21T19:59:30+02:00"
last-verified: "2026-07-21T19:59:30+02:00"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit du chapitre 25 — Narration, quêtes, codex et connaissances

## 1. Porte de création

Le chapitre a été créé sur la branche dédiée `docs/livre-ii-ch25-narration-quetes-codex` après vérification du chapitre 24 et des frontières avec les systèmes 14 à 24.

## 2. Résultats

- lignes finales : **1438** ;
- titres Markdown : **55** ;
- blocs de code ou de données : **55** ;
- marqueurs d’explication : **55** ;
- cas d’erreurs détaillés : **10** ;
- contre-exemples expliqués : **10** ;
- corrections expliquées : **10** ;
- doublons de titres : **0** ;
- paragraphes longs dupliqués : **0** ;
- blocs significatifs sans explication : **0** ;
- commandes de validation QA dans le chapitre lecteur : **0** ;
- instruction `Prochaine étape` dans le chapitre : **0** ;
- synthèse finale `Project Asteria` : **présente**.
- segments d’explication antérieurs conservés : **100** ;
- segments d’explication antérieurs perdus : **0** ;
- points pédagogiques complémentaires ajoutés : **202** ;
- sections Solo/Studio rendues en Markdown ordinaire : **oui**.

## 3. Complétude et frontières

Le chapitre couvre faits narratifs, arcs, quêtes, objectifs, conditions, conséquences, codex, connaissances, journal, idempotence, IA consultative et persistance. Les systèmes 14 à 24 restent propriétaires de leurs états et préparent toute conséquence externe.

## 4. Revue statique

Les signatures, types, sentinelles, révisions, copies détachées, décisions à trois états, limites, idempotence, commits multi-autorités et restauration préparée ont été relus. Cette revue ne constitue pas une exécution du parseur GDScript.

## 5. Explications pédagogiques



Les **55** blocs possèdent **55** marqueurs. Les explications antérieures ont été décomposées en **100** segments techniques conservés mot pour mot, puis regroupées sous des rubriques uniques et adaptées. Les libellés génériques sont interdits ; chaque point cite un champ, une fonction, une garde, un retour, un effet, un chemin ou une relation réellement visible dans le bloc. **202** segments complémentaires spécifiques ont été ajoutés à partir de la syntaxe et de la structure propres à chaque extrait.

## 6. Réserves

- parseur Godot 4.7.1 non exécuté ;
- collections typées non vérifiées au runtime ;
- commit narratif multi-autorités non exécuté ;
- adaptateurs des systèmes 14 à 24 non matérialisés ;
- scène pédagogique non instanciée ;
- restauration non exécutée ;
- performances non mesurées ;
- replay interplateforme non vérifié ;
- aucun PDF construit.


Les sections pédagogiques d’erreurs conservent leur séquence sémantique directe : symptôme, exemple fautif, explication du défaut, exemple corrigé et explication de la correction. Les rubriques générales de restructuration ne sont pas appliquées à ces deux explications, afin d’éviter répétitions, sous-titres intermédiaires et commentaires génériques.

## 7. Décision

Le chapitre 25 est **accepté au niveau `static-review`**, sous les réserves runtime et PDF de fin de Livre.
