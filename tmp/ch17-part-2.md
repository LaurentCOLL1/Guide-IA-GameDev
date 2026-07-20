
## 12. Conditions et effets déclaratifs

Le planificateur de référence raisonne sur des faits booléens contrôlés. Il ne reçoit pas un accès arbitraire aux propriétés des nœuds.

> **[VSC] Visual Studio Code — Créer : `res://src/features/agents/domain/agent_condition.gd`.**

```gdscript
class_name AgentCondition
extends Resource

@export var fact_key: StringName
@export var expected_value: bool = true

func validate() -> Error:
	return OK if StableId.is_valid(fact_key) else ERR_INVALID_DATA

func matches(facts: Dictionary[StringName, bool]) -> bool:
	return facts.get(fact_key, false) == expected_value
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** `AgentCondition` décrit une précondition de conception modifiable dans l’inspecteur et évaluée contre un snapshot booléen.
- **Valeur absente :** une clé inexistante est lue comme `false`. Une condition qui attend `false` peut donc réussir en l’absence de clé ; cette convention doit rester stable dans tout le catalogue.
- **Retour :** `matches()` ne modifie ni la condition ni le dictionnaire reçu.
- **Limite :** les comparaisons de distance, de quantité ou de relation utilisent des faits calculés par les requêtes du monde, pas des opérateurs dynamiques stockés dans une chaîne.

> **[VSC] Visual Studio Code — Créer : `res://src/features/agents/domain/agent_effect.gd`.**

```gdscript
class_name AgentEffect
extends Resource

@export var fact_key: StringName
@export var value: bool = true

func validate() -> Error:
	return OK if StableId.is_valid(fact_key) else ERR_INVALID_DATA

func apply_to(facts: Dictionary[StringName, bool]) -> void:
	facts[fact_key] = value
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** `AgentEffect` décrit l’état hypothétique obtenu après une action réussie.
- **Effet de bord :** `apply_to()` modifie le dictionnaire fourni ; le planificateur doit donc lui transmettre une copie de l’état parent.
- **Frontière :** cet effet ne mutile jamais le monde réel. Il sert uniquement à simuler la conséquence attendue pendant la recherche de plan.
- **Vérification :** appliquer un effet à une copie ne doit pas changer le snapshot d’origine.

## 13. Définition d’une action

Une action déclarative relie préconditions, effets, coût et clé d’exécuteur. Elle ne contient pas de référence vers une scène.

> **[VSC] Visual Studio Code — Créer : `res://src/features/agents/domain/agent_action_definition.gd`.**

```gdscript
class_name AgentActionDefinition
extends Resource

const MAX_COST := 100000
const MAX_CONDITIONS := 32
const MAX_EFFECTS := 32

@export var action_id: StringName
@export var executor_key: StringName
@export_range(0, MAX_COST, 1) var base_cost: int = 1
@export var preconditions: Array[AgentCondition] = []
@export var effects: Array[AgentEffect] = []

func validate() -> Error:
	if not StableId.is_valid(action_id) or not StableId.is_valid(executor_key):
		return ERR_INVALID_DATA
	if base_cost < 0 or base_cost > MAX_COST:
		return ERR_INVALID_DATA
	if preconditions.size() > MAX_CONDITIONS or effects.is_empty():
		return ERR_INVALID_DATA
	if effects.size() > MAX_EFFECTS:
		return ERR_INVALID_DATA
	for condition: AgentCondition in preconditions:
		if condition == null or condition.validate() != OK:
			return ERR_INVALID_DATA
	for effect: AgentEffect in effects:
		if effect == null or effect.validate() != OK:
			return ERR_INVALID_DATA
	return OK

func can_apply(facts: Dictionary[StringName, bool]) -> bool:
	for condition: AgentCondition in preconditions:
		if not condition.matches(facts):
			return false
	return true

func simulate(facts: Dictionary[StringName, bool]) -> Dictionary[StringName, bool]:
	var result := facts.duplicate()
	for effect: AgentEffect in effects:
		effect.apply_to(result)
	return result
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** cette `Resource` constitue la donnée de conception d’une action planifiable ; `executor_key` choisit l’adaptateur autorisé qui demandera l’exécution réelle.
- **Bornes :** les coûts et tailles de collections sont limités afin qu’un catalogue erroné ne rende pas la recherche imprévisible.
- **Précondition :** une action sans effet est refusée, car elle ne peut pas rapprocher un plan d’un état cible dans ce modèle.
- **Simulation :** `simulate()` duplique le dictionnaire avant d’appliquer les effets, ce qui protège l’état parent de la recherche.
- **Immutabilité attendue :** une action chargée depuis le catalogue est traitée comme immuable pendant le gameplay.
- **Limite :** le coût de planification n’est pas automatiquement une durée, une dépense d’endurance ou un prix économique ; ces valeurs appartiennent aux systèmes concernés.

## 14. Catalogue validé

Le catalogue refuse les doublons et renvoie les actions dans un ordre stable.

> **[VSC] Visual Studio Code — Créer : `res://src/features/agents/application/agent_action_catalog.gd`.**

```gdscript
class_name AgentActionCatalog
extends RefCounted

var _actions_by_id: Dictionary[StringName, AgentActionDefinition] = {}

func replace_all(actions: Array[AgentActionDefinition]) -> Error:
	var candidate: Dictionary[StringName, AgentActionDefinition] = {}
	for action: AgentActionDefinition in actions:
		if action == null or action.validate() != OK:
			return ERR_INVALID_DATA
		if candidate.has(action.action_id):
			return ERR_ALREADY_EXISTS
		candidate[action.action_id] = action
	_actions_by_id = candidate
	return OK

func get_action(action_id: StringName) -> AgentActionDefinition:
	return _actions_by_id.get(action_id)

func all_sorted() -> Array[AgentActionDefinition]:
	var result: Array[AgentActionDefinition] = []
	result.assign(_actions_by_id.values())
	result.sort_custom(
		func(left: AgentActionDefinition, right: AgentActionDefinition) -> bool:
			return String(left.action_id) < String(right.action_id)
	)
	return result
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** `AgentActionCatalog` construit un candidat complet avant de remplacer le catalogue actif.
- **Erreurs :** une action invalide produit `ERR_INVALID_DATA` ; deux identifiants identiques produisent `ERR_ALREADY_EXISTS` ; aucun remplacement partiel n’est effectué.
- **Ordre stable :** `all_sorted()` neutralise l’ordre d’insertion du dictionnaire et fournit le départage lexical utilisé par le planificateur.
- **Lecture :** le tableau retourné est nouveau, mais les `Resource` restent partagées et considérées comme immuables.

## 15. Snapshot de décision

Le snapshot rassemble uniquement les valeurs nécessaires à une décision. Il porte une révision du monde qui permet d’invalider un plan devenu obsolète.

> **[VSC] Visual Studio Code — Créer : `res://src/features/agents/domain/agent_world_snapshot.gd`.**

```gdscript
class_name AgentWorldSnapshot
extends RefCounted

const MAX_BOOLEAN_FACTS := 256

var owner_character_id: StringName
var logical_tick: int
var world_revision: int
var boolean_facts: Dictionary[StringName, bool] = {}
var visible_character_ids: Array[StringName] = []
var nearby_positions: Dictionary[StringName, Vector3] = {}

func validate() -> Error:
	if not CharacterId.is_valid(owner_character_id):
		return ERR_INVALID_DATA
	if logical_tick < 0 or world_revision < 0:
		return ERR_INVALID_DATA
	if boolean_facts.size() > MAX_BOOLEAN_FACTS:
		return ERR_OUT_OF_MEMORY
	for character_id: StringName in visible_character_ids:
		if not CharacterId.is_valid(character_id):
			return ERR_INVALID_DATA
	for location_id: StringName in nearby_positions:
		if not StableId.is_valid(location_id):
			return ERR_INVALID_DATA
		if not nearby_positions[location_id].is_finite():
			return ERR_INVALID_DATA
	return OK

func duplicate_snapshot() -> AgentWorldSnapshot:
	var copy := AgentWorldSnapshot.new()
	copy.owner_character_id = owner_character_id
	copy.logical_tick = logical_tick
	copy.world_revision = world_revision
	copy.boolean_facts = boolean_facts.duplicate()
	copy.visible_character_ids = visible_character_ids.duplicate()
	copy.nearby_positions = nearby_positions.duplicate()
	return copy
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce DTO fige les entrées de lecture utilisées par une décision afin que le planificateur ne consulte pas un monde changeant au milieu de son calcul.
- **Révision :** `world_revision` augmente lorsqu’une mutation pertinente peut invalider un plan ; sa granularité exacte appartient au service d’agrégation du monde.
- **Bornes :** le nombre de faits booléens est limité ; les identifiants et positions sont contrôlés avant planification.
- **Copie :** les trois collections sont dupliquées. Le contenu est composé de valeurs et ne partage pas d’objet mutable personnalisé.
- **Frontière :** les relations et liens familiaux sont lus par leurs services de requête puis convertis en faits ; leurs dépôts ne sont jamais exposés au planificateur.

## 16. Construire les faits depuis les systèmes existants

Le service de snapshot orchestre des ports de lecture. Il ne dépend pas des implémentations en mémoire ou des nœuds actifs.

> **[LECTURE] Exemple d’agrégation — Structure de référence.**

```gdscript
func build_snapshot(
	character_id: StringName,
	logical_tick: int,
) -> AgentWorldSnapshot:
	var snapshot := AgentWorldSnapshot.new()
	snapshot.owner_character_id = character_id
	snapshot.logical_tick = logical_tick
	snapshot.world_revision = _world_revision_source.current_revision()

	var social_view := _social_query.get_mutual_view(
		character_id,
		_focus_target_id,
	)
	snapshot.boolean_facts[&"agent.fact.focus_target_trusted"] = (
		social_view != null and social_view.mutual_trust >= 40
	)

	var parents := _family_query.get_parents(character_id)
	snapshot.boolean_facts[&"agent.fact.has_known_parent"] = not parents.is_empty()
	return snapshot
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** l’agrégateur convertit des lectures sociales et familiales en faits utiles sans modifier les systèmes interrogés.
- **Dépendances :** `_social_query`, `_family_query` et `_world_revision_source` sont des contrats injectés ; `_focus_target_id` provient du contexte de décision validé.
- **Valeurs dérivées :** le seuil de confiance appartient à une politique d’agent versionnée, pas à `SocialRelationshipState`.
- **Résultat :** le snapshot peut encore être refusé par `validate()` avant d’être transmis au planificateur.
- **Limite :** ce petit exemple ne définit pas la visibilité physique, la navigation, le combat ni l’économie.

## 17. Plan et résultat de recherche

Le résultat distingue l’absence de plan d’un dépassement de budget. Ces deux situations ne doivent pas produire la même réaction.

> **[VSC] Visual Studio Code — Créer : `res://src/features/agents/domain/agent_plan.gd`.**

```gdscript
class_name AgentPlan
extends RefCounted

var goal_id: StringName
var action_ids: Array[StringName] = []
var total_cost: int = 0
var snapshot_revision: int = 0
var built_at_tick: int = 0

func validate() -> Error:
	if not StableId.is_valid(goal_id) or action_ids.is_empty():
		return ERR_INVALID_DATA
	if total_cost < 0 or snapshot_revision < 0 or built_at_tick < 0:
		return ERR_INVALID_DATA
	for action_id: StringName in action_ids:
		if not StableId.is_valid(action_id):
			return ERR_INVALID_DATA
	return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** `AgentPlan` conserve une suite ordonnée d’identifiants d’actions liée à un but et à la révision du snapshot utilisé.
- **Données transitoires :** le plan est validable et diagnosticable, mais il n’est pas une donnée durable de sauvegarde.
- **Invalidation :** si la révision courante diffère de `snapshot_revision`, le service revalide au minimum la prochaine action ou reconstruit le plan.
- **Frontière :** `total_cost` permet de comparer des plans ; il ne garantit pas que l’exécution réelle réussira.

> **[VSC] Visual Studio Code — Créer : `res://src/features/agents/application/agent_plan_result.gd`.**

```gdscript
class_name AgentPlanResult
extends RefCounted

enum Status {
	FOUND,
	NO_PLAN,
	BUDGET_EXCEEDED,
	INVALID_INPUT,
}

var status: Status = Status.INVALID_INPUT
var plan: AgentPlan
var expanded_nodes: int = 0
var message: String = ""

static func found(value: AgentPlan, expanded: int) -> AgentPlanResult:
	var result := AgentPlanResult.new()
	result.status = Status.FOUND
	result.plan = value
	result.expanded_nodes = expanded
	return result
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** le résultat transporte un statut fermé, le plan éventuel et le nombre de nœuds développés pour le diagnostic.
- **Retour de fabrique :** `found()` garantit que le statut et le plan sont assignés ensemble ; les autres statuts utilisent des fabriques équivalentes dans l’implémentation complète.
- **Erreur fréquente :** `NO_PLAN` signifie que la recherche bornée a épuisé les possibilités autorisées ; `BUDGET_EXCEEDED` signifie qu’elle s’est arrêtée avant cette conclusion.

## 18. Nœud interne de recherche

Chaque nœud contient un état hypothétique, le coût accumulé et les actions déjà choisies.

> **[VSC] Visual Studio Code — Créer : `res://src/features/agents/application/agent_search_node.gd`.**

```gdscript
class_name AgentSearchNode
extends RefCounted

var facts: Dictionary[StringName, bool] = {}
var action_ids: Array[StringName] = []
var cost: int = 0

func depth() -> int:
	return action_ids.size()

func signature() -> String:
	return ",".join(PackedStringArray(action_ids))
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** cet objet est une structure de travail du planificateur et n’appartient ni au domaine persistant ni au monde actif.
- **Signature :** la chaîne d’identifiants sert uniquement au départage stable de deux chemins de coût et profondeur identiques.
- **Limite :** concaténer de longues signatures coûte de la mémoire ; la profondeur maximale faible du planificateur rend ce choix acceptable pour le parcours pédagogique.

## 19. Planificateur borné et déterministe

Le planificateur explore les actions applicables par coût croissant. Les égalités sont résolues par profondeur puis par signature lexicale.

> **[VSC] Visual Studio Code — Créer : `res://src/features/agents/application/bounded_agent_planner.gd`.**

```gdscript
class_name BoundedAgentPlanner
extends RefCounted

const MAX_EXPANSIONS := 256
const MAX_PLAN_DEPTH := 8

func plan(
	snapshot: AgentWorldSnapshot,
	goal: AgentGoal,
	goal_conditions: Array[AgentCondition],
	catalog: AgentActionCatalog,
) -> AgentPlanResult:
	if snapshot == null or snapshot.validate() != OK:
		return _failure(AgentPlanResult.Status.INVALID_INPUT, 0, "snapshot invalide")
	if goal == null or goal.validate() != OK or catalog == null:
		return _failure(AgentPlanResult.Status.INVALID_INPUT, 0, "but ou catalogue invalide")
	if goal_conditions.is_empty():
		return _failure(AgentPlanResult.Status.INVALID_INPUT, 0, "conditions de but absentes")

	var root := AgentSearchNode.new()
	root.facts = snapshot.boolean_facts.duplicate()
	var frontier: Array[AgentSearchNode] = [root]
	var best_cost_by_state: Dictionary[String, int] = {
		_state_key(root.facts): 0,
	}
	var expanded := 0
	var actions := catalog.all_sorted()

	while not frontier.is_empty():
		if expanded >= MAX_EXPANSIONS:
			return _failure(
				AgentPlanResult.Status.BUDGET_EXCEEDED,
				expanded,
				"budget de recherche atteint",
			)
		var current := _take_best(frontier)
		if _matches_goal(current.facts, goal_conditions):
			if current.action_ids.is_empty():
				return _failure(AgentPlanResult.Status.NO_PLAN, expanded, "but déjà satisfait")
			var result_plan := AgentPlan.new()
			result_plan.goal_id = goal.goal_id
			result_plan.action_ids = current.action_ids.duplicate()
			result_plan.total_cost = current.cost
			result_plan.snapshot_revision = snapshot.world_revision
			result_plan.built_at_tick = snapshot.logical_tick
			return AgentPlanResult.found(result_plan, expanded)

		if current.depth() >= MAX_PLAN_DEPTH:
			continue
		expanded += 1

		for action: AgentActionDefinition in actions:
			if not action.can_apply(current.facts):
				continue
			var child := AgentSearchNode.new()
			child.facts = action.simulate(current.facts)
			child.action_ids = current.action_ids.duplicate()
			child.action_ids.append(action.action_id)
			child.cost = current.cost + action.base_cost
			var key := _state_key(child.facts)
			if best_cost_by_state.has(key) and best_cost_by_state[key] <= child.cost:
				continue
			best_cost_by_state[key] = child.cost
			frontier.append(child)

	return _failure(AgentPlanResult.Status.NO_PLAN, expanded, "aucun chemin autorisé")

func _take_best(frontier: Array[AgentSearchNode]) -> AgentSearchNode:
	frontier.sort_custom(
		func(left: AgentSearchNode, right: AgentSearchNode) -> bool:
			if left.cost != right.cost:
				return left.cost < right.cost
			if left.depth() != right.depth():
				return left.depth() < right.depth()
			return left.signature() < right.signature()
	)
	return frontier.pop_front()

func _matches_goal(
	facts: Dictionary[StringName, bool],
	conditions: Array[AgentCondition],
) -> bool:
	for condition: AgentCondition in conditions:
		if condition == null or not condition.matches(facts):
			return false
	return true

func _state_key(facts: Dictionary[StringName, bool]) -> String:
	var keys: Array[StringName] = []
	keys.assign(facts.keys())
	keys.sort()
	var parts := PackedStringArray()
	for key: StringName in keys:
		parts.append("%s=%s" % [String(key), str(facts[key])])
	return "|".join(parts)

func _failure(
	status: AgentPlanResult.Status,
	expanded: int,
	message: String,
) -> AgentPlanResult:
	var result := AgentPlanResult.new()
	result.status = status
	result.expanded_nodes = expanded
	result.message = message
	return result
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** cette recherche de coût uniforme explore un espace booléen borné et retourne un statut explicite plutôt qu’une liste vide ambiguë.
- **Entrées :** le snapshot, le but et chaque condition sont validés avant la création de la frontière ; le catalogue fournit déjà des actions valides triées.
- **Budgets déterministes :** `MAX_EXPANSIONS` et `MAX_PLAN_DEPTH` limitent la quantité de travail de manière indépendante de la vitesse du processeur.
- **Déroulement :** le meilleur nœud est retiré, le but est testé, puis les actions applicables produisent des enfants sur des copies de faits.
- **Élagage :** `best_cost_by_state` ignore un état déjà atteint à coût inférieur ou égal ; la clé canonique trie les faits pour ne pas dépendre de l’ordre du dictionnaire.
- **Départage :** coût, profondeur et signature donnent le même choix avec les mêmes entrées.
- **Cas déjà satisfait :** le modèle retourne ici `NO_PLAN` avec un message spécifique ; le service de décision peut alors marquer le but satisfait au lieu d’exécuter une action vide.
- **Complexité :** trier toute la frontière à chaque retrait reste pédagogique, mais une file de priorité spécialisée sera préférable si les budgets augmentent.
- **Vérification :** exécuter la même recherche après permutation du catalogue doit conserver le statut, le coût et la liste d’actions.

## 20. Pourquoi le budget en microsecondes n’est pas l’autorité

`Time.get_ticks_usec()` est monotone et utile pour mesurer. Toutefois, interrompre le planificateur uniquement parce qu’une machine a consommé plus de microsecondes peut produire des décisions différentes sur deux matériels.

La règle de référence est donc :

> **[LECTURE] Budgets complémentaires — Ne pas saisir.**

```text
budget autoritaire : nombre d’expansions, profondeur, agents par tick
budget de sécurité : microsecondes observées, alerte, report du travail restant
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** le premier budget protège la reproductibilité ; le second protège la fluidité et fournit une télémétrie dépendante de la machine.
- **Conséquence :** une mesure trop élevée peut dégrader la fréquence future ou déclencher un diagnostic, mais elle ne change pas rétroactivement le résultat d’une recherche déjà autorisée par son budget logique.
- **Lien moteur :** l’horloge monotone évite les sauts de l’heure système, mais elle ne rend pas deux processeurs aussi rapides.
