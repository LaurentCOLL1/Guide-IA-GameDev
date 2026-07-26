---
title: "Audit post-création — Livre IV, chapitre 10"
id: "DOC-L4-QA-AUDIT-CH10"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
chapter-id: "DOC-L4-CH10"
chapter-version: "1.0.0"
audit-date: "2026-07-26T10:13:20+02:00"
last-verified: "2026-07-26T10:13:20+02:00"
audit-level: "static-review"
protocol: "Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit post-création — Chapitre 10

## 1. Décision

Le chapitre est accepté au niveau `static-review` avec réserves de matérialisation des benchmarks, seuils d’activation, LOD logiques, pools gameplay, migrations vers les API serveur et campagnes avant/après.

Aucun gain CPU, seuil qualifié, pool runtime, campagne de profiler ou optimisation exécutée de `Project Asteria` n’est revendiqué comme produit.

## 2. Périmètre comparé au plan maître

Le chapitre couvre les objectifs du plan maître :

- réduction des fréquences de mise à jour ;
- pooling, activation par distance et LOD logique ;
- découpage des scènes et systèmes ;
- optimisation des signaux, recherches et allocations ;
- préservation de la lisibilité et de la testabilité.

Les livrables sont préparés comme contrats : catalogue de techniques, benchmarks, exemples avant/après, seuils d’activation et checklist de revue.

## 3. Frontières contrôlées

- le chapitre 6 conserve le profilage CPU général ;
- le chapitre 7 conserve le coût GPU et le rendu ;
- le chapitre 8 conserve budgets mémoire, fuites et caches génériques ;
- le chapitre 9 conserve chargement et streaming ;
- le chapitre 10 possède le coût des scènes et systèmes déjà actifs ;
- le chapitre 11 ouvrira l’architecture multijoueur ;
- représentation, simulation stratégique et autorité gameplay sont distinguées ;
- aucune optimisation n’est présentée comme bénéfique sans profiler et tests.

## 4. Contrôles pédagogiques

- coût par appel, fréquence, multiplicité, quota, time slicing, LOD logique et dette définis ;
- contrat de benchmark et manifeste d’environnement préparés ;
- médiane, p95, p99, maximum et échantillons bruts couverts ;
- traitement visuel, physique, entrée et mode global distingués ;
- accumulateur, time slicing, quotas adaptatifs et ordre d’exécution encadrés ;
- activation par visibilité, distance et hystérésis distinguée ;
- LOD logique, autorité stratégique et conversion d’état documentés ;
- groupes, appels différés uniques, références mises en cache et index spatial traités ;
- cycle de vie des signaux et coalescence documentés ;
- pooling borné, remise à zéro et tampons réutilisés encadrés ;
- découpage de scènes et porte de migration serveur documentés ;
- threads limités à la préparation de données indépendantes ;
- comparaison avant/après, seuils, porte de promotion et rollback préparés ;
- modes Solo et Studio documentés ;
- dix diagnostics suivent la séquence sémantique complète ;
- références techniques présentées sous forme de liens Markdown cliquables.

## 5. Contrôles documentaires

- lignes : 1951 ;
- titres : 62 ;
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

Le chapitre précise que `set_process(false)` ne désactive pas `_physics_process()` ni les callbacks d’entrée. Il réserve `PROCESS_MODE_DISABLED` aux sous-arbres dont tous les callbacks peuvent être suspendus.

Il documente `process_priority`, `process_physics_priority`, `VisibleOnScreenEnabler3D`, `SceneTree.call_group_flags()`, `GROUP_CALL_DEFERRED`, `GROUP_CALL_UNIQUE`, les groupes, les références faibles et les API serveur avec leurs limites.

La visibilité caméra n’est jamais utilisée comme autorité gameplay. L’arbre de scène actif n’est pas manipulé depuis un thread arbitraire. Les API serveur restent une option de dernier recours après mesure.

## 7. Contrôle des régressions

- baseline et candidate utilisent le même scénario et le même environnement ;
- une cause principale est modifiée ;
- fréquence, multiplicité et portée sont mesurées ;
- latence et famine des files sont contrôlées ;
- transitions de LOD logique et réveil sont testées ;
- pooling et remise à zéro possèdent un contrat ;
- mémoire et chargements restent des portes indépendantes ;
- suite fonctionnelle, déterminisme et lisibilité restent obligatoires ;
- rollback défini avant décision ;
- approbation humaine conservée.

## 8. Réserves ouvertes

- scène de benchmark non matérialisée ;
- manifeste d’environnement non rempli ;
- aucune capture de profiler produite ;
- aucune série baseline ou candidate produite ;
- fréquences, quotas et seuils non qualifiés ;
- LOD logique non exécuté ;
- pool gameplay non intégré ni testé ;
- migration vers une API serveur non exécutée ;
- préparation en thread non exécutée ;
- aucune campagne avant/après réalisée ;
- aucune suite fonctionnelle exécutée ;
- aucune validation de latence ou de déterminisme exécutée ;
- aucune revue de lisibilité ou de testabilité exécutée ;
- aucun coût d’instrumentation mesuré ;
- licence globale de collection non définie ;
- balisage d’accessibilité de l’export final toujours ouvert.

## 9. Conclusion

Le chapitre satisfait le périmètre du plan maître au niveau documentaire et statique. Les contrôles du dépôt ont réussi ; la preuve QA peut être fermée avec les réserves déclarées.
