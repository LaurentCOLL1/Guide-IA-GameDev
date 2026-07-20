---
title: "Audit du Livre II — Chapitre 19"
id: "DOC-L2-QA-AUDIT-CH19"
status: "complete"
version: "1.0.1"
chapter-id: "DOC-L2-CH19"
chapter-version: "1.0.1"
audit-level: "static-review"
audit-date: "2026-07-20T16:52:26+02:00"
last-verified: "2026-07-20T16:52:26+02:00"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit du chapitre 19 — Compétences et pouvoirs

## 1. Porte de brouillon

Le chapitre a d’abord été matérialisé avec un rapport d’audit à l’état `draft`. Une seconde lecture distincte a ensuite corrigé les contrats avant la présente clôture `1.0.0`.

## 2. Résultats

- lignes finales : **2 386** ;
- titres Markdown : **55** ;
- blocs de code ou de données : **56** ;
- marqueurs d’explication : **56** ;
- cas d’erreurs détaillés : **10** ;
- contre-exemples expliqués : **10** ;
- corrections expliquées : **10** ;
- doublons de titres : **0** ;
- blocs significatifs sans explication : **0** ;
- instruction `Prochaine étape` dans le chapitre : **0** ;
- synthèse finale `Project Asteria` : **présente**.

## 3. Complétude et périmètre

Le chapitre couvre :

- les définitions de compétences et pouvoirs ;
- les coûts par ressource ;
- les charges et recharges en ticks logiques ;
- les ciblages sur soi, personnage, point et zone ;
- les effets composables de dégâts, d’état et de ressource ;
- le déblocage, le rang et l’expérience ;
- les commandes et résultats métier ;
- les candidats de mutation et l’unité de travail commune ;
- les adaptateurs joueur et agent ;
- la persistance stricte et la restauration préparée.

Les frontières sont respectées :

- le combat conserve cible, portée, ligne de vue, défense, dégâts et états temporaires ;
- les personnages conservent santé et endurance ;
- les compétences possèdent définitions, progression, charges, recharge et orchestration ;
- l’inventaire du chapitre 20 pourra accorder une compétence sans devenir son autorité ;
- la présentation consomme seulement des résultats committés.

## 4. Corrections issues de la seconde lecture

La seconde lecture a notamment :

1. supprimé le commit séquentiel des coûts et effets ;
2. ajouté `AbilityMutationUnitOfWork` afin de préparer puis committer coût, effets, charge et recharge comme un même lot ;
3. transformé les ports de combat et de personnage en ports de préparation de candidats ;
4. ajouté `AbilityContextPort` pour relire une révision de compétence sans exposer le dépôt ;
5. ajouté une fabrique centrale de `AbilityResult` ;
6. fermé le dispatch sur trois types d’effets explicitement autorisés ;
7. clarifié que `PARTIALLY_RESOLVED` est une utilisation consommée ;
8. conservé les recharges en ticks logiques, indépendantes des `Timer` ;
9. limité la persistance aux données durables ;
10. maintenu les objets du chapitre 20 hors de la progression et de l’état runtime des compétences.

11. retiré du chapitre lecteur la procédure interne `Validation légère sans PDF`, qui appartient au rapport QA, à la preuve et aux workflows.

## 5. Revue statique du code

Les extraits ont été relus pour vérifier :

- les signatures, types, paramètres et valeurs de retour ;
- les sentinelles `null`, `&""` et `-1` ;
- les codes `Error` et refus métier ;
- les bornes de rangs, charges, coûts, cibles et effets ;
- les copies profondes et candidates ;
- les révisions du monde et des compétences ;
- l’ordre canonique des cibles et effets ;
- l’absence de mutation active avant commit ;
- l’absence de nœuds et de `Resource` mutable dans les snapshots ;
- l’absence de chargement dynamique de classe depuis les données.

Cette revue ne constitue pas une exécution du parseur GDScript.

## 6. Explications pédagogiques

Les **56** blocs possèdent chacun un marqueur `<!-- qa:code-explanation -->` et une explication proportionnée portant, selon le besoin, sur :

- le rôle concret ;
- les entrées et types ;
- les paramètres et valeurs par défaut ;
- les retours et refus contrôlés ;
- les effets de bord ;
- les invariants ;
- le déroulement ;
- le résultat attendu ;
- les frontières avec les systèmes voisins.

Aucune rubrique ne justifie un extrait en répétant seulement le titre de sa section.

## 7. Règle sémantique des erreurs

La section `Erreurs fréquentes et corrections` porte le marqueur `<!-- qa:error-correction-section -->`.

Chacun des dix cas contient :

- un symptôme ou risque ;
- un exemple fautif ;
- `Pourquoi cet exemple est fautif` ;
- un exemple corrigé ;
- `Pourquoi la correction fonctionne`.

Les cas couvrent notamment l’écriture directe des dégâts, les `Timer` autoritaires, le coût consommé trop tôt, l’état runtime stocké dans une `Resource`, le chargement dynamique de classes, la prévisualisation non revalidée, les plans persistés, les noms affichés utilisés comme identités, les effets requis ignorés et les retries de résultats partiels.

## 8. Contextes d’utilisation

Les commandes, fichiers, actions graphiques, sorties et structures de référence utilisent les repères reconnus :

- `[PS]` pour les validations légères ;
- `[VSC]` pour les fichiers à créer ;
- `[APP]` pour la ressource Godot ;
- `[SORTIE]` pour les résultats attendus ;
- `[LECTURE]` pour les structures et contre-exemples.

Les repères `[CMD]`, `[WSL]`, `[DCT]`, `[DCK]` et `[WEB]` restent déclarés dans l’en-tête mais ne sont pas artificiellement ajoutés à des procédures qui ne les utilisent pas.

## 9. Sources et exactitude technique

Les API et types moteur sont reliés aux pages officielles Godot 4.7 concernant notamment `Resource`, `RefCounted`, `Array`, `Dictionary`, `StringName`, `Variant`, `Vector3`, les signaux et `Timer`.

Les dépendances internes renvoient aux chapitres 7, 9, 14, 17 et 18. La version de référence reste Godot `4.7.1-stable`.

## 10. Clôture éditoriale

La dernière section du chapitre est une synthèse opérationnelle des décisions retenues pour `Project Asteria`. Elle ne contient ni chemin du chapitre suivant, ni niveau GPT futur, ni instruction de production.

## 11. Réserves

- le parseur Godot 4.7.1 n’a pas été exécuté ;
- `duplicate(true)` n’a pas été vérifié sur toutes les combinaisons de sous-ressources ;
- l’atomicité runtime de `AbilityMutationUnitOfWork` n’a pas été exécutée ;
- les ports de combat et de personnage n’ont pas été matérialisés ;
- la scène pédagogique n’a pas été instanciée ;
- les budgets n’ont pas été mesurés ;
- le codec et une future migration n’ont pas été exécutés ;
- le replay interplateforme n’a pas été vérifié ;
- aucun PDF n’a été construit.

## 12. Décision

Le chapitre 19 est **accepté au niveau `static-review`**, sous les réserves runtime et PDF de fin de Livre indiquées ci-dessus.
