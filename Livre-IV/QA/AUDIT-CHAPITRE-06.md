---
title: "Audit post-création — Livre IV, chapitre 6"
id: "DOC-L4-QA-AUDIT-CH06"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
chapter-id: "DOC-L4-CH06"
chapter-version: "1.0.0"
audit-date: "2026-07-26T02:53:24+02:00"
last-verified: "2026-07-26T02:53:24+02:00"
audit-level: "static-review"
protocol: "Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit post-création — Chapitre 6

## 1. Décision

Le chapitre est accepté au niveau `static-review` avec réserves de matérialisation des scènes de benchmark, captures du Profiler, budgets CPU, campagnes avant/après et tests de régression associés.

Aucune scène de benchmark, aucune capture, aucun échantillon de frame, aucun budget qualifié et aucune amélioration runtime de `Project Asteria` ne sont revendiqués comme produits.

## 2. Périmètre comparé au plan maître

Le chapitre couvre les objectifs du plan maître :

- utilisation du Profiler Godot et d’outils système ;
- mesure des scripts, de la physique, de la navigation, de l’IA et des threads ;
- identification de la fréquence, de la durée et des appels coûteux ;
- définition de budgets par frame ;
- prévention des optimisations prématurées.

Les livrables sont préparés comme contrats : scènes de benchmark, captures de profilage, budget CPU, rapport avant/après et checklist de diagnostic.

## 3. Frontières contrôlées

- le chapitre 5 conserve la journalisation et l’observabilité légère ;
- le chapitre 6 possède les campagnes et budgets CPU ;
- le chapitre 7 conservera le profilage GPU et l’optimisation du rendu ;
- le chapitre 8 conservera les budgets mémoire et allocations ;
- aucune amélioration n’est acceptée sans comparaison ;
- aucune optimisation ne remplace les tests fonctionnels ;
- aucun budget théorique n’est présenté comme une mesure observée.

## 4. Contrôles pédagogiques

- vocabulaire frame, tick, temps propre, temps inclusif, goulot, pic, percentile, warm-up et baseline défini ;
- cycle scénario, baseline, hypothèse, modification, mesure et test documenté ;
- budget de frame et sous-budgets explicitement qualifiés comme cibles ;
- contrat de benchmark, environnement, scénarios et warm-up couverts ;
- Profiler Godot, Monitors et singleton `Performance` expliqués ;
- moniteurs personnalisés et chronométrage manuel borné documentés ;
- conservation des échantillons et analyse médiane, p95, p99 et dépassements couverte ;
- outils système limités au contexte hôte ;
- scripts, physique, navigation, IA et tâches parallèles traités séparément ;
- temps propre et temps inclusif distingués ;
- frontière CPU, GPU et attente explicitée ;
- hypothèse, rapport avant/après et porte de décision documentés ;
- coût d’instrumentation et scènes de benchmark encadrés ;
- modes Solo et Studio documentés ;
- dix diagnostics suivent la séquence sémantique complète ;
- références techniques présentées sous forme de liens Markdown cliquables.

## 5. Contrôles documentaires

- lignes : 1396 ;
- titres : 67 ;
- blocs de code ou données : 46 ;
- marqueurs d’explication : 46 ;
- explications structurées hors diagnostics : 26 ;
- diagnostics détaillés : 10 ;
- exemples fautifs expliqués : 10 ;
- exemples corrigés expliqués : 10 ;
- titres dupliqués : 0 ;
- blocs significatifs dupliqués : 0 ;
- paragraphes longs dupliqués : 0 ;
- synthèse opérationnelle `Project Asteria` présente ;
- absence de recommandation GPT, de prochaine action et de chaîne d’export du guide dans le texte lecteur.

## 6. Exactitude technique

Le chapitre distingue le Profiler standard du Visual Profiler, le temps propre du temps inclusif et les moniteurs légers des captures détaillées.

Les extraits utilisent `Performance.get_monitor()`, des moniteurs personnalisés bornés et `Time.get_ticks_usec()` pour des durées monotones. Les scripts Python conservent les échantillons, contrôlent les nombres finis et évitent les divisions relatives sur un dénominateur nul.

La commande PowerShell mesure le processeur hôte dans une fenêtre bornée et n’est pas présentée comme attribution de coût à une fonction Godot.

Les budgets à 60 images par seconde sont des plafonds théoriques ; aucun résultat mesuré n’est inventé.

## 7. Contrôle des régressions

- contrats d’environnement et d’échantillonnage séparés ;
- baseline et candidate symétriques ;
- changement principal déclaré ;
- runs valides défavorables conservés ;
- p95, p99 et dépassements contrôlés ;
- cadence physique traitée comme variable fonctionnelle ;
- tâches parallèles soumises à une empreinte de correction ;
- suite fonctionnelle obligatoire avant acceptation ;
- approbation humaine conservée.

## 8. Réserves ouvertes

- scènes et fixtures de benchmark non matérialisées ;
- aucun manifeste d’environnement rempli ;
- aucune capture du Profiler créée ;
- aucun CSV ou résumé statistique produit ;
- aucun budget CPU qualifié ;
- aucune hypothèse exécutée ;
- aucune campagne avant/après réalisée ;
- aucune suite fonctionnelle exécutée ;
- aucun coût d’instrumentation mesuré ;
- licence globale de collection non définie ;
- balisage d’accessibilité de l’export final toujours ouvert.

## 9. Conclusion

Le chapitre satisfait le périmètre du plan maître au niveau documentaire et statique. Les contrôles du lot doivent réussir avant la fermeture de la preuve QA.
