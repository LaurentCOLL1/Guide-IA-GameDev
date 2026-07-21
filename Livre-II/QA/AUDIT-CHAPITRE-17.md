---
title: "Audit du Livre II — Chapitre 17"
id: "DOC-L2-QA-AUDIT-CH17"
status: "complete"
version: "1.0.4"
chapter-id: "DOC-L2-CH17"
chapter-version: "1.0.4"
audit-level: "static-review"
audit-date: "2026-07-21T17:35:51+02:00"
last-verified: "2026-07-21T17:35:51+02:00"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit du chapitre 17 — Agents IA et comportements autonomes

## 1. Porte de brouillon observée

Le premier commit permanent a conservé `status: draft`, `version: 0.9.0`, `audit-status: pending` et `audit-level: not-audited`. Le présent rapport appartient à une passe distincte.

## 2. Résultats

- lignes finales : **2648** ;
- blocs clôturés : **68** ;
- marqueurs d’explication : **68** ;
- cas d’erreurs détaillés : **16** ;
- auto-paraphrases du titre courant : **0** ;
- fragments internes non résolus : **0** ;
- sources Godot 4.7 nommées : **13** ;
- doublons de titres ou blocs significatifs : **0 selon la validation automatique** ;
- PDF produit : **non** ;
- exécution runtime : **non**.

## 3. Corrections issues de la seconde lecture

1. ajout de l’ancre précise `ch17-agent-state` ;
2. conversion explicite des `StringName` pour la signature d’un chemin ;
3. documentation des six ports applicatifs utilisés ;
4. implémentation stricte de `AgentSnapshotCodec` ;
5. réutilisation de `SaveValueCodec` pour `Vector3` ;
6. refus des clés, types, versions, identités et buts dupliqués ;
7. ajout d’un drapeau de préparation à `AgentSaveSection` ;
8. conversion explicite vers `Array[AgentState]` ;
9. consommation du candidat seulement après succès ;
10. explication du bloc de prochaine étape ;
11. maintien de l’IA générative dans un rôle consultatif ;
12. séparation conservée avec combat, compétences, économie, monde vivant et narration.

## 4. Audit du déterminisme

Le chemin de référence utilise :

- snapshots détachés ;
- actions et buts triés ;
- clés d’état canoniques ;
- limites d’expansions et de profondeur ;
- nombre d’agents par tick ;
- phases stables ;
- ticks et séquences logiques ;
- RNG local restaurable seulement pour variantes équivalentes ;
- microsecondes limitées à la télémétrie.

## 5. Explications pédagogiques


Les **68** blocs possèdent **68** marqueurs. Les explications antérieures ont été décomposées en **246** segments techniques conservés mot pour mot, puis regroupées sous des rubriques uniques et adaptées. Les libellés génériques sont interdits ; chaque point cite un champ, une fonction, une garde, un retour, un effet, un chemin ou une relation réellement visible dans le bloc.

## 5. Réserves

Aucun script n’a été analysé par le parseur Godot. La scène, les signaux, le contrôleur, le planificateur, le codec, la restauration, les performances, la parallélisation et le packaging n’ont pas été exécutés.

## 6. Décision

**Accepté au niveau `static-review`**, sous réserve des validations documentaires permanentes et des tests runtime futurs du chapitre 27.

## 7. Addendum terminologique et ordonnanceur — version 1.0.1

La relecture postérieure à la fusion a distingué six libellés ambigus hors de la section 37 :

- `Valeurs de retour` pour une sentinelle ou un résultat non limité à `Error` ;
- `Codes de retour` pour `ERR_*` ;
- `Refus contrôlé` pour une clé non enregistrée ;
- `Statuts à distinguer` pour `NO_PLAN` et `BUDGET_EXCEEDED` ;
- `Traitement du résultat` pour la consommation du retour de `decide()`.

La phrase des intervalles associe désormais explicitement `ACTIVE`, `BACKGROUND` et `DORMANT` aux valeurs `6`, `60` et `600`, précise la dépendance à `Engine.physics_ticks_per_second` et qualifie les fréquences de nominales.

L’audit a également détecté un défaut fonctionnel dans l’exemple de `AgentTickPolicy` : le test modulo exact pouvait perdre une échéance lorsque la limite de huit décisions empêchait de visiter l’agent au tick prévu. La politique calcule maintenant `next_due_tick` et utilise `logical_tick >= next_due_tick`, ce qui conserve l’échéance jusqu’au traitement effectif.

## 8. Addendum d’horodatage — version 1.0.2

La vérification corrective est horodatée en heure locale `Europe/Paris` avec le format ISO 8601 et son décalage UTC : `2026-07-20T10:19:05+02:00`. Les métadonnées `audit-date` et `last-verified` portent désormais l’heure, les minutes, les secondes et l’offset.

Les anciens audits qui ne disposent que d’une date ne reçoivent pas d’heure reconstruite artificiellement. Ils adopteront ce format lors de leur prochaine modification auditée.

## 9. Addendum de clôture — version 1.0.3

La section `44. Prochaine étape` a été retirée du chapitre. Le chemin et le niveau du chapitre suivant sont des informations de pilotage du projet et restent dans `CONTINUITE-PROJET.md`, pas dans le texte destiné au lecteur.

La fin du chapitre porte désormais une synthèse opérationnelle des décisions retenues pour `Project Asteria`, conformément aux chapitres de systèmes précédents. La vérification corrective est horodatée `2026-07-20T11:27:57+02:00`.
