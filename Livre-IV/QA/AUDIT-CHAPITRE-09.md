---
title: "Audit post-création — Livre IV, chapitre 9"
id: "DOC-L4-QA-AUDIT-CH09"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
chapter-id: "DOC-L4-CH09"
chapter-version: "1.0.0"
audit-date: "2026-07-26T08:52:20+02:00"
last-verified: "2026-07-26T08:52:20+02:00"
audit-level: "static-review"
protocol: "Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit post-création — Chapitre 9

## 1. Décision

Le chapitre est accepté au niveau `static-review` avec réserves de matérialisation du gestionnaire de chargement, des profils de streaming, des scènes de transition, des tests de stockage lent et des campagnes de parcours prolongé.

Aucun gestionnaire runtime, profil qualifié, scène de transition intégrée, série de chargement ou gain de `Project Asteria` n’est revendiqué comme produit.

## 2. Périmètre comparé au plan maître

Le chapitre couvre les objectifs du plan maître :

- chargement en arrière-plan ;
- transitions, préchargement et éviction ;
- zones, chunks et priorités ;
- progression fiable et accessible ;
- erreurs, reprises et annulation.

Les livrables sont préparés comme contrats : gestionnaire de chargement, profils de streaming, scènes de transition, tests de stockage lent et rapport de temps de chargement.

## 3. Frontières contrôlées

- le chapitre 8 conserve budgets mémoire, fuites et caches génériques ;
- le chapitre 9 possède files, transitions, streaming, progression et erreurs ;
- le chapitre 10 conservera fréquences de mise à jour et optimisation des systèmes actifs ;
- le Livre III conserve la conception du monde et la production des assets ;
- chargement, instanciation et activation restent des phases distinctes ;
- l’annulation logique n’est pas présentée comme interruption garantie du travail interne ;
- aucune amélioration n’est acceptée depuis une transition chaude unique.

## 4. Contrôles pédagogiques

- vocabulaire demande, lecture, décodage, dépendance, staging, activation, chunk et éviction défini ;
- budgets de transition, concurrence et mémoire documentés ;
- manifeste de build, stockage et cache préparé ;
- architecture persistante de transition expliquée ;
- `ResourceLoader.load_threaded_request()`, statut et récupération encadrés ;
- polling réparti entre les frames et progression pondérée documentés ;
- priorités, vieillissement, admission et coalescence des chemins traités ;
- annulation logique, erreurs, reprises bornées et replis distingués ;
- modes de cache et dépendances inspectés ;
- scènes de transition et activation sous racine persistante documentées ;
- zones, chunks, hystérésis, prédiction et éviction bornées ;
- tests de stockage lent, parcours prolongé et rapport avant/après préparés ;
- modes Solo et Studio documentés ;
- dix diagnostics suivent la séquence sémantique complète ;
- références techniques présentées sous forme de liens Markdown cliquables.

## 5. Contrôles documentaires

- lignes : 2006 ;
- titres : 65 ;
- blocs de code ou données : 54 ;
- marqueurs d’explication : 54 ;
- explications structurées hors diagnostics : 34 ;
- diagnostics détaillés : 10 ;
- exemples fautifs expliqués : 10 ;
- exemples corrigés expliqués : 10 ;
- titres dupliqués : 0 ;
- blocs significatifs dupliqués : 0 ;
- paragraphes longs dupliqués : 0 ;
- synthèse opérationnelle `Project Asteria` présente ;
- absence de recommandation GPT, de prochaine action et de chaîne d’export du guide dans le texte lecteur.

## 6. Exactitude technique

Le chapitre distingue `preload()`, chargement synchrone et chargement fileté. Il précise que `load_threaded_get()` peut bloquer si la ressource n’est pas encore chargée et recommande l’interrogation du statut sur plusieurs frames.

Les extraits utilisent `ResourceLoader.exists()`, `load_threaded_request()`, `load_threaded_get_status()`, `load_threaded_get()`, `get_dependencies()`, `has_cached()`, `get_resource_uid()`, `PackedScene.instantiate()` et `SceneTree.change_scene_to_packed()` avec leurs préconditions.

Les modes de cache, les APIs thread-safe et les tâches personnalisées sont présentés avec limites. L’arbre de scène actif n’est pas manipulé depuis un thread arbitraire.

## 7. Contrôle des régressions

- baseline et candidate utilisent build, stockage et état de cache comparables ;
- froid, chaud, lecture, staging et activation sont séparés ;
- médiane, p95, p99, maximum et blocage principal sont conservés ;
- succès, annulations et erreurs sont analysés séparément ;
- mémoire transitoire et coût de reconstruction sont contrôlés ;
- parcours prolongé et erreurs injectées sont prévus ;
- tests fonctionnels, accessibilité et progression honnête restent obligatoires ;
- rollback et menu sûr sont définis avant décision ;
- l’approbation humaine est conservée.

## 8. Réserves ouvertes

- gestionnaire de chargement non matérialisé ;
- catalogue et profils de streaming non qualifiés ;
- scènes de transition non intégrées ;
- manifeste de stockage non rempli ;
- aucune série froide ou chaude produite ;
- aucun test de stockage lent exécuté ;
- aucun parcours prolongé exécuté ;
- aucune politique d’éviction exécutée ;
- aucune campagne avant/après réalisée ;
- aucune suite fonctionnelle exécutée ;
- aucune revue d’accessibilité exécutée ;
- aucun coût d’instrumentation mesuré ;
- licence globale de collection non définie ;
- balisage d’accessibilité de l’export final toujours ouvert.

## 9. Conclusion

Le chapitre satisfait le périmètre du plan maître au niveau documentaire et statique. Les contrôles du lot doivent réussir avant la fermeture de la preuve QA.
