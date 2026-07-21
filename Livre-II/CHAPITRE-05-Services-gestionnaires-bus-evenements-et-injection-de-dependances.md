---
title: "Livre II — Chapitre 5 : Services, gestionnaires, bus d’événements et injection de dépendances"
id: "DOC-L2-CH05"
status: "reviewed"
version: "1.1.0"
lang: "fr-FR"
book: "Livre II"
chapter: 5
last-verified: "2026-07-19"
audit-status: "complete"
audit-date: "2026-07-19"
audit-report: "Livre-II/QA/AUDIT-CHAPITRE-05.md"
supplemental-audit: "Livre-II/QA/AUDIT-RETROACTIF-EXEMPLES-ERREURS-CH01-CH06.md"
audit-level: "static-review"
reference-engine:
  name: "Godot Engine"
  version: "4.7.1-stable"
  edition: "Standard"
  language: "GDScript"
reference-project:
  name: "Project Asteria"
  renderer: "Forward+"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Services, gestionnaires, bus d’événements et injection de dépendances

> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir, **[LECTURE]** exemple à étudier. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L2-CH05`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Version de référence :** Godot `4.7.1-stable`, édition Standard, GDScript, Forward+  
> **Niveau de raisonnement conseillé pour produire ou réviser ce chapitre :** GPT-5.6 Sol — Élevée  
> **Audit post-création :** terminé au niveau `static-review` — voir `Livre-II/QA/AUDIT-CHAPITRE-05.md`.

## 1. Rôle du chapitre

Le chapitre 4 a défini **où** vivent les responsabilités de `Project Asteria` et dans quelle direction les modules peuvent dépendre les uns des autres.

Ce chapitre explique maintenant **comment les objets concrets sont créés, démarrés, reliés, utilisés et arrêtés à l’exécution**.

Sans règle explicite, un projet Godot grandissant dérive souvent vers :

- des Autoloads accessibles depuis tous les scripts ;
- des classes nommées `Manager` sans responsabilité précise ;
- des appels globaux impossibles à remplacer dans un test ;
- des services initialisés dans un ordre implicite ;
- des signaux globaux dont personne ne connaît les émetteurs ;
- des dépendances circulaires ;
- un état persistant entre deux scènes de test ;
- des erreurs de démarrage découvertes tardivement.

À la fin du chapitre, le lecteur doit savoir :

- distinguer service, gestionnaire, système, contrôleur et repository ;
- choisir entre `Node`, `RefCounted`, `Resource` et Autoload ;
- construire une dépendance plutôt que la rechercher globalement ;
- injecter une dépendance par constructeur, méthode de configuration ou propriété exportée ;
- utiliser un registre de services minimal sans le transformer en localisateur universel ;
- définir un bus d’événements limité et typé ;
- organiser le démarrage et l’arrêt dans un ordre déterministe ;
- diagnostiquer une dépendance absente ou un double enregistrement ;
- préparer des remplacements de test sans traiter encore toute la stratégie du chapitre 27 ;
- adapter l’approche aux parcours Solo et Studio.

## 2. Prérequis

Le lecteur doit avoir terminé :

- le chapitre 2 pour les classes, fonctions, paramètres, types et dictionnaires ;
- le chapitre 3 pour les scènes, signaux, `Callable`, `Node` et `Resource` ;
- le chapitre 4 pour l’architecture feature-first, les couches, les contrats et `src/app`.

Le chapitre réutilise les décisions suivantes sans les redéfinir :

- `src/app` est le point de composition ;
- `core` ne dépend d’aucune fonctionnalité ;
- les modules fonctionnels ne connaissent pas les détails internes les uns des autres ;
- la présentation communique par interfaces publiques, signaux ou services injectés.

## 3. Périmètre et frontières

Ce chapitre définit :

- le vocabulaire des composants transversaux ;
- les critères de choix d’un Autoload ;
- un registre de services minimal ;
- un bus d’événements typé ;
- trois formes d’injection de dépendances ;
- un cycle de vie `configure → start → use → stop` ;
- le bootstrap de l’application ;
- un exercice de démonstration autour du module `beacons`.

Il ne définit pas encore :

- les entrées joueur, contrôleurs et caméras du chapitre 6 ;
- les formats de données et catalogues du chapitre 7 ;
- les repositories SQLite du chapitre 8 ;
- les sauvegardes du chapitre 9 ;
- le réseau et les services IA des chapitres 11 à 13 ;
- la campagne complète de tests automatisés du chapitre 27 ;
- l’observabilité structurée du chapitre 28.

> **Frontière essentielle :** un service orchestre une capacité ; il ne doit pas devenir un conteneur arbitraire pour tout le projet.

## 4. Vocabulaire : ne pas appeler tout « Manager »

### 4.1 Service

Un **service** fournit une capacité identifiable à d’autres objets.

Exemples futurs :

- calculer une activation de balise ;
- charger une sauvegarde ;
- envoyer une requête à une IA locale ;
- résoudre une transaction économique ;
- fournir l’heure simulée du monde.

Un service possède idéalement :

- un nom précis ;
- une interface publique courte ;
- des dépendances déclarées ;
- peu ou pas d’état mutable caché ;
- un cycle de vie documenté ;
- une stratégie d’erreur.

### 4.2 Gestionnaire ou manager

Le mot **gestionnaire** décrit un objet qui coordonne un ensemble d’éléments similaires pendant leur durée de vie.

Exemples acceptables :

- `SceneTransitionManager` coordonne des transitions de scènes ;
- `AudioVoiceManager` coordonne des voix simultanées ;
- `ChunkStreamingManager` charge et décharge des zones.

Le nom `GameManager` est trop vague. Il ne révèle ni la donnée contrôlée, ni la frontière, ni le cycle de vie.

### 4.3 Système

Un **système** applique des règles à un ensemble d’entités ou de données.

Exemples :

- système de combat ;
- système d’économie ;
- système de relations sociales.

Dans le Livre II, les grands systèmes de gameplay commencent au chapitre 14. Le présent chapitre ne les implémente pas ; il prépare leur assemblage.

### 4.4 Contrôleur

Un **contrôleur** traduit une intention ou une entrée en action d’application.

Exemples :

- `PlayerController` traduit les actions d’entrée en commandes de déplacement ;
- `CameraController` transforme une intention de visée en rotation ;
- `MenuController` orchestre les actions d’une interface.

Les contrôleurs détaillés appartiennent au chapitre 6.

### 4.5 Repository

Un **repository** fournit un contrat d’accès à des données persistantes ou externes.

Il masque par exemple :

- un fichier JSON ;
- SQLite ;
- une API locale ;
- un cache.

Le service dépend du contrat du repository, pas directement de SQLite. L’implémentation concrète arrive aux chapitres 7 et 8.

### 4.6 Tableau de décision

| Besoin | Nom conseillé | Exemple |
|---|---|---|
| capacité réutilisable | service | `BeaconActivationService` |
| collection d’objets vivants | manager | `VoicePlaybackManager` |
| règles sur plusieurs entités | système | `CombatSystem` |
| traduction d’une intention | controller | `PlayerController` |
| accès aux données | repository | `SaveRepository` |
| communication ponctuelle locale | signal direct | `StatusBeacon.activated` |
| événement transversal rare | bus typé | `GameEventBus` |

## 5. Choisir le bon type Godot

### 5.1 Utiliser `RefCounted` pour une logique sans présence dans l’arbre

Un service n’a pas besoin d’être un `Node` lorsqu’il :

- n’utilise pas `_process()` ou `_physics_process()` ;
- ne dépend pas de l’arbre de scènes ;
- n’a pas besoin d’être visible dans le Remote SceneTree ;
- ne reçoit pas de notifications de nœud ;
- peut être créé et détruit comme un objet logique.

`RefCounted` est alors un bon choix. Ses instances sont libérées automatiquement lorsque plus aucune référence ne les conserve.

### 5.2 Utiliser `Node` pour une présence runtime explicite

Un service peut être un `Node` lorsqu’il :

- doit recevoir `_process()` ;
- doit posséder des enfants ;
- doit écouter des notifications de l’arbre ;
- doit survivre à un changement de scène via un Autoload ;
- doit être inspectable dans l’arbre distant.

Un `Node` possède un propriétaire de durée de vie : son parent, une scène principale ou un Autoload.

### 5.3 Utiliser `Resource` pour des données, pas comme service global mutable

Une `Resource` convient à :

- une configuration ;
- un profil ;
- un catalogue de conception ;
- un contrat de données sérialisable.

Elle ne doit pas devenir, par facilité, un service mutable partagé entre toutes les scènes. Les Resources chargées par chemin peuvent être mises en cache et partagées ; une mutation inattendue peut donc affecter plusieurs consommateurs.

### 5.4 Utiliser un Autoload avec parcimonie

Un Autoload est chargé avant les scènes ordinaires et reste disponible pendant l’exécution. Godot précise qu’il se comporte comme un singleton, sans être un singleton strict : le même script peut toujours être instancié ailleurs.

Un Autoload est justifié lorsqu’un objet :

1. doit exister pendant toute la session ;
2. doit survivre aux changements de scène ;
3. possède un cycle de vie global clair ;
4. ne peut pas être simplement fourni par une scène parente ;
5. reste testable derrière un contrat ou un point de composition.

Un Autoload n’est pas justifié uniquement parce qu’écrire `Global.service` semble plus court.

## 6. Les trois formes d’injection de dépendances

L’**injection de dépendances** signifie qu’un objet reçoit ce dont il a besoin depuis l’extérieur, au lieu d’aller le chercher lui-même dans une variable globale ou dans un chemin arbitraire.

### 6.1 Injection par constructeur

Elle convient particulièrement aux objets `RefCounted`.

> **[VSC] Visual Studio Code — Créer : `src/features/beacons/application/beacon_activation_service.gd`.**

```gdscript
class_name BeaconActivationService
extends RefCounted

var _events: GameEventBus

func _init(events: GameEventBus) -> void:
	if events == null:
		push_error("BeaconActivationService exige un GameEventBus.")
	_events = events
```

Décomposition :

- `class_name BeaconActivationService` rend le type disponible dans le projet ;
- `extends RefCounted` crée un objet logique sans l’ajouter à l’arbre de scènes ;
- `_events` est une variable membre privée par convention ;
- son type `GameEventBus` exprime la dépendance attendue ;
- `_init()` est le constructeur GDScript ;
- `events` est le paramètre reçu lors de `BeaconActivationService.new(events)` ;
- `-> void` indique que le constructeur ne renvoie pas de valeur ;
- `events == null` détecte l’absence de dépendance ;
- `push_error()` affiche une erreur dans le débogueur ;
- `_events = events` conserve la référence pour les futurs appels.

La dépendance est visible dans la signature. Un lecteur ne peut pas créer correctement le service sans fournir le bus.

### 6.2 Injection par méthode de configuration

Elle convient à un `Node` déjà instancié par une scène.

> **[VSC] Visual Studio Code — Exemple à adapter dans un script de nœud.**

```gdscript
var _activation_service: BeaconActivationService

func configure(activation_service: BeaconActivationService) -> void:
	if activation_service == null:
		push_error("Le service d’activation est obligatoire.")
		return
	_activation_service = activation_service
```

Décomposition :

- `configure()` constitue une étape explicite avant l’utilisation du nœud ;
- `activation_service` est le paramètre injecté ;
- `return` interrompt la fonction lorsqu’il manque ;
- `_activation_service` conserve la dépendance ;
- le nœud peut être instancié par Godot, puis configuré par le bootstrap.

Une méthode `configure()` doit préciser si elle peut être appelée plusieurs fois. Dans ce guide, elle ne doit être appelée qu’une fois sauf mention contraire.

### 6.3 Injection par propriété exportée

Elle convient surtout à une dépendance de scène ou de configuration choisie dans l’Inspector.

> **[VSC] Visual Studio Code — Exemple de propriété exportée dans un nœud de présentation.**

```gdscript
@export var beacon_profile: BeaconProfile
```

Cette forme permet à l’éditeur d’affecter une `Resource`. Elle ne convient pas à un service runtime construit dynamiquement, car l’Inspector ne doit pas sérialiser une instance de service temporaire.

### 6.4 Mauvais exemple : recherche globale cachée

> **[LECTURE] Anti-pattern GDScript — Ne pas recopier.**

```gdscript
func activate_beacon() -> void:
	GlobalServices.beacon_activation.activate()
```

Le script ne déclare aucune dépendance. Il suppose :

- qu’un Autoload nommé `GlobalServices` existe ;
- qu’il est déjà initialisé ;
- qu’il contient une propriété précise ;
- que le test dispose du même état global.

La dépendance cachée rend la scène difficile à réutiliser et à tester.

## 7. Créer un bus d’événements limité et typé

### 7.1 Rôle

Un bus d’événements transmet quelques événements transversaux entre modules qui ne doivent pas se connaître directement.

Il ne remplace pas :

- un appel de fonction local ;
- un signal entre un enfant et son parent ;
- un service d’application ;
- une file réseau ;
- une base de données.

### 7.2 Événement, commande et état

- un **événement** décrit quelque chose qui s’est produit : `beacon_activated` ;
- une **commande** demande une action : `beacon_activation_requested` ;
- un **état** décrit une situation durable : `is_online`.

Un événement est généralement nommé au passé. Un bus ne doit pas devenir une collection de propriétés globales.

### 7.3 Implémentation du bus

> **[VSC] Visual Studio Code — Créer : `src/core/events/game_event_bus.gd`.**

```gdscript
class_name GameEventBus
extends Node

signal beacon_activation_requested(beacon_id: StringName)
signal beacon_activated(beacon_id: StringName)
signal service_failed(service_id: StringName, message: String)
```

Décomposition :

- `GameEventBus` hérite de `Node` afin d’avoir une durée de vie visible dans l’arbre ;
- `signal` déclare un canal typé ;
- `beacon_id` est l’identifiant transmis aux abonnés ;
- `StringName` convient aux identifiants répétés et stables ;
- `service_failed` transporte l’identifiant du service et un message lisible ;
- aucun signal générique `event(name, data)` n’est utilisé.

Un bus générique à base de chaînes et de dictionnaires perd l’autocomplétion, les types et la traçabilité.

### 7.4 Émettre un événement

> **[VSC] Visual Studio Code — Ajouter à `beacon_activation_service.gd`.**

```gdscript
func request_activation(beacon_id: StringName) -> bool:
	if beacon_id.is_empty():
		push_warning("L’identifiant de balise est vide.")
		return false

	_events.beacon_activation_requested.emit(beacon_id)
	return true
```

Décomposition :

- `request_activation()` exprime une intention d’application ;
- `beacon_id` est le paramètre obligatoire ;
- `-> bool` annonce un résultat de succès ou d’échec ;
- `is_empty()` vérifie l’identifiant ;
- `return false` indique que la demande a été refusée ;
- `_events.beacon_activation_requested` désigne le signal ;
- `.emit(beacon_id)` déclenche tous les `Callable` connectés ;
- `return true` signifie que la demande a été publiée.

Le retour `true` ne prouve pas que la balise a été activée. Il prouve uniquement que la demande valide a été émise.

### 7.5 Écouter sans double connexion

> **[VSC] Visual Studio Code — Exemple dans un nœud de démonstration.**

```gdscript
var activation_callback := Callable(self, "_on_beacon_activation_requested")

func _ready() -> void:
	if not _events.beacon_activation_requested.is_connected(activation_callback):
		_events.beacon_activation_requested.connect(activation_callback)

func _exit_tree() -> void:
	if _events != null and _events.beacon_activation_requested.is_connected(activation_callback):
		_events.beacon_activation_requested.disconnect(activation_callback)
```

Décomposition :

- `Callable(self, "...")` désigne la méthode à appeler sur l’objet courant ;
- `is_connected()` empêche une seconde connexion identique ;
- `connect()` enregistre l’abonné ;
- `_exit_tree()` nettoie la connexion avant la disparition du nœud ;
- le test `_events != null` évite d’utiliser une dépendance absente ;
- `disconnect()` retire la connexion existante.

Godot refuse normalement une seconde connexion du même signal au même `Callable`. La vérification explicite rend le cycle de vie plus lisible et évite une erreur.

### 7.6 Quand préférer un signal direct

Utiliser un signal direct lorsque :

- l’émetteur et le récepteur appartiennent à la même scène ;
- le parent crée l’enfant ;
- l’événement ne concerne qu’une fonctionnalité ;
- le chemin de communication est simple à suivre.

Utiliser le bus lorsque :

- plusieurs modules indépendants doivent observer le même événement ;
- l’émetteur ne doit pas connaître les consommateurs ;
- l’événement traverse une frontière d’architecture ;
- la liste des événements reste courte et documentée.

## 8. Construire un registre de services minimal

### 8.1 Rôle

Le registre conserve les instances créées par le point de composition. Il permet :

- de détecter un doublon ;
- de retrouver un service lors du bootstrap ;
- de centraliser l’arrêt ;
- d’afficher un diagnostic.

Il ne doit pas être injecté partout. Sinon il devient un **Service Locator**, c’est-à-dire une nouvelle forme de dépendance globale cachée.

### 8.2 Implémentation

> **[VSC] Visual Studio Code — Créer : `src/core/services/service_registry.gd`.**

```gdscript
class_name ServiceRegistry
extends RefCounted

var _services: Dictionary[StringName, Object] = {}

func register_service(service_id: StringName, service: Object) -> bool:
	if service_id.is_empty():
		push_error("Un identifiant de service ne peut pas être vide.")
		return false

	if service == null:
		push_error("Le service '%s' est null." % service_id)
		return false

	if _services.has(service_id):
		push_error("Le service '%s' est déjà enregistré." % service_id)
		return false

	_services[service_id] = service
	return true

func has_service(service_id: StringName) -> bool:
	return _services.has(service_id)

func require_service(service_id: StringName) -> Object:
	if not _services.has(service_id):
		push_error("Service obligatoire introuvable : %s" % service_id)
		return null
	return _services[service_id]

func unregister_service(service_id: StringName) -> bool:
	return _services.erase(service_id)

func clear() -> void:
	_services.clear()
```

### 8.3 Explication détaillée

`Dictionary[StringName, Object]` signifie :

- les clés sont des `StringName` ;
- les valeurs sont des objets Godot ;
- le registre peut contenir un `Node` ou un `RefCounted` ;
- la vérification du type concret reste effectuée lors de la récupération.

Dans `register_service()` :

- `service_id` est le nom stable du service ;
- `service` est l’instance à conserver ;
- `_services.has(service_id)` détecte une clé déjà présente ;
- `_services[service_id] = service` associe la clé à l’instance ;
- la fonction renvoie `true` uniquement après l’enregistrement.

Dans `require_service()` :

- le verbe `require` indique que l’absence est une erreur de configuration ;
- le type de retour reste `Object`, car GDScript ne permet pas de rendre un dictionnaire générique différent pour chaque clé ;
- l’appelant doit vérifier ou convertir le type reçu.

Dans `unregister_service()` :

- `erase()` supprime la clé ;
- il renvoie `true` si la clé existait ;
- retirer une référence du registre ne libère pas immédiatement un service encore référencé ailleurs.

### 8.4 Récupération typée au point de composition

> **[VSC] Visual Studio Code — Exemple limité au bootstrap.**

```gdscript
var raw_service: Object = registry.require_service(&"beacon_activation")
var activation_service := raw_service as BeaconActivationService

if activation_service == null:
	push_error("Le service beacon_activation possède un type inattendu.")
	return
```

Décomposition :

- `&"beacon_activation"` crée un littéral `StringName` ;
- `raw_service` reçoit le type général `Object` ;
- `as BeaconActivationService` tente un cast ;
- le résultat vaut `null` si l’objet n’est pas compatible ;
- le contrôle protège le bootstrap contre un mauvais enregistrement.

Le code métier ne doit pas répéter cette recherche. Le bootstrap récupère l’instance une fois, puis l’injecte directement.

## 9. Définir le cycle de vie des services

### 9.1 États recommandés

> **[LECTURE] Machine d’états conceptuelle — Ne pas saisir.**

```text
CREATED → CONFIGURED → STARTED → STOPPED
                └────→ FAILED
```

- `CREATED` : l’objet existe ;
- `CONFIGURED` : ses dépendances obligatoires sont fournies ;
- `STARTED` : il peut recevoir des demandes ;
- `FAILED` : le démarrage a échoué ;
- `STOPPED` : ses ressources ont été relâchées.

Tous les petits services n’ont pas besoin d’une énumération formelle. Le cycle doit néanmoins être clair.

### 9.2 Contrat de cycle de vie

> **[VSC] Visual Studio Code — Créer : `src/core/services/service_lifecycle.gd`.**

```gdscript
class_name ServiceLifecycle
extends RefCounted

func start() -> Error:
	return OK

func stop() -> void:
	pass
```

Cette classe fournit un contrat minimal :

- `start()` renvoie un `Error` Godot ;
- `OK` représente un démarrage réussi ;
- une autre valeur comme `ERR_UNCONFIGURED` signale un échec ;
- `stop()` ne renvoie rien ;
- `pass` indique une implémentation vide à remplacer.

GDScript n’offre pas d’interfaces multiples comme certains langages. Une classe qui hérite déjà d’un autre type ne pourra pas hériter aussi de `ServiceLifecycle`. Dans ce cas, documenter les mêmes signatures ou utiliser une vérification de méthodes au point de composition.

### 9.3 Ordre de démarrage et d’arrêt

Les services doivent démarrer dans l’ordre de leurs dépendances :

1. bus d’événements ;
2. services fondamentaux ;
3. services d’application ;
4. présentation.

L’arrêt suit l’ordre inverse :

1. présentation ;
2. services d’application ;
3. services fondamentaux ;
4. bus d’événements.

Cette symétrie évite qu’un service tente d’émettre un événement après la destruction du bus.

## 10. Construire le point de composition

### 10.1 Responsabilité de `AppBootstrap`

`AppBootstrap` est le seul endroit autorisé à :

- créer les implémentations concrètes ;
- enregistrer les services ;
- relier les événements transversaux ;
- injecter les dépendances ;
- démarrer et arrêter l’application.

### 10.2 Implémentation minimale

> **[VSC] Visual Studio Code — Créer : `src/app/app_bootstrap.gd`.**

```gdscript
class_name AppBootstrap
extends Node

const EVENT_BUS_ID: StringName = &"event_bus"
const BEACON_ACTIVATION_ID: StringName = &"beacon_activation"

var _registry := ServiceRegistry.new()
var _events: GameEventBus
var _beacon_activation: BeaconActivationService
var _started := false

func _ready() -> void:
	var error := start_application()
	if error != OK:
		push_error("Échec du démarrage de Project Asteria : %s" % error_string(error))

func start_application() -> Error:
	if _started:
		return ERR_ALREADY_IN_USE

	_events = GameEventBus.new()
	_events.name = "GameEventBus"
	add_child(_events)

	if not _registry.register_service(EVENT_BUS_ID, _events):
		_events.queue_free()
		_events = null
		return ERR_ALREADY_EXISTS

	_beacon_activation = BeaconActivationService.new(_events)
	if not _registry.register_service(BEACON_ACTIVATION_ID, _beacon_activation):
		_registry.unregister_service(EVENT_BUS_ID)
		_beacon_activation = null
		_events.queue_free()
		_events = null
		return ERR_ALREADY_EXISTS

	_started = true
	return OK

func stop_application() -> void:
	if not _started:
		return

	_registry.unregister_service(BEACON_ACTIVATION_ID)
	_beacon_activation = null

	_registry.unregister_service(EVENT_BUS_ID)
	if is_instance_valid(_events):
		_events.queue_free()
	_events = null

	_registry.clear()
	_started = false

func _exit_tree() -> void:
	stop_application()

func get_beacon_activation_service() -> BeaconActivationService:
	return _beacon_activation
```

### 10.3 Explication des constantes

- `EVENT_BUS_ID` et `BEACON_ACTIVATION_ID` évitent de répéter des chaînes ;
- `const` empêche leur réaffectation ;
- `StringName` convient aux identifiants stables ;
- `&"..."` crée directement un `StringName`.

### 10.4 Explication de `_ready()`

- Godot appelle `_ready()` lorsque le nœud et ses enfants sont prêts ;
- `start_application()` renvoie un code `Error` ;
- `error != OK` détecte un échec ;
- `error_string(error)` produit un message lisible.

### 10.5 Explication de `start_application()`

- `_started` empêche un second démarrage ;
- `ERR_ALREADY_IN_USE` décrit cet état ;
- `GameEventBus.new()` crée le bus ;
- `name` facilite son identification dans le Remote SceneTree ;
- `add_child()` lui donne une durée de vie gérée par `AppBootstrap` ;
- `register_service()` conserve une référence de diagnostic ;
- `BeaconActivationService.new(_events)` injecte le bus par constructeur ;
- les branches d’échec nettoient les objets déjà créés ;
- `_started = true` n’est exécuté qu’après tous les enregistrements.

### 10.6 Explication de `stop_application()`

- l’arrêt est idempotent : un second appel ne fait rien ;
- le service d’application est retiré avant le bus dont il dépend ;
- affecter `null` retire la référence locale ;
- `is_instance_valid()` vérifie que le `Node` existe toujours ;
- `queue_free()` programme sa suppression sûre en fin de frame ;
- le registre est vidé ;
- `_started` revient à `false`.

### 10.7 Limite volontaire

`get_beacon_activation_service()` expose temporairement un accès typé pour le chapitre. Dans une architecture plus vaste, `AppBootstrap` injectera le service dans les contrôleurs et scènes qu’il crée. Les scripts de fonctionnalité ne doivent pas parcourir l’arbre pour retrouver `AppBootstrap`.

## 11. Décider si `AppBootstrap` devient un Autoload

### 11.1 Option A — scène principale ordinaire

Utiliser une scène principale ordinaire lorsque :

- le jeu possède un point d’entrée unique ;
- les changements de monde remplacent seulement un enfant de la scène principale ;
- les services peuvent appartenir à cette scène ;
- les scènes de test peuvent créer leur propre bootstrap.

Cette option facilite l’isolation.

### 11.2 Option B — Autoload

Utiliser un Autoload lorsque :

- le bootstrap doit survivre à `change_scene_to_file()` ;
- plusieurs scènes autonomes doivent partager la même session ;
- le cycle global est réellement nécessaire ;
- les tests savent remplacer ou désactiver ce comportement.

### 11.3 Ajouter l’Autoload dans Godot

> **[APP] Godot — Ouvrir `Project > Project Settings > Globals > Autoload`.**

1. sélectionner `res://src/app/app_bootstrap.gd` ;
2. choisir le nom `AppRuntime` afin de ne pas entrer en collision avec la classe globale `AppBootstrap` ;
3. vérifier que l’entrée est activée ;
4. placer le bootstrap avant les Autoloads qui dépendraient de lui ;
5. fermer la fenêtre ;
6. exécuter le projet ;
7. ouvrir le Remote SceneTree et vérifier la présence du nœud.

> **Attention :** ne jamais appeler `queue_free()` sur le nœud Autoload lui-même. Godot avertit que la suppression d’un Autoload à l’exécution n’est pas prise en charge. Le code précédent supprime seulement son enfant `_events`.

### 11.4 Règle de `Project Asteria`

Pour les chapitres 5 à 9 :

- le parcours **Solo** peut utiliser `AppBootstrap` comme scène racine persistante ;
- le parcours **Studio** conserve la capacité de construire un bootstrap isolé pour les tests ;
- le bus et les services concrets ne sont pas des Autoloads individuels ;
- un seul point global est toléré : le composition root.

## 12. Exercice : relier le module `beacons`

### 12.1 Arborescence cible

> **[LECTURE] Arborescence de l’exercice — Créer les fichiers aux étapes indiquées.**

```text
src/
├── app/
│   └── app_bootstrap.gd
├── core/
│   ├── events/
│   │   └── game_event_bus.gd
│   └── services/
│       ├── service_lifecycle.gd
│       └── service_registry.gd
└── features/
    └── beacons/
        ├── application/
        │   └── beacon_activation_service.gd
        ├── domain/
        │   └── beacon_profile.gd
        ├── presentation/
        │   ├── status_beacon.gd
        │   └── status_beacon.tscn
        └── README.md
scenes/
└── learning/
    ├── ch05_services_demo.gd
    └── ch05_services_demo.tscn
```

### 12.2 Créer la scène de démonstration

> **[APP] Godot — Créer `scenes/learning/ch05_services_demo.tscn`.**

Créer :

1. un nœud racine `Node` nommé `Ch05ServicesDemo` ;
2. une instance de `StatusBeacon` nommée `DemoBeacon` ;
3. un `Button` nommé `ActivateButton` ;
4. un `Label` nommé `ResultLabel` ;
5. attacher `ch05_services_demo.gd` au nœud racine.

### 12.3 Script de démonstration

> **[VSC] Visual Studio Code — Créer : `scenes/learning/ch05_services_demo.gd`.**

```gdscript
extends Node

@onready var demo_beacon: StatusBeacon = $DemoBeacon
@onready var activate_button: Button = $ActivateButton
@onready var result_label: Label = $ResultLabel

var _events: GameEventBus
var _activation_service: BeaconActivationService

func configure(
	events: GameEventBus,
	activation_service: BeaconActivationService
) -> void:
	_events = events
	_activation_service = activation_service

func _ready() -> void:
	if _events == null or _activation_service == null:
		result_label.text = "Dépendances absentes"
		push_error("Ch05ServicesDemo doit être configurée avant son utilisation.")
		return

	activate_button.pressed.connect(_on_activate_button_pressed)
	_events.beacon_activation_requested.connect(_on_activation_requested)
	demo_beacon.activated.connect(_on_beacon_activated)

func _on_activate_button_pressed() -> void:
	var accepted := _activation_service.request_activation(&"demo_beacon")
	result_label.text = "Demande publiée" if accepted else "Demande refusée"

func _on_activation_requested(beacon_id: StringName) -> void:
	if beacon_id != &"demo_beacon":
		return
	demo_beacon.activate(&"Chapter05Service")

func _on_beacon_activated(
	beacon_id: StringName,
	message: String,
) -> void:
	_events.beacon_activated.emit(beacon_id)
	result_label.text = message
```

### 12.4 Explication de `configure()`

La signature s’étend sur plusieurs lignes pour rester lisible :

- `events` reçoit le bus ;
- `activation_service` reçoit le service d’application ;
- les deux paramètres sont obligatoires ;
- les affectations conservent les dépendances ;
- la méthode doit être appelée avant l’ajout de la scène au jeu ou avant son utilisation.

### 12.5 Explication de `_ready()`

- les références `@onready` utilisant `$NomDuNœud` sont disponibles ;
- la condition vérifie les deux dépendances ;
- `or` renvoie vrai lorsqu’au moins une dépendance manque ;
- le `Label` rend l’erreur visible ;
- les trois connexions ont des responsabilités différentes :
  - le bouton déclenche l’intention locale ;
  - le bus transmet la demande transversale ;
  - la balise confirme son activation réelle.

### 12.6 Explication du ternaire

> **[LECTURE] Forme générale de l’expression conditionnelle GDScript.**

```gdscript
valeur_si_vrai if condition else valeur_si_faux
```

Dans l’exercice :

- `accepted` est la condition ;
- `"Demande publiée"` est choisie lorsque `accepted == true` ;
- `"Demande refusée"` est choisie sinon ;
- le résultat est affecté à `result_label.text`.

### 12.7 Injecter la scène depuis le bootstrap

> **[VSC] Visual Studio Code — Exemple à ajouter au point de composition lors de l’instanciation de la scène.**

```gdscript
const DEMO_SCENE := preload(
	"res://scenes/learning/ch05_services_demo.tscn"
)

func create_chapter_05_demo() -> Node:
	var demo := DEMO_SCENE.instantiate()
	demo.configure(_events, _beacon_activation)
	return demo
```

Décomposition :

- `preload()` charge la scène avec un chemin constant ;
- `instantiate()` crée une nouvelle instance ;
- `demo.configure(...)` fournit les deux dépendances ;
- la configuration précède l’ajout à l’arbre lorsque l’appelant utilise ensuite `add_child(demo)` ;
- la fonction renvoie le nœud prêt à être ajouté.

## 13. Démarrage dégradé et gestion des erreurs

### 13.1 Service obligatoire

Un service obligatoire bloque le démarrage lorsqu’il manque.

Exemples :

- registre ;
- bus utilisé par les services déjà créés ;
- système de sauvegarde lorsqu’une session ne peut pas fonctionner sans lui.

### 13.2 Service optionnel

Un service optionnel peut échouer sans bloquer le jeu.

Exemples futurs :

- IA locale ;
- télémétrie de développement ;
- génération vocale ;
- intégration d’un outil externe.

Le bootstrap doit alors :

1. consigner l’erreur ;
2. enregistrer un remplacement local déterministe ;
3. informer l’interface ;
4. continuer lorsque la fonctionnalité essentielle reste disponible.

### 13.3 Null Object

Un **Null Object** est une implémentation sûre qui ne réalise pas l’effet externe, mais respecte le contrat.

Exemple futur : `OfflineNarrationService` peut retourner un texte local prédéfini lorsque le LLM n’est pas disponible.

Le Null Object ne doit pas masquer silencieusement une erreur critique. Son activation doit être visible dans les journaux et l’interface de diagnostic.

## 14. Préparer les tests sans anticiper le chapitre 27

L’injection permet de remplacer une dépendance réelle par un double.

### 14.1 Bus d’enregistrement minimal

> **[VSC] Visual Studio Code — Exemple pédagogique, à placer plus tard dans `tests/doubles/recording_event_bus.gd`.**

```gdscript
class_name RecordingEventBus
extends GameEventBus

var requested_beacon_ids: Array[StringName] = []

func _init() -> void:
	beacon_activation_requested.connect(_record_requested_beacon)

func _record_requested_beacon(beacon_id: StringName) -> void:
	requested_beacon_ids.append(beacon_id)
```

Ce double :

- hérite du contrat de signaux ;
- conserve les identifiants observés ;
- permet une assertion future ;
- ne dépend pas d’une scène complète.

Le chapitre 27 définira le framework, les fixtures, les assertions et l’exécution automatisée. Ici, le but est seulement de montrer que la dépendance peut être remplacée.

### 14.2 Vérification manuelle

> **[APP] Godot — Exécuter la scène `ch05_services_demo.tscn`.**

Vérifier :

1. que le bouton affiche `Demande publiée` ;
2. que la balise s’active ;
3. que le label affiche ensuite `Balise activée` ;
4. qu’aucune double connexion n’apparaît ;
5. que l’arrêt de la scène ne produit pas d’erreur ;
6. que le Remote SceneTree montre le bus sous le bootstrap.

> **[PS] PowerShell 7 — Vérifier statiquement le chargement de la scène depuis la racine du projet Godot.**

```powershell
godot --headless --path . --editor --quit-after 2
```

Explication :

- `godot` lance l’exécutable présent dans le `PATH` ;
- `--headless` désactive la fenêtre graphique ;
- `--path .` utilise le dossier courant comme projet ;
- `--editor` charge le projet et importe les ressources ;
- `--quit-after 2` quitte après deux itérations de la boucle principale.

Cette commande détecte de nombreuses erreurs d’analyse et de ressources, mais ne remplace pas l’exécution fonctionnelle de la démonstration.

## 15. Anti-patterns et corrections

<!-- qa:error-correction-section -->

Le titre « Anti-patterns » désigne ici des erreurs de conception récurrentes. Chaque cas possède donc les mêmes preuves pédagogiques qu’une section « Erreurs fréquentes ».

### 15.1 Un Autoload par service

**Symptôme ou risque :** chaque capacité devient globale et son ordre dépend de la liste Project Settings.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```text
Autoloads :
- AudioService
- SaveService
- QuestService
- BeaconService
- InventoryService
```

**Correction :** conserver un composition root persistant et construire les services ordinaires sous son contrôle.

> **[LECTURE] Organisation corrigée — Ne pas saisir.**

```text
Autoload : AppRuntime
AppRuntime crée :
- GameEventBus
- BeaconActivationService
- autres services nécessaires
```

**Différence :** la version corrigée limite le point global et rend le cycle de vie des services explicite.

### 15.2 Le registre injecté partout

**Symptôme ou risque :** un objet métier recherche lui-même sa dépendance dans le registre.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```gdscript
func activate() -> void:
	var bus := registry.require_service(&'event_bus')
	bus.beacon_activated.emit(id)
```

**Correction :** résoudre la dépendance dans le bootstrap puis injecter le type attendu.

> **[VSC] Visual Studio Code — Exemple corrigé par constructeur.**

```gdscript
var _events: GameEventBus

func _init(events: GameEventBus) -> void:
	_events = events
```

**Différence :** la dépendance corrigée est visible et typée ; le registre reste un outil du point de composition.

### 15.3 Un bus générique à dictionnaires

**Symptôme ou risque :** un seul signal transporte un nom libre et un payload sans schéma.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```gdscript
signal event_published(name: String, payload: Dictionary)

event_published.emit('becon_actvated', {'id': 42})
```

**Correction :** déclarer des signaux nommés avec des paramètres typés.

> **[VSC] Visual Studio Code — Exemple corrigé dans `GameEventBus`.**

```gdscript
signal beacon_activated(beacon_id: StringName)

beacon_activated.emit(&'beacon.training')
```

**Différence :** le moteur peut vérifier le nom du signal et la forme de ses arguments ; la faute de frappe du bus générique reste invisible.

### 15.4 Des événements pour chaque appel local

**Symptôme ou risque :** un enfant demande à son parent une action simple par le bus global.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```gdscript
_events.event_published.emit('label_text_requested', {'text': message})
```

**Correction :** utiliser un appel direct ou un signal local lorsque les composants appartiennent à la même scène.

> **[VSC] Visual Studio Code — Exemple corrigé dans la présentation locale.**

```gdscript
result_label.text = message
```

**Différence :** la correction conserve un flux direct et traçable ; le bus reste réservé aux frontières transversales.

### 15.5 Un service qui connaît l’interface graphique

**Symptôme ou risque :** le service cherche et modifie un `Label`.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```gdscript
func request_activation(id: StringName) -> void:
	get_node('/root/Main/UI/ResultLabel').text = 'Activation demandée'
```

**Correction :** retourner une valeur ou émettre un événement que la présentation traduit en affichage.

> **[VSC] Visual Studio Code — Exemple corrigé avec retour métier.**

```gdscript
func request_activation(id: StringName) -> bool:
	if id.is_empty():
		return false
	_events.beacon_activation_requested.emit(id)
	return true
```

**Différence :** le service corrigé ne dépend plus de l’arbre d’interface et peut être testé sans scène graphique.

### 15.6 Un démarrage non idempotent

**Symptôme ou risque :** chaque appel recrée le bus et reconnecte les signaux.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```gdscript
func start_application() -> void:
	_events = GameEventBus.new()
	add_child(_events)
```

**Correction :** refuser un second démarrage ou retourner l’état existant.

> **[VSC] Visual Studio Code — Exemple corrigé avec garde.**

```gdscript
func start_application() -> Error:
	if _started:
		return ERR_ALREADY_IN_USE
	_started = true
	return OK
```

**Différence :** la garde rend le cycle de vie déterministe et empêche les doublons de nœuds ou de connexions.

### 15.7 Un arrêt dans le mauvais ordre

**Symptôme ou risque :** le bus est supprimé avant les services susceptibles d’émettre pendant leur arrêt.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```gdscript
func stop_application() -> void:
	_events.queue_free()
	_beacon_activation.stop()
```

**Correction :** arrêter les consommateurs avant leurs dépendances.

> **[VSC] Visual Studio Code — Exemple corrigé dans l’ordre inverse du démarrage.**

```gdscript
func stop_application() -> void:
	_beacon_activation.stop()
	_beacon_activation = null
	_events.queue_free()
	_events = null
```

**Différence :** le service termine alors que le bus existe encore ; la version fautive peut émettre vers un objet déjà libéré.

## 16. Parcours Solo

Le parcours Solo adopte le minimum suivant :

- un seul `AppBootstrap` ;
- un `ServiceRegistry` utilisé seulement par le bootstrap ;
- un `GameEventBus` avec peu de signaux ;
- des services `RefCounted` lorsque l’arbre n’est pas nécessaire ;
- un document court listant l’ordre de démarrage ;
- aucun conteneur d’injection automatique.

Le développeur Solo peut conserver des méthodes d’accès typées sur `AppBootstrap` tant que leur nombre reste faible et que les dépendances sont ensuite injectées.

## 17. Parcours Studio

Le parcours Studio ajoute :

- un propriétaire par service ;
- une ADR pour tout nouvel Autoload ;
- une revue de la liste des événements ;
- une matrice de démarrage et d’arrêt ;
- des contrats d’erreur ;
- des doubles de test ;
- une règle interdisant le registre dans les modules métier ;
- un contrôle des dépendances circulaires ;
- une documentation des services obligatoires et optionnels.

> **[VSC] Visual Studio Code — Créer : `docs/architecture/service-catalog.md`.**

Le catalogue doit contenir au minimum :

| Service | Type | Propriétaire | Dépendances | Obligatoire | Démarrage | Arrêt | Remplacement |
|---|---|---|---|---|---|---|---|
| `event_bus` | `Node` | Core | aucune | oui | 1 | dernier | bus de test |
| `beacon_activation` | `RefCounted` | Beacons | event_bus | oui | 2 | avant bus | fake service |

## 18. Checklist d’audit du chapitre

- [ ] Chaque type transversal possède un nom précis.
- [ ] Les Autoloads sont justifiés par leur durée de vie.
- [ ] Les dépendances obligatoires sont visibles dans les signatures.
- [ ] Le registre n’est utilisé que par le point de composition.
- [ ] Le bus contient des signaux typés et documentés.
- [ ] Les signaux locaux ne sont pas déplacés inutilement vers le bus.
- [ ] Le démarrage est déterministe.
- [ ] L’arrêt suit l’ordre inverse.
- [ ] Les erreurs obligatoires et optionnelles sont distinguées.
- [ ] Les fonctions, paramètres, types et retours nouveaux sont expliqués.
- [ ] Les blocs possèdent le bon repère d’utilisation.
- [ ] Les frontières avec les chapitres 6 à 9 et 27 à 28 sont respectées.
- [ ] Le Mode Solo et le Mode Studio sont présents.
- [ ] Le rapport `Livre-II/QA/AUDIT-CHAPITRE-05.md` est à jour.

## 19. Résultat attendu

À la fin du chapitre, `Project Asteria` possède une stratégie documentée pour :

- créer ses services au même endroit ;
- injecter les dépendances ;
- limiter les Autoloads ;
- transmettre des événements transversaux typés ;
- détecter les doublons de services ;
- démarrer et arrêter dans un ordre déterministe ;
- préparer des remplacements de test.

Le projet reste au niveau `static-review` tant que les fichiers du Starter Kit ne sont pas matérialisés et exécutés.

## 20. Sources officielles

- Godot Engine, **Singletons (Autoload)**, documentation stable : <https://docs.godotengine.org/en/stable/tutorials/scripting/singletons_autoload.html>
- Godot Engine, **Using signals**, documentation 4.7 : <https://docs.godotengine.org/en/4.7/getting_started/step_by_step/signals.html>
- Godot Engine, **Scene organization**, documentation 4.x : <https://docs.godotengine.org/fr/4.x/tutorials/best_practices/scene_organization.html>
- Godot Engine, **RefCounted**, documentation stable : <https://docs.godotengine.org/en/stable/classes/class_refcounted.html>
- Godot Engine, **Object**, documentation stable : <https://docs.godotengine.org/en/stable/classes/class_object.html>
- Godot Engine, **Node**, documentation 4.x : <https://docs.godotengine.org/fr/4.x/classes/class_node.html>
- Godot Engine, **Resources**, documentation 4.7 : <https://docs.godotengine.org/en/4.7/tutorials/scripting/resources.html>
- Godot Engine, **Godot 4.7.1 maintenance release**, 14 juillet 2026 : <https://godotengine.org/article/maintenance-release-godot-4-7-1/>
