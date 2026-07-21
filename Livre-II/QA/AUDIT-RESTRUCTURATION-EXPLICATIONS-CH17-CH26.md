---
title: "Audit de restructuration des explications — chapitres 17 à 26"
id: "DOC-L2-QA-AUDIT-EXPLANATIONS-CH17-CH26"
status: "complete"
version: "1.0.0"
audit-level: "static-review"
audit-date: "2026-07-21T15:28:42+02:00"
last-verified: "2026-07-21T15:28:42+02:00"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit de restructuration des explications — chapitres 17 à 26

## 1. Objet

Cet audit vérifie la restructuration demandée des explications de blocs. Le contenu pédagogique déjà publié dans les chapitres 17 à 24 a été conservé puis classé sous une rubrique explicite. Les explications plus courtes des chapitres 25 et 26 ont été conservées et complétées à partir des déclarations, signatures, gardes, retours et effets visibles dans chaque extrait.

## 2. Résultats

| Chapitre | Version | Blocs | Marqueurs | Segments conservés | Segments perdus | Segments ajoutés |
|---:|---:|---:|---:|---:|---:|---:|
| 17 | `1.0.4` | 68 | 68 | 246 | 0 | 0 |
| 18 | `1.0.1` | 67 | 67 | 217 | 0 | 0 |
| 19 | `1.0.2` | 56 | 56 | 190 | 0 | 0 |
| 20 | `1.0.1` | 56 | 56 | 202 | 0 | 0 |
| 21 | `1.0.1` | 60 | 60 | 222 | 0 | 0 |
| 22 | `1.0.2` | 61 | 61 | 231 | 0 | 0 |
| 23 | `1.0.1` | 71 | 71 | 283 | 0 | 0 |
| 24 | `1.0.1` | 61 | 61 | 225 | 0 | 0 |
| 25 | `1.0.1` | 55 | 55 | 100 | 0 | 202 |
| 26 | `1.0.1` | 71 | 71 | 166 | 0 | 304 |

Totaux : **2082** segments antérieurs conservés, **0** segment perdu et **506** segments complémentaires ajoutés.

## 3. Règles appliquées

- chaque marqueur est suivi de `Explication structurée du bloc` ;
- chaque information antérieure reste présente sous un point adapté ;
- une rubrique technique supplémentaire est créée lorsque les catégories usuelles ne conviennent pas ;
- les chapitres 25 et 26 possèdent au moins quatre points structurés par bloc ;
- les sections Solo/Studio des chapitres 25 et 26 utilisent des sous-sections et listes Markdown ;
- aucun bloc Solo/Studio artificiel ne contribue désormais au comptage des blocs de code ;
- le contrôle permanent `tools/check_code_explanation_structure.py` empêche une régression de forme.

## 4. Limites

La conservation a été vérifiée textuellement sur chaque segment extrait avant reclassement. Les formulations génériques issues du premier passage ont été supprimées et remplacées par des points fondés sur la syntaxe ou la structure visible. L’audit ne constitue pas une exécution des extraits dans Godot et ne remplace pas les réserves runtime propres à chaque chapitre. Aucun PDF n’a été produit.

## 5. Décision

La restructuration est acceptée au niveau `static-review`. Les workflows officiels ont réussi et les preuves QA des chapitres 17 à 26 sont fermées sur le commit validé.
