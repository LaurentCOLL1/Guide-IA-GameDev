---
title: "Audit post-création — Livre II, chapitre 7"
id: "DOC-L2-QA-AUDIT-CH07"
status: "complete"
version: "1.0.0"
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
> **Décision provisoire :** accepté sous réserve du passage automatique final, des tests runtime et du PDF de fin de Livre  
> **Politique PDF :** aucune construction intermédiaire.

## 1. Périmètre contrôlé

L’audit couvre :

- les quatre familles de données ;
- la matrice de choix des formats ;
- les identifiants stables ;
- le cache et le partage des Resources ;
- `duplicate(true)` et `resource_local_to_scene` ;
- les diagnostics structurés ;
- `BeaconCatalog` et sa validation ;
- le repository de lecture ;
- le chargement centralisé et typé ;
- les fichiers JSON par défaut et Studio ;
- les erreurs `FileAccess` et `JSON` ;
- la validation des types et plages ;
- la fusion récursive des objets ;
- `RuntimeConfiguration` et ses cinq lecteurs ;
- l’assemblage dans `AppBootstrap` ;
- `res://`, `user://` et l’export ;
- `ConfigFile` comme alternative ;
- le chargement en arrière-plan ;
- la sécurité des chemins et secrets ;
- les parcours Solo et Studio ;
- la profondeur des explications ;
- les repères d’utilisation ;
- les doublons ;
- les frontières avec les chapitres 3, 5, 8 et 9.

## 2. Contrôles quantitatifs

Les métriques définitives sont produites par le workflow `Validate Chapters Without PDF` après ouverture de la pull request.

Le rapport final doit confirmer :

- tous les blocs clôturés ;
- un repère explicite avant chaque bloc ;
- aucun titre identique ;
- aucun bloc significatif identique ;
- aucun long paragraphe identique ;
- aucune erreur bloquante ;
- aucun PDF produit.

Les nombres exacts et les identifiants d’exécution seront enregistrés après la campagne automatique finale.

## 3. Non-conformités détectées et corrigées

### L2-CH07-001 — Définition et état runtime confondus

**Risque :** modifier une `BeaconProfile` partagée pour stocker un cooldown courant.

**Correction :** séparation explicite entre données de conception, configuration, état runtime et sauvegarde ; règle d’immuabilité des Resources canoniques.

### L2-CH07-002 — Nom affiché utilisé comme identité

**Risque :** casser les relations lors d’une traduction ou d’une reformulation.

**Correction :** identifiants `StringName` stables, ASCII, non traduits et uniques.

### L2-CH07-003 — Cache des Resources ignoré

**Risque :** une mutation locale devient visible dans plusieurs consommateurs.

**Correction :** explication du cache, du partage, de `duplicate(true)` et de `resource_local_to_scene` avec leurs limites.

### L2-CH07-004 — Catalogue non validé

**Risque :** entrée `null`, identifiant vide, format incorrect, doublon ou cooldown invalide.

**Correction :** `BeaconCatalog.validate()` produit un `DataValidationReport` structuré avant injection.

### L2-CH07-005 — Position de tableau utilisée comme identifiant

**Risque :** réordonner le catalogue modifie le sens des références.

**Correction :** l’index sert uniquement à localiser une erreur ; les recherches utilisent `find_by_id()`.

### L2-CH07-006 — Erreurs directement affichées par le modèle de données

**Risque :** coupler catalogue, interface, journal et CI.

**Correction :** `DataValidationIssue` et `DataValidationReport` transportent les problèmes ; le point de composition choisit leur rendu.

### L2-CH07-007 — Repository absent

**Risque :** chaque service connaît les chemins et les API de chargement.

**Correction :** contrat `BeaconCatalogRepository`, implémentation Resource et injection depuis `AppBootstrap`.

### L2-CH07-008 — Chemin de catalogue non contrôlé

**Risque :** charger un chemin absolu, un autre dossier ou une extension inattendue.

**Correction :** `_is_allowed_catalog_path()` et `_load_catalog_at(path)` contrôlent préfixe, extension, existence, type et contenu.

### L2-CH07-009 — Appel d’une fonction de chargement inexistante

**Risque :** exemple incomplet dans lequel `_build_data_services()` appelle `_load_catalog_at()` sans définition.

**Correction :** la seconde lecture a ajouté la fonction complète avant l’assemblage.

### L2-CH07-010 — Lecteurs de configuration appelés mais absents

**Risque :** `RuntimeConfiguration.apply()` appelle `_read_ai_services()` et `_read_data_paths()` sans implémentation.

**Correction :** les deux fonctions sont désormais définies, détaillées et cohérentes avec le JSON fourni.

### L2-CH07-011 — JSON accepté après simple parsing

**Risque :** syntaxe valide mais clés, types, plages ou chemins invalides.

**Correction :** validation de la racine, des sections, des types, des valeurs autorisées, des délais et du chemin du catalogue.

### L2-CH07-012 — Diagnostic JSON insuffisant

**Risque :** `JSON.parse_string()` renvoie `null` sans localisation exploitable.

**Correction :** instance `JSON`, code d’erreur, ligne et message détaillé.

### L2-CH07-013 — Erreurs d’ouverture non différenciées

**Risque :** fichier absent et refus d’ouverture produisent le même diagnostic.

**Correction :** `file_exists()`, `FileAccess.open()`, `get_open_error()` et `error_string()` sont traités séparément.

### L2-CH07-014 — Fusion modifiant la configuration de base

**Risque :** une surcharge altère le dictionnaire source partagé.

**Correction :** `merge_objects()` commence par `base.duplicate(true)` et renvoie un nouvel objet.

### L2-CH07-015 — Politique de fusion implicite

**Risque :** outils Godot et Python produisent des résultats différents.

**Correction :** objets fusionnés récursivement ; tableaux et valeurs scalaires remplacés ; suppression par `null` non prise en charge.

### L2-CH07-016 — Configuration brute utilisée par les services

**Risque :** chaînes de clés et casts répétés dans le gameplay.

**Correction :** conversion vers `RuntimeConfiguration` avant injection.

### L2-CH07-017 — Sections IA incomplètement expliquées

**Risque :** paramètres, types et bornes de `enabled`, `base_url` et `request_timeout_seconds` laissés implicites.

**Correction :** fonction dédiée, contrôle booléen, URL locale et intervalle de délai documentés.

### L2-CH07-018 — Sauvegarde anticipée

**Risque :** écrire réglages ou progression avant la stratégie de versionnement du chapitre 9.

**Correction :** aucune écriture sous `user://`; la frontière est répétée dans le périmètre, les chemins et les erreurs fréquentes.

### L2-CH07-019 — SQLite consommé prématurément

**Risque :** introduire schéma relationnel et migrations avant le chapitre 8.

**Correction :** le repository prépare le remplacement, mais l’implémentation reste fondée sur une Resource.

### L2-CH07-020 — JSON non inclus dans l’export

**Risque :** fonctionnement dans l’éditeur mais fichier absent dans la construction livrée.

**Correction :** vérification du filtre `config/**/*.json` et test d’export conservé comme réserve runtime.

### L2-CH07-021 — Chargement en arrière-plan rendu bloquant

**Risque :** boucle serrée ou appel prématuré à `load_threaded_get()`.

**Correction :** statut interrogé sur plusieurs images et avertissement explicite contre la boucle bloquante.

### L2-CH07-022 — Secret versionné

**Risque :** jeton ou mot de passe présent dans Git ou le paquet exporté.

**Correction :** interdiction explicite et séparation avec la sécurité des services des chapitres 11 à 13.

### L2-CH07-023 — PDF reconstruit par habitude

**Risque :** contrevenir à la décision de différer les constructions.

**Correction :** seul le workflow léger doit s’exécuter ; la publication PDF reste manuelle et différée.

## 4. Vérification pédagogique

Les fonctions principales possèdent une explication de leurs paramètres, retours et effets :

- `DataValidationIssue._init()` ;
- `add_warning()` ;
- `add_error()` ;
- `has_errors()` ;
- `is_valid()` ;
- `BeaconCatalog.validate()` ;
- `find_by_id()` ;
- `run_validation()` ;
- `BeaconCatalogRepository.get_by_id()` ;
- `get_all()` ;
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
- `Ch07DataDemo.configure()` ;
- `run_demo()`.

Les notions nouvelles sont définies avant ou lors de leur première utilisation :

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

## 5. Vérification technique statique

La revue est fondée sur la documentation officielle Godot 4.7 relative à :

- `Resource` et les Resources personnalisées ;
- le cache et le partage des Resources ;
- `duplicate()` ;
- `resource_local_to_scene` ;
- `ResourceLoader.exists()` et `load()` ;
- les modes de cache ;
- les méthodes de chargement en arrière-plan ;
- `FileAccess` ;
- `JSON.parse()` et ses diagnostics ;
- `ConfigFile` ;
- les filtres d’export des fichiers non-ressources.

Points spécifiques relus :

- les fonctions appelées dans `RuntimeConfiguration.apply()` existent toutes ;
- `_build_data_services()` appelle une fonction `_load_catalog_at()` définie ;
- chaque cast intervient après un contrôle ou possède un test `null` ;
- les échecs sont transmis dans le rapport ou renvoient `false` ;
- la Resource est validée avant le repository ;
- le chargement différé ne contient aucune boucle bloquante ;
- la configuration ne contient aucun secret ;
- `res://` et `user://` ne sont pas confondus.

## 6. Frontières de collection

Le chapitre ne consomme pas :

- la création initiale de Resource déjà couverte au chapitre 3 ;
- la définition générale du registre et du bootstrap du chapitre 5 ;
- les migrations, transactions et index SQLite du chapitre 8 ;
- l’écriture et la migration des sauvegardes du chapitre 9 ;
- les communications réseau des chapitres 11 et 12 ;
- la politique complète de sécurité IA du chapitre 13 ;
- l’inventaire du chapitre 20 ;
- les outils de contenu du chapitre 26 ;
- les tests complets du chapitre 27.

## 7. Portes de qualité

| Porte | Résultat attendu |
|---|---|
| Q0 — intégrité | validation automatique requise |
| Q1 — complétude pédagogique | validée après seconde lecture |
| Q2 — cohérence de collection | validée |
| Q3 — vérification technique statique | validée |
| Q4 — outils et contextes | validation automatique requise |
| Q5 — sécurité et licences | validée avec réserve de licence globale |
| Q6 — validation documentaire du chapitre | requise sans PDF |
| Q7 — publication PDF de fin de Livre | différée |

## 8. Réserves

- scripts et Resources non matérialisés dans le Starter Kit ;
- aucune exécution dans Godot ;
- aucun test réel du cache, du parseur ou du repository ;
- aucun fichier JSON chargé dans un export ;
- aucun chargement en arrière-plan exécuté ;
- aucune migration SQLite ou sauvegarde implémentée ;
- licence globale à définir ;
- PDF non construit avant la fin du Livre II.

## 9. Décision

Après réussite des workflows légers, le chapitre 7 peut être déclaré :

> **rédigé, repéré et audité au niveau documentaire et statique, avec réserves runtime et sans construction PDF intermédiaire.**
