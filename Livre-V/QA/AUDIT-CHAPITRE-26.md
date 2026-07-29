---
title: "Audit — Livre V, fiche 26 : Index croisés"
id: "DOC-L5-AUDIT-CH26"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 26
audit-level: "static-review"
audit-date: "2026-07-30T01:18:00+02:00"
last-verified: "2026-07-30T01:18:00+02:00"
---

# Audit de la fiche 26 — Index croisés

## 1. Périmètre audité

L’audit couvre `Livre-V/CHAPITRE-26-Index-croises.md` selon le protocole spécialisé du Livre V. Il vérifie la fonction d’index, les identités canoniques, les relations typées, les synonymes, les routes thématiques, la navigation multiformat, les contrôles d’intégrité et les frontières avec les sources propriétaires.

Le niveau reste `static-review`. Aucun moteur d’indexation, scénario utilisateur, PDF, HTML, EPUB, rapport exhaustif d’orphelins ou outil du Companion Pack n’est revendiqué.

## 2. Conformité au plan maître

| Exigence | Statut | Observation |
|---|---|---|
| indexer outils, systèmes, formats, erreurs, licences et concepts | conforme | cartes IDX-05 à IDX-09 et Matrice A |
| relier synonymes et anciennes appellations | conforme | IDX-04 et Matrice B |
| fournir navigation PDF/HTML | conforme comme contrat documentaire | IDX-11 distingue précondition Markdown et validation du format produit |
| détecter références orphelines | conforme comme méthode | Matrice C et IDX-12 interdisent la suppression automatique |
| index alphabétiques et thématiques | conforme | IDX-02 et IDX-03 |
| liens croisés | conforme | relations typées, routes et destinations propriétaires |
| tables de synonymes | conforme | acronymes, traductions, graphies, termes voisins et dépréciations |
| rapport d’intégrité | conforme comme contrat | corpus, outil, résultats, limites et historique définis |
| clôturer l’encyclopédie sans dupliquer | conforme | navigation et frontières, aucune procédure complète recopiée |

## 3. Structure Livre V

| Contrôle | Résultat |
|---|---:|
| lignes | __CHAPTER_LINES__ |
| titres | __CHAPTER_HEADINGS__ |
| cartes `l5:card` | __REFERENCE_CARDS__ |
| matrices `l5:matrix` | __MATRICES__ |
| liens Markdown | __MARKDOWN_LINKS__ |
| renvois directs vers les Livres I à IV | __SOURCE_BOOK_LINKS__ |
| liens avec fragment | __FRAGMENT_LINKS__ |
| diagrammes compacts | __COMPACT_DIAGRAMS__ |
| blocs clôturés | __FENCED_BLOCKS__ |
| titres dupliqués | __DUPLICATE_HEADINGS__ |

La fiche privilégie les tables et routes directement consultables. Elle porte treize cartes, trois matrices et neuf diagrammes compacts sans structure tutoriel importée.

## 4. Identités, alias et relations

- une entrée possède un identifiant stable distinct du libellé et du chemin ;
- `owner`, `prerequisite`, `validates`, `diagnoses`, `alternative`, `supersedes` et `related` sont séparés ;
- `canonical`, `alias`, `deprecated`, `planned`, `unresolved` et `retired` sont visibles ;
- un alias ne porte pas de définition concurrente ;
- les homonymes exigent un qualificateur ;
- les boucles de redirection sont interdites ;
- un terme voisin n’est pas déclaré synonyme par commodité.

## 5. Couverture des routes

La fiche fournit des points d’entrée pour :

- outils, environnements et services ;
- systèmes, architecture, données et gameplay ;
- formats, fichiers, protocoles et interfaces ;
- symptômes, erreurs, preuves et diagnostics ;
- licences, provenance, conformité et publication ;
- besoins de production et parcours Solo/Studio ;
- navigation Markdown, HTML, PDF, EPUB et assistive.

Chaque route renvoie vers une fiche du Livre V ou une procédure propriétaire des Livres I à IV. Les index ne fusionnent pas les autorités.

## 6. Intégrité et orphelins

La Matrice C distingue :

- chemin absent ;
- fragment absent ;
- identifiant dupliqué ;
- terme canonique concurrent ;
- alias en boucle ;
- cible planifiée présentée comme existante ;
- entrée sans propriétaire ;
- document sans lien entrant ou sortant ;
- cible retirée encore active ;
- libellé obsolète ;
- support de publication non testé ;
- résultats contradictoires.

Un document sans lien entrant est seulement un candidat orphelin. Les racines, annexes, audits et artefacts peuvent être volontairement atypiques. Toute suppression exige une revue humaine.

## 7. Frontières préservées

- la fiche 01 conserve la carte générale et les parcours principaux ;
- la fiche 02 conserve les décisions ;
- les fiches 03 à 25 conservent leurs définitions spécialisées ;
- les Livres I à IV conservent les procédures et validations ;
- le Companion Pack conserve les moteurs, bases, exports et rapports exécutables ;
- M8 conserve la construction PDF/HTML/EPUB et l’accessibilité du format final ;
- la licence globale de la collection reste indécise.

## 8. Validation et réserves

| Contrôle | Statut | Limite |
|---|---|---|
| structure, métadonnées, liens et doublons | à confirmer par CI | validation légère du dépôt |
| cartes et liens profonds du Livre V | à confirmer par CI | cible Markdown uniquement |
| repères et cohérence sémantique | à confirmer par CI | aucun test utilisateur |
| lot permanent de huit fichiers | à vérifier par CI | contrôle avant commit final |
| absence de PDF | à confirmer par CI | aucune publication multiformat dans ce lot |

Aucune recherche utilisateur, aucune mesure du temps de recherche, aucun générateur d’index, aucune base d’alias, aucun graphe de connaissances, aucun rapport exhaustif d’orphelins, aucun contrôle d’accessibilité du format final et aucune licence globale ne sont produits.

## 9. Décision d’audit

**Accepté au niveau `static-review`, sous réserve de réussite des validateurs légers et du contrôle des huit fichiers permanents.**
