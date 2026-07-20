---
title: "Audit du Livre II — Chapitre 16"
id: "DOC-L2-QA-CH16"
status: "complete"
version: "1.2.0"
book: "Livre II"
chapter: 16
category: "quality-report"
audit-date: "2026-07-20"
audit-level: "static-review"
chapter-id: "DOC-L2-CH16"
chapter-version: "1.2.0"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit du Livre II — Chapitre 16

> **Chapitre audité :** `Livre-II/CHAPITRE-16-Famille-et-generations.md`  
> **Niveau GPT-5.6 Sol annoncé :** Élevée  
> **Décision :** accepté après corrections, avec réserves runtime et PDF de fin de Livre.

## 1. Objet

L’audit vérifie que le troisième système de gameplay modélise la famille comme un graphe logique indépendant des personnages actifs, des perceptions sociales et des règles politiques futures.

Il contrôle notamment :

- les identités fondées sur `CharacterId` ;
- la filiation dirigée parent vers enfant ;
- la distinction biologique, adoption, tutelle et union ;
- la paire canonique des unions ;
- les intervalles logiques ;
- les doublons et chevauchements ;
- le refus des cycles d’ascendance ;
- les requêtes bornées ;
- les fratries et générations dérivées ;
- la conservation des personnages absents, décédés ou archivés ;
- les événements et l’historique typés ;
- la persistance stricte ;
- la restauration par graphe candidat ;
- les frontières avec succession, politique et narration.

## 2. Porte d’audit distincte

Le premier commit du chapitre est `7ad1ad849913d7b7af4a211a8ce612b29822a7a3`.

Il portait explicitement :

- `status: draft` ;
- `version: 0.9.0` ;
- `audit-status: pending` ;
- `audit-level: not-audited`.

Le chapitre n’a donc pas été déclaré audité avant la seconde lecture.

La séquence appliquée est :

1. annonce du titre et du niveau GPT-5.6 Sol ;
2. vérification des sources officielles Godot 4.7 ;
3. création de la branche dédiée ;
4. rédaction du brouillon ;
5. audit de complétude et de frontières ;
6. audit des repères d’utilisation ;
7. revue statique des extraits GDScript ;
8. contrôle des erreurs et corrections ;
9. création du présent rapport ;
10. corrections du chapitre ;
11. preuve QA, gouvernance et workflows.

## 3. Complétude du périmètre

Les éléments enregistrés dans `CONTINUITE-PROJET.md` sont couverts :

- système familial séparé des axes sociaux ;
- filiation dirigée ;
- unions non orientées par paire canonique ;
- types biologique, adoption, tutelle et union ;
- identités `CharacterId` ;
- absence de dépendance aux nœuds actifs ;
- refus des auto-liens et doublons ;
- détection des cycles d’ascendance ;
- ancêtres, descendants et fratries ;
- génération relative dérivée ;
- ticks de début et de fin ;
- événements et historique familial ;
- section de sauvegarde indépendante ;
- personnages décédés, absents ou archivés ;
- frontières avec agents, succession, politique et narration ;
- parcours Solo et Studio.

## 4. Corrections appliquées

### 4.1 Réutilisation de l’index logique existant

Le brouillon demandait de créer à nouveau `character_identity_index.gd`, déjà introduit par le chapitre 15.

Correction :

- l’instruction devient une réutilisation du contrat existant ;
- aucune seconde définition de `CharacterIdentityIndex` n’est créée ;
- le chapitre 16 dépend explicitement du même index logique que le système social.

### 4.2 Validation explicite des enums

Le brouillon utilisait une comparaison fondée sur `Value.size()` et un cast `as` vers un enum.

Correction :

- ajout de `FamilyLinkKind.is_known(value: int)` ;
- passage de l’entier validé au constructeur typé ;
- suppression du cast ambigu réservé principalement aux objets.

### 4.3 Parcours doublement bornés

Le brouillon limitait la détection de cycle à 4 096 nœuds, mais les requêtes d’ancêtres et de descendants ne comptaient pas les nœuds visités.

Correction :

- validation de `max_depth` entre `0` et `32` ;
- compteur de nœuds visités ;
- arrêt et diagnostic au-delà de `MAX_TRAVERSAL_NODES` ;
- valeur de résultat incomplète jamais présentée comme exhaustive.

### 4.4 API de lecture défensive

Le validateur utilisait `get_parent_links()`, `get_guardianship_links()` et `get_union_links()` sans que leurs implémentations soient montrées.

Correction :

- ajout des trois méthodes ;
- duplication profonde de chaque lien retourné ;
- interdiction de retourner les dictionnaires internes mutables.

### 4.5 Remplacement complet du graphe

Le brouillon citait `replace_all_from()` sans implementation.

Correction :

- construction d’un nouveau graphe candidat ;
- réinsertion de chaque lien via les méthodes validées ;
- remplacement des structures internes uniquement après succès ;
- reconstruction des index secondaires ;
- retour `Error` propagé à la section de sauvegarde.

### 4.6 Codec complet

Le brouillon détaillait seulement la filiation et laissait les tutelles, unions, historique et `encode_graph()` sous forme de fonctions implicites.

Correction :

- encodeurs et décodeurs complets pour les trois familles de liens ;
- encodeur et décodeur de l’historique ;
- validation des clés exactes au niveau racine et au niveau de chaque record ;
- limites de taille avant construction ;
- refus d’une version future ou inconnue.

### 4.7 Initialisation de la section de sauvegarde

Le brouillon déclarait les dépendances sans constructeur.

Correction :

- ajout de `_init(graph, codec, identities)` ;
- contrôle des dépendances nulles ;
- `capture()` refuse un graphe invalide ;
- `apply_prepared()` propage l’erreur de `replace_all_from()` ;
- le candidat reste disponible tant que le remplacement n’a pas réussi.

### 4.8 Historique cohérent

Le journal borné n’était pas relié aux invariants de séquence pendant une restauration.

Correction :

- restauration par copie profonde ;
- séquences strictement croissantes ;
- calcul de `_next_sequence` depuis le maximum chargé ;
- limite de 256 records appliquée au décodage.

### 4.9 Politique des liens temporels

La borne de fin inclusive était implicite.

Correction :

- l’intervalle est documenté comme `[début, fin]` ;
- `OPEN_END` signifie absence de fin connue ;
- les chevauchements utilisent la même convention ;
- une fermeture à un tick antérieur est refusée.

### 4.10 Repères d’utilisation

Les blocs procéduraux sans instruction de création restent marqués `[LECTURE]`. Les fichiers et scènes possèdent respectivement `[VSC]` ou `[APP]`, et les arbres attendus utilisent `[SORTIE]`.

## 5. Revue technique

### 5.1 GDScript

La revue statique contrôle :

- types et annotations ;
- parenthèses et blocs ;
- retours `Error` ;
- copies défensives ;
- dictionnaires typés ;
- appels aux signaux ;
- sérialisation explicite des `StringName` ;
- absence de nœud ou de `Resource` dans le snapshot ;
- limites de parcours et de collections.

Aucun parseur Godot n’a été exécuté.

### 5.2 Graphe

Les invariants retenus sont :

- une filiation est orientée ;
- aucun personnage ne peut être son propre ancêtre ;
- un dépassement de budget refuse la mutation ;
- une union est identifiée par une paire canonique ;
- les fratries et générations sont dérivées ;
- les liens vers les personnages non actifs restent valides ;
- les index secondaires sont reconstructibles.

### 5.3 Persistance

Le snapshot :

- possède `format_version: 1` ;
- contient uniquement liens et historique autoritaires ;
- utilise des clés exactes ;
- refuse les références inconnues ;
- refuse les cycles pendant le décodage ;
- ne modifie jamais le graphe actif avant validation complète.

## 6. Sources

Les quinze sources techniques du chapitre sont nommées et cliquables. Elles privilégient la documentation officielle Godot 4.7 et le RFC 8259 pour JSON.

Les points actuels vérifiés incluent :

- `RefCounted` et sa libération par comptage de références ;
- les tableaux et dictionnaires typés ;
- les limites des collections typées imbriquées ;
- les signaux comme mécanisme de notification ;
- la conversion explicite des valeurs vers JSON.

## 7. Erreurs et corrections

La section porte `<!-- qa:error-correction-section -->` et contient seize cas. Chaque cas fournit :

1. un symptôme ou risque ;
2. un exemple fautif ;
3. une correction ;
4. un exemple corrigé ;
5. une différence explicite.

Les cas couvrent identité, scène active, confusion sociale, fratrie, génération, cycles, budgets, union canonique, horloge logique, intervalles, index logique, collections mutables, restauration, index persistés, autorité IA et succession.

## 8. Frontières

Le chapitre ne consomme pas prématurément :

- les décisions d’agents du chapitre 17 ;
- la succession et la justice du chapitre 23 ;
- l’héritage d’objets et d’économie ;
- les quêtes et secrets familiaux du chapitre 25 ;
- le multijoueur du Livre IV.

## 9. Réserves runtime

Restent à produire :

- parsing Godot 4.7.1 des scripts ;
- matérialisation du Starter Kit ;
- exécution de la scène de démonstration ;
- tests unitaires de cycles courts et longs ;
- tests de propriété sur les graphes aléatoires ;
- mesure des limites de profondeur et de nœuds ;
- test de restauration coordonnée avec les personnages ;
- migrations de format ;
- test des personnages archivés ;
- packaging multi-plateforme ;
- PDF de fin de Livre.

## 10. Décision

**Accepté après corrections, avec réserves runtime et PDF de fin de Livre.**

Le chapitre peut être déclaré `reviewed`, version `1.0.0`, audit `complete`, niveau `static-review`, après application et vérification des corrections recensées.


## Addendum 2026-07-20 — explications détaillées du code

Le retour de lecture a identifié une non-conformité pédagogique : plusieurs blocs techniquement cohérents ne donnaient pas encore au lecteur débutant les explications nécessaires sur leurs paramètres, retours, effets et invariants.

La correction finale couvre **67 blocs de code ou données** dans le chapitre 16. **43 explications** ont été affinées après seconde lecture et **24 explications manquantes** ont été ajoutées, notamment pour les blocs GDScript d’une seule ligne.

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

La passe précédente était complète mais trop répétitive. Cette correction éditoriale applique les règles suivantes aux **67 blocs** du chapitre 16 :

- 35 rubriques `Emplacement` supprimées parce que le chemin est déjà fourni avant le code ;
- 30 rappels généraux sur `:` et `->` supprimés des blocs et remplacés par une convention unique renvoyant au chapitre 2 ;
- 16 rubriques `Rôle` supprimées parce qu’elles reformulaient seulement le titre de la section ;
- 16 contre-exemples réduits à une explication précise de leur faute ;
- 16 corrections réduites à la raison concrète de leur fonctionnement ;
- 12 renvois contextuels ajoutés avant des erreurs lorsque le chapitre avait déjà établi la règle concernée.

Les rôles qui nomment un contrat, une classe, une fonction ou une responsabilité concrète sont conservés. La décision reste `static-review` : aucune exécution Godot supplémentaire n’est revendiquée.

- suppression des lignes autonomes `Correction` et `Différence` lorsque leur contenu est déjà intégré aux deux justifications ;
