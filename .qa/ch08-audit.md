---
title: "Audit post-création — Livre IV, chapitre 8"
id: "DOC-L4-QA-AUDIT-CH08"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
chapter-id: "DOC-L4-CH08"
chapter-version: "1.0.0"
audit-date: "2026-07-26T08:02:49+02:00"
last-verified: "2026-07-26T08:02:49+02:00"
audit-level: "static-review"
protocol: "Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit post-création — Chapitre 8

## 1. Décision

Le chapitre est accepté au niveau `static-review` avec réserves de matérialisation des budgets mémoire, rapports d’allocations, stratégies de cache, tests de longue durée et campagnes avant/après.

Aucune campagne RAM/VRAM, série de processus, analyse de fuite, qualification de cache ou réduction mémoire de `Project Asteria` n’est revendiquée comme produite.

## 2. Périmètre comparé au plan maître

Le chapitre couvre les objectifs du plan maître :

- mesure de la consommation et des pics RAM/VRAM ;
- identification des fuites, duplications et caches excessifs ;
- gestion de la durée de vie, de la libération et de la réutilisation ;
- réduction des allocations temporaires ;
- définition de limites par plateforme.

Les livrables sont préparés comme contrats : budgets mémoire, rapport d’allocation, stratégie de cache, test de longue durée et procédure de diagnostic.

## 3. Frontières contrôlées

- le chapitre 7 conserve les passes de rendu et le temps GPU ;
- le chapitre 8 possède budgets RAM/VRAM, allocations, caches et longue durée ;
- le chapitre 9 conservera streaming, préchargement, priorités et transitions ;
- le Livre III conserve la production des assets optimisés ;
- aucun compteur moteur n’est présenté comme inventaire exhaustif du processus ou du pilote ;
- une baisse de pic ne suffit pas si le plateau ou les orphelins augmentent ;
- aucune réduction de qualité n’est acceptée sans revue visuelle et fonctionnelle.

## 4. Contrôles pédagogiques

- vocabulaire RAM, VRAM, working set, mémoire privée, rétention, duplication, cache, pool et fragmentation défini ;
- budgets souples et durs par plateforme documentés ;
- contrat cyclique, warm-up, phases et plateaux préparés ;
- moniteurs `Performance`, appels `OS` et `RenderingServer` distingués ;
- échantillons moteur et système corrélés par PID, phase et cycle ;
- médiane, p95, p99, maximum, plateaux et pente couverts ;
- critères de suspicion de fuite bornés ;
- durée de vie des nœuds, `WeakRef`, `RefCounted`, signaux et ressources encadrée ;
- caches LRU, caches pondérés, expiration et pools bornés documentés ;
- allocations temporaires, tampons réutilisés et structures compactes traités ;
- textures, images CPU, ressources GPU et sous-ressources distinguées ;
- test de longue durée, rapport avant/après, rollback et portes documentés ;
- modes Solo et Studio documentés ;
- dix diagnostics suivent la séquence sémantique complète ;
- références techniques présentées sous forme de liens Markdown cliquables.

## 5. Contrôles documentaires

- lignes : 1750 ;
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

Le chapitre distingue mémoire statique du moteur, working set, mémoire privée, objets, ressources et indicateurs vidéo. Il ne suppose pas que ces compteurs doivent coïncider.

Les extraits utilisent `Performance.get_monitor()`, `OS.get_static_memory_usage()`, `OS.get_static_memory_peak_usage()`, `OS.get_process_id()` et `RenderingServer.get_rendering_info()` avec leurs limites déclarées.

Les références faibles, caches bornés, pools et duplications sont présentés comme stratégies à mesurer, non comme optimisations universelles. Les scripts Python conservent les valeurs sources et refusent les séries vides ou non finies.

## 7. Contrôle des régressions

- baseline et candidate utilisent le même cycle et le même environnement ;
- les pics et plateaux sont analysés séparément ;
- les fenêtres de récupération sont observées ;
- une variable principale est modifiée ;
- la longue durée complète le test court ;
- le coût de reconstruction du cache est conservé ;
- les tests fonctionnels et visuels restent obligatoires ;
- le rollback est défini avant décision ;
- l’approbation humaine est conservée.

## 8. Réserves ouvertes

- budgets RAM/VRAM non qualifiés ;
- scénario cyclique et fixtures non matérialisés ;
- manifeste d’environnement non rempli ;
- aucune série moteur ou système produite ;
- aucun rapport d’allocations créé ;
- aucune fuite ou rétention attribuée ;
- aucune stratégie de cache exécutée ;
- aucun test de longue durée réalisé ;
- aucune campagne avant/après réalisée ;
- aucune suite fonctionnelle exécutée ;
- aucune comparaison visuelle exécutée ;
- aucun coût d’instrumentation mesuré ;
- licence globale de collection non définie ;
- balisage d’accessibilité de l’export final toujours ouvert.

## 9. Conclusion

Le chapitre satisfait le périmètre du plan maître au niveau documentaire et statique. Les contrôles du lot doivent réussir avant la fermeture de la preuve QA.
