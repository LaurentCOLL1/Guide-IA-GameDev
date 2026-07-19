---
title: "Audit post-création — Livre II, chapitre 7"
id: "DOC-L2-QA-AUDIT-CH07"
status: "complete"
version: "1.1.0"
lang: "fr-FR"
book: "Livre II"
chapter: 7
audit-date: "2026-07-19"
audit-level: "static-review"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
recommended-reasoning: "GPT-5.6 Sol — Élevée"
decision: "accepted-with-runtime-and-pdf-reservations"
---

# Audit post-création — Chapitre 7

> **Chapitre audité :** `Livre-II/CHAPITRE-07-Donnees-avec-Resources-JSON-et-configurations.md`  
> **Version auditée :** `1.0.1`  
> **Moteur de référence :** Godot `4.7.1-stable`  
> **Décision :** accepté avec réserves runtime et PDF de fin de Livre  
> **Politique PDF :** aucune construction intermédiaire.

## 1. Périmètre contrôlé

L’audit couvre :

- données de conception, configuration, état runtime et persistance ;
- choix entre Resource, JSON, ConfigFile, mémoire et SQLite futur ;
- identifiants stables ;
- cache, partage, duplication et `resource_local_to_scene` ;
- diagnostics structurés ;
- `BeaconCatalog` et sa validation ;
- repository de lecture ;
- chargement centralisé, chemin, type et cache ;
- JSON par défaut et surcharge Studio ;
- erreurs `FileAccess` et `JSON` ;
- validation des types, valeurs et plages ;
- fusion récursive ;
- `RuntimeConfiguration` et ses cinq lecteurs ;
- assemblage dans `AppBootstrap` ;
- `res://`, `user://` et export ;
- `ConfigFile` ;
- chargement en arrière-plan ;
- sécurité des chemins et secrets ;
- parcours Solo et Studio ;
- explication des fonctions et paramètres ;
- repères d’utilisation ;
- doublons ;
- frontières avec les chapitres 3, 5, 8 et 9.

## 2. Contrôles quantitatifs

Résultats de la validation automatique légère :

| Contrôle | Résultat |
|---|---:|
| lignes du chapitre | 2 101 |
| titres contrôlés | 96 |
| blocs significatifs | 32 |
| titres identiques | 0 |
| blocs significatifs identiques | 0 |
| paragraphes longs identiques | 0 |
| erreurs bloquantes du dépôt | 0 |
| avertissements | 1 |
| sources déclarées | 53 |
| chapitres du Livre II | 7 |
| identifiants uniques | 52 |
| fichiers contrôlés pour les contextes | 51 |
| blocs de code ou texte contrôlés | 968 |
| blocs précédés d’un repère | 968 sur 968 |
| non-conformités de contexte | 0 |
| incohérences sémantiques | 0 |
| PDF produit | 0 |

L’unique avertissement concerne la licence globale, toujours à définir avant publication officielle.

## 3. Campagne automatique

Première campagne verte :

- `Validate Chapters Without PDF` : exécution `29672887015` ;
- `Validate Usage Contexts` : exécution `29672887018` ;
- commit contrôlé : `f11b4baf6a355252b8b8f8cc623477de3d0a3235` ;
- artefact chapitre : `8437873759` ;
- artefact contextes : `8437873481`.

Les étapes suivantes ont réussi :

- structure, métadonnées, liens et doublons ;
- présence des repères ;
- cohérence sémantique des repères ;
- mesure de couverture ;
- assertion qu’aucun PDF n’a été produit ;
- publication des preuves QA.

## 4. Non-conformités détectées et corrigées

| Identifiant | Risque | Correction |
|---|---|---|
| L2-CH07-001 | définition et état runtime confondus | taxonomie et immuabilité des définitions canoniques |
| L2-CH07-002 | nom affiché utilisé comme identité | `StringName` stable, non traduit et validé |
| L2-CH07-003 | cache des Resources ignoré | partage, `duplicate(true)` et localité de scène expliqués |
| L2-CH07-004 | catalogue utilisé sans validation | `BeaconCatalog.validate()` et rapport structuré |
| L2-CH07-005 | index de tableau utilisé comme identité | recherche exclusivement par identifiant |
| L2-CH07-006 | modèle de données couplé à l’affichage | diagnostics transportés sans décider du rendu |
| L2-CH07-007 | chemins et chargeurs connus du gameplay | repository injecté |
| L2-CH07-008 | chemin arbitraire accepté | dossier, extension, existence et type contrôlés |
| L2-CH07-009 | `_load_catalog_at()` appelée mais absente | fonction complète ajoutée pendant la seconde lecture |
| L2-CH07-010 | deux lecteurs appelés mais absents | `_read_ai_services()` et `_read_data_paths()` ajoutées |
| L2-CH07-011 | JSON accepté après seul parsing | structure, types, plages et chemins validés |
| L2-CH07-012 | diagnostic JSON trop pauvre | instance `JSON`, ligne et message d’erreur |
| L2-CH07-013 | fichier absent et refus d’ouverture confondus | traitements `file_exists()` et `get_open_error()` séparés |
| L2-CH07-014 | fusion modifiant la base | copie profonde du dictionnaire avant fusion |
| L2-CH07-015 | politique de fusion implicite | objets fusionnés, tableaux et scalaires remplacés |
| L2-CH07-016 | dictionnaire brut utilisé dans les services | conversion en `RuntimeConfiguration` |
| L2-CH07-017 | paramètres IA insuffisamment bornés | booléen, URL locale et délai contrôlés |
| L2-CH07-018 | sauvegarde anticipée | aucune écriture `user://` avant le chapitre 9 |
| L2-CH07-019 | SQLite consommé prématurément | repository préparé, implémentation Resource conservée |
| L2-CH07-020 | JSON absent de l’export | filtre ciblé et test d’export déclaré |
| L2-CH07-021 | chargement différé rendu bloquant | interrogation du statut sur plusieurs images |
| L2-CH07-022 | secret versionné | interdiction explicite et séparation des responsabilités |
| L2-CH07-023 | PDF reconstruit par habitude | workflow léger uniquement |

## 5. Vérification pédagogique

Les fonctions principales disposent d’une explication de leurs paramètres, retours et effets :

- `DataValidationIssue._init()` ;
- `add_warning()` et `add_error()` ;
- `has_errors()` et `is_valid()` ;
- `BeaconCatalog.validate()` ;
- `find_by_id()` ;
- `run_validation()` ;
- `BeaconCatalogRepository.get_by_id()` et `get_all()` ;
- `ResourceBeaconCatalogRepository._init()` ;
- `_is_allowed_catalog_path()` ;
- `_load_catalog_at()` ;
- `_print_data_issues()` ;
- `JsonConfigLoader.load_object()` ;
- `read_integer()` ;
- `merge_objects()` ;
- `RuntimeConfiguration.apply()` ;
- `_read_schema()` ;
- `_read_environment()` ;
- `_read_logging()` ;
- `_read_ai_services()` ;
- `_read_data_paths()` ;
- `load_runtime_configuration()` ;
- `_resolve_environment_path()` ;
- `_build_data_services()` ;
- `Ch07DataDemo.configure()` et `run_demo()`.

Les notions sont définies avant ou lors de leur première utilisation :

- données de conception ;
- configuration ;
- état runtime ;
- persistance ;
- cache de Resource ;
- immuabilité par convention ;
- version de schéma ;
- identifiant stable ;
- diagnostic structuré ;
- repository ;
- parsing ;
- validation sémantique ;
- fusion récursive ;
- surcharge d’environnement ;
- chargement en arrière-plan.

## 6. Vérification technique statique

La revue utilise les références officielles Godot 4.7 relatives à :

- `Resource` et les Resources personnalisées ;
- cache, partage, `duplicate()` et `resource_local_to_scene` ;
- `ResourceLoader.exists()`, `load()` et modes de cache ;
- chargement en arrière-plan ;
- `FileAccess` ;
- `JSON.parse()` et ses diagnostics ;
- `ConfigFile` ;
- filtres d’export des fichiers non-ressources.

Points spécifiques relus :

- les cinq fonctions appelées par `RuntimeConfiguration.apply()` existent ;
- `_build_data_services()` appelle une fonction `_load_catalog_at()` définie ;
- chaque cast est précédé d’un contrôle ou suivi d’un test `null` ;
- la Resource est validée avant création du repository ;
- les chemins sont contrôlés à la lecture de configuration et au chargement ;
- le chargement différé ne contient aucune boucle bloquante ;
- la configuration ne contient aucun secret ;
- `res://` et `user://` ne sont pas confondus.

## 7. Frontières de collection

Le chapitre ne répète pas l’initiation aux Resources du chapitre 3 et ne redéfinit pas le registre du chapitre 5.

Il ne consomme pas :

- transactions, index et migrations SQLite du chapitre 8 ;
- écriture et migration des sauvegardes du chapitre 9 ;
- communications réseau des chapitres 11 et 12 ;
- sécurité IA complète du chapitre 13 ;
- inventaire du chapitre 20 ;
- outils de contenu du chapitre 26 ;
- tests complets du chapitre 27.

## 8. Portes de qualité

| Porte | Résultat |
|---|---|
| Q0 — intégrité | validée |
| Q1 — complétude pédagogique | validée |
| Q2 — cohérence de collection | validée |
| Q3 — vérification technique statique | validée |
| Q4 — outils et contextes | validée |
| Q5 — sécurité et licences | validée avec réserve de licence globale |
| Q6 — validation documentaire du chapitre | validée sans PDF |
| Q7 — publication PDF de fin de Livre | différée |

## 9. Réserves

- scripts, JSON, scènes et Resources non matérialisés dans le Starter Kit ;
- aucune exécution dans Godot ;
- aucun test réel du cache, du parseur ou du repository ;
- aucun JSON chargé dans un export ;
- aucun chargement en arrière-plan exécuté ;
- aucune migration SQLite ou sauvegarde implémentée ;
- licence globale à définir ;
- PDF non construit avant la fin du Livre II.

## 10. Décision

Le chapitre 7 est **accepté avec réserves runtime et PDF de fin de Livre**.

Il peut être déclaré :

> **rédigé, repéré et audité au niveau documentaire et statique, sans construction PDF intermédiaire.**
