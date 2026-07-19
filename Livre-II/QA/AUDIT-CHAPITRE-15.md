---
title: "Audit du Livre II — Chapitre 15"
id: "DOC-L2-QA-CH15"
status: "complete"
version: "1.2.0"
book: "Livre II"
chapter: 15
category: "quality-report"
audit-date: "2026-07-20"
audit-level: "static-review"
chapter-id: "DOC-L2-CH15"
chapter-version: "1.2.0"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit du Livre II — Chapitre 15

> **Chapitre audité :** `Livre-II/CHAPITRE-15-Relations-sociales.md`  
> **Niveau GPT-5.6 Sol annoncé :** Élevée  
> **Décision :** accepté après corrections, avec réserves runtime et PDF de fin de Livre.

## 1. Objet

L’audit vérifie que le système de relations sociales reste séparé du personnage, des nœuds actifs et des systèmes futurs.

Il contrôle notamment :

- l’identité orientée `source → cible` ;
- la coexistence de deux perceptions divergentes ;
- les axes sociaux bornés ;
- les causes et provenances stables ;
- l’historique causal borné ;
- la mutation atomique d’une relation ;
- les requêtes indépendantes de la scène ;
- les vues mutuelles calculées ;
- la persistance stricte ;
- la validation contre les identités logiques ;
- les frontières avec famille, agents, factions, réputation et narration.

## 2. Porte d’audit distincte

Le premier commit du chapitre est `054b14e133d4f6263fe06ce4a564ca9650a39934`.

Il portait explicitement :

- `status: draft` ;
- `version: 0.9.0` ;
- `audit-status: pending` ;
- `audit-level: not-audited`.

Le chapitre n’a donc pas été déclaré audité avant la seconde lecture.

La séquence appliquée est :

1. annonce du titre et du niveau GPT-5.6 Sol ;
2. création d’une branche dédiée ;
3. rédaction du brouillon ;
4. audit du périmètre ;
5. audit des repères ;
6. audit technique des extraits ;
7. contrôle des erreurs et corrections ;
8. corrections ;
9. création du présent rapport ;
10. déclaration finale du chapitre ;
11. preuve QA, gouvernance et workflows.

## 3. Complétude du périmètre

Les éléments enregistrés dans `CONTINUITE-PROJET.md` sont couverts :

- état relationnel séparé de `CharacterRuntimeState` ;
- identité fondée sur deux `CharacterId` ;
- relations dirigées ;
- vues mutuelles explicitement calculées ;
- affinité, confiance, respect et peur ;
- valeurs et deltas bornés ;
- causes, provenance et contexte ;
- historique borné ;
- opérations applicatives validées ;
- événements typés ;
- requêtes de voisinage ;
- absence de dépendance aux nœuds actifs ;
- section de sauvegarde indépendante ;
- validation des références ;
- modes Solo et Studio ;
- critères d’acceptation et tests à préparer.

## 4. Corrections appliquées

### 4.1 Mutation atomique par relation

Le brouillon utilisait d’abord `get_or_create()` puis modifiait directement l’objet conservé dans le dépôt.

Correction :

- suppression de cette mutation directe du service ;
- ajout de `replace_one()` au contrat du dépôt ;
- duplication de l’état courant ;
- application sur un candidat ;
- validation du candidat et de l’événement ;
- remplacement seulement après succès ;
- émission de l’événement après remplacement.

Une validation tardive ne peut plus laisser un état partiellement modifié.

### 4.2 Copie profonde de l’historique

Une simple duplication de l’`Array` conservait les mêmes `SocialChangeRecord`.

Correction :

- ajout de `duplicate_record()` ;
- copie de chaque enregistrement ;
- `get_history_copy()` et `duplicate_state()` utilisent les copies profondes.

Un observateur ou un candidat ne partage plus les enregistrements mutables de l’état courant.

### 4.3 Validation des changements historiques

Le brouillon validait l’identité et l’ordre d’un enregistrement, mais pas complètement ses deltas.

Correction :

- chaque delta est limité à `100` en valeur absolue ;
- un enregistrement sans effet est refusé ;
- la validation du record est cohérente avec celle de la commande.

### 4.4 Cohérence révision, tick et historique

Le brouillon pouvait accepter une révision positive avec un historique vide.

Correction :

- révision `0` exige tick `0` et historique vide ;
- révision positive exige au moins un enregistrement ;
- le dernier enregistrement doit porter la révision et le tick courants ;
- les révisions et ticks restent ordonnés.

### 4.5 Décodage complet du snapshot

Le brouillon annonçait `_decode_record()` sans montrer son implémentation complète.

Correction :

- vérification des clés exactes ;
- vérification des types exacts ;
- décodage séparé des deltas ;
- validation du record avant retour ;
- contrôle du code retourné par `set_history_for_restore()`.

### 4.6 Préparation de chargement explicite

Le brouillon permettait théoriquement d’appeler `apply_prepared()` sans préparation réussie.

Correction :

- ajout de `_has_prepared_load` ;
- remise à zéro au début de chaque préparation et lors d’une annulation ;
- refus de l’application sans préparation complète ;
- vérification de l’index d’identités avant lecture des entrées.

### 4.7 Repères d’utilisation

Deux blocs `text` intermédiaires n’avaient pas de repère adjacent.

Correction :

- ajout de deux repères `[LECTURE]` ;
- les `66` blocs clôturés du chapitre possèdent désormais un contexte explicite lors du contrôle local.

### 4.8 Sources techniques

Les références sont présentées sous forme de liens Markdown nommés :

- quatorze liens vers la documentation officielle Godot `4.7` ;
- un lien local vers le chapitre 14.

Aucune adresse technique n’est laissée dans un bloc de code imposant une copie manuelle.

## 5. Cohérence avec les chapitres voisins

### 5.1 Chapitre 14

Le chapitre 15 réutilise `CharacterId` et l’index logique des identités.

Il n’ajoute aucun champ social à `CharacterRuntimeState`.

### 5.2 Chapitre 16

La parenté, le mariage, la filiation et les générations restent réservés au système familial.

Une relation sociale ne déduit jamais une parenté depuis l’affinité.

### 5.3 Chapitre 17

Le système social fournit des données aux agents, mais ne choisit aucune action.

Une suggestion IA doit être convertie vers une commande bornée et validée.

### 5.4 Chapitres 20, 23 et 25

La réputation des objets, les factions, la justice et les conséquences narratives restent dans leurs systèmes propres.

## 6. Revue statique des extraits

Contrôles locaux réalisés :

- front matter relu ;
- `2 177` lignes ;
- `69` titres Markdown ;
- `66` blocs clôturés ;
- `16` cas d’erreurs détaillés ;
- un bloc JSON analysé avec succès ;
- tous les blocs clôturés associés à un repère reconnu ;
- aucune revendication de test Godot runtime.

La revue statique vérifie notamment :

- l’orientation des clés ;
- les bornes ;
- la cohérence des révisions ;
- l’encapsulation des tableaux ;
- l’ordre mutation/remplacement/événement ;
- la préparation avant application ;
- le refus des conversions JSON silencieuses.

## 7. Réserves runtime

N’ont pas été exécutés :

- le parseur GDScript de Godot `4.7.1-stable` ;
- les signaux ;
- la scène de démonstration ;
- l’index réel des identités de personnages ;
- la restauration transactionnelle entre sections ;
- les migrations ;
- les charges proches de `N²` ;
- les lots d’événements mondiaux ;
- le multijoueur ;
- le packaging ;
- le PDF de fin de Livre.

## 8. Décision

**Accepté avec réserves.**

Le chapitre peut être déclaré :

- `status: reviewed` ;
- `version: 1.2.0` ;
- `audit-status: complete` ;
- `audit-level: static-review`.

La preuve finale reste `pending-ci` jusqu’à la réussite des workflows permanents.


## Addendum 2026-07-20 — explications détaillées du code

Le retour de lecture a identifié une non-conformité pédagogique : plusieurs blocs techniquement cohérents ne donnaient pas encore au lecteur débutant les explications nécessaires sur leurs paramètres, retours, effets et invariants.

La correction finale couvre **56 blocs de code ou données** dans le chapitre 15. **44 explications** ont été affinées après seconde lecture et **12 explications manquantes** ont été ajoutées, notamment pour les blocs GDScript d’une seule ligne.

Chaque explication couvre désormais, selon le contenu réel du bloc :

- le rôle et le chemin cible ;
- les fonctions, paramètres, types et retours ;
- les variables, constantes, signaux et dépendances ;
- le déroulement des conditions, boucles et retours anticipés ;
- les effets de bord ;
- les invariants protégés ;
- la différence entre exemples fautifs et corrigés ;
- le résultat attendu et la vérification minimale.

**Décision révisée :** accepté au niveau `static-review` après enrichissement pédagogique. Cette décision reste documentaire : aucun parseur Godot ni test runtime supplémentaire n’a été exécuté.

La seconde lecture a aussi corrigé la détection des `static func`, les contre-exemples nommés « mauvaise pratique » et les formulations génériques de résultat attendu.

## Addendum 2026-07-20 — concision et contextualisation des explications

La passe précédente était complète mais trop répétitive. Cette correction éditoriale applique les règles suivantes aux **56 blocs** du chapitre 15 :

- 23 rubriques `Emplacement` supprimées parce que le chemin est déjà fourni avant le code ;
- 21 rappels généraux sur `:` et `->` supprimés des blocs et remplacés par une convention unique renvoyant au chapitre 2 ;
- 7 rubriques `Rôle` supprimées parce qu’elles reformulaient seulement le titre de la section ;
- 17 contre-exemples réduits à une explication précise de leur faute ;
- 16 corrections réduites à la raison concrète de leur fonctionnement ;
- 11 renvois contextuels ajoutés avant des erreurs lorsque le chapitre avait déjà établi la règle concernée.

Les rôles qui nomment un contrat, une classe, une fonction ou une responsabilité concrète sont conservés. La décision reste `static-review` : aucune exécution Godot supplémentaire n’est revendiquée.

- suppression des lignes autonomes `Correction` et `Différence` lorsque leur contenu est déjà intégré aux deux justifications ;
