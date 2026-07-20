
## 21. Requête d’action typée

Le plan produit un identifiant d’action. Le service de décision le convertit en requête typée destinée à un exécuteur autorisé.

> **[VSC] Visual Studio Code — Créer : `res://src/features/agents/application/agent_action_request.gd`.**

```gdscript
class_name AgentActionRequest
extends RefCounted

var request_id: StringName
var owner_character_id: StringName
var goal_id: StringName
var action_id: StringName
var executor_key: StringName
var target_character_id: StringName = &""
var target_position: Vector3 = Vector3.ZERO
var logical_tick: int = 0
var decision_sequence: int = 0
var snapshot_revision: int = 0

func validate() -> Error:
	if not StableId.is_valid(request_id):
		return ERR_INVALID_DATA
	if not CharacterId.is_valid(owner_character_id):
		return ERR_INVALID_DATA
	if not StableId.is_valid(goal_id):
		return ERR_INVALID_DATA
	if not StableId.is_valid(action_id) or not StableId.is_valid(executor_key):
		return ERR_INVALID_DATA
	if logical_tick < 0 or decision_sequence <= 0 or snapshot_revision < 0:
		return ERR_INVALID_DATA
	if not target_position.is_finite():
		return ERR_INVALID_DATA
	return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** cette commande transporte l’identité de la décision, l’action choisie et le contexte minimal nécessaire à l’exécuteur.
- **Corrélation :** `request_id` distingue deux tentatives ; `decision_sequence` ordonne les décisions du même agent ; `snapshot_revision` permet de refuser une requête fondée sur un monde obsolète.
- **Cibles :** une action peut utiliser une identité, une position ou aucune cible. L’exécuteur vérifie les champs réellement requis par son contrat.
- **Frontière :** aucune valeur d’effet autoritaire n’est incluse. Une future requête de combat ne transporte pas directement « points de vie après attaque ».

## 22. Service de décision

Le service orchestre snapshot, mémoire, but, plan et requête. Il n’exécute pas l’action.

> **[VSC] Visual Studio Code — Créer : `res://src/features/agents/application/agent_decision_service.gd`.**

```gdscript
class_name AgentDecisionService
extends RefCounted

signal action_requested(request: AgentActionRequest)
signal decision_failed(character_id: StringName, code: Error, message: String)
signal plan_invalidated(character_id: StringName, reason: StringName)

var _catalog: AgentActionCatalog
var _planner: BoundedAgentPlanner
var _snapshot_builder: AgentSnapshotBuilder
var _goal_policy: AgentGoalPolicy
var _goal_conditions: AgentGoalConditionCatalog
var _world_revision_source: WorldRevisionSource

func decide(
	state: AgentState,
	memory: AgentMemory,
	logical_tick: int,
) -> Error:
	if state == null or state.validate() != OK or memory == null:
		return ERR_INVALID_DATA
	if _catalog == null or _planner == null or _snapshot_builder == null:
		return ERR_UNCONFIGURED

	var sequence := state.next_sequence(logical_tick)
	if sequence < 0:
		return ERR_INVALID_DATA
	var snapshot := _snapshot_builder.build_snapshot(
		state.owner_character_id,
		logical_tick,
	)
	if snapshot == null or snapshot.validate() != OK:
		decision_failed.emit(state.owner_character_id, ERR_INVALID_DATA, "snapshot invalide")
		return ERR_INVALID_DATA

	var goal := _goal_policy.select_goal(state.durable_goals, logical_tick)
	if goal == null:
		return OK
	var conditions := _goal_conditions.get_for(goal.goal_type)
	var result := _planner.plan(snapshot, goal, conditions, _catalog)
	if result.status != AgentPlanResult.Status.FOUND:
		decision_failed.emit(
			state.owner_character_id,
			ERR_CANT_RESOLVE,
			result.message,
		)
		return ERR_CANT_RESOLVE

	if _world_revision_source.current_revision() != snapshot.world_revision:
		plan_invalidated.emit(state.owner_character_id, &"agent.reason.world_changed")
		return ERR_BUSY

	var first_action_id := result.plan.action_ids.front()
	var definition := _catalog.get_action(first_action_id)
	if definition == null:
		return ERR_DOES_NOT_EXIST
	var request := AgentActionRequest.new()
	request.request_id = StringName(
		"agent.request.%s.%d" % [String(state.owner_character_id), sequence]
	)
	request.owner_character_id = state.owner_character_id
	request.goal_id = goal.goal_id
	request.action_id = definition.action_id
	request.executor_key = definition.executor_key
	request.target_character_id = goal.target_character_id
	request.target_position = goal.target_position
	request.logical_tick = logical_tick
	request.decision_sequence = sequence
	request.snapshot_revision = snapshot.world_revision
	if request.validate() != OK:
		return ERR_INVALID_DATA
	action_requested.emit(request)
	return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** `AgentDecisionService` constitue le point d’orchestration d’une décision et émet une requête seulement après validation complète.
- **Ordre :** il valide l’état et ses dépendances, réserve une séquence, construit un snapshot, choisit un but, planifie, recontrôle la révision puis fabrique la requête.
- **Révision concurrente :** si le monde change pendant le calcul, le plan n’est pas appliqué ; `ERR_BUSY` invite l’ordonnanceur à reprogrammer une décision.
- **Absence de but :** retourner `OK` sans signal signifie que l’attente est une issue normale, distincte d’un échec de planification.
- **Effets de bord :** la séquence de l’agent avance et un signal typé peut être émis. Aucun état social, familial, physique ou de combat n’est modifié ici.
- **Limite du brouillon :** les catalogues `AgentGoalPolicy`, `AgentGoalConditionCatalog`, `AgentSnapshotBuilder` et `WorldRevisionSource` sont des ports à documenter dans le projet matérialisé.

## 23. Exécuteurs et systèmes propriétaires

Un registre limité au point de composition associe chaque `executor_key` à un exécuteur. Le registre n’est pas accessible au domaine.

> **[LECTURE] Contrat d’exécution — Structure de référence.**

```gdscript
class_name AgentActionExecutor
extends RefCounted

func can_execute(request: AgentActionRequest) -> Error:
	return ERR_UNAVAILABLE

func start(request: AgentActionRequest) -> Error:
	return ERR_UNAVAILABLE

func cancel(request_id: StringName, reason: StringName) -> Error:
	return ERR_UNAVAILABLE
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce port impose trois opérations distinctes : prévalidation, démarrage et demande d’annulation.
- **Retours :** la classe de base refuse par défaut ; une implémentation doit remplacer chaque méthode qu’elle supporte.
- **Annulation :** `cancel()` est coopérative. Un mouvement déjà transmis au contrôleur peut nécessiter un tick supplémentaire avant l’arrêt observable.
- **Frontière :** l’exécuteur adapte la requête au service propriétaire. Il ne réimplémente pas les règles du système cible.

Exemples de clés :

> **[LECTURE] Vocabulaire d’exécuteurs — Ne pas saisir.**

```text
agent.executor.wait
agent.executor.move_intent
agent.executor.social_command
agent.executor.family_command
agent.executor.combat_command
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ces identifiants découplent les `Resource` de conception des classes concrètes composées au bootstrap.
- **Disponibilité :** les deux premières clés peuvent être matérialisées dans ce chapitre ; les exécuteurs de combat restent indisponibles avant le chapitre 18.
- **Erreur attendue :** demander une clé non enregistrée produit un refus explicite, jamais un appel dynamique par nom de méthode fourni par les données.

## 24. Contrôleur autonome actif

Le contrôleur transforme une requête de mouvement autorisée en `CharacterIntent`, puis réutilise la chaîne du chapitre 6.

> **[VSC] Visual Studio Code — Créer : `res://src/features/agents/presentation/autonomous_character_controller.gd`.**

```gdscript
class_name AutonomousCharacterController
extends Node

var _controlled_character_id: StringName
var _intent_sink: CharacterIntentSink
var _active_request_id: StringName = &""
var _target_position: Vector3 = Vector3.ZERO

func initialize(
	character_id: StringName,
	intent_sink: CharacterIntentSink,
) -> Error:
	if not CharacterId.is_valid(character_id) or intent_sink == null:
		return ERR_INVALID_PARAMETER
	_controlled_character_id = character_id
	_intent_sink = intent_sink
	return OK

func start_move(request: AgentActionRequest) -> Error:
	if request == null or request.validate() != OK:
		return ERR_INVALID_DATA
	if request.owner_character_id != _controlled_character_id:
		return ERR_INVALID_DATA
	_active_request_id = request.request_id
	_target_position = request.target_position
	return OK

func _physics_process(_delta: float) -> void:
	if _active_request_id.is_empty() or _intent_sink == null:
		return
	var origin := _intent_sink.current_global_position()
	var offset := _target_position - origin
	var intent := CharacterIntent.new()
	intent.move_direction = Vector2(offset.x, offset.z).normalized()
	_intent_sink.submit_intent(intent)

func cancel(request_id: StringName) -> Error:
	if request_id != _active_request_id:
		return ERR_DOES_NOT_EXIST
	_active_request_id = &""
	_intent_sink.submit_intent(CharacterIntent.new())
	return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce nœud adapte une action autonome au même contrat d’intention que le contrôleur humain, sans appeler directement `Input` ni déplacer le corps.
- **Initialisation :** l’identité et le puits d’intention sont obligatoires avant toute requête.
- **Traitement physique :** la direction XZ est recalculée à chaque tick depuis la position actuelle ; le moteur de mouvement reste responsable de la vitesse, des collisions et de `move_and_slide()`.
- **Annulation :** une intention neutre est envoyée afin d’arrêter la commande précédente ; une requête inconnue ne modifie pas le contrôleur.
- **Limites :** l’exemple ne traite ni navigation, ni obstacles, ni distance d’arrivée. Une implémentation complète injectera un port de navigation sans déplacer les règles de décision dans `NavigationAgent3D`.

## 25. Simulation hors écran

Un personnage non représenté ne possède pas de contrôleur actif. Son agent peut néanmoins évoluer à une fréquence réduite au moyen d’un exécuteur logique.

> **[VSC] Visual Studio Code — Créer : `res://src/features/agents/application/agent_simulation_mode.gd`.**

```gdscript
class_name AgentSimulationMode
extends RefCounted

enum Value {
	ACTIVE,
	BACKGROUND,
	DORMANT,
}

static func decision_interval_ticks(value: Value) -> int:
	match value:
		Value.ACTIVE:
			return 6
		Value.BACKGROUND:
			return 60
		Value.DORMANT:
			return 600
		_:
			return 600
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** cette politique associe un mode explicite à une fréquence de décision, sans déduire l’existence métier de la présence dans la scène.
- **Intervalles :** avec 60 ticks physiques par seconde, les valeurs correspondent approximativement à 10 décisions/s, 1 décision/s et 1 décision/10 s, mais la logique utilise les ticks et non les secondes murales.
- **Mode dormant :** dormant ne signifie pas supprimé ; les buts durables et l’état persistent.
- **Frontière :** le système de partition du monde choisit le mode. Le registre des personnages actifs ne constitue qu’un signal parmi d’autres.

Une simulation hors écran ne doit pas reproduire à haute fidélité la physique, la navigation et les animations. Elle produit des transitions logiques autorisées et laisse le chapitre 22 définir la simulation globale du monde vivant.

## 26. Politique de tick

La fréquence de décision est distincte de la fréquence d’exécution d’une action. Un déplacement actif peut produire une intention à chaque tick physique tout en ne replanifiant que toutes les six étapes.

> **[VSC] Visual Studio Code — Créer : `res://src/features/agents/application/agent_tick_policy.gd`.**

```gdscript
class_name AgentTickPolicy
extends RefCounted

const MAX_CATCH_UP_DECISIONS := 1

func is_due(
	logical_tick: int,
	last_decision_tick: int,
	mode: AgentSimulationMode.Value,
	phase: int,
) -> bool:
	var interval := AgentSimulationMode.decision_interval_ticks(mode)
	if logical_tick < 0 or interval <= 0:
		return false
	if last_decision_tick >= logical_tick:
		return false
	return (logical_tick + phase) % interval == 0
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** la politique répartit les agents sur les ticks grâce à `phase`, tout en interdisant plusieurs décisions au même tick.
- **Phase :** elle est dérivée de manière stable depuis le `CharacterId`, par exemple `abs(hash(id)) % interval` ; elle ne provient pas d’un tirage aléatoire au démarrage.
- **Rattrapage :** après une longue pause, le système ne rejoue pas toutes les décisions manquées ; une seule nouvelle décision est autorisée, puis le monde courant est observé.
- **Vérification :** deux agents ayant des phases différentes doivent répartir leurs échéances sur l’intervalle.

## 27. Ordonnanceur borné

L’ordonnanceur trie les identités, conserve un curseur round-robin et limite le nombre d’agents décidés par tick.

> **[VSC] Visual Studio Code — Créer : `res://src/features/agents/application/agent_tick_scheduler.gd`.**

```gdscript
class_name AgentTickScheduler
extends Node

const MAX_DECISIONS_PER_PHYSICS_TICK := 8
const WARNING_BUDGET_USEC := 2000

var _logical_tick: int = 0
var _cursor: int = 0
var _agent_ids: Array[StringName] = []
var _registry: AgentRuntimeRegistry
var _decision_service: AgentDecisionService
var _tick_policy: AgentTickPolicy
var _last_elapsed_usec: int = 0

func _physics_process(_delta: float) -> void:
	_logical_tick += 1
	if _registry == null or _decision_service == null or _tick_policy == null:
		return
	_agent_ids = _registry.all_character_ids_sorted()
	if _agent_ids.is_empty():
		_cursor = 0
		return

	var started_usec := Time.get_ticks_usec()
	var visited := 0
	var decided := 0
	while visited < _agent_ids.size() and decided < MAX_DECISIONS_PER_PHYSICS_TICK:
		var index := (_cursor + visited) % _agent_ids.size()
		var character_id := _agent_ids[index]
		var runtime := _registry.get_runtime(character_id)
		visited += 1
		if runtime == null:
			continue
		if not _tick_policy.is_due(
			_logical_tick,
			runtime.state.last_decision_tick,
			runtime.mode,
			runtime.phase,
		):
			continue
		_decision_service.decide(runtime.state, runtime.memory, _logical_tick)
		decided += 1

	_cursor = (_cursor + max(visited, 1)) % _agent_ids.size()
	_last_elapsed_usec = Time.get_ticks_usec() - started_usec
	if _last_elapsed_usec > WARNING_BUDGET_USEC:
		push_warning(
			"Agents: tick de décision lent: %d µs" % _last_elapsed_usec
		)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce nœud distribue les décisions sans parcourir indéfiniment tous les agents à chaque tick physique.
- **Ordre autoritaire :** le registre renvoie des identités triées ; le curseur avance du nombre d’entrées visitées, ce qui évite de favoriser toujours les premiers identifiants.
- **Budget :** `MAX_DECISIONS_PER_PHYSICS_TICK` contrôle le travail déterministe. `WARNING_BUDGET_USEC` ne coupe pas la boucle et sert uniquement à signaler un coût matériel élevé.
- **Temps :** `_logical_tick` est local à cet exemple. Dans le projet complet, il doit provenir de l’horloge de simulation autoritaire utilisée par les autres systèmes.
- **Erreurs :** le code de retour de `decide()` devrait être enregistré dans une trace ou un compteur ; le brouillon ne l’ignore que pour garder l’extrait centré sur l’ordonnancement.
- **Limite :** l’ordonnanceur s’exécute sur le thread principal. Une future parallélisation exige des snapshots immuables et interdit tout accès aux nœuds depuis les workers.

## 28. Invalidation et annulation

Un plan doit être revalidé lorsque :

- la révision du monde change ;
- la cible disparaît ou change d’état ;
- le but est satisfait, échoue ou est annulé ;
- une précondition de la prochaine action devient fausse ;
- l’exécuteur refuse ou annule l’action ;
- la politique de l’agent change.

> **[LECTURE] Séquence d’invalidation — Ne pas saisir.**

```text
événement métier pertinent
    ↓
incrément de world_revision ou invalidation ciblée
    ↓
annulation coopérative de la requête active
    ↓
plan transitoire supprimé
    ↓
nouveau snapshot au prochain tick autorisé
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** cette séquence évite d’appliquer la suite d’un plan construit pour un monde ancien.
- **Ordre :** l’annulation est demandée avant d’oublier l’identifiant de la requête active ; sinon l’exécuteur ne pourrait plus être corrélé.
- **Résultat :** une nouvelle décision repart des données autoritaires, pas de l’état hypothétique du plan abandonné.

## 29. Événements et trace de décision

Les événements observables ne doivent pas exposer le dictionnaire interne du snapshot ou de la mémoire.

> **[VSC] Visual Studio Code — Créer : `res://src/features/agents/application/agent_decision_record.gd`.**

```gdscript
class_name AgentDecisionRecord
extends RefCounted

var owner_character_id: StringName
var decision_sequence: int
var logical_tick: int
var goal_id: StringName
var selected_action_id: StringName
var plan_cost: int
var expanded_nodes: int
var snapshot_revision: int
var outcome: StringName
var diagnostic_hash: StringName

func validate() -> Error:
	if not CharacterId.is_valid(owner_character_id):
		return ERR_INVALID_DATA
	if decision_sequence <= 0 or logical_tick < 0:
		return ERR_INVALID_DATA
	if plan_cost < 0 or expanded_nodes < 0 or snapshot_revision < 0:
		return ERR_INVALID_DATA
	if outcome.is_empty() or diagnostic_hash.is_empty():
		return ERR_INVALID_DATA
	return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** cette valeur résume une décision pour les journaux, tests de reproductibilité et outils Studio.
- **Diagnostic :** `diagnostic_hash` est calculé depuis une représentation canonique des entrées pertinentes et de la sortie ; il ne constitue ni une signature de sécurité ni une preuve de vérité.
- **Données exclues :** le texte généré, les prompts complets, les nœuds, les collections mutables et les secrets ne figurent pas dans le record.
- **Persistance :** la trace de diagnostic peut être conservée dans un journal rotatif séparé, mais elle n’appartient pas au snapshot autoritaire de l’agent.

Une trace mémoire de référence est bornée à `64` décisions par agent. Le chapitre 28 approfondira les journaux, corrélations et replays.

## 30. Variation pseudo-aléatoire contrôlée

Le choix de référence reste déterministe sans hasard. Lorsqu’une politique autorise plusieurs variantes cosmétiques équivalentes, elle utilise un `RandomNumberGenerator` propre à l’agent.

> **[LECTURE] Tirage reproductible — Structure de référence.**

```gdscript
func choose_variant(
	state: AgentState,
	variants: Array[StringName],
) -> StringName:
	if variants.is_empty():
		return &""
	var sorted := variants.duplicate()
	sorted.sort()
	var rng := RandomNumberGenerator.new()
	rng.seed = state.random_seed
	rng.state = state.random_state
	var selected := sorted[rng.randi_range(0, sorted.size() - 1)]
	state.random_state = rng.state
	return selected
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** cette fonction choisit une variante dans un ordre canonique puis sauvegarde le nouvel état du générateur.
- **Initialisation :** la graine est assignée avant l’état restauré ; l’état doit provenir d’une instance précédente et ne doit pas être inventé arbitrairement.
- **Effet de bord :** `state.random_state` avance exactement une fois après le tirage.
- **Frontière :** un tirage ne départage pas deux actions ayant des conséquences métier différentes dans la politique de référence.
- **Vérification :** restaurer le même couple graine/état et le même tableau de variantes doit produire le même choix et le même nouvel état.

## 31. IA générative consultative

Un service local peut proposer :

- une reformulation textuelle d’un but déjà autorisé ;
- des tags de contexte parmi un vocabulaire fermé ;
- un classement de buts que la politique revalide ;
- une suggestion d’action limitée au catalogue disponible.

Il ne peut pas :

- écrire dans `AgentState` ;
- créer librement un `action_id` ou un `executor_key` ;
- modifier une relation, une filiation, un inventaire ou des points de vie ;
- contourner un budget ou une précondition ;
- rendre le runtime essentiel dépendant du service.

> **[VSC] Visual Studio Code — Créer : `res://src/features/agents/application/agent_suggestion_policy.gd`.**

```gdscript
class_name AgentSuggestionPolicy
extends RefCounted

const MAX_SUGGESTED_ACTIONS := 8

func filter_action_ids(
	raw_ids: Array[StringName],
	catalog: AgentActionCatalog,
) -> Array[StringName]:
	var accepted: Array[StringName] = []
	for action_id: StringName in raw_ids:
		if accepted.size() >= MAX_SUGGESTED_ACTIONS:
			break
		if accepted.has(action_id):
			continue
		if catalog.get_action(action_id) == null:
			continue
		accepted.append(action_id)
	accepted.sort()
	return accepted
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** cette politique transforme une sortie externe non fiable en une petite liste d’identifiants déjà présents dans le catalogue local.
- **Filtrage :** les doublons, identifiants inconnus et entrées au-delà de la limite sont retirés.
- **Ordre :** le résultat est trié ; la formulation ou l’ordre de la réponse générative ne devient pas un départage autoritaire implicite.
- **Étape suivante :** le planificateur revalide toujours les préconditions, effets, coûts et budgets.
- **Repli :** en cas d’indisponibilité, de timeout ou de capacité absente, la politique déterministe complète s’exécute sans suggestion.

## 32. Persistance minimale

Le snapshot autoritaire conserve :

- l’identité du propriétaire ;
- l’identifiant de politique ;
- les buts durables actifs ;
- la séquence de décision ;
- la graine et l’état pseudo-aléatoires lorsque utilisés ;
- le dernier tick de décision.

Il exclut :

- perceptions ;
- mémoire de travail ;
- tableau noir ;
- intention courante ;
- plan ;
- frontière de recherche ;
- caches de conditions ;
- références de nœuds ;
- microsecondes mesurées ;
- suggestions ou textes génératifs bruts.

> **[LECTURE] Forme JSON de référence — Ne pas saisir.**

```json
{
  "format": "project-asteria-agent-state",
  "version": 1,
  "owner_character_id": "chr_01jz8r5d2w4f8m1k3n6p9q0s7t",
  "policy_id": "agent.policy.villager.default",
  "decision_sequence": 42,
  "random_seed": 729184,
  "random_state": 1674336221,
  "last_decision_tick": 8140,
  "durable_goals": [
    {
      "goal_id": "agent.goal.return_home.01",
      "goal_type": "agent.goal.return_home",
      "target_character_id": "",
      "target_position": [12.0, 0.0, -4.0],
      "priority": 200,
      "created_tick": 7200,
      "deadline_tick": -1,
      "status": "active",
      "provenance": "system.schedule"
    }
  ]
}
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce document décrit les données nécessaires pour reprendre les motivations durables et la suite pseudo-aléatoire de l’agent.
- **Version :** `format` et `version` sont contrôlés avant tout décodage ; une version future est refusée.
- **Vecteur :** `target_position` est encodé sous forme de trois nombres finis et reconstruit explicitement en `Vector3`.
- **Statut :** la chaîne `active` est mappée vers l’énumération ; une valeur inconnue n’est pas convertie silencieusement.
- **Données absentes :** après chargement, le premier passage reconstruit perceptions et plan depuis le monde restauré.

## 33. Codec strict et section de sauvegarde

Le codec suit les mêmes règles que les chapitres 14 à 16 : clés exactes, types contrôlés, références validées et candidat complet.

> **[LECTURE] Contrat du codec — Structure de référence.**

```gdscript
class_name AgentSnapshotCodec
extends RefCounted

func encode(state: AgentState) -> Dictionary:
	return {}

func decode(
	raw: Dictionary,
	identities: CharacterIdentityIndex,
) -> AgentState:
	return null
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce contrat sépare la représentation JSON de `AgentState` et reçoit l’index logique nécessaire pour vérifier le propriétaire et les cibles de buts.
- **Valeurs de repli :** les corps vides ne sont pas une implémentation fonctionnelle ; ils marquent le contrat minimal du brouillon et doivent être remplacés avant le passage d’audit.
- **Erreur attendue :** `decode()` retourne `null` au premier champ inconnu, type incorrect, identifiant absent, doublon de but ou état pseudo-aléatoire invalide.

> **[VSC] Visual Studio Code — Créer : `res://src/features/agents/infrastructure/agent_save_section.gd`.**

```gdscript
class_name AgentSaveSection
extends SaveSection

var _prepared_states: Dictionary[StringName, AgentState] = {}
var _codec: AgentSnapshotCodec
var _identity_index: CharacterIdentityIndex
var _repository: AgentStateRepository

func prepare_load(raw: Variant) -> Error:
	_prepared_states.clear()
	if not raw is Array:
		return ERR_INVALID_DATA
	for item: Variant in raw:
		if not item is Dictionary:
			_prepared_states.clear()
			return ERR_INVALID_DATA
		var state := _codec.decode(item, _identity_index)
		if state == null or _prepared_states.has(state.owner_character_id):
			_prepared_states.clear()
			return ERR_INVALID_DATA
		_prepared_states[state.owner_character_id] = state
	return OK

func apply_prepared() -> Error:
	return _repository.replace_all(_prepared_states.values())

func cancel_load() -> void:
	_prepared_states.clear()
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** la section décode tous les agents dans un candidat avant de demander un remplacement global au dépôt.
- **Échec fermé :** une entrée invalide ou dupliquée vide le candidat et interrompt la préparation.
- **Application :** `replace_all()` doit lui-même valider l’ensemble et ne remplacer l’état actif qu’après succès.
- **Annulation :** le candidat est supprimé sans effet sur le dépôt.
- **Réserve :** le brouillon doit encore vérifier les dépendances nulles et convertir explicitement `_prepared_states.values()` vers `Array[AgentState]` avant l’audit final.

## 34. Démonstration pédagogique

La scène de démonstration utilise trois actions abstraites : observer, aller au point de rassemblement et attendre. Elle ne simule ni combat ni économie.

> **[APP] Godot — Créer la scène : `res://scenes/learning/ch17_agents_demo.tscn`.**

```text
Ch17AgentsDemo (Node3D)
├── AgentTickScheduler (Node)
├── ActiveCharacter (CharacterBody3D)
├── TargetMarker (Marker3D)
└── DebugPanel (CanvasLayer)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** la scène sépare l’ordonnanceur, la représentation active, une cible spatiale et l’affichage de diagnostic.
- **Résultat attendu :** l’agent construit une requête de déplacement, le contrôleur produit des intentions, puis une invalidation de cible annule l’action et déclenche une nouvelle décision.
- **Limite :** la scène ne prouve pas la correction runtime tant qu’elle n’est pas matérialisée et exécutée.

> **[VSC] Visual Studio Code — Créer : `res://scenes/learning/ch17_agents_demo.gd`.**

```gdscript
extends Node3D

@onready var scheduler: AgentTickScheduler = $AgentTickScheduler
@onready var target_marker: Marker3D = $TargetMarker

func _ready() -> void:
	print("Chapitre 17 : démonstration documentaire à matérialiser")
	print("Cible initiale : ", target_marker.global_position)
	print("Ordonnanceur présent : ", scheduler != null)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce script confirme uniquement les références de scène et affiche la cible initiale.
- **Annotations de scène :** `@onready` diffère la résolution des nœuds jusqu’à l’entrée dans l’arbre.
- **Sortie :** trois lignes doivent apparaître dans l’onglet Output ; elles ne constituent pas un test de planification.
- **Réserve :** le scénario complet sera connecté après matérialisation des contrats du Starter Kit.

## 35. Mode Solo et Mode Studio

### 35.1 Mode Solo

Le parcours Solo privilégie :

- un catalogue d’actions réduit ;
- un seul planificateur synchrone borné ;
- des politiques sous forme de `Resource` ;
- une trace mémoire courte ;
- un repli déterministe systématique ;
- une simulation hors écran à fréquence faible.

### 35.2 Mode Studio

Le parcours Studio ajoute :

- propriétaire explicite de chaque catalogue et politique ;
- revue des changements de préconditions et effets ;
- corpus de scénarios de décision versionnés ;
- budgets par plateforme ;
- tableaux de bord de coût et taux d’échec ;
- identifiants de décisions corrélés aux journaux ;
- validation des suggestions génératives ;
- tests de reproductibilité sur plusieurs machines.

## 36. Budgets de référence

| Ressource | Limite pédagogique | Comportement au dépassement |
|---|---:|---|
| buts durables par agent | 16 | refuser l’ajout |
| faits en mémoire | 128 | évincer le plus ancien de manière stable |
| entrées de tableau noir | 32 | refuser le schéma |
| faits booléens du snapshot | 256 | refuser la décision |
| préconditions par action | 32 | refuser le catalogue |
| effets par action | 32 | refuser le catalogue |
| profondeur de plan | 8 | ne plus développer le nœud |
| expansions par recherche | 256 | `BUDGET_EXCEEDED` |
| décisions par tick physique | 8 | reporter au tick suivant |
| suggestions d’action | 8 | tronquer après filtrage |
| traces mémoire par agent | 64 | supprimer la plus ancienne |

Ces valeurs sont des points de départ. Toute augmentation doit être mesurée sur la configuration de référence et consignée.

## 37. Erreurs fréquentes et corrections

<!-- qa:error-correction-section -->

<a id="ch17-error-state-separation"></a>

### 37.1 Placer l’agent dans `CharacterRuntimeState`

> **À relire :** [§ 6. État logique de l’agent](#ch17-agent-state).

**Symptôme ou risque :** l’état du personnage mélange santé, décision, mémoire, plan et contrôleur.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
character_state.current_plan = planner.plan(world)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi cet exemple est fautif :** un plan transitoire devient une propriété de l’état autoritaire du personnage et complique sa sauvegarde.

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var runtime := agent_registry.get_runtime(character_id)
runtime.current_plan = planner.plan(snapshot, goal, conditions, catalog).plan
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi la correction fonctionne :** le plan reste dans un runtime d’agent reconstructible et séparé de `CharacterRuntimeState`.

### 37.2 Conserver des nœuds dans la mémoire

**Symptôme ou risque :** un déchargement de scène laisse une référence invalide ou empêche la libération.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
memory[&"target"] = target_node
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi cet exemple est fautif :** la mémoire logique dépend de la durée de vie d’un nœud de présentation.

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
fact.subject_id = target_character_id
fact.position = last_known_position
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi la correction fonctionne :** l’identité et la dernière position restent sérialisables et vérifiables hors scène.

### 37.3 Utiliser un dictionnaire libre comme tableau noir

**Symptôme ou risque :** deux graphies créent deux états invisiblement différents.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
blackboard["targte_id"] = target_id
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi cet exemple est fautif :** la faute de frappe devient une nouvelle clé acceptée sans diagnostic.

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var error := blackboard.write(&"agent.bb.target_id", target_id)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi la correction fonctionne :** le schéma contrôle l’existence de la clé et le type de la valeur.

### 37.4 Persister le plan

**Symptôme ou risque :** le chargement reprend une suite d’actions calculée pour un monde ancien.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
snapshot["current_plan"] = runtime.current_plan.action_ids
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi cet exemple est fautif :** les préconditions et cibles du plan peuvent être invalides après restauration.

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
snapshot["durable_goals"] = codec.encode_goals(state.durable_goals)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi la correction fonctionne :** les motivations durables sont restaurées, puis un nouveau plan est construit depuis le monde chargé.

### 37.5 Lire directement les dépôts sociaux ou familiaux

**Symptôme ou risque :** le planificateur dépend des structures internes et peut les modifier par alias.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
snapshot.facts = social_repository._states
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi cet exemple est fautif :** une collection interne devient une entrée mutable du raisonnement.

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var view := social_query.get_mutual_view(actor_id, target_id)
snapshot.boolean_facts[&"agent.fact.target_trusted"] = view != null and view.mutual_trust >= 40
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi la correction fonctionne :** un port de lecture produit une valeur dérivée puis une copie simple est placée dans le snapshot.

### 37.6 Dépendre de l’ordre d’un dictionnaire

**Symptôme ou risque :** deux exécutions choisissent des actions différentes avec les mêmes données logiques.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
var selected := actions_by_id.values().front()
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi cet exemple est fautif :** aucune règle métier ne définit quelle valeur doit apparaître en premier.

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var actions := catalog.all_sorted()
var selected := actions.front() if not actions.is_empty() else null
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi la correction fonctionne :** le catalogue applique un ordre canonique documenté avant la sélection.

### 37.7 Utiliser le temps CPU comme seul budget

**Symptôme ou risque :** un ordinateur lent choisit un autre plan qu’un ordinateur rapide.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
while Time.get_ticks_usec() - start < 1000:
	expand_next_node()
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi cet exemple est fautif :** le nombre de nœuds explorés dépend de la vitesse matérielle et de la charge courante.

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
while expanded < MAX_EXPANSIONS and not frontier.is_empty():
	expand_next_node()
	expanded += 1
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi la correction fonctionne :** le même nombre maximal d’expansions est autorisé avec les mêmes entrées.

### 37.8 Rejouer toutes les décisions manquées

**Symptôme ou risque :** le retour d’une pause provoque une pointe de calcul et applique des décisions obsolètes.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
for tick in range(last_tick + 1, current_tick + 1):
	decide(agent, tick)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi cet exemple est fautif :** chaque décision intermédiaire utilise un monde qui n’existe plus sous cette forme.

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
if tick_policy.is_due(current_tick, last_tick, mode, phase):
	decide(agent, current_tick)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi la correction fonctionne :** une seule décision observe le monde autoritaire actuel.

### 37.9 Confondre hors écran et inexistant

**Symptôme ou risque :** les buts disparaissent lorsque le personnage n’a plus de nœud actif.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
if active_registry.get_node(character_id) == null:
	agent_repository.erase(character_id)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi cet exemple est fautif :** la représentation visuelle devient l’autorité de l’existence logique.

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
runtime.mode = AgentSimulationMode.Value.BACKGROUND
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi la correction fonctionne :** l’agent reste enregistré et seule sa fréquence de simulation change.

### 37.10 Appliquer la suggestion générative

> **À relire :** [§ 4. Chaîne d’autorité](#ch17-authority-chain).

**Symptôme ou risque :** une sortie non déterministe contourne le catalogue et les systèmes propriétaires.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
executor.start(ai_response)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi cet exemple est fautif :** le contenu externe est traité comme une commande déjà validée.

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var allowed_ids := suggestion_policy.filter_action_ids(raw_ids, catalog)
var result := planner.plan(snapshot, goal, conditions, catalog)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi la correction fonctionne :** la suggestion est réduite à des identifiants connus et le planificateur reste l’autorité de sélection.

### 37.11 Oublier la révision du monde

**Symptôme ou risque :** l’agent demande une action sur une cible modifiée pendant la planification.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
action_requested.emit(request)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi cet exemple est fautif :** aucune vérification ne confirme que le snapshot est encore actuel.

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
if revisions.current_revision() != snapshot.world_revision:
	return ERR_BUSY
action_requested.emit(request)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi la correction fonctionne :** une mutation pertinente force une nouvelle observation avant émission.

### 37.12 Annuler sans corrélation

**Symptôme ou risque :** l’exécuteur arrête la mauvaise action ou ignore la demande.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
executor.cancel(&"", &"world_changed")
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi cet exemple est fautif :** aucun identifiant ne désigne la requête active.

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
executor.cancel(runtime.active_request_id, &"agent.reason.world_changed")
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi la correction fonctionne :** la demande cible l’opération enregistrée par le runtime de l’agent.

### 37.13 Émettre avant la mutation propriétaire

**Symptôme ou risque :** les observateurs croient qu’une action a réussi avant son refus métier.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
action_completed.emit(request)
var result := social_service.apply_change(command)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi cet exemple est fautif :** l’événement décrit un succès qui n’a pas encore été obtenu.

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var result := social_service.apply_change(command)
if result == OK:
	action_completed.emit(request)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi la correction fonctionne :** l’événement n’est émis qu’après l’acceptation du système autoritaire.

### 37.14 Utiliser un RNG global non restauré

**Symptôme ou risque :** une animation ou un autre système déplace la suite aléatoire de l’agent.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
var selected := variants.pick_random()
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi cet exemple est fautif :** le choix dépend de l’état aléatoire global et de l’ordre d’autres appels.

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var selected := choose_variant(state, variants)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi la correction fonctionne :** un générateur propre à l’agent utilise une graine et un état restaurables.

### 37.15 Créer un exécuteur depuis une chaîne externe

**Symptôme ou risque :** une donnée non fiable choisit une classe ou une méthode arbitraire.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
var executor := load(ai_response["script_path"]).new()
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi cet exemple est fautif :** la sortie externe contrôle un chemin de code chargé au runtime.

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var executor := executor_registry.get(definition.executor_key)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi la correction fonctionne :** la clé validée sélectionne uniquement un exécuteur composé et autorisé par le projet.

### 37.16 Paralléliser l’accès aux nœuds

**Symptôme ou risque :** un worker lit ou modifie l’arbre de scène pendant le traitement principal.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
worker_pool.add_task(func(): target_node.global_position)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi cet exemple est fautif :** la tâche capture un nœud mutable dont l’accès n’est pas isolé par un snapshot.

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var snapshot := snapshot_builder.build_snapshot(character_id, logical_tick)
worker_pool.add_task(func(): planner.plan(snapshot, goal, conditions, catalog))
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi la correction fonctionne :** le worker reçoit des valeurs détachées de la scène ; toute mutation reste renvoyée au thread propriétaire sous forme de résultat.

## 38. Checklist de réalisation

- [ ] Créer `AgentState` séparé de `CharacterRuntimeState`.
- [ ] Définir les faits, leur provenance et leur expiration.
- [ ] Borner la mémoire et le tableau noir.
- [ ] Distinguer buts, intentions, plans et actions.
- [ ] Valider le catalogue d’actions sans doublons.
- [ ] Canoniser l’ordre des actions et des états.
- [ ] Borner profondeur et expansions du planificateur.
- [ ] Produire des statuts distincts pour absence de plan et budget dépassé.
- [ ] Construire un snapshot immuable depuis des ports de lecture.
- [ ] Revalider la révision avant émission d’une requête.
- [ ] Corréler annulation et action active.
- [ ] Distribuer les décisions par ticks et phases stables.
- [ ] Séparer simulation active et hors écran.
- [ ] Filtrer toute suggestion générative par un vocabulaire fermé.
- [ ] Persister uniquement l’état durable.
- [ ] Préparer toute la section avant application.
- [ ] Enregistrer les décisions sans données sensibles.
- [ ] Documenter les réserves runtime.

## 39. Critères d’acceptation

Le chapitre est accepté au niveau documentaire lorsque :

1. une même entrée produit le même but, le même plan et la même première action ;
2. les budgets de recherche ne dépendent pas uniquement de la vitesse CPU ;
3. aucun plan, nœud, perception ou tableau noir n’est persisté ;
4. l’agent hors écran conserve ses buts sans contrôleur actif ;
5. un changement de révision invalide une requête avant émission ;
6. une suggestion générative inconnue est ignorée ;
7. une action ne modifie pas directement le système propriétaire ;
8. les lectures sociales et familiales passent par des requêtes ;
9. les collections retournées sont défensives ou traitées comme immuables ;
10. chaque bloc de code significatif possède une explication spécifique ;
11. les sections d’erreurs contiennent faute et correction sans paraphraser leur titre ;
12. index, roadmap, `contents.txt` et continuité reflètent l’état réel.

## 40. Tests à préparer

### 40.1 Tests unitaires

- validation de chaque type ;
- expiration inclusive des faits ;
- éviction déterministe de la mémoire ;
- refus des clés de tableau noir inconnues ;
- tri des buts ;
- duplication des états simulés ;
- refus des actions et catalogues invalides ;
- canonisation de la clé d’état ;
- plan de coût minimal ;
- départage stable ;
- distinction `NO_PLAN` / `BUDGET_EXCEEDED` ;
- filtrage des suggestions ;
- restauration du RNG.

### 40.2 Tests d’intégration

- snapshot social et familial sans mutation ;
- requête d’action puis refus par l’exécuteur ;
- invalidation par révision ;
- annulation corrélée ;
- passage actif → arrière-plan ;
- sauvegarde puis reconstruction d’un plan ;
- indisponibilité de `LocalAiGateway` avec repli déterministe.

### 40.3 Simulations

- 1, 10, 100 et 1 000 agents ;
- répartition des phases ;
- fréquence active, background et dormant ;
- catalogues de tailles croissantes ;
- graphes de recherche proches des budgets ;
- comparaison de deux exécutions depuis le même snapshot ;
- mesure des microsecondes sans les utiliser comme résultat métier.

## 41. Réserves runtime

Cette rédaction est une revue statique. Elle ne prouve pas :

- que tous les scripts passent le parseur Godot 4.7.1 ;
- que les types personnalisés et tableaux typés se convertissent comme attendu ;
- que la scène de démonstration est instanciable ;
- que les intentions déplacent réellement un `CharacterBody3D` ;
- que l’annulation arrête un exécuteur matérialisé ;
- que les budgets tiennent sur la configuration de référence ;
- que 1 000 agents respectent le temps de trame ;
- qu’une parallélisation est sûre ;
- que le codec et la section de sauvegarde sont complets ;
- que les replays sont identiques entre plateformes ;
- que le packaging inclut les `Resource` du catalogue.

## 42. Résumé

Un agent autonome n’est ni un nœud, ni une relation, ni une réponse générative. C’est un état logique séparé qui observe des faits bornés, poursuit des buts durables, construit un plan transitoire et demande une action à un système autoritaire.

La reproductibilité provient d’entrées figées, d’ordres canoniques, de budgets logiques, de ticks et séquences croissants, d’un RNG local restaurable et d’une invalidation explicite.

L’IA générative reste facultative. Elle propose dans un vocabulaire fermé ; le jeu filtre, planifie, valide et peut refuser.

## 43. Sources techniques

- [Godot 4.7 — `Node` et `_physics_process()`](https://docs.godotengine.org/en/4.7/classes/class_node.html)
- [Godot 4.7 — `Engine.physics_ticks_per_second`](https://docs.godotengine.org/en/4.7/classes/class_engine.html)
- [Godot 4.7 — `Time.get_ticks_usec()` et horloge monotone](https://docs.godotengine.org/en/4.7/classes/class_time.html)
- [Godot 4.7 — `RandomNumberGenerator`](https://docs.godotengine.org/en/4.7/classes/class_randomnumbergenerator.html)
- [Godot 4.7 — génération pseudo-aléatoire et reproductibilité](https://docs.godotengine.org/en/4.7/tutorials/math/random_number_generation.html)
- [Godot 4.7 — `Resource`](https://docs.godotengine.org/en/4.7/classes/class_resource.html)
- [Godot 4.7 — `RefCounted`](https://docs.godotengine.org/en/4.7/classes/class_refcounted.html)
- [Godot 4.7 — `Object` et signaux](https://docs.godotengine.org/en/4.7/classes/class_object.html)
- [Godot 4.7 — `Dictionary`](https://docs.godotengine.org/en/4.7/classes/class_dictionary.html)
- [Godot 4.7 — `Array`](https://docs.godotengine.org/en/4.7/classes/class_array.html)
- [Godot 4.7 — `StringName`](https://docs.godotengine.org/en/4.7/classes/class_stringname.html)
- [Godot 4.7 — `Variant`](https://docs.godotengine.org/en/4.7/classes/class_variant.html)
- [Godot 4.7 — `Performance` et moniteurs personnalisés](https://docs.godotengine.org/en/4.7/classes/class_performance.html)

## 44. Prochaine étape

Le chapitre 18 utilisera les requêtes d’action et les frontières établies ici pour définir le combat, sans déplacer les règles de dégâts, portée, défense ou initiative dans le planificateur.

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-II/CHAPITRE-18-Combat.md
Niveau GPT-5.6 Sol recommandé : Élevée
```
