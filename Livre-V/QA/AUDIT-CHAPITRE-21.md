---
title: "Audit — Livre V, fiche 21 : Benchmarks et méthodes de mesure"
id: "DOC-L5-QA-AUDIT-CH21"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 21
last-verified: "2026-07-29T18:11:00+02:00"
audit-date: "2026-07-29T18:11:00+02:00"
audit-level: "static-review"
chapter-path: "Livre-V/CHAPITRE-21-Benchmarks-et-methodes-de-mesure.md"
validation-proof: "Livre-V/QA/VALIDATION-FINALE-CHAPITRE-21.yaml"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit de la fiche 21 — Benchmarks et méthodes de mesure

## 1. Décision

**Statut : accepté au niveau `static-review`, sous réserves explicites.**

La fiche respecte le profil spécialisé du Livre V : consultation non linéaire, contrat transversal, matrices de routage et de contrôle, formats de résultats, niveaux de preuve et liens profonds vers les méthodes propriétaires des Livres I à IV.

## 2. Périmètre revu

- contrat minimal d’un benchmark ;
- routage CPU, GPU, mémoire, chargement, systèmes, gameplay, réseau, CI, assets, audio et IA ;
- question, hypothèse, métrique primaire, seuil pratique et décision ;
- empreinte de l’objet, du build, du matériel et de l’instrumentation ;
- scénario, charge, fixtures, phases et oracle fonctionnel ;
- warm-up, caches, états froid/chaud et stabilisation thermique ;
- facteurs contrôlés, randomisés, contrebalancés ou rapportés ;
- runs, observations, répétitions, ordre, pauses et règles d’arrêt ;
- unités, horloges, précision, conversions et coût de l’instrumentation ;
- données brutes, statuts, nullabilité, schéma et intégrité ;
- moyenne, médiane, quantiles, dispersion, taux de dépassement et incertitude ;
- valeurs aberrantes, exclusions, données manquantes et sensibilité ;
- comparaison baseline/candidate, effet, seuil pratique et portes qualité ;
- visualisation, rapport, séparation données/calcul/interprétation/décision ;
- répétition indépendante, maintenance, dépréciation et retrait.

## 3. Frontières vérifiées

La fiche ne reprend pas les procédures détaillées des chapitres propriétaires :

- métriques d’équilibrage et simulations : Livre IV, chapitre 1 ;
- risques, portes, réserves et dérogations : Livre IV, chapitre 2 ;
- cas, fixtures, oracles et non-régression : Livre IV, chapitre 3 ;
- reproduction des anomalies : Livre IV, chapitre 4 ;
- événements, métriques et traces : Livre IV, chapitre 5 ;
- campagnes CPU, GPU, mémoire, chargement et systèmes : Livre IV, chapitres 6 à 10 ;
- synchronisation réseau : Livre IV, chapitre 12 ;
- CI et artefacts : Livre IV, chapitre 14 ;
- budgets et contrôles graphique/audio : fiches 18 et 19 ;
- catalogue diagnostique : fiche 20 ;
- matrices de support : future fiche 22 ;
- comparatifs et recommandations : future fiche 23 ;
- scripts, fixtures, données et rapports exécutables : Companion Pack.

## 4. Conformité au profil Livre V

- `document-format: "reference-cards"` présent ;
- treize marqueurs `<!-- l5:card -->` ;
- trois marqueurs `<!-- l5:matrix -->` ;
- index express en tête ;
- réponses rapides, limites et portes visibles ;
- tables orientées décision ;
- liens profonds vers les chapitres propriétaires ;
- absence de bloc de code et de commande exécutable ;
- absence de structure tutoriel complète ;
- séparation entre revue statique, run, série locale, répétition indépendante et décision produit.

## 5. Revue sémantique

### 5.1 Question avant données

La métrique primaire, la direction favorable, le seuil pratique et le plan d’arrêt sont définis avant l’ouverture des résultats. Une analyse exploratoire ne devient pas silencieusement une confirmation.

### 5.2 Comparabilité

La fiche exige objet, environnement, scénario, cache, ordre, instrumentation et unités compatibles. Une différence de build, de renderer, de pilote, de charge ou de phase peut rendre les séries non comparables.

### 5.3 Indépendance des observations

Les frames ou observations d’un même run ne sont pas présentées comme autant de répétitions indépendantes. Les résumés par run précèdent la comparaison entre runs.

### 5.4 Statistiques et queues

La moyenne n’est pas universelle. Médiane, quantiles, dispersion, dépassements et séries temporelles sont choisis selon la décision et la distribution, sans suppression automatique des pics.

### 5.5 Valeurs manquantes et exclusions

`missing`, `blocked`, `invalid` et `not_applicable` restent distincts de zéro. Toute exclusion conserve son motif, son nombre de lignes et son effet sur la conclusion.

### 5.6 Effet pratique et qualité

Une différence numérique n’est pas automatiquement utile. Le résultat doit franchir le seuil pratique et les portes fonctionnelles, visuelles, sonores, de sécurité ou de maintenabilité concernées.

### 5.7 Portée et maintenance

Chaque résultat reste daté et lié à un périmètre. Les changements de versions, matériel, protocole ou méthode déclenchent répétition, dépréciation, remplacement ou retrait.

## 6. Vérifications techniques prévues

La validation légère doit contrôler :

1. front matter, identifiant, dates, statut et chemin d’audit ;
2. structure Markdown, titres et doublons ;
3. résolution des fichiers et fragments locaux ;
4. marqueurs de cartes et matrices du Livre V ;
5. densité des renvois vers les Livres I à IV ;
6. absence de blocs non expliqués ;
7. présence et cohérence des repères d’utilisation ;
8. couverture des contextes ;
9. absence de PDF ;
10. cohérence du lot permanent de huit fichiers.

## 7. Métriques finales

Les valeurs statiques du chapitre stabilisé sont enregistrées dans la preuve QA : 462 lignes, 20 titres, 13 cartes, 3 matrices, 64 liens Markdown, 41 renvois vers les Livres I à IV, 47 liens avec fragment, 8 diagrammes compacts, aucun bloc clôturé et aucun titre dupliqué.

## 8. Réserves

- aucun benchmark réel n’a été exécuté ;
- aucun warm-up, cache froid/chaud, run ou répétition n’a été observé ;
- aucun profiler, compteur, capture, chronomètre ou outil de mesure n’a été utilisé ;
- aucune donnée brute, série, statistique, distribution, intervalle ou graphique n’a été produit ;
- aucune baseline, candidate, comparaison, différence, speedup ou effet pratique n’a été calculé ;
- aucune campagne CPU, GPU, RAM, VRAM, chargement, gameplay, réseau, CI, asset, audio ou IA n’a été réalisée ;
- aucune répétition indépendante ou qualification de plateforme n’a été conduite ;
- aucune donnée joueur, donnée personnelle, secret, voix, contrat ou artefact confidentiel n’a été traité ;
- aucun script ou jeu de fixtures du Companion Pack et aucun PDF n’a été produit.

## 9. Conclusion

La fiche peut être intégrée comme contrat documentaire transversal des benchmarks. Toute promotion ultérieure devra citer le protocole, l’environnement, le build, les données brutes, les transformations, les statistiques, les portes qualité, le responsable et les limites de généralisation.
