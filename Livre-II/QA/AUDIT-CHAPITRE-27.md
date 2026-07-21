---
title: "Audit du Livre II — Chapitre 27"
id: "DOC-L2-QA-AUDIT-CH27"
status: "complete"
version: "1.0.2"
chapter-id: "DOC-L2-CH27"
chapter-version: "1.0.1"
audit-level: "static-review"
audit-date: "2026-07-22T01:40:00+02:00"
last-verified: "2026-07-22T01:40:00+02:00"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit du chapitre 27 — Tests unitaires, tests d’intégration et simulations

## 1. Porte de création

Le chapitre a été créé sur la branche dédiée `docs/livre-ii-ch27-tests-simulations` depuis `main`, après fusion de la correction sémantique des sections d’erreurs des chapitres 17 à 26. Aucun chapitre 27, aucune branche homonyme et aucune pull request concurrente n’étaient présents.

## 2. Résultats

- lignes finales : **1961** ;
- titres Markdown contrôlés : **74** ;
- blocs de code ou de données : **64** ;
- marqueurs d’explication : **64** ;
- explications structurées hors sections d’erreurs : **44** ;
- cas d’erreurs détaillés : **10** ;
- contre-exemples expliqués : **10** ;
- corrections expliquées : **10** ;
- doublons de titres : **0** ;
- paragraphes longs dupliqués : **0** ;
- blocs sans explication identifiable : **0** ;
- sections Solo/Studio placées dans un bloc de code : **0** ;
- commandes de procédure QA dans le chapitre lecteur : **0** ;
- instruction de pilotage du chapitre suivant : **0** ;
- métadonnée ou en-tête de niveau de raisonnement : **0** ;
- synthèse finale `Project Asteria` : **présente**.

## 3. Complétude et frontières

Le chapitre distingue tests unitaires, tests de composant, tests d’intégration, simulations déterministes, campagnes de non-régression et campagnes de plateforme. Il documente GUT, sa gouvernance de dépendance, l’organisation des suites, les assertions, les fixtures, builders, fakes, stubs, spies, scènes sous `SceneTree`, signaux bornés, codecs, fichiers temporaires, SQLite, sauvegardes, pipelines de contenu, adaptateurs enregistrés, scénarios versionnés, graines, empreintes, invariants, golden files, budgets d’opérations, rapports JUnit et critères de passage.

Le chapitre exerce les contrats des chapitres 1 à 26 sans transférer leurs autorités vers le framework de test. Les journaux structurés, la corrélation et les paquets de reproductibilité détaillés restent au chapitre 28. L’orchestration Python des campagnes et la génération de données restent au chapitre 29. L’organisation finale des parcours Solo et Studio reste au chapitre 30.

## 4. Revue statique des références

Les distinctions entre les tests du moteur et les tests de scripts utilisateur, le mode headless, l’exécution d’un script de ligne de commande et les contrats de `SceneTree` ont été relus contre la documentation officielle Godot 4.7.

La matrice de compatibilité, l’installation, la licence, la CLI, les codes de sortie, les fichiers `.gutconfig.json`, les doubles, stubs, spies, tests paramétrés, attentes bornées, `simulate()` et l’export JUnit ont été relus contre le dépôt et la documentation officiels de GUT destinés à Godot 4.7.

Cette revue ne constitue ni une installation de GUT, ni une analyse par le parseur GDScript, ni une exécution de Godot.

## 5. Explications pédagogiques

Les **64** blocs possèdent **64** marqueurs. Les **44** blocs hors sections d’erreurs sont expliqués par des points spécifiques : rôle concret, paramètres et types, déroulement, valeurs de retour, effets de bord, invariants, résultat attendu, dépendances et limites selon l’extrait.

Les dix cas pédagogiques d’erreurs suivent directement la séquence sémantique obligatoire : symptôme, exemple fautif, `Pourquoi cet exemple est fautif`, exemple corrigé, puis `Pourquoi la correction fonctionne`. Aucun wrapper `Explication structurée du bloc`, aucune rubrique parasite et aucune répétition ne s’intercalent dans ces séquences.

Les parcours Solo et Studio sont rédigés en Markdown ordinaire. Les blocs de texte sont réservés aux arborescences, matrices, configurations et artefacts littéraux.

## 6. Contrôles particuliers

- le test moteur `--test` n’est pas présenté comme runner des scripts du projet ;
- la dépendance GUT est épinglée par commit et séparée du runtime ;
- `SCRIPT_ONLY` reste la stratégie de doubles par défaut ;
- les assertions exactes sont séparées des comparaisons flottantes avec tolérance ;
- l’heure logique et les suites pseudo-aléatoires sont injectées ;
- les fichiers, bases et workspaces utilisent des racines temporaires uniques ;
- les scènes et signaux utilisent des attentes bornées ;
- les simulations déclarent version, scénario, graines et maximum de ticks ;
- les golden files ne sont jamais régénérés par le test de comparaison ;
- les retries automatiques d’un test instable sont interdits ;
- les appels IA ou réseau réels sont exclus des suites déterministes ;
- les codes de sortie non nuls restent bloquants.

## 7. Réserves

- parseur Godot `4.7.1-stable` non exécuté ;
- GUT non téléchargé, non activé et non exécuté ;
- fichiers de support de test non matérialisés dans le Starter Kit ;
- scènes non instanciées dans un `SceneTree` réel ;
- signaux et callbacks de frame non observés ;
- bases SQLite temporaires non créées ;
- sauvegardes et transactions de fichiers non exercées ;
- adaptateurs HTTP, WebSocket et processus compagnon non exécutés ;
- simulations, graines et golden files non rejoués ;
- rapports JUnit non produits ;
- performances et reproductibilité multiplateforme non mesurées ;
- aucun PDF construit.

## Correction terminologique du 22 juillet 2026

Les calques anglais relatifs à `wall-clock time` ou `wall-clock duration` ont été remplacés par `durée réelle (durée de l’horloge système)` ; `horloge système` désigne la source temporelle réelle. Le validateur documentaire refuse désormais les anciennes formulations.

## 8. Décision

Le chapitre 27 est **accepté au niveau `static-review`**, sous réserve d’une matérialisation et d’une campagne runtime ultérieures dans le Starter Kit, ainsi que du PDF de fin de Livre II.
