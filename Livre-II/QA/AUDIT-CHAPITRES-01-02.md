---
title: "Audit post-création — Livre II, chapitres 1 et 2"
id: "DOC-L2-QA-AUDIT-CH01-CH02"
status: "complete"
version: "1.0.0"
book: "Livre II"
category: "quality-report"
validation-date: "2026-07-18"
---

# Audit post-création — Livre II, chapitres 1 et 2

## 1. Périmètre

Documents contrôlés :

- `DOC-L2-CH01` — Découvrir Godot et créer le projet fil rouge ;
- `DOC-L2-CH02` — Fondamentaux de GDScript.

L’audit applique le protocole `DOC-L2-QA-POST-CREATION` et compare les deux documents au sommaire maître du Livre II.

## 2. Méthode

Les contrôles ont porté sur :

- la complétude pédagogique ;
- les frontières entre chapitres ;
- les métadonnées et identifiants ;
- les versions et liens officiels ;
- la syntaxe et la cohérence des commandes ;
- la relecture statique des extraits GDScript ;
- les risques, licences et diagnostics ;
- l’intégration à `contents.txt`, à l’index et à la roadmap ;
- la compilation Pandoc/XeLaTeX.

Le dépôt du guide ne contient pas encore une copie exécutable complète de `Project Asteria`. Les extraits GDScript font donc l’objet d’une **revue statique** contre la documentation Godot 4.7. Leur exécution réelle reste à reproduire lorsque les fichiers du projet fil rouge seront matérialisés dans le Companion Pack ou dans un dépôt dédié.

## 3. Chapitre 1 — Résultats

### Couverture validée

Le chapitre couvre correctement :

- le rôle et le périmètre de `Project Asteria` ;
- la version stable de Godot ;
- les éditions Standard et .NET ;
- Forward+, Mobile et Compatibility ;
- le téléchargement, l’empreinte et l’installation portable ;
- la création du dépôt et du projet ;
- `res://`, `user://` et `.gdignore` ;
- l’éditeur, les nœuds, scènes et Resources ;
- l’arborescence par fonctionnalité ;
- la scène de bootstrap et le premier script ;
- la validation visuelle et headless ;
- Git, les addons, le diagnostic et les modes Solo/Studio.

### Oublis détectés et corrigés

| ID | Gravité | Constat | Correction |
|---|---|---|---|
| L2-AUD-001 | majeure | La base Git ne documentait pas suffisamment `.gitattributes`. | Ajout de la génération et du contenu minimal de `.gitattributes`, avec normalisation LF. |
| L2-AUD-002 | majeure | Le fichier généré `*.translation` n’était pas exclu. | Ajout à `.gitignore` conformément à la documentation Godot 4.7. |
| L2-AUD-003 | mineure | La liste des fichiers initiaux omettait `.gitattributes`. | Ajout à l’inventaire attendu. |
| L2-AUD-004 | mineure | `--quit-after` pouvait être interprété comme une durée. | Précision qu’il s’agit d’un nombre d’itérations et ajustement du test. |
| L2-AUD-005 | majeure | La licence MIT de Godot et l’obligation d’attribution n’étaient pas explicitées dans le chapitre d’installation. | Ajout d’une section licence et notices tierces. |

### Décision

**Accepté avec réserve runtime.** Le chapitre est complet sur le plan documentaire après corrections. La scène et les commandes doivent encore être exécutées sur une copie matérialisée de `Project Asteria` pour passer au niveau `runtime-tested`.

## 4. Chapitre 2 — Résultats

### Couverture validée

Le chapitre couvre correctement :

- la nature de GDScript et sa différence avec Python ;
- fichiers, classes, indentation et style ;
- types, variables, constantes et énumérations ;
- tableaux, dictionnaires, conditions, `match` et boucles ;
- fonctions, classes, héritage et accesseurs ;
- annotations, cycle de vie et validité des objets ;
- chargement des ressources, chaînes, mathématiques et aléatoire ;
- gestion des erreurs, avertissements et débogueur ;
- un exercice intégré à `Project Asteria` ;
- des tests manuels, déterministes et headless ;
- les modes Solo et Studio.

### Oublis détectés et corrigés

| ID | Gravité | Constat | Correction |
|---|---|---|---|
| L2-AUD-006 | majeure | Les opérateurs de contrôle et conversion de type `is` et `as` n’étaient pas enseignés. | Ajout d’une section avec contrôle sûr, conversion nullable et avertissement sur les échecs silencieux. |
| L2-AUD-007 | majeure | Les dictionnaires typés, disponibles dans la version de référence, n’étaient pas présentés. | Ajout de `Dictionary[StringName, float]` et des règles d’usage. |
| L2-AUD-008 | mineure | Les PackedArrays n’étaient pas distingués des tableaux ordinaires. | Ajout d’un aperçu et d’une règle de choix. |
| L2-AUD-009 | mineure | `await` et les coroutines n’étaient pas mentionnés. | Ajout d’un aperçu limité, avec approfondissement reporté au chapitre sur les signaux. |
| L2-AUD-010 | mineure | Plusieurs liens utilisaient `/stable/`, susceptible de changer de branche. | Épinglage des références techniques à la documentation `/en/4.7/`. |
| L2-AUD-011 | mineure | La description de `String` pouvait laisser entendre une mutabilité directe. | Reformulation en « chaîne Unicode ». |

### Décision

**Accepté avec réserve runtime.** Le périmètre « fondamentaux de GDScript » est complet après corrections. Les extraits ont été relus statiquement ; l’exécution réelle dans Godot reste à matérialiser.

## 5. Frontières entre les chapitres

La séparation retenue est cohérente :

- le chapitre 1 installe le moteur et crée une scène minimale ;
- le chapitre 2 enseigne le langage sans construire l’architecture globale ;
- le chapitre 3 approfondira scènes, instances, Resources et signaux ;
- le chapitre 4 définira l’architecture modulaire ;
- les services globaux et bus d’événements restent réservés au chapitre 5.

Aucune duplication majeure ou consommation prématurée du périmètre suivant n’a été détectée.

## 6. Portes qualité

- [x] Q0 — Intégrité des fichiers et métadonnées
- [x] Q1 — Complétude pédagogique
- [x] Q2 — Cohérence avec le sommaire maître
- [x] Q3 — Relecture technique statique
- [x] Q4 — Sécurité et licences documentées
- [ ] Q3 runtime — Exécution sur le projet matérialisé
- [ ] Q5 — Compilation finale de la branche corrigée

Les deux dernières cases sont mises à jour après exécution de la CI et, ultérieurement, après création des fichiers exécutables du projet fil rouge.

## 7. Règle permanente adoptée

Chaque nouveau chapitre du Livre II doit désormais :

1. recevoir un audit post-création ;
2. corriger les oublis détectés ;
3. porter les métadonnées `audit-status`, `audit-date`, `audit-report` et `audit-level` ;
4. être intégré aux index avant validation ;
5. réussir la compilation CI ;
6. être présenté comme « rédigé et audité », et non simplement « fait ».