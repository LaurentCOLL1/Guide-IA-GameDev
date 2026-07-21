---
title: "Audit du Livre II — Chapitre 22"
id: "DOC-L2-QA-AUDIT-CH22"
status: "complete"
version: "1.0.3"
chapter-id: "DOC-L2-CH22"
chapter-version: "1.0.3"
audit-level: "static-review"
audit-date: "2026-07-21T19:59:30+02:00"
last-verified: "2026-07-21T19:59:30+02:00"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit du chapitre 22 — Monde vivant et simulation écologique

## 1. Porte de brouillon

Le chapitre a été matérialisé sur la branche dédiée `docs/livre-ii-ch22-monde-vivant` et dans la pull request en brouillon #48. La seconde lecture a corrigé les contrats incomplets avant la clôture `1.0.0`.

## 2. Résultats

- lignes finales : **3218** ;
- titres Markdown : **69** ;
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
- unités d’explication antérieures conservées : **228** ;
- segments d’explication antérieurs perdus : **0** ;
- points pédagogiques complémentaires ajoutés : **0** ;
- sections Solo/Studio rendues en Markdown ordinaire : **oui**.

## 3. Complétude et périmètre

Le chapitre couvre l’horloge logique globale, les régions écologiques, les définitions d’espèces et de ressources, les populations agrégées, les réserves, les capacités d’accueil, les résidus, la simulation à plusieurs fréquences, le rattrapage borné, la matérialisation, les commandes causales, les récoltes, les indices économiques, les observations d’agents et la persistance.

Les frontières sont respectées :

- les personnages restent propriétaires des identités individuelles et représentations ;
- les agents soumettent des requêtes sans modifier le monde vivant ;
- le combat transmet une mort validée sous forme de commande causale ;
- l’inventaire prépare et possède les objets issus d’une récolte ;
- l’économie calcule prix, offres et transactions depuis des indices écologiques ;
- les factions, lois, domaines et récits restent réservés aux chapitres 23 à 25.

## 4. Corrections issues des lectures statiques

Les lectures distinctes ont notamment :

1. ajouté une ressource alimentaire explicite aux espèces consommatrices ;
2. borné tous les résidus par `ticks_per_day` ;
3. supprimé le résidu de migration non matérialisé dans le périmètre ;
4. ajouté l’enregistrement et la validation croisée du catalogue ;
5. sécurisé les calculs en points de base et les additions de population ;
6. matérialisé les helpers de simulation des ressources et populations ;
7. ajouté le port de mode régional ;
8. matérialisé le commit et les résultats de l’ordonnanceur ;
9. complété le dépôt pour l’horloge et l’idempotence ;
10. ajouté le port d’autorisation écologique ;
11. ajouté le service de commandes de population et de récolte ;
12. validé les candidats avant les ports de commit ;
13. enregistré résultat, identité et empreinte dans le même lot ;
14. borné et validé les observations remises aux agents ;
15. complété la persistance des résultats idempotents ;
16. restauré le port d’autorisation consommé par `EcologyService` et exigé les identifiants sur tout résultat réussi.

## 5. Revue statique du code

Les extraits ont été relus pour vérifier les signatures, types, paramètres, retours, sentinelles, codes `Error`, copies détachées, bornes entières, résidus, ordre lexical, révisions, idempotence, émission après commit et absence de mutation depuis une scène ou une sortie IA.

Cette revue ne constitue pas une exécution du parseur GDScript.

## 6. Explications pédagogiques



Les **61** blocs possèdent **61** marqueurs. Les explications antérieures ont été décomposées en **231** segments techniques conservés mot pour mot, puis regroupées sous des rubriques uniques et adaptées. Les libellés génériques sont interdits ; chaque point cite un champ, une fonction, une garde, un retour, un effet, un chemin ou une relation réellement visible dans le bloc.

## 7. Règle sémantique des erreurs

La section `Erreurs fréquentes et corrections` porte le marqueur `<!-- qa:error-correction-section -->`. Chacun des dix cas contient un symptôme, un exemple fautif expliqué, puis un exemple corrigé expliqué.

## 8. Contextes d’utilisation

Les fichiers à créer utilisent `[VSC]`. Les flux, contrats, résultats et contre-exemples utilisent `[LECTURE]`. Le chapitre ne contient aucune procédure de workflow ou commande de validation documentaire destinée à l’équipe éditoriale.

## 9. Sources et exactitude technique

Les API et types moteur renvoient aux pages officielles Godot 4.7 concernant `Resource`, `RefCounted`, `Array`, `Dictionary`, `StringName`, `Time`, les entiers GDScript et la génération pseudo-aléatoire. Les dépendances internes renvoient aux chapitres 9, 14, 17, 20 et 21.

## 10. Clôture éditoriale

La dernière section du chapitre synthétise les décisions retenues pour `Project Asteria`. Elle ne contient ni chemin du chapitre suivant, ni niveau GPT futur, ni instruction de production.

## 11. Réserves

- le parseur Godot 4.7.1 n’a pas été exécuté ;
- les dictionnaires typés n’ont pas été vérifiés dans toutes les signatures ;
- les contrôles de dépassement n’ont pas été exécutés aux bornes ;
- l’équilibrage du modèle de croissance n’a pas été mesuré ;
- la stabilité avec 4 096 régions n’a pas été mesurée ;
- l’atomicité runtime entre écologie et inventaire n’a pas été exécutée ;
- les adaptateurs d’accès et de matérialisation n’ont pas été matérialisés ;
- l’intégration d’un contexte météo futur n’a pas été exécutée ;
- la scène pédagogique n’a pas été instanciée ;
- le codec et une migration future n’ont pas été exécutés ;
- la reproductibilité interplateforme n’a pas été vérifiée ;
- aucun PDF n’a été construit.


Les sections pédagogiques d’erreurs conservent leur séquence sémantique directe : symptôme, exemple fautif, explication du défaut, exemple corrigé et explication de la correction. Les rubriques générales de restructuration ne sont pas appliquées à ces deux explications, afin d’éviter répétitions, sous-titres intermédiaires et commentaires génériques.

## 12. Décision

Le chapitre 22 est **accepté au niveau `static-review`**, sous les réserves runtime et PDF de fin de Livre indiquées ci-dessus.
