---
title: "Audit de correction — Livre V, fiche 01"
id: "DOC-L5-AUDIT-CH01"
status: "complete"
version: "1.1.0"
lang: "fr-FR"
book: "Livre V"
chapter: 1
audit-date: "2026-07-28T11:28:35+02:00"
last-verified: "2026-07-28T11:28:35+02:00"
audit-level: "static-review"
target-document: "Livre-V/CHAPITRE-01-Carte-generale-de-la-collection.md"
protocol: "Livre-V/QA/PROTOCOLE-FICHES-LIVRE-V.md"
---

# Audit de correction — Fiche 01

## 1. Motif de la correction

La version `1.0.0` utilisait une structure héritée des Livres II à IV : résultats d’apprentissage, longues explications de blocs, commandes de validation, dix diagnostics détaillés, checklist et synthèse `Project Asteria`.

Cette forme contredisait la fonction du Livre V : transformer les connaissances des quatre premiers Livres en fiches, matrices, recettes minimales et index consultables rapidement.

La version `1.1.0` remplace donc le chapitre tutoriel par une fiche d’orientation non linéaire.

## 2. Décision

La fiche 01 — **Carte générale de la collection** est acceptée au niveau `static-review` selon le protocole spécialisé du Livre V.

La décision couvre la structure de référence, les liens internes, les matrices, les prérequis, les frontières éditoriales et la cohérence avec le plan maître. Elle ne revendique aucune étude utilisateur, exécution runtime, compatibilité matérielle ou publication PDF.

## 3. Changement de profil éditorial

La correction applique les décisions suivantes :

- titre éditorial « Fiche 01 » dans les métadonnées ;
- suppression de la progression pédagogique linéaire ;
- suppression des sections « Résultats d’apprentissage » et « Synthèse opérationnelle » ;
- suppression des commandes et exemples de code sans valeur de consultation immédiate ;
- suppression de l’obligation artificielle de dix diagnostics ;
- remplacement des paragraphes longs par des cartes et matrices ;
- index express placé au début ;
- renvois répétés vers les Livres I à IV ;
- liens profonds vers des sous-sections lorsque les titres sont stables ;
- contrat explicite d’une fiche du Livre V.

## 4. Couverture du plan maître

Les quatre objectifs du chapitre 1 restent couverts :

1. structure Volume 0, Livres I à V et Companion Pack ;
2. dépendances et parcours Solo/Studio ;
3. entrées par besoin, outil ou système ;
4. prérequis et ordre conseillé.

Les quatre livrables restent présents :

- carte de navigation ;
- matrice Livre/compétence sous forme de cartes et matrices spécialisées ;
- parcours débutant, production et dépannage ;
- index des prérequis.

La frontière est renforcée : aucune installation, architecture complète, chaîne artistique complète ou procédure de publication n’est recopiée.

## 5. Navigation et liens

Métriques statiques de la version `1.1.0` :

- 263 lignes ;
- 17 titres ;
- 12 marqueurs de fiches ;
- 2 marqueurs de matrices ;
- 185 liens internes au total ;
- 167 liens vers les Livres I à IV ;
- 29 liens profonds avec fragment vers une sous-section ;
- aucun bloc clôturé ;
- aucun titre, bloc significatif ou paragraphe long dupliqué.

Chaque famille de besoin renvoie vers un tutoriel propriétaire, puis vers un prérequis, une validation ou une alternative.

## 6. Différence avec les chapitres voisins

Le chapitre 2 conserve les arbres de décision détaillés et les critères de choix.

Le chapitre 3 conservera les fiches normalisées des logiciels et outils.

Les chapitres 4 à 25 conserveront leurs familles de fiches, recettes, références, diagnostics et matrices.

Le chapitre 26 conservera les index croisés complets. La fiche 01 fournit seulement la carte d’entrée générale.

## 7. QA spécialisée

Le nouveau protocole `Livre-V/QA/PROTOCOLE-FICHES-LIVRE-V.md` distingue :

- les règles communes qui restent obligatoires ;
- les règles tutoriel qui ne s’appliquent pas automatiquement ;
- le contrat minimal des fiches ;
- la politique de liens internes ;
- la forme visuelle ;
- le traitement minimal du code et des diagnostics ;
- le profil automatique du Livre V.

Les validateurs sont adaptés afin de contrôler le format de référence sans imposer les sections d’erreurs pédagogiques aux fiches du Livre V.

## 8. Réserves

- aucune étude chronométrée de navigation n’a été exécutée ;
- les fragments de liens ont été relus contre les titres Markdown, sans test de tous les moteurs de publication ;
- aucun index interactif HTML ou EPUB n’a été matérialisé ;
- aucun artefact du Companion Pack n’a été créé ;
- aucune exécution runtime n’a été effectuée ;
- la licence globale et le balisage avancé des publications restent ouverts ;
- aucun PDF n’a été produit.

## 9. Conclusion

La version `1.1.0` correspond désormais au rôle réel du Livre V. Elle se lit comme un ensemble de fiches et de matrices, renvoie fréquemment vers les sources propriétaires et ne ressemble plus à un chapitre pédagogique des Livres précédents.
