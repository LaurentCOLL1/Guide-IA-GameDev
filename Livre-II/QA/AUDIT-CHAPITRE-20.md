---
title: "Audit du Livre II — Chapitre 20"
id: "DOC-L2-QA-AUDIT-CH20"
status: "complete"
version: "1.0.1"
chapter-id: "DOC-L2-CH20"
chapter-version: "1.0.1"
audit-level: "static-review"
audit-date: "2026-07-21T15:28:42+02:00"
last-verified: "2026-07-21T15:28:42+02:00"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit du chapitre 20 — Inventaire et réputation des objets

## 1. Porte de brouillon

Le chapitre a été matérialisé sur une branche dédiée et dans une pull request en brouillon. Plusieurs lectures statiques distinctes ont ensuite corrigé les contrats avant la présente clôture `1.0.0`.

## 2. Résultats

- lignes finales : **2762** ;
- titres Markdown : **59** ;
- blocs de code ou de données : **56** ;
- marqueurs d’explication : **56** ;
- cas d’erreurs détaillés : **10** ;
- contre-exemples expliqués : **10** ;
- corrections expliquées : **10** ;
- doublons de titres : **0** ;
- blocs significatifs sans explication : **0** ;
- commandes de validation QA dans le chapitre lecteur : **0** ;
- instruction `Prochaine étape` dans le chapitre : **0** ;
- synthèse finale `Project Asteria` : **présente**.
- segments d’explication antérieurs conservés : **202** ;
- segments d’explication antérieurs perdus : **0** ;
- points pédagogiques complémentaires ajoutés : **0** ;
- sections Solo/Studio rendues en Markdown ordinaire : **oui**.

## 3. Complétude et périmètre

Le chapitre couvre :

- définitions partagées et instances uniques ;
- lots fongibles, division, fusion et transfert ;
- conteneurs, capacités et masse dérivée ;
- équipement et compétences accordées ;
- durabilité demandée par le combat ;
- propriété distincte de la garde matérielle ;
- autorisation de transfert ;
- provenance des instances et origine des lots ;
- réputation globale d’un objet identifié ;
- actions d’agents et présentation ;
- codec strict et restauration préparée.

Les frontières sont respectées :

- le combat conserve ses calculs et prépare seulement une demande de durabilité ;
- les compétences conservent progression, charges, recharges, coûts et effets ;
- l’économie du chapitre 21 conservera monnaies, prix, paiements et contrats de transaction ;
- la justice future pourra adapter l’autorisation sans muter directement l’inventaire ;
- la présentation consomme uniquement des résultats committés.

## 4. Corrections issues des lectures statiques

Les lectures distinctes ont notamment :

1. ajouté une copie détachée explicite pour `ItemReputationState` ;
2. validé les valeurs nulles avant toute lecture d’instance ou de pile ;
3. séparé validation de forme et références croisées des loadouts ;
4. ajouté l’origine complète des lots avec cause, système source et tick logique ;
5. ajouté une fabrique validée pour instances et lots ;
6. vérifié propriété, état brisé et révisions avant équipement ;
7. comparé toute l’origine et protégé les propriétaires lors d’une fusion ;
8. ajouté `InventoryAccessPort` afin d’interdire les transferts non autorisés ;
9. distingué les statuts de préparation au lieu de transformer tous les refus en absence ;
10. interdit le transfert direct d’un objet encore équipé ;
11. incrémenté les révisions des deux conteneurs préparés ;
12. matérialisé le transfert total et partiel des piles ;
13. rendu la division complète en renvoyant source décrémentée et pile créée ;
14. supprimé le tableau mutable par défaut du contrat d’unité de travail ;
15. séparé les révisions d’instance, de loadout et de compétences ;
16. matérialisé le port de contexte utilisé par l’adaptateur d’agent ;
17. validé les états candidats avec leur conteneur de destination ;
18. distingué les refus propres aux piles avant construction ;
19. ajouté le déséquipement symétrique et le retrait du seul grant source ;
20. ajouté l’initialisation séparée de la réputation des instances concernées.

## 5. Revue statique du code

Les extraits ont été relus pour vérifier :

- les signatures, types, paramètres et valeurs de retour ;
- les sentinelles `null`, `{}`, `&""` et `-1` ;
- les codes `Error` et refus métier ;
- les bornes de masse, quantité, durabilité, réputation et historiques ;
- les copies détachées et candidats ;
- les révisions des conteneurs, entrées, loadouts, réputations et compétences ;
- les identifiants des nouvelles piles ;
- l’ordre de préparation avant commit ;
- l’absence de mutation active par le combat, les agents ou la présentation ;
- l’absence de chargement dynamique de classes depuis les données.

Cette revue ne constitue pas une exécution du parseur GDScript.

## 6. Explications pédagogiques



Les **56** blocs possèdent **56** marqueurs. Les explications antérieures ont été décomposées en **202** segments techniques conservés mot pour mot, puis regroupées sous des rubriques uniques et adaptées. Les libellés génériques sont interdits ; chaque point cite un champ, une fonction, une garde, un retour, un effet, un chemin ou une relation réellement visible dans le bloc.

## 7. Règle sémantique des erreurs

La section `Erreurs fréquentes et corrections` porte le marqueur `<!-- qa:error-correction-section -->`.

Chacun des dix cas contient un symptôme ou risque, un exemple fautif expliqué, puis un exemple corrigé expliqué. Les cas couvrent les définitions partagées mutées, noms affichés comme identités, empilements invalides, inventaire stocké dans un nœud, source retirée trop tôt, pile équipée, combat écrivant la durabilité, inventaire écrivant une compétence, valeurs dérivées persistées et sortie IA modifiant la réputation.

## 8. Contextes d’utilisation

Les fichiers à créer utilisent `[VSC]`. Les flux, contrats, résultats et contre-exemples utilisent `[LECTURE]`. Les autres repères restent déclarés dans l’en-tête sans être ajoutés artificiellement à des procédures absentes.

Le chapitre ne contient aucune commande de workflow ou procédure de validation documentaire destinée à l’équipe éditoriale.

## 9. Sources et exactitude technique

Les API et types moteur renvoient aux pages officielles Godot 4.7 concernant `Resource`, `RefCounted`, `Array`, `Dictionary`, `StringName`, `Variant` et les signaux.

Les dépendances internes renvoient aux chapitres 7, 9, 14, 17, 18 et 19. La version de référence reste Godot `4.7.1-stable`.

## 10. Clôture éditoriale

La dernière section du chapitre est une synthèse opérationnelle des décisions retenues pour `Project Asteria`. Elle ne contient ni chemin du chapitre suivant, ni niveau GPT futur, ni instruction de production.

## 11. Réserves

- le parseur Godot 4.7.1 n’a pas été exécuté ;
- les dictionnaires typés n’ont pas été vérifiés dans toutes les signatures présentées ;
- l’atomicité runtime de `InventoryMutationUnitOfWork` n’a pas été exécutée ;
- l’autorisation de transfert n’a pas été matérialisée ;
- le grant de compétences et son retrait n’ont pas été exécutés ;
- l’intégration combat-durabilité n’a pas été exécutée ;
- la scène pédagogique n’a pas été instanciée ;
- les budgets n’ont pas été mesurés ;
- le codec et une future migration n’ont pas été exécutés ;
- le replay interplateforme n’a pas été vérifié ;
- aucun PDF n’a été construit.

## 12. Décision

Le chapitre 20 est **accepté au niveau `static-review`**, sous les réserves runtime et PDF de fin de Livre indiquées ci-dessus.
