---
title: "Audit du Livre II — Chapitre 21"
id: "DOC-L2-QA-AUDIT-CH21"
status: "complete"
version: "1.0.1"
chapter-id: "DOC-L2-CH21"
chapter-version: "1.0.1"
audit-level: "static-review"
audit-date: "2026-07-21T15:28:42+02:00"
last-verified: "2026-07-21T15:28:42+02:00"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit du chapitre 21 — Économie

## 1. Porte de brouillon

Le chapitre a été matérialisé sur une branche dédiée et dans une pull request en brouillon. Une seconde lecture automatisée puis une troisième lecture statique ciblée ont corrigé les contrats avant la présente clôture `1.0.0`.

## 2. Résultats

- lignes finales : **3111** ;
- titres Markdown : **64** ;
- blocs de code ou de données : **60** ;
- marqueurs d’explication : **60** ;
- cas d’erreurs détaillés : **10** ;
- contre-exemples expliqués : **10** ;
- corrections expliquées : **10** ;
- doublons de titres : **0** ;
- blocs significatifs sans explication : **0** ;
- commandes de validation QA dans le chapitre lecteur : **0** ;
- instruction `Prochaine étape` dans le chapitre : **0** ;
- synthèse finale `Project Asteria` : **présente**.
- segments d’explication antérieurs conservés : **222** ;
- segments d’explication antérieurs perdus : **0** ;
- points pédagogiques complémentaires ajoutés : **0** ;
- sections Solo/Studio rendues en Markdown ordinaire : **oui**.

## 3. Complétude et périmètre

Le chapitre couvre :

- devises immuables et unités mineures entières ;
- portefeuilles multi-devises, soldes non négatifs et révisions ;
- écritures signées et records équilibrés par devise ;
- valeurs économiques séparées des définitions d’objets ;
- multiplicateurs en points de base et arithmétique bornée ;
- création d’offres verrouillées et devis temporaires ;
- achats, taxes, ventes et récompenses monétaires ;
- idempotence avec empreinte canonique ;
- candidat économique et commit commun avec l’inventaire ;
- adaptateur d’agent, présentation, codec et restauration préparée.

Les frontières sont respectées :

- l’inventaire conserve identité, quantité, propriété et transfert des objets ;
- les relations, l’écologie et les systèmes futurs fournissent seulement des contextes bornés ;
- la politique et la justice futures pourront autoriser ou taxer sans écrire les soldes ;
- les domaines et factions futurs restent propriétaires de leur existence ;
- la présentation consomme uniquement des résultats committés ou rejoués.

## 4. Corrections issues des lectures statiques

Les lectures distinctes ont notamment :

1. séparé les révisions d’inventaire de la source, de la destination et de l’entrée ;
2. renommé le port de commit afin de couvrir achats et récompenses ;
3. supprimé les plages d’export irréalistes et conservé les bornes dans `validate()` ;
4. protégé les contrôles signés contre le cas limite de `abs()` ;
5. ajouté une fabrique d’offres qui verrouille un prix calculé ;
6. recoupé chaque écriture avec le solde candidat correspondant ;
7. exigé une révision attendue pour chaque portefeuille et offre mutés ;
8. distingué fonds insuffisants et panne de préparation ;
9. transmis explicitement la devise aux fabriques d’écritures ;
10. complété les helpers de résultats et de journal ;
11. matérialisé une récompense équilibrée et ses refus précis ;
12. vérifié la configuration avant toute lecture du service de récompense ;
13. rendu le candidat d’inventaire explicitement optionnel pour une récompense monétaire ;
14. ajouté les révisions vendeur et fiscales au contexte d’agent ;
15. borné quantités, totaux et empreintes de commandes ;
16. interdit les devises non transférables dans les offres et transferts ;
17. renforcé les validations nulles des catalogues ;
18. corrigé la désactivation d’une offre lorsque le reliquat devient inférieur au minimum.

## 5. Revue statique du code

Les extraits ont été relus pour vérifier :

- les signatures, types, paramètres et valeurs de retour ;
- les sentinelles `null`, `{}`, `&""` et `-1` ;
- les codes `Error` et refus métier ;
- la plage entière JSON sûre ;
- les copies détachées de portefeuilles et records ;
- l’équilibre séparé de chaque devise ;
- les soldes finaux non négatifs ;
- les révisions des portefeuilles, offres et agrégats d’inventaire ;
- l’idempotence et les conflits d’empreinte ;
- l’absence de mutation active depuis l’interface, l’agent ou une sortie IA.

Cette revue ne constitue pas une exécution du parseur GDScript.

## 6. Explications pédagogiques



Les **60** blocs possèdent **60** marqueurs. Les explications antérieures ont été décomposées en **222** segments techniques conservés mot pour mot, puis regroupées sous des rubriques uniques et adaptées. Les libellés génériques sont interdits ; chaque point cite un champ, une fonction, une garde, un retour, un effet, un chemin ou une relation réellement visible dans le bloc.

## 7. Règle sémantique des erreurs

La section `Erreurs fréquentes et corrections` porte le marqueur `<!-- qa:error-correction-section -->`.

Chacun des dix cas contient un symptôme ou risque, un exemple fautif expliqué, puis un exemple corrigé expliqué. Les cas couvrent les `float`, les mutations depuis l’interface, les soldes négatifs, les récompenses sans contrepartie, les totaux clients, les commits séquentiels, les prix dans les objets, les retries avec nouvelle identité, les conversions implicites et les prix issus d’une sortie IA.

## 8. Contextes d’utilisation

Les fichiers à créer utilisent `[VSC]`. Les flux, contrats, résultats et contre-exemples utilisent `[LECTURE]`. Les autres repères restent déclarés dans l’en-tête sans être ajoutés artificiellement.

Le chapitre ne contient aucune procédure de workflow ou commande de validation documentaire destinée à l’équipe éditoriale.

## 9. Sources et exactitude technique

Les API et types moteur renvoient aux pages officielles Godot 4.7 concernant `Resource`, `RefCounted`, `Array`, `Dictionary`, `StringName`, `Variant`, les signaux et les entiers GDScript 64 bits.

Les dépendances internes renvoient aux chapitres 7, 8, 9, 14, 15, 17 et 20. La version de référence reste Godot `4.7.1-stable`.

## 10. Clôture éditoriale

La dernière section du chapitre est une synthèse opérationnelle des décisions retenues pour `Project Asteria`. Elle ne contient ni chemin du chapitre suivant, ni niveau GPT futur, ni instruction de production.

## 11. Réserves

- le parseur Godot 4.7.1 n’a pas été exécuté ;
- les dictionnaires typés n’ont pas été vérifiés dans toutes les signatures ;
- les contrôles de dépassement n’ont pas été exécutés aux bornes ;
- l’atomicité runtime du commit économie-inventaire n’a pas été exécutée ;
- l’adaptateur d’autorisation n’a pas été matérialisé ;
- les taxes et contextes futurs n’ont pas été exécutés ;
- l’action d’agent n’a pas été matérialisée ;
- la scène pédagogique n’a pas été instanciée ;
- les budgets n’ont pas été mesurés ;
- le codec et une future migration n’ont pas été exécutés ;
- le replay interplateforme n’a pas été vérifié ;
- aucun PDF n’a été construit.

## 12. Décision

Le chapitre 21 est **accepté au niveau `static-review`**, sous les réserves runtime et PDF de fin de Livre indiquées ci-dessus.
