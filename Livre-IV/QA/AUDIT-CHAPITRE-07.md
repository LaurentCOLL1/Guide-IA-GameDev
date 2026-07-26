---
title: "Audit post-création — Livre IV, chapitre 7"
id: "DOC-L4-QA-AUDIT-CH07"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
chapter-id: "DOC-L4-CH07"
chapter-version: "1.0.0"
audit-date: "2026-07-26T03:23:02+02:00"
last-verified: "2026-07-26T03:23:02+02:00"
audit-level: "static-review"
protocol: "Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit post-création — Chapitre 7

## 1. Décision

Le chapitre est accepté au niveau `static-review` avec réserves de matérialisation de la scène de stress, des captures Visual Profiler et externes, des budgets GPU, des profils graphiques et des campagnes avant/après.

Aucune scène de stress, capture de frame, série de temps GPU, qualification de profil ou amélioration visuelle de `Project Asteria` n’est revendiquée comme produite.

## 2. Périmètre comparé au plan maître

Le chapitre couvre les objectifs du plan maître :

- passes de rendu, draw calls, overdraw et shaders ;
- lumières, ombres, transparence et post-traitement ;
- indicateurs VRAM et bande passante ;
- profils graphiques versionnés ;
- adaptation à la Radeon RX 6750 XT de référence.

Les livrables sont préparés comme contrats : budget GPU, captures de frame, profils graphiques, rapport de coût par effet et scène de stress.

## 3. Frontières contrôlées

- le chapitre 6 conserve les benchmarks et budgets CPU ;
- le chapitre 7 possède les campagnes, captures et profils GPU ;
- le chapitre 8 conservera les budgets mémoire, allocations et tests de longue durée ;
- le Livre III conserve la production des assets optimisés ;
- une mesure native reste distincte d’un replay de capture ;
- aucune réduction de qualité n’est acceptée sans comparaison visuelle ;
- aucun indicateur VRAM local n’est présenté comme inventaire exhaustif.

## 4. Contrôles pédagogiques

- vocabulaire passes, draw calls, overdraw, fill rate, shaders, bande passante, VRAM et pipelines défini ;
- distinction CPU de rendu, GPU et synchronisation documentée ;
- budget GPU et contrats de benchmark explicitement qualifiés comme cibles ;
- manifeste AMD, scène de stress et points de capture préparés ;
- Visual Profiler, moniteurs `Performance` et `RenderingServer` expliqués ;
- temps GPU de viewport, draw calls visibles et ombres collectés séparément ;
- médiane, p95, p99, maximum et dépassements couverts ;
- sondes de résolution, transparence, lumières, ombres et post-traitement documentées ;
- LOD, culling, matériaux, shaders et compilations de pipeline encadrés ;
- profils graphiques, captures AMD et inspection RenderDoc distingués ;
- comparaison visuelle, rapport avant/après, rollback et porte de décision documentés ;
- modes Solo et Studio documentés ;
- dix diagnostics suivent la séquence sémantique complète ;
- références techniques présentées sous forme de liens Markdown cliquables.

## 5. Contrôles documentaires

- lignes : 1563 ;
- titres : 63 ;
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

Le chapitre distingue le Profiler standard du Visual Profiler, les catégories CPU de rendu du temps GPU, et les valeurs globales de rendu des informations par viewport.

Les extraits utilisent `Performance.get_monitor()`, `RenderingServer.get_rendering_info()`, `viewport_get_render_info()`, `viewport_set_measure_render_time()` et `viewport_get_measured_render_time_gpu()` avec leurs préconditions.

Les compteurs de compilation de pipeline sont traités comme compteurs et non comme durées. Les captures externes AMD et RenderDoc sont séparées des mesures natives.

La RX 6750 XT 12 Go, RDNA 2, Windows 11 et Forward+ constituent le profil de référence sans prétendre que la compatibilité d’un outil externe a été exécutée.

## 7. Contrôle de qualité visuelle

- caméra, résolution, exposition et profil contrôlés ;
- images de référence et candidates conservées ;
- image de différence prévue ;
- régions importantes soumises à revue humaine ;
- silhouettes, ombres, transparences et effets contrôlés ;
- accessibilité visuelle incluse dans la porte ;
- rollback défini avant décision ;
- profils plateforme séparés.

## 8. Réserves ouvertes

- scène et fixtures de stress non matérialisées ;
- manifeste d’environnement non rempli ;
- aucune capture Visual Profiler créée ;
- aucune capture AMD ou RenderDoc créée ;
- aucun échantillon GPU ou résumé statistique produit ;
- aucun budget GPU qualifié ;
- aucun profil graphique qualifié ;
- aucune campagne avant/après réalisée ;
- aucune comparaison visuelle exécutée ;
- aucune suite fonctionnelle exécutée ;
- aucun coût d’instrumentation mesuré ;
- licence globale de collection non définie ;
- balisage d’accessibilité de l’export final toujours ouvert.

## 9. Conclusion

Le chapitre satisfait le périmètre du plan maître au niveau documentaire et statique. Les contrôles du lot ont réussi et la preuve QA peut être fermée avec les réserves de matérialisation déclarées.
