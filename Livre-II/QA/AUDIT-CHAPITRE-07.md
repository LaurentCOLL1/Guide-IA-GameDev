---
title: "Audit post-création — Livre II, chapitre 7"
id: "DOC-L2-QA-CH07"
status: "complete"
version: "1.1.0"
lang: "fr-FR"
book: "Livre II"
chapter: 7
audit-date: "2026-07-19"
audit-level: "static-review"
chapter-file: "Livre-II/CHAPITRE-07-Donnees-avec-Resources-JSON-et-configurations.md"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
pdf-built: false
---

# Audit post-création — Livre II, chapitre 7

## 1. Décision

**Accepté au niveau `static-review`, avec réserves runtime et PDF différé.**

Le chapitre couvre son périmètre prévu sans introduire SQLite, le système de sauvegarde, les API IA ou les pipelines automatisés des chapitres ultérieurs.

## 2. Périmètre contrôlé

Le contrôle a porté sur :

- données de conception, configuration, état runtime et persistance ;
- `Resource` personnalisées, externes et imbriquées ;
- cache, partage, duplication et `resource_local_to_scene` ;
- identifiants stables et catalogues typés ;
- `preload()`, `load()` et `ResourceLoader` ;
- lecture JSON avec `FileAccess` et `JSON` ;
- validation structurelle et métier ;
- versionnement des formats ;
- `ConfigFile`, `res://` et `user://` ;
- fusion des configurations ;
- injection d’un catalogue dans un service ;
- parcours Solo et Studio ;
- frontières avec les chapitres 8, 9, 26, 27, 28 et 29.

## 3. Vérification pédagogique

Les premières apparitions significatives expliquent :

- le rôle de chaque classe ;
- le type des propriétés ;
- la fonction des annotations `@export` ;
- les paramètres et retours de `validate()` ;
- la différence entre clé et valeur d’un dictionnaire typé ;
- les codes `Error` retournés par le catalogue ;
- le sens du paramètre de `duplicate()` ;
- les retours possibles de `load()` et des conversions `as` ;
- les arguments de `FileAccess.open()` ;
- les informations fournies par `JSON.get_error_line()` et `get_error_message()` ;
- les paramètres des lecteurs de champs ;
- la fusion des sections et clés d’un `ConfigFile` ;
- la différence entre version de format et version de contenu.

Les exemples sont accompagnés d’un contexte `[VSC]`, `[APP]`, `[LECTURE]` ou `[SORTIE]`. La seconde Resource, la scène de vérification et les huit erreurs fréquentes disposent désormais d’exemples détaillés et comparables.

## 4. Contrôle des frontières

Le chapitre n’implémente pas :

- de schéma ou migration SQLite ;
- de repository SQL ;
- de fichier de sauvegarde du joueur ;
- de migration de sauvegarde ;
- de mémoire vectorielle ;
- de requête HTTP ou WebSocket ;
- de génération Python ;
- d’outil d’import automatisé ;
- de test runtime revendiqué comme exécuté.

Les données `.tres` restent des définitions de conception. L’état runtime est placé dans `BeaconRuntimeState` et la persistance est explicitement reportée au chapitre 9.

## 5. Contrôle technique statique

### 5.1 Resources

Le chapitre rappelle que le chargement d’un même chemin peut retourner la même ressource en cache et traite les définitions chargées comme des données partagées à ne pas modifier implicitement.

La duplication superficielle et profonde est distinguée. Le résultat est converti et vérifié avant utilisation.

`resource_local_to_scene` est présenté comme un outil ciblé, pas comme une solution générale aux états runtime.

### 5.2 Catalogues

Le catalogue :

- refuse `null` ;
- appelle la validation métier ;
- vérifie l’identifiant ;
- refuse les doublons ;
- retourne un code `Error` ;
- fournit une liste triée d’identifiants ;
- ne parcourt pas lui-même le système de fichiers.

### 5.3 JSON

Le lecteur :

- vérifie l’existence du fichier ;
- contrôle l’ouverture ;
- rapporte la ligne et le message d’erreur JSON ;
- exige une racine dictionnaire ;
- sépare validation structurelle et validation métier ;
- refuse une version de format inconnue ;
- vérifie les éléments d’un tableau un par un.

### 5.4 Configuration

La configuration :

- charge des valeurs par défaut depuis `res://` ;
- applique une surcharge facultative depuis `user://` ;
- convertit le résultat vers `AppConfig` ;
- ne propage pas `ConfigFile` dans le domaine ;
- ne contient aucun secret versionné ;
- ne réécrit pas silencieusement les fichiers sources.

## 6. Risques détectés et corrections intégrées

### Risque 1 — confondre définition et état runtime

**Correction :** introduction de `BeaconRuntimeState` distinct de `BeaconProfile`.

### Risque 2 — modifier une Resource partagée

**Correction :** explication du cache, règle d’immuabilité et duplication explicite.

### Risque 3 — utiliser le nom affiché comme identifiant

**Correction :** convention `StableId` indépendante de l’affichage et des chemins.

### Risque 4 — accepter un JSON seulement parce qu’il est syntaxiquement valide

**Correction :** validation de racine, champs, types, plages, tableaux, doublons et version.

### Risque 5 — lire un fichier texte avec `ResourceLoader`

**Correction :** utilisation de `FileAccess` et `JSON` pour le JSON brut.

### Risque 6 — dépendre de l’ordre d’un parcours de dossier

**Correction :** liste explicite de chemins et tri des identifiants exposés.

### Risque 7 — propager des dictionnaires non typés

**Correction :** conversion aux frontières vers `BeaconProfile`, `BeaconCatalog` et `AppConfig`.

### Risque 8 — utiliser `ConfigFile` comme objet global

**Correction :** mapping vers une configuration typée injectée depuis le bootstrap.

### Risque 9 — stocker des secrets dans le dépôt

**Correction :** interdiction explicite et distinction entre URL locale et jeton secret.

### Risque 10 — introduire SQLite prématurément

**Correction :** frontières répétées avec le chapitre 8.

### Risque 11 — utiliser les données de conception comme sauvegarde

**Correction :** persistance du joueur reportée au chapitre 9.

### Risque 12 — masquer une donnée manquante avec une valeur arbitraire

**Correction :** modes strict, audit et dégradé explicités ; Null Object seulement s’il est nommé et journalisé.

### Risque 13 — oublier la version du format externe

**Correction :** champ `format_version`, version courante et politique de refus.

### Risque 14 — construire le PDF après le chapitre

**Correction :** validation légère obligatoire et PDF différé à la fin du Livre II.

### Risque 15 — renvoi ambigu au chapitre 28

**Correction :** précision de la frontière entre rapport d’import au chapitre 7, tests automatisés au chapitre 27 et journalisation/reproductibilité globale au chapitre 28.

### Risque 16 — seconde Resource décrite sans contenu vérifiable

**Correction :** ajout du contenu `.tres` attendu, de son explication et de la liste complète `BeaconCatalogPaths.PATHS`.

### Risque 17 — scène de vérification non expliquée

**Correction :** ajout des protections `null` et d’une décomposition détaillée du chargement des Resources, du JSON, de la configuration et du formatage des sorties.

### Risque 18 — erreurs fréquentes sans exemples concrets

**Correction :** chaque erreur de la section 35 possède maintenant un exemple fautif, un exemple corrigé et une explication de la différence.

### Risque 19 — exemples corrigés incompatibles avec les contrats déjà définis

**Correction :** seconde relecture des noms publics : utilisation de `cooldown_remaining`, `tick()`, `record_activation()`, du constructeur `BeaconRuntimeState.new(profile)`, de `BeaconJsonMapper.from_dictionary()` sur une instance et de `BeaconCatalog.register()`.

### Risque 20 — code inline interprété comme lien Markdown

**Correction :** le validateur de liens ignore désormais les blocs clôturés et les expressions placées entre backticks, par exemple `Array[StringName](...)`.

## 7. Vérification des doublons

La seconde lecture a recherché :

- titres identiques ;
- blocs significatifs identiques ;
- longs paragraphes identiques ;
- répétitions inutiles des explications de `Resource`, JSON et configuration.

Les rappels courts sont conservés lorsqu’ils préviennent une erreur concrète. Les explications intégrales ne sont pas répétées.

Les mesures exactes sont produites par `tools/validate_chapters.py` dans le workflow `Validate Chapters Without PDF`.

## 8. Sources techniques

La vérification repose sur les pages officielles Godot 4.7 relatives à :

- `Resource` et ressources personnalisées ;
- cache et chargement des ressources ;
- `ResourceLoader` ;
- `FileAccess` ;
- `JSON` ;
- `ConfigFile` ;
- système de fichiers `res://` et `user://`.

Aucune source communautaire n’est utilisée pour établir les contrats techniques du chapitre.

## 9. Livrables documentés

- `src/features/beacons/domain/beacon_profile.gd` ;
- `src/features/beacons/domain/beacon_runtime_state.gd` ;
- `src/features/beacons/application/beacon_catalog.gd` ;
- `src/features/beacons/infrastructure/beacon_catalog_loader.gd` ;
- `src/features/beacons/infrastructure/beacon_json_mapper.gd` ;
- `src/features/beacons/infrastructure/beacon_json_importer.gd` ;
- `src/core/data/stable_id.gd` ;
- `src/core/data/json_file_reader.gd` ;
- `src/core/data/dictionary_reader.gd` ;
- `src/core/config/app_config.gd` ;
- `src/core/config/app_config_loader.gd` ;
- `data/beacons/*.tres` ;
- `data/import/beacons.json` ;
- `config/default.cfg` ;
- `scenes/learning/ch07_data_demo.gd`.

## 10. Réserves runtime

Les éléments suivants ne sont pas revendiqués comme exécutés :

- import réel des scripts et ressources dans Godot ;
- sérialisation effective des `.tres` ;
- comportement de duplication sur les ressources du Starter Kit ;
- export d’un JSON brut dans un build ;
- emplacement physique de `user://` sur la station de référence ;
- fusion réelle d’un fichier `user://app.cfg` ;
- chargement en arrière-plan ;
- intégration du catalogue avec `AppBootstrap` ;
- tests d’erreurs et mesures de performance.

Ces réserves seront réduites lors de la matérialisation du Starter Kit et des chapitres de tests.

## 11. Politique PDF

Aucun PDF ne doit être construit pour ce chapitre.

Le workflow léger doit vérifier explicitement l’absence de fichier PDF. La compilation Pandoc/XeLaTeX est réservée à la fin du Livre II ou à une modification directe de la chaîne de publication.

## 12. Critère de clôture

Le chapitre peut être déclaré rédigé, repéré et audité lorsque :

- le fichier est intégré à `contents.txt` ;
- l’index et la roadmap indiquent 7 chapitres sur 30 ;
- le document de continuité désigne le chapitre 8 comme prochaine action ;
- le workflow léger réussit ;
- le workflow PDF n’est pas déclenché ;
- les résultats exacts sont enregistrés dans la PR ou une preuve QA.
