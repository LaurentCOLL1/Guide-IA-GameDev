---
title: "Audit du Livre II — Chapitre 24"
id: "DOC-L2-QA-AUDIT-CH24"
status: "complete"
version: "1.0.0"
chapter-id: "DOC-L2-CH24"
chapter-version: "1.0.0"
audit-level: "static-review"
audit-date: "2026-07-21T09:05:12+02:00"
last-verified: "2026-07-21T09:05:12+02:00"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit du chapitre 24 — Construction et gestion de domaines

## 1. Porte de création

Le chapitre a été créé sur la branche dédiée `docs/livre-ii-ch24-domaines-construction`. Son périmètre a été comparé aux chapitres 20 à 23 avant la rédaction afin de conserver les autorités des droits, objets, monnaies et régions.

## 2. Résultats

- lignes finales : **2645** ;
- titres Markdown : **48** ;
- blocs de code ou de données : **61** ;
- marqueurs d’explication : **61** ;
- cas d’erreurs détaillés : **10** ;
- contre-exemples expliqués : **10** ;
- corrections expliquées : **10** ;
- doublons de titres : **0** ;
- blocs significatifs sans explication : **0** ;
- commandes de validation QA dans le chapitre lecteur : **0** ;
- instruction `Prochaine étape` dans le chapitre : **0** ;
- synthèse finale `Project Asteria` : **présente**.

## 3. Complétude et périmètre

Le chapitre couvre domaines, parcelles, liens de tenure, bâtiments, recettes, chantiers, matériaux, travail, achèvement, production, entretien, permissions, événements, observations d’agents et persistance.

Les frontières sont respectées :

- le chapitre 23 conserve droits, lois et décisions politiques ;
- le chapitre 20 conserve objets, lots, conteneurs et transferts ;
- le chapitre 21 conserve monnaies, portefeuilles et écritures ;
- le chapitre 22 conserve régions, populations et ressources ;
- le chapitre 25 conserve quêtes et conséquences narratives.

## 4. Corrections issues des lectures statiques

Les lectures ont notamment :

1. séparé lien de tenure et droit politique ;
2. réservé la capacité de parcelle dès l’ouverture du chantier ;
3. distingué matériaux livrés et travail accompli ;
4. interdit les surlivraisons ;
5. préparé coûts, matériaux, intrants et extrants avant commit ;
6. conservé un chantier terminé comme historique ;
7. borné progression, condition, cycles et collections ;
8. appliqué le refus par défaut aux décisions absentes ou indéterminées ;
9. rendu production et entretien idempotents ;
10. séparé représentation 3D et existence logique.

## 5. Revue statique du code

Les extraits ont été relus pour signatures, types, paramètres, retours, sentinelles, copies détachées, révisions, points de base, idempotence, ordre de préparation, émissions après commit et restauration globale.

Cette revue ne constitue pas une exécution du parseur GDScript.

## 6. Explications pédagogiques

Les **61** blocs possèdent chacun un marqueur `<!-- qa:code-explanation -->` et une explication proportionnée. Les chemins sont indiqués par `[VSC]` et les structures non exécutables par `[LECTURE]`.

## 7. Règle sémantique des erreurs

La section `Erreurs fréquentes et corrections` porte `<!-- qa:error-correction-section -->`. Chacun des dix cas contient un symptôme, un exemple fautif expliqué et un exemple corrigé expliqué.

## 8. Clôture éditoriale

La dernière section synthétise les décisions retenues pour `Project Asteria` sans annoncer le chapitre suivant.

## 9. Réserves

- le parseur Godot 4.7.1 n’a pas été exécuté ;
- les collections typées n’ont pas été vérifiées au runtime ;
- le commit domaine-inventaire-économie n’a pas été exécuté ;
- les adaptateurs de droits et de site n’ont pas été matérialisés ;
- les performances aux bornes n’ont pas été mesurées ;
- la scène pédagogique n’a pas été instanciée ;
- le codec et la restauration n’ont pas été exécutés ;
- la reproductibilité interplateforme n’a pas été vérifiée ;
- aucun PDF n’a été construit.

## 10. Décision

Le chapitre 24 est **accepté au niveau `static-review`**, sous les réserves runtime et PDF de fin de Livre indiquées ci-dessus.
