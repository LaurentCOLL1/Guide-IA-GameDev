---
title: "Audit post-création — Livre II, chapitre 3"
id: "DOC-L2-QA-AUDIT-CH03"
status: "complete"
version: "1.0.0"
book: "Livre II"
chapter: 3
category: "quality-report"
validation-date: "2026-07-18"
audit-level: "static-review"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
validation-evidence: "Livre-II/QA/VALIDATION-FINALE-CHAPITRE-03.yaml"
---

# Audit post-création — Livre II, chapitre 3

> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir, **[LECTURE]** exemple à étudier. Voir la [convention complète](../../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

## 1. Périmètre

Document contrôlé :

- `DOC-L2-CH03` — Scènes, nœuds, Resources et signaux.

Documents de cohérence contrôlés :

- `Livre-II/index.md` ;
- `Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md` ;
- `ROADMAP.md` ;
- `contents.txt` ;
- `CONTINUITE-PROJET.md`.

Version de référence : Godot `4.7.1-stable`, édition Standard, GDScript, renderer Forward+.

## 2. Méthode

La campagne comprend :

- comparaison au plan maître du Livre II ;
- lecture pédagogique pour un public débutant ;
- vérification des frontières avec les chapitres 2, 4, 5, 6 et 7 ;
- revue statique des exemples GDScript ;
- contrôle des fonctions, paramètres, types, opérateurs et retours ;
- vérification des repères d’utilisation ;
- contrôle éditorial des répétitions ;
- vérification contre la documentation officielle Godot 4.7 ;
- compilation et inspection PDF par la CI ;
- déclaration explicite des limites runtime.

## 3. Couverture du plan maître

Le chapitre couvre :

- scène, nœud, branche, racine et instance ;
- `SceneTree` ;
- parent et propriété `owner` ;
- composition et instanciation de scènes ;
- `PackedScene`, `preload()`, `load()` et `instantiate()` ;
- `NodePath`, `get_node()`, `$`, `%NomUnique` et `get_node_or_null()` ;
- références typées et `@onready` ;
- `_init()`, `_enter_tree()`, `_ready()` et `_exit_tree()` ;
- signaux intégrés et personnalisés ;
- connexion dans l’éditeur et dans le code ;
- `Callable`, `bind()`, `connect()`, `emit()`, `is_connected()` et `disconnect()` ;
- Resources natives, personnalisées et partagées ;
- création et suppression de nœuds runtime ;
- exercice `StatusBeacon` intégré à `Project Asteria` ;
- diagnostic, modes Solo/Studio et critères d’acceptation.

Décision de périmètre : **conforme**.

Les services globaux, Autoloads, bus d’événements et injection de dépendances restent au chapitre 5. La stratégie générale des données reste au chapitre 7.

## 4. Vérification pédagogique

Les concepts nouveaux sont définis avant leur usage opérationnel.

Les extraits principaux sont décomposés :

- déclaration d’une Resource personnalisée ;
- `StringName` et littéral `&"..."` ;
- annotations d’export ;
- références de nœuds ;
- déclaration et paramètres d’un signal ;
- connexion à un signal intégré ;
- nature d’un `Callable` ;
- fonction publique `activate()` ;
- émission des arguments ;
- expression conditionnelle ;
- instanciation et cast typé ;
- ordre de configuration avant `add_child()` ;
- signature du récepteur.

Les rappels de notions du chapitre 2 sont courts et appliqués à un contexte nouveau. Aucune répétition intégrale volontaire du cours sur les fonctions ou les collections n’est introduite.

Décision pédagogique : **conforme**.

## 5. Vérification technique statique

### 5.1 Scènes et nœuds

- une scène possède une racine et peut être instanciée plusieurs fois ;
- `PackedScene.instantiate()` crée l’arbre en mémoire ;
- les callbacks d’entrée ne sont déclenchés qu’après ajout au `SceneTree` ;
- `owner` est distingué du parent runtime ;
- `queue_free()` est présenté comme suppression différée.

### 5.2 Cycle de vie

Ordre vérifié :

1. `_enter_tree()` du parent ;
2. `_enter_tree()` des enfants ;
3. `_ready()` des enfants ;
4. `_ready()` du parent.

La possibilité de réentrée et la sortie des enfants avant le parent sont déclarées.

### 5.3 Références

- `get_node()` et `$` utilisent un chemin ;
- `%NomUnique` reste limité à sa scène ;
- `get_node_or_null()` est réservé aux dépendances optionnelles ;
- `@onready` retarde correctement la résolution.

### 5.4 Signaux

- la forme recommandée `signal.connect(callable)` est utilisée ;
- les paramètres déclarés correspondent aux arguments émis ;
- les signatures des callbacks correspondent aux signaux ;
- les doubles connexions sont évitées avec `is_connected()` ;
- la déconnexion vérifie l’existence de la connexion.

### 5.5 Resources

- `BeaconProfile` hérite de `Resource` ;
- les propriétés sont exportées et typées ;
- l’état runtime `_is_available` reste dans le nœud ;
- le risque de modification d’une Resource partagée est expliqué ;
- `resource_local_to_scene` est présenté comme mécanisme à utiliser avec discernement.

### 5.6 Ligne de commande

Les options `--headless`, `--path`, `--import`, `--scene` et `--quit-after` correspondent à la référence officielle Godot 4.7.

Décision technique : **conforme au niveau static-review**.

## 6. Non-conformités corrigées pendant la rédaction et la seconde lecture

| ID | Gravité | Constat | Résolution |
|---|---|---|---|
| L2-CH03-001 | majeure | Le terme « propriété » pouvait être confondu avec la relation parent-enfant. | Ajout d’une distinction détaillée entre `parent` et `owner`. |
| L2-CH03-002 | majeure | `%NomUnique` pouvait être interprété comme une recherche globale. | Ajout de la limite à la scène propriétaire et d’un exemple de frontière d’instance. |
| L2-CH03-003 | majeure | Une instance pouvait entrer dans l’arbre avant de recevoir sa Resource obligatoire. | Assignation de `profile` avant `parent.add_child(beacon)`, avec explication de l’ordre. |
| L2-CH03-004 | majeure | Une Resource partagée pouvait recevoir par erreur un état runtime. | Séparation explicite entre `BeaconProfile` et `_is_available`. |
| L2-CH03-005 | majeure | Une reconnexion pouvait provoquer des callbacks multiples. | Ajout de `is_connected()` avant les connexions et déconnexions. |
| L2-CH03-006 | mineure | Les connexions de l’éditeur et du code n’étaient pas comparées. | Ajout d’une matrice de décision locale. |
| L2-CH03-007 | mineure | La commande headless ne ciblait pas explicitement la scène de démonstration. | Ajout de `--scene` et explication de `--quit-after`. |
| L2-CH03-008 | gouvernance | Le niveau de raisonnement conseillé n’était pas enregistré dans les métadonnées. | Ajout de `recommended-reasoning: "GPT-5.6 Sol — Élevée"`. |

Aucune non-conformité majeure reste ouverte.

## 7. Contextes d’utilisation

Le chapitre utilise :

- `[PS]` pour les commandes PowerShell et Godot headless ;
- `[VSC]` pour les scripts `.gd` et leurs chemins ;
- `[APP]` pour la création de scènes, Resources, nœuds, noms uniques et réglages Inspector ;
- `[SORTIE]` pour arbres, journaux et fichiers attendus ;
- `[LECTURE]` pour les extraits conceptuels ou partiels ;
- `[WEB]` dans la légende et les références officielles.

Chaque bloc procédural doit être validé par le workflow permanent des contextes.

## 8. Contrôle des doublons

La relecture recherche :

- titres identiques ;
- paragraphes longs répétés ;
- blocs de code significatifs identiques ;
- répétition intégrale des explications du chapitre 2 ;
- duplication du périmètre des chapitres 4, 5 et 7.

Résultat éditorial : **aucun doublon majeur détecté**.

Les répétitions courtes de `connect()`, `is_connected()` et des signatures sont conservées lorsqu’elles servent une décomposition différente.

## 9. Sécurité et licences

- aucune commande destructive n’est demandée ;
- aucun secret réel n’est utilisé ;
- aucun addon tiers n’est requis ;
- Godot reste soumis à sa licence MIT ;
- les fichiers de l’exercice sont destinés au futur Starter Kit avec licence et provenance du projet.

## 10. Portes qualité

- [x] Q0 — Intégrité des fichiers et métadonnées
- [x] Q1 — Complétude pédagogique
- [x] Q2 — Cohérence avec le plan maître
- [x] Q3 — Relecture technique statique
- [x] Q4 — Outils et contextes d’utilisation
- [x] Q5 — Sécurité et licences
- [ ] Q6 — CI, compilation et inspection PDF : à enregistrer dans la preuve finale après exécution
- [ ] Runtime — matérialisation et exécution du projet dans le Starter Kit

## 11. Décision

**Accepté avec réserve CI et runtime au moment de la création du rapport.**

La décision deviendra **Accepté avec réserve runtime** lorsque les workflows de la branche auront réussi et que leurs identifiants seront enregistrés dans `VALIDATION-FINALE-CHAPITRE-03.yaml`.

Le chapitre ne doit jamais être présenté comme `runtime-tested` tant que les fichiers de `Project Asteria` décrits dans le guide n’ont pas été matérialisés et exécutés avec journaux conservés.
