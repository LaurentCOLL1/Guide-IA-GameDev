#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTER = ROOT / "Livre-II/CHAPITRE-07-Donnees-avec-Resources-JSON-et-configurations.md"
AUDIT = ROOT / "Livre-II/QA/AUDIT-CHAPITRE-07.md"
CONTINUITY = ROOT / "CONTINUITE-PROJET.md"


def replace_between(text: str, start: str, end: str, replacement: str) -> str:
    if start not in text:
        raise RuntimeError(f"Ancre de début absente : {start}")
    if end not in text:
        raise RuntimeError(f"Ancre de fin absente : {end}")
    i = text.index(start)
    j = text.index(end, i)
    return text[:i] + replacement.rstrip() + "\n\n" + text[j:]


chapter = CHAPTER.read_text(encoding="utf-8")
chapter = chapter.replace('version: "1.0.0"', 'version: "1.1.0"', 1)

chapter = replace_between(
    chapter,
    "## 33. Rapport de validation",
    "## 34. Exercice guidé",
    '''## 33. Rapport de validation

Un import de données doit pouvoir produire :

- chemin source ;
- version du format ;
- nombre d’entrées lues ;
- nombre d’entrées acceptées ;
- erreurs par index ou identifiant ;
- doublons ;
- avertissements ;
- durée de traitement.

Le renvoi au chapitre 28 est volontaire. Le chapitre 7 se limite à un **rapport d’import local**, destiné à expliquer pourquoi un catalogue a été accepté ou refusé.

Le chapitre 27 ajoutera les tests automatisés et les assertions capables de vérifier ces rapports. Le chapitre 28, intitulé **« Journalisation, diagnostic et reproductibilité »**, généralisera ensuite cette discipline à l’ensemble du projet : niveaux de journal, contexte d’exécution, identifiants de corrélation, graines aléatoires, versions, durées et informations nécessaires pour reproduire une anomalie.

La frontière est donc :

> **[LECTURE] Répartition des responsabilités — Ne pas saisir.**

```text
chapitre 7  : rapport d’import de données
chapitre 27 : vérification automatisée du résultat
chapitre 28 : journalisation et reproductibilité de tout le runtime
```
'''
)

chapter = replace_between(
    chapter,
    "### 34.3 Deuxième balise",
    "### 34.4 Scène de vérification",
    '''### 34.3 Deuxième balise

> **[APP] Godot - Créer :** une ressource `BeaconProfile` nommée `res://data/beacons/beacon_village_west.tres`.

Dans la boîte de dialogue **Create New Resource**, choisir `BeaconProfile`, puis renseigner dans l’Inspector :

- `id` : `beacon.village.west` ;
- `display_name` : `Balise ouest du village` ;
- `activation_radius` : `6.0` ;
- `cooldown_seconds` : `5.0` ;
- tags : `village`, `navigation`.

Godot génère le fichier `.tres`. Son contenu textuel doit être équivalent à l’exemple suivant ; les identifiants internes peuvent différer sans modifier le résultat.

> **[LECTURE] Contenu sérialisé attendu de `res://data/beacons/beacon_village_west.tres` — Ne pas recopier si la ressource a été créée dans Godot.**

```ini
[gd_resource type="Resource" script_class="BeaconProfile" load_steps=2 format=3]

[ext_resource type="Script" path="res://src/features/beacons/domain/beacon_profile.gd" id="1_profile"]

[resource]
script = ExtResource("1_profile")
id = &"beacon.village.west"
display_name = "Balise ouest du village"
activation_radius = 6.0
cooldown_seconds = 5.0
tags = Array[StringName]([&"village", &"navigation"])
```

Explication :

- `[gd_resource ...]` déclare un fichier de ressource texte Godot ;
- `script_class="BeaconProfile"` indique la classe personnalisée ;
- `[ext_resource ...]` référence le script qui définit cette classe ;
- `script = ExtResource("1_profile")` associe le script à l’instance ;
- `&"beacon.village.west"` est un littéral `StringName` stable ;
- `Array[StringName](...)` conserve le type des tags ;
- les valeurs appartiennent à la définition de conception, pas à l’état runtime.

Ajouter ensuite les deux chemins au catalogue.

> **[VSC] Visual Studio Code - Modifier :** `res://data/beacons/catalog_paths.gd`.

```gdscript
class_name BeaconCatalogPaths
extends RefCounted

const PATHS: Array[String] = [
	"res://data/beacons/beacon_training.tres",
	"res://data/beacons/beacon_village_west.tres",
]
```

`PATHS` est un tableau constant de chemins de ressources. L’ordre est explicite et versionné ; le chargeur ne dépend donc pas de l’ordre variable d’un parcours de dossier.
'''
)

chapter = replace_between(
    chapter,
    "### 34.4 Scène de vérification",
    "### 34.5 Résultat attendu",
    '''### 34.4 Scène de vérification

> **[VSC] Visual Studio Code - Créer :** `res://scenes/learning/ch07_data_demo.gd`.

```gdscript
extends Node

func _ready() -> void:
	var loader := BeaconCatalogLoader.new()
	var catalog := loader.load_catalog(BeaconCatalogPaths.PATHS)
	if catalog == null:
		push_error("Le catalogue de balises n’a pas pu être chargé.")
		return

	print("Profils chargés : %d" % catalog.size())
	for id: StringName in catalog.get_ids():
		var profile := catalog.get_profile(id)
		if profile == null:
			push_warning("Profil absent pour l’identifiant : %s" % id)
			continue
		print("%s — %s" % [id, profile.display_name])

	var importer := BeaconJsonImporter.new()
	var imported := importer.import_catalog("res://data/import/beacons.json")
	if imported != null:
		print("Profils JSON valides : %d" % imported.size())

	var config_loader := AppConfigLoader.new()
	var config := config_loader.load_config(
		"res://config/default.cfg",
		"user://app.cfg"
	)
	if config != null:
		print("Validation stricte : %s" % config.strict_data_validation)
```

#### 34.4.1 Déclaration et point d’entrée

- `extends Node` fait du script un nœud pouvant être attaché à une scène ;
- `_ready()` est appelé lorsque le nœud entre dans l’arbre et que ses enfants sont prêts ;
- `-> void` indique que la fonction ne renvoie aucune valeur.

#### 34.4.2 Chargement du catalogue de Resources

- `BeaconCatalogLoader.new()` construit le chargeur ;
- `BeaconCatalogPaths.PATHS` fournit les deux chemins déclarés à la section précédente ;
- `load_catalog()` renvoie un `BeaconCatalog` valide ou `null` en cas d’échec ;
- le test `catalog == null` empêche d’appeler `size()` sur une référence absente ;
- `push_error()` consigne la cause dans le débogueur ;
- `return` arrête `_ready()` puisque les vérifications suivantes dépendent du catalogue.

#### 34.4.3 Affichage des profils

- `catalog.size()` renvoie le nombre de profils acceptés ;
- `%d` réserve un emplacement pour un entier ;
- l’opérateur `%` remplace cet emplacement par la valeur fournie ;
- `catalog.get_ids()` renvoie les identifiants triés ;
- `id: StringName` type la variable locale de boucle ;
- `get_profile(id)` récupère le profil associé à la clé courante ;
- `continue` passe à l’identifiant suivant lorsqu’un profil manque ;
- `"%s — %s"` contient deux emplacements textuels ;
- `[id, profile.display_name]` fournit les deux valeurs dans le même ordre.

#### 34.4.4 Vérification du JSON

- `BeaconJsonImporter.new()` crée l’importeur ;
- `import_catalog(path)` lit, analyse, valide et convertit le document ;
- le chemin appartient à `res://`, donc au projet versionné ;
- `imported != null` distingue un catalogue valide d’un import refusé ;
- le nombre affiché correspond uniquement aux profils ayant franchi toutes les validations.

#### 34.4.5 Chargement de la configuration

- `AppConfigLoader.new()` crée le chargeur de configuration ;
- le premier argument est la configuration par défaut obligatoire ;
- le second est la surcharge locale facultative ;
- les parenthèses réparties sur plusieurs lignes ne changent pas l’appel ;
- `config != null` protège l’accès à la propriété ;
- `strict_data_validation` indique si les données invalides doivent bloquer le démarrage.

Cette scène vérifie trois frontières différentes : Resources typées, JSON externe validé et configuration locale fusionnée. Elle n’écrit aucune sauvegarde.
'''
)

chapter = replace_between(
    chapter,
    "## 35. Erreurs fréquentes et corrections",
    "## 36. Checklist de fin de chapitre",
    '''## 35. Erreurs fréquentes et corrections

Chaque erreur ci-dessous comporte un exemple fautif et un exemple corrigé. Les fragments sont volontairement courts afin d’isoler la différence importante.

### 35.1 Modifier une Resource partagée pendant le gameplay

**Symptôme :** plusieurs instances changent en même temps, car elles référencent la même Resource chargée depuis le même chemin.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```gdscript
func update_cooldown(delta: float) -> void:
	profile.cooldown_seconds -= delta
```

Le code modifie la définition de conception `profile`. Toute autre balise utilisant cette même instance voit aussi la nouvelle valeur.

**Correction :** conserver la durée configurée dans `BeaconProfile` et l’évolution courante dans `BeaconRuntimeState`.

> **[VSC] Visual Studio Code - Exemple corrigé à adapter dans le composant runtime.**

```gdscript
func update_cooldown(delta: float) -> void:
	runtime_state.remaining_cooldown = maxf(
		runtime_state.remaining_cooldown - delta,
		0.0
	)
```

`delta` représente le temps écoulé. `maxf(..., 0.0)` empêche une durée négative. La Resource reste inchangée.

### 35.2 Utiliser le nom affiché comme identifiant

**Symptôme :** une traduction ou une correction éditoriale casse les références.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```gdscript
profile.id = StringName(profile.display_name)
```

Après traduction, `Balise ouest du village` pourrait devenir `West village beacon`, ce qui changerait la clé.

**Correction :** utiliser une clé technique stable et conserver le texte visible séparément.

> **[VSC] Visual Studio Code - Exemple corrigé dans une Resource de conception.**

```gdscript
profile.id = &"beacon.village.west"
profile.display_name = "Balise ouest du village"
```

L’identifiant sert aux relations métier ; `display_name` peut être traduit sans modifier ces relations.

### 35.3 Accepter tout JSON syntaxiquement valide

**Symptôme :** le parseur accepte le document, puis le gameplay échoue sur un champ absent ou du mauvais type.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```gdscript
var data = JSON.parse_string(text)
var radius: float = data["activation_radius"]
```

Un JSON peut être syntaxiquement valide tout en ayant une racine tableau, un champ absent ou une chaîne à la place d’un nombre.

**Correction :** vérifier successivement la racine, les champs, leurs types et les règles métier.

> **[VSC] Visual Studio Code - Exemple corrigé à la frontière JSON.**

```gdscript
var data = JSON.parse_string(text)
if not data is Dictionary:
	push_error("La racine JSON doit être un objet.")
	return null

var row: Dictionary = data
if not row.has("activation_radius"):
	push_error("Champ activation_radius absent.")
	return null

var raw_radius: Variant = row["activation_radius"]
if not raw_radius is float and not raw_radius is int:
	push_error("activation_radius doit être numérique.")
	return null

var radius := float(raw_radius)
if radius < 0.0:
	push_error("activation_radius ne peut pas être négatif.")
	return null
```

Chaque contrôle produit une erreur proche de sa cause au lieu d’attendre un échec tardif.

### 35.4 Lire un fichier texte avec `ResourceLoader`

**Symptôme :** chargement impossible d’un JSON brut qui n’est pas pris en charge par un chargeur de ressource enregistré.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```gdscript
var document = ResourceLoader.load("res://data/import/beacons.json")
```

`ResourceLoader` charge les formats reconnus comme ressources. Un fichier texte ordinaire doit être lu comme texte.

**Correction :** utiliser `FileAccess`, puis analyser le contenu avec `JSON`.

> **[VSC] Visual Studio Code - Exemple corrigé dans un lecteur JSON.**

```gdscript
var file := FileAccess.open(
	"res://data/import/beacons.json",
	FileAccess.READ
)
if file == null:
	push_error("Impossible d’ouvrir le document JSON.")
	return null

var parser := JSON.new()
var error := parser.parse(file.get_as_text())
if error != OK:
	push_error(parser.get_error_message())
	return null

var document: Variant = parser.data
```

`FileAccess.READ` ouvre le fichier en lecture. `parser.data` n’est utilisé qu’après un retour `OK`.

### 35.5 Enregistrer l’état du joueur dans une `.tres` de conception

**Symptôme :** les données sources sont modifiées dans l’éditeur ou l’écriture échoue dans un export où `res://` est en lecture seule.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```gdscript
profile.is_active = true
ResourceSaver.save(profile, "res://data/beacons/beacon_training.tres")
```

La définition versionnée est utilisée comme sauvegarde et reçoit en plus une propriété runtime qui ne lui appartient pas.

**Correction :** conserver l’état vivant dans un objet runtime et transmettre plus tard un instantané au système de sauvegarde du chapitre 9.

> **[VSC] Visual Studio Code - Exemple corrigé pour le chapitre 7.**

```gdscript
var runtime_state := BeaconRuntimeState.new()
runtime_state.is_active = true
runtime_state.remaining_cooldown = profile.cooldown_seconds
```

Ce chapitre ne persiste pas encore cet objet. Le chapitre 9 créera un format versionné sous `user://` et une procédure de migration.

### 35.6 Mettre un secret dans `default.cfg`

**Symptôme :** le secret apparaît dans Git, dans les archives et éventuellement dans le paquet exporté.

> **[LECTURE] Exemple fautif — Ne pas recopier et ne jamais utiliser de valeur réelle.**

```ini
[remote_service]
api_token="secret-reel-a-ne-jamais-committer"
```

**Correction :** ne versionner que les options non sensibles et recevoir le secret depuis un mécanisme externe autorisé.

> **[VSC] Visual Studio Code - Exemple corrigé de configuration versionnée.**

```ini
[remote_service]
enabled=false
base_url="https://example.invalid"
```

> **[VSC] Visual Studio Code - Exemple de lecture runtime à traiter avec la politique de sécurité des chapitres 11 à 13.**

```gdscript
var api_token := OS.get_environment("ASTERIA_API_TOKEN")
if api_token.is_empty():
	push_warning("ASTERIA_API_TOKEN n’est pas défini.")
```

Cet exemple ne constitue pas à lui seul un gestionnaire de secrets. Il montre seulement que la valeur ne doit pas être écrite dans le dépôt.

### 35.7 Parcourir un dossier sans trier ni valider

**Symptôme :** l’ordre varie selon le système ou l’historique du dossier, ce qui rend les résultats difficiles à reproduire.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```gdscript
for file_name in DirAccess.get_files_at("res://data/beacons"):
	catalog.add_profile(load("res://data/beacons/" + file_name))
```

Le code ne trie pas, ne filtre pas l’extension, ne vérifie ni le type ni le résultat de `load()`.

**Correction :** utiliser une liste explicite ou construire une liste filtrée, triée et validée.

> **[VSC] Visual Studio Code - Exemple corrigé pour un parcours déterministe.**

```gdscript
var paths: Array[String] = []
for file_name: String in DirAccess.get_files_at("res://data/beacons"):
	if file_name.get_extension() == "tres":
		paths.append("res://data/beacons/" + file_name)
paths.sort()

for path: String in paths:
	var profile := load(path) as BeaconProfile
	if profile == null:
		push_error("Resource BeaconProfile invalide : %s" % path)
		continue
	catalog.add_profile(profile)
```

Le chapitre privilégie malgré tout `BeaconCatalogPaths.PATHS` tant que la collection reste petite, car cette liste rend les changements explicites dans Git.

### 35.8 Propager des dictionnaires partout

**Symptôme :** les consommateurs répètent des clés magiques et découvrent les erreurs trop tard.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```gdscript
func activate_beacon(data: Dictionary) -> void:
	print(data["display_name"])
	start_cooldown(float(data["cooldown_seconds"]))
```

Chaque appelant doit connaître l’orthographe des clés et les conversions attendues.

**Correction :** convertir le dictionnaire à la frontière puis transmettre un objet typé.

> **[VSC] Visual Studio Code - Exemple corrigé dans le mapper puis le service.**

```gdscript
var profile := BeaconJsonMapper.to_profile(data)
if profile == null:
	return

catalog.add_profile(profile)
activation_service.configure(event_bus, catalog)
```

`BeaconJsonMapper` concentre les clés et validations. `BeaconCatalog` et `BeaconProfile` fournissent ensuite des méthodes et propriétés connues par le moteur et l’éditeur.
'''
)

CHAPTER.write_text(chapter, encoding="utf-8")

audit = AUDIT.read_text(encoding="utf-8")
audit = audit.replace('version: "1.0.0"', 'version: "1.1.0"', 1)
audit = audit.replace(
    "### Risque 14 — construire le PDF après le chapitre\n\n**Correction :** validation légère obligatoire et PDF différé à la fin du Livre II.",
    """### Risque 14 — construire le PDF après le chapitre

**Correction :** validation légère obligatoire et PDF différé à la fin du Livre II.

### Risque 15 — renvoi ambigu au chapitre 28

**Correction :** précision de la frontière entre rapport d’import au chapitre 7, tests automatisés au chapitre 27 et journalisation/reproductibilité globale au chapitre 28.

### Risque 16 — seconde Resource décrite sans contenu vérifiable

**Correction :** ajout du contenu `.tres` attendu, de son explication et de la liste complète `BeaconCatalogPaths.PATHS`.

### Risque 17 — scène de vérification non expliquée

**Correction :** ajout des protections `null` et d’une décomposition détaillée du chargement des Resources, du JSON, de la configuration et du formatage des sorties.

### Risque 18 — erreurs fréquentes sans exemples concrets

**Correction :** chaque erreur de la section 35 possède maintenant un exemple fautif, un exemple corrigé et une explication de la différence."""
)
audit = audit.replace(
    "Les exemples sont accompagnés d’un contexte `[VSC]`, `[APP]`, `[LECTURE]` ou `[SORTIE]`.",
    "Les exemples sont accompagnés d’un contexte `[VSC]`, `[APP]`, `[LECTURE]` ou `[SORTIE]`. La seconde Resource, la scène de vérification et les huit erreurs fréquentes disposent désormais d’exemples détaillés et comparables."
)
AUDIT.write_text(audit, encoding="utf-8")

continuity = CONTINUITY.read_text(encoding="utf-8")
continuity = continuity.replace('version: "3.5.0"', 'version: "3.6.0"', 1)
continuity = continuity.replace(
    "Les rappels courts sont permis. Les duplications intégrales sont interdites.",
    "Les rappels courts sont permis. Les duplications intégrales sont interdites. Toute section intitulée « Erreurs fréquentes et corrections » doit fournir, pour chaque erreur, au moins un exemple fautif, un exemple corrigé et l’explication de la différence."
)
continuity = continuity.replace(
    "## 17. Journal\n\n### 2026-07-19 — version 3.5.0",
    """## 17. Journal

### 2026-07-19 — version 3.6.0

- réaudit pédagogique du chapitre 7 après retour utilisateur ;
- clarification du renvoi vers les chapitres 27 et 28 ;
- ajout du code complet de la seconde balise ;
- explication ligne par ligne de la scène de vérification ;
- obligation d’un exemple fautif et corrigé pour chaque erreur fréquente ;
- chapitre 7 porté en version `1.1.0`.

### 2026-07-19 — version 3.5.0"""
)
CONTINUITY.write_text(continuity, encoding="utf-8")

print("Chapitre 7, audit et continuité corrigés.")
