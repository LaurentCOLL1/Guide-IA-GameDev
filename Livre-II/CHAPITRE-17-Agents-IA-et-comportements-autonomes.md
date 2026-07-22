---
title: "Livre II — Chapitre 17 : Agents IA et comportements autonomes"
id: "DOC-L2-CH17"
status: "reviewed"
version: "1.0.5"
lang: "fr-FR"
book: "Livre II"
chapter: 17
last-verified: "2026-07-21T19:59:30+02:00"
audit-status: "complete"
audit-date: "2026-07-21T19:59:30+02:00"
audit-report: "Livre-II/QA/AUDIT-CHAPITRE-17.md"
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

# Agents IA et comportements autonomes

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L2-CH17`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Version de référence :** Godot `4.7.1-stable`, édition Standard, GDScript, Forward+  

## 1. Rôle du chapitre

Les chapitres 14 à 16 ont défini l’identité et l’état des personnages, leurs perceptions sociales et leurs liens familiaux. Aucun de ces systèmes ne doit décider à la place d’un agent.

Ce chapitre construit une couche autonome qui :

- observe le monde au moyen de faits structurés ;
- conserve une mémoire de travail bornée ;
- poursuit des buts durables ;
- choisit une intention puis un plan transitoire ;
- sélectionne des actions dans un catalogue validé ;
- produit des requêtes d’action sans contourner les systèmes métier ;
- distribue le coût de décision sur plusieurs ticks ;
- reste reproductible et diagnosticable ;
- continue à fonctionner sans service d’IA générative.

À la fin, le lecteur saura distinguer six notions souvent mélangées :

| Notion | Question traitée | Durée typique |
|---|---|---|
| perception | qu’est-ce qui vient d’être observé ? | très courte |
| mémoire de travail | quels faits récents sont encore utiles ? | courte et bornée |
| but | quel état durable l’agent veut-il atteindre ? | moyenne ou longue |
| intention | quel but est actuellement poursuivi ? | transitoire |
| plan | quelle suite d’actions est proposée ? | transitoire et invalidable |
| action | quelle opération autorisée est demandée maintenant ? | ponctuelle |

## 2. Prérequis

Le lecteur doit avoir parcouru :

- le chapitre 4 pour l’architecture feature-first ;
- le chapitre 5 pour les services injectés et événements typés ;
- le chapitre 6 pour la chaîne entrée → intention → contrôleur ;
- le chapitre 9 pour les sections de sauvegarde préparées avant application ;
- les chapitres 11 à 13 pour le port `LocalAiGateway`, les délais et la séparation production/runtime ;
- le chapitre 14 pour `CharacterId`, `CharacterRuntimeState` et le contrôleur autonome réservé ici ;
- les chapitres 15 et 16 pour les requêtes sociales et familiales sans mutation directe.

## 3. Périmètre et frontières

Ce chapitre définit :

- l’état logique d’un agent autonome ;
- les faits perçus et leur expiration ;
- une mémoire et un tableau noir bornés ;
- les buts durables et leur ordre de priorité ;
- un catalogue d’actions déclaratif ;
- un planificateur déterministe et borné ;
- l’invalidation et l’annulation ;
- un ordonnanceur par ticks ;
- la simulation active et hors écran ;
- les événements et traces de décision ;
- une passerelle consultative vers l’IA locale ;
- une persistance minimale.

Il ne définit pas :

- les règles de dégâts, portée, couverture ou initiative du chapitre 18 ;
- le calcul des compétences et pouvoirs du chapitre 19 ;
- les transactions et prix du chapitre 21 ;
- la simulation écologique globale du chapitre 22 ;
- les lois, factions et sanctions du chapitre 23 ;
- les quêtes et conséquences narratives du chapitre 25 ;
- le multijoueur du Livre IV.

> **Frontière essentielle :** l’agent choisit une requête. Le système propriétaire de l’action valide et applique l’effet réel.

<a id="ch17-authority-chain"></a>

## 4. Chaîne d’autorité

Une décision autonome suit cette chaîne :

> **[LECTURE] Flux d’autorité — Ne pas saisir.**

```text
monde autoritaire
    ↓ requêtes de lecture
snapshot de décision immuable
    ↓
mémoire de travail bornée
    ↓
but prioritaire
    ↓
plan déterministe borné
    ↓
requête d’action typée
    ↓ validation par le système propriétaire
mutation autoritaire ou refus explicite
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** ce schéma sépare le raisonnement de l’écriture autoritaire ; aucune étape de perception ou de planification ne modifie directement le monde.

- **Paramètres, sorties et types importants :** **Entrées et sorties :** les requêtes de lecture produisent un snapshot ; le planificateur produit une proposition ; le système propriétaire retourne un succès ou un refus.

- **Invariants protégés :** **Invariant protégé :** une conclusion de l’agent, même cohérente, ne devient pas automatiquement un fait du jeu.

- **Résultat attendu et vérification :** **Vérification :** une action sociale passe par `SocialRelationshipService`, une action familiale par `FamilyGraphService`, et les futures actions de combat par le service du chapitre 18.

## 5. Architecture retenue

Le système `agents` reste une fonctionnalité distincte :

> **[LECTURE] Arborescence cible — Ne pas créer depuis un terminal.**

```text
res://src/features/agents/
├── domain/
│   ├── agent_fact.gd
│   ├── agent_memory.gd
│   ├── agent_goal.gd
│   ├── agent_state.gd
│   ├── agent_condition.gd
│   ├── agent_effect.gd
│   ├── agent_action_definition.gd
│   ├── agent_world_snapshot.gd
│   └── agent_plan.gd
├── application/
│   ├── agent_action_catalog.gd
│   ├── bounded_agent_planner.gd
│   ├── agent_decision_service.gd
│   ├── agent_tick_policy.gd
│   ├── agent_tick_scheduler.gd
│   ├── agent_action_request.gd
│   └── agent_suggestion_policy.gd
├── infrastructure/
│   ├── agent_snapshot_codec.gd
│   └── agent_save_section.gd
└── presentation/
    └── autonomous_character_controller.gd
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** l’arborescence place les règles pures dans `domain`, l’orchestration dans `application`, la persistance dans `infrastructure` et l’adaptation au personnage actif dans `presentation`.

- **Dépendances et ports utilisés :** **Dépendances :** `domain` ne dépend ni d’un nœud, ni d’un transport IA, ni d’une scène ; `presentation` peut dépendre des contrats de mouvement du chapitre 6.

- **Résultat attendu :** **Résultat attendu :** une simulation hors écran peut utiliser le même domaine et le même service de décision sans instancier `autonomous_character_controller.gd`.

<a id="ch17-agent-state"></a>

## 6. État logique de l’agent

L’état autonome est indexé par le `CharacterId` du propriétaire, mais il n’est pas stocké dans `CharacterRuntimeState`.

> **[VSC] Visual Studio Code — Créer : `res://src/features/agents/domain/agent_state.gd`.**

```gdscript
class_name AgentState
extends RefCounted

const MAX_GOALS := 16

var owner_character_id: StringName
var policy_id: StringName
var durable_goals: Array[AgentGoal] = []
var decision_sequence: int = 0
var random_seed: int = 0
var random_state: int = 0
var last_decision_tick: int = -1

func validate() -> Error:
	if not CharacterId.is_valid(owner_character_id):
		return ERR_INVALID_DATA
	if not StableId.is_valid(policy_id):
		return ERR_INVALID_DATA
	if durable_goals.size() > MAX_GOALS:
		return ERR_OUT_OF_MEMORY
	if decision_sequence < 0 or last_decision_tick < -1:
		return ERR_INVALID_DATA
	for goal: AgentGoal in durable_goals:
		if goal == null or goal.validate() != OK:
			return ERR_INVALID_DATA
	return OK

func next_sequence(logical_tick: int) -> int:
	if logical_tick < last_decision_tick:
		return -1
	decision_sequence += 1
	last_decision_tick = logical_tick
	return decision_sequence
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** `AgentState` conserve uniquement les données durables nécessaires à la continuité et à la reproductibilité de l’agent.

- **Paramètres et types importants :** **Données importantes :** `owner_character_id` relie l’agent à une identité métier ; `policy_id` sélectionne sa politique ; `durable_goals` est borné ; `decision_sequence` ordonne les décisions ; `random_seed` et `random_state` permettent de restaurer une suite pseudo-aléatoire lorsqu’une variation autorisée l’exige.

- **Valeur de retour ou code d’échec :** **Valeurs de retour :** `validate()` renvoie un code de l’énumération `Error`. `next_sequence()` renvoie une séquence strictement positive après succès, ou la sentinelle `-1` lorsque le tick régresse ; dans ce dernier cas, aucun compteur n’est modifié.

- **Effets de bord :** **Effets de bord :** `next_sequence()` incrémente la séquence et mémorise le tick uniquement après la vérification d’ordre.

- **Invariants protégés :** **Invariants protégés :** identité stable, nombre de buts borné, séquence croissante et temps logique non décroissant.

- **Résultat attendu :** **Résultat attendu :** deux exécutions restaurées avec le même snapshot, les mêmes observations et le même ordre de ticks commencent avec le même état de décision.

- **Limites et réserves :** La mémoire, le tableau noir, l’intention et le plan ne figurent pas dans cette classe. Ils sont reconstruits ou invalidés.

## 7. Représenter un fait perçu

Un fait décrit une observation datée. Il ne conserve ni `Node`, ni `Resource` partagée, ni référence de scène.

> **[VSC] Visual Studio Code — Créer : `res://src/features/agents/domain/agent_fact.gd`.**

```gdscript
class_name AgentFact
extends RefCounted

const MAX_CONFIDENCE := 1000
const NO_EXPIRATION := -1

enum Kind {
	CHARACTER_VISIBLE,
	CHARACTER_LAST_POSITION,
	SOCIAL_ATTITUDE,
	DANGER_REPORTED,
	RESOURCE_AVAILABLE,
	LOCATION_REACHED,
}

var fact_id: StringName
var kind: Kind
var subject_id: StringName
var object_id: StringName = &""
var position: Vector3 = Vector3.ZERO
var value: int = 0
var confidence: int = MAX_CONFIDENCE
var observed_tick: int = 0
var expires_at_tick: int = NO_EXPIRATION
var source_system: StringName

func validate() -> Error:
	if not StableId.is_valid(fact_id):
		return ERR_INVALID_DATA
	if subject_id.is_empty() or source_system.is_empty():
		return ERR_INVALID_DATA
	if confidence < 0 or confidence > MAX_CONFIDENCE:
		return ERR_INVALID_DATA
	if observed_tick < 0:
		return ERR_INVALID_DATA
	if expires_at_tick != NO_EXPIRATION and expires_at_tick < observed_tick:
		return ERR_INVALID_DATA
	if not position.is_finite():
		return ERR_INVALID_DATA
	return OK

func is_expired(logical_tick: int) -> bool:
	return expires_at_tick != NO_EXPIRATION and logical_tick > expires_at_tick
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** cette valeur transporte une observation structurée avec sa provenance, sa confiance et sa durée de validité.

- **Paramètres et types importants :** **Types et sentinelle :** `Kind` ferme le vocabulaire initial ; `confidence` utilise un entier de `0` à `1000` pour éviter les comparaisons flottantes ambiguës ; `NO_EXPIRATION` signifie que seule une invalidation explicite retire le fait.

- **Invariants protégés :** **Validation :** une position non finie, un tick négatif ou une expiration antérieure à l’observation rendent le fait invalide.

- **Temps logique et expiration :** **Sémantique temporelle :** un fait reste valide au tick `expires_at_tick` et devient expiré au tick suivant.

- **Limites et réserves :** **Limite :** `confidence` exprime la confiance du modèle de jeu, pas une probabilité scientifique de vérité.

## 8. Mémoire de travail bornée

La mémoire remplace un fait portant le même `fact_id`, retire les faits expirés et évince les plus anciens lorsque la capacité est atteinte.

> **[VSC] Visual Studio Code — Créer : `res://src/features/agents/domain/agent_memory.gd`.**

```gdscript
class_name AgentMemory
extends RefCounted

const MAX_FACTS := 128

var _facts_by_id: Dictionary[StringName, AgentFact] = {}

func remember(fact: AgentFact, logical_tick: int) -> Error:
	if fact == null or fact.validate() != OK:
		return ERR_INVALID_DATA
	forget_expired(logical_tick)
	if not _facts_by_id.has(fact.fact_id) and _facts_by_id.size() >= MAX_FACTS:
		_evict_oldest()
	_facts_by_id[fact.fact_id] = fact
	return OK

func forget_expired(logical_tick: int) -> void:
	var expired_ids: Array[StringName] = []
	for fact_id: StringName in _facts_by_id:
		var fact := _facts_by_id[fact_id]
		if fact.is_expired(logical_tick):
			expired_ids.append(fact_id)
	for fact_id: StringName in expired_ids:
		_facts_by_id.erase(fact_id)

func read_all(logical_tick: int) -> Array[AgentFact]:
	forget_expired(logical_tick)
	var result: Array[AgentFact] = []
	result.assign(_facts_by_id.values())
	result.sort_custom(
		func(left: AgentFact, right: AgentFact) -> bool:
			if left.observed_tick != right.observed_tick:
				return left.observed_tick > right.observed_tick
			return String(left.fact_id) < String(right.fact_id)
	)
	return result

func _evict_oldest() -> void:
	var oldest_id: StringName = &""
	var oldest_tick := 9223372036854775807
	for fact_id: StringName in _facts_by_id:
		var fact := _facts_by_id[fact_id]
		if fact.observed_tick < oldest_tick:
			oldest_tick = fact.observed_tick
			oldest_id = fact_id
		elif fact.observed_tick == oldest_tick and String(fact_id) < String(oldest_id):
			oldest_id = fact_id
	if not oldest_id.is_empty():
		_facts_by_id.erase(oldest_id)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** `AgentMemory` maintient un ensemble borné de faits récents sans exposer son dictionnaire interne.

- **Paramètres et types importants :** **Entrées :** `remember()` reçoit un fait déjà structuré et le tick logique courant ; `read_all()` utilise le tick pour nettoyer avant lecture.

- **Effets de bord :** **Effets de bord :** mémoriser peut supprimer les faits expirés, évincer un fait ancien puis insérer ou remplacer une entrée.

- **Déterminisme et ordre :** **Ordre déterministe :** les lectures trient d’abord par récence décroissante, puis par `fact_id` ; l’éviction départage deux faits du même tick par leur identifiant.

- **Copies et mutabilité :** **Copie défensive :** le tableau retourné est nouveau, mais les objets `AgentFact` restent partagés et doivent être traités comme immuables après insertion.

- **Limites et réserves :** **Limite :** pour autoriser la mutation d’un fait, il faudrait retourner des duplications profondes ou remplacer systématiquement l’objet complet.

## 9. Tableau noir à clés autorisées

Le tableau noir contient de petites valeurs de coordination. Une clé doit être déclarée dans un schéma ; un dictionnaire libre transformerait les fautes de frappe en état caché.

> **[VSC] Visual Studio Code — Créer : `res://src/features/agents/domain/agent_blackboard.gd`.**

```gdscript
class_name AgentBlackboard
extends RefCounted

const MAX_ENTRIES := 32

var _allowed_keys: Dictionary[StringName, int] = {}
var _values: Dictionary[StringName, Variant] = {}

func configure(schema: Dictionary[StringName, int]) -> Error:
	if schema.is_empty() or schema.size() > MAX_ENTRIES:
		return ERR_INVALID_DATA
	_allowed_keys = schema.duplicate()
	_values.clear()
	return OK

func write(key: StringName, value: Variant) -> Error:
	if not _allowed_keys.has(key):
		return ERR_DOES_NOT_EXIST
	if typeof(value) != _allowed_keys[key]:
		return ERR_INVALID_DATA
	_values[key] = value
	return OK

func read(key: StringName, default_value: Variant = null) -> Variant:
	return _values.get(key, default_value)

func snapshot() -> Dictionary[StringName, Variant]:
	return _values.duplicate(true)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** ce contrat limite les clés et le type `Variant.Type` accepté pour chacune d’elles.

- **Configuration :** **Configuration :** `configure()` copie le schéma afin que l’appelant ne puisse pas modifier ultérieurement la liste autorisée par alias de dictionnaire.

- **Codes de retour de `write()` :** **Codes de retour de `write()` :** une clé absente du schéma renvoie `ERR_DOES_NOT_EXIST` ; une valeur dont le type ne correspond pas au schéma renvoie `ERR_INVALID_DATA`. Dans les deux cas, `_values` reste inchangé.

- **Effets de bord :** **Effets de bord :** reconfigurer efface les anciennes valeurs ; écrire remplace la valeur associée à une clé valide.

- **Copie profonde :** **Copie profonde :** `snapshot()` duplique aussi les tableaux et dictionnaires imbriqués, mais une `Resource` imbriquée resterait partagée ; le schéma de référence n’autorise donc que des scalaires, `StringName`, `Vector3` et petites collections de valeurs.

- **Persistance :** **Persistance :** le tableau noir n’est pas sauvegardé ; il décrit le contexte de la décision courante.

## 10. But durable

Un but exprime un état recherché. Il ne contient pas la suite d’actions prévue pour l’atteindre.

> **[VSC] Visual Studio Code — Créer : `res://src/features/agents/domain/agent_goal.gd`.**

```gdscript
class_name AgentGoal
extends RefCounted

const NO_DEADLINE := -1

enum Status {
	ACTIVE,
	SATISFIED,
	FAILED,
	CANCELLED,
}

var goal_id: StringName
var goal_type: StringName
var target_character_id: StringName = &""
var target_position: Vector3 = Vector3.ZERO
var priority: int = 0
var created_tick: int = 0
var deadline_tick: int = NO_DEADLINE
var status: Status = Status.ACTIVE
var provenance: StringName

func validate() -> Error:
	if not StableId.is_valid(goal_id) or not StableId.is_valid(goal_type):
		return ERR_INVALID_DATA
	if priority < -1000 or priority > 1000:
		return ERR_INVALID_DATA
	if created_tick < 0:
		return ERR_INVALID_DATA
	if deadline_tick != NO_DEADLINE and deadline_tick < created_tick:
		return ERR_INVALID_DATA
	if not target_position.is_finite() or provenance.is_empty():
		return ERR_INVALID_DATA
	return OK

func is_actionable(logical_tick: int) -> bool:
	if status != Status.ACTIVE:
		return false
	return deadline_tick == NO_DEADLINE or logical_tick <= deadline_tick
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** `AgentGoal` porte une motivation durable, sa priorité, sa provenance et son éventuelle échéance.

- **Bornes :** **Bornes :** la priorité signée permet de désactiver temporairement un but sans inventer une valeur infinie ; les politiques peuvent néanmoins filtrer les priorités négatives.

- **États terminaux :** **États terminaux :** un but satisfait, échoué ou annulé n’est plus actionnable et doit être archivé ou retiré par le service applicatif.

- **Temps logique :** **Temps logique :** l’échéance est inclusive ; le but reste actionnable au tick de sa deadline.

- **Séparation :** **Séparation :** aucune référence vers `AgentPlan` n’est stockée, car un plan est une hypothèse transitoire invalidée par le monde.

## 11. Sélection déterministe du but

La politique trie les candidats avec des critères stables plutôt que d’utiliser l’ordre d’un dictionnaire ou un tirage implicite.

> **[LECTURE] Extrait de politique — Ajouter à un service applicatif dédié.**

```gdscript
func select_goal(
	goals: Array[AgentGoal],
	logical_tick: int,
) -> AgentGoal:
	var candidates: Array[AgentGoal] = []
	for goal: AgentGoal in goals:
		if goal != null and goal.is_actionable(logical_tick):
			candidates.append(goal)
	candidates.sort_custom(
		func(left: AgentGoal, right: AgentGoal) -> bool:
			if left.priority != right.priority:
				return left.priority > right.priority
			if left.created_tick != right.created_tick:
				return left.created_tick < right.created_tick
			return String(left.goal_id) < String(right.goal_id)
	)
	return candidates.front() if not candidates.is_empty() else null
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** cette fonction choisit le but actif le plus prioritaire avec deux critères de départage reproductibles.

- **Déroulement ou instructions importantes :** **Ordre :** une priorité élevée gagne ; à priorité égale, le but le plus ancien gagne ; une égalité restante est résolue par l’identifiant.

- **Retour :** **Retour :** l’absence de candidat produit `null` et doit conduire l’agent à une intention d’attente explicite, pas à une réutilisation silencieuse du plan précédent.

- **Effets de bord :** **Effets de bord :** le tableau d’entrée n’est pas trié ; seul `candidates` est modifié.

- **Résultat attendu et vérification :** **Vérification :** permuter l’ordre initial des mêmes buts doit produire le même `goal_id` sélectionné.

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

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** `AgentCondition` décrit une précondition de conception modifiable dans l’inspecteur et évaluée contre un snapshot booléen.

- **Valeur absente :** **Valeur absente :** une clé inexistante est lue comme `false`. Une condition qui attend `false` peut donc réussir en l’absence de clé ; cette convention doit rester stable dans tout le catalogue.

- **Retour :** **Retour :** `matches()` ne modifie ni la condition ni le dictionnaire reçu.

- **Limites et réserves :** **Limite :** les comparaisons de distance, de quantité ou de relation utilisent des faits calculés par les requêtes du monde, pas des opérateurs dynamiques stockés dans une chaîne.

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

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** `AgentEffect` décrit l’état hypothétique obtenu après une action réussie.

- **Effet de bord :** **Effet de bord :** `apply_to()` modifie le dictionnaire fourni ; le planificateur doit donc lui transmettre une copie de l’état parent.

- **Frontières d’autorité :** **Frontière :** cet effet ne mutile jamais le monde réel. Il sert uniquement à simuler la conséquence attendue pendant la recherche de plan.

- **Résultat attendu et vérification :** **Vérification :** appliquer un effet à une copie ne doit pas changer le snapshot d’origine.

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

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** cette `Resource` constitue la donnée de conception d’une action planifiable ; `executor_key` choisit l’adaptateur autorisé qui demandera l’exécution réelle.

- **Bornes :** **Bornes :** les coûts et tailles de collections sont limités afin qu’un catalogue erroné ne rende pas la recherche imprévisible.

- **Précondition :** **Précondition :** une action sans effet est refusée, car elle ne peut pas rapprocher un plan d’un état cible dans ce modèle.

- **Simulation :** **Simulation :** `simulate()` duplique le dictionnaire avant d’appliquer les effets, ce qui protège l’état parent de la recherche.

- **Immutabilité attendue :** **Immutabilité attendue :** une action chargée depuis le catalogue est traitée comme immuable pendant le gameplay.

- **Limites et réserves :** **Limite :** le coût de planification n’est pas automatiquement une durée, une dépense d’endurance ou un prix économique ; ces valeurs appartiennent aux systèmes concernés.

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

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** `AgentActionCatalog` construit un candidat complet avant de remplacer le catalogue actif.

- **Codes de retour de `replace_all()` :** **Codes de retour de `replace_all()` :** une action invalide renvoie `ERR_INVALID_DATA` ; deux actions portant le même `action_id` renvoient `ERR_ALREADY_EXISTS`. Le catalogue actif n’est remplacé qu’après validation complète du candidat.

- **Ordre stable :** **Ordre stable :** `all_sorted()` neutralise l’ordre d’insertion du dictionnaire et fournit le départage lexical utilisé par le planificateur.

- **Lecture :** **Lecture :** le tableau retourné est nouveau, mais les `Resource` restent partagées et considérées comme immuables.

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

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** ce DTO fige les entrées de lecture utilisées par une décision afin que le planificateur ne consulte pas un monde changeant au milieu de son calcul.

- **Révision :** **Révision :** `world_revision` augmente lorsqu’une mutation pertinente peut invalider un plan ; sa granularité exacte appartient au service d’agrégation du monde.

- **Bornes :** **Bornes :** le nombre de faits booléens est limité ; les identifiants et positions sont contrôlés avant planification.

- **Copie :** **Copie :** les trois collections sont dupliquées. Le contenu est composé de valeurs et ne partage pas d’objet mutable personnalisé.

- **Frontières d’autorité :** **Frontière :** les relations et liens familiaux sont lus par leurs services de requête puis convertis en faits ; leurs dépôts ne sont jamais exposés au planificateur.

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

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** l’agrégateur convertit des lectures sociales et familiales en faits utiles sans modifier les systèmes interrogés.

- **Dépendances et ports utilisés :** **Dépendances :** `_social_query`, `_family_query` et `_world_revision_source` sont des contrats injectés ; `_focus_target_id` provient du contexte de décision validé.

- **Valeurs dérivées :** **Valeurs dérivées :** le seuil de confiance appartient à une politique d’agent versionnée, pas à `SocialRelationshipState`.

- **Résultat :** **Résultat :** le snapshot peut encore être refusé par `validate()` avant d’être transmis au planificateur.

- **Limites et réserves :** **Limite :** ce petit exemple ne définit pas la visibilité physique, la navigation, le combat ni l’économie.

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

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** `AgentPlan` conserve une suite ordonnée d’identifiants d’actions liée à un but et à la révision du snapshot utilisé.

- **Données transitoires :** **Données transitoires :** le plan est validable et diagnosticable, mais il n’est pas une donnée durable de sauvegarde.

- **Invalidation :** **Invalidation :** si la révision courante diffère de `snapshot_revision`, le service revalide au minimum la prochaine action ou reconstruit le plan.

- **Frontières d’autorité :** **Frontière :** `total_cost` permet de comparer des plans ; il ne garantit pas que l’exécution réelle réussira.

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

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** le résultat transporte un statut fermé, le plan éventuel et le nombre de nœuds développés pour le diagnostic.

- **Retour de fabrique :** **Retour de fabrique :** `found()` garantit que le statut et le plan sont assignés ensemble ; les autres statuts utilisent des fabriques équivalentes dans l’implémentation complète.

- **Statuts à distinguer :** **Statuts à distinguer :** `NO_PLAN` signifie qu’aucune action n’est à exécuter dans le résultat courant : soit le but est déjà satisfait, soit la recherche complète n’a trouvé aucun chemin autorisé. `BUDGET_EXCEEDED` signifie que la limite d’expansions a interrompu la recherche avant qu’elle puisse conclure.

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
	var parts := PackedStringArray()
	for action_id: StringName in action_ids:
		parts.append(String(action_id))
	return ",".join(parts)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** cet objet est une structure de travail du planificateur et n’appartient ni au domaine persistant ni au monde actif.

- **Signature :** **Signature :** la chaîne d’identifiants sert uniquement au départage stable de deux chemins de coût et profondeur identiques.

- **Limites et réserves :** **Limite :** concaténer de longues signatures coûte de la mémoire ; la profondeur maximale faible du planificateur rend ce choix acceptable pour le parcours pédagogique.

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

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** cette recherche de coût uniforme explore un espace booléen borné et retourne un statut explicite plutôt qu’une liste vide ambiguë.

- **Paramètres et types importants :** **Entrées :** le snapshot, le but et chaque condition sont validés avant la création de la frontière ; le catalogue fournit déjà des actions valides triées.

- **Budgets déterministes :** **Budgets déterministes :** `MAX_EXPANSIONS` et `MAX_PLAN_DEPTH` limitent la quantité de travail de manière indépendante de la vitesse du processeur.

- **Déroulement ou instructions importantes :** **Déroulement :** le meilleur nœud est retiré, le but est testé, puis les actions applicables produisent des enfants sur des copies de faits.

- **Élagage :** **Élagage :** `best_cost_by_state` ignore un état déjà atteint à coût inférieur ou égal ; la clé canonique trie les faits pour ne pas dépendre de l’ordre du dictionnaire.

- **Départage :** **Départage :** coût, profondeur et signature donnent le même choix avec les mêmes entrées.

- **Cas déjà satisfait :** **Cas déjà satisfait :** le modèle retourne ici `NO_PLAN` avec un message spécifique ; le service de décision peut alors marquer le but satisfait au lieu d’exécuter une action vide.

- **Complexité :** **Complexité :** trier toute la frontière à chaque retrait reste pédagogique, mais une file de priorité spécialisée sera préférable si les budgets augmentent.

- **Résultat attendu et vérification :** **Vérification :** exécuter la même recherche après permutation du catalogue doit conserver le statut, le coût et la liste d’actions.

## 20. Pourquoi le budget en microsecondes n’est pas l’autorité

`Time.get_ticks_usec()` est monotone et utile pour mesurer. Toutefois, interrompre le planificateur uniquement parce qu’une machine a consommé plus de microsecondes peut produire des décisions différentes sur deux matériels.

La règle de référence est donc :

> **[LECTURE] Budgets complémentaires — Ne pas saisir.**

```text
budget autoritaire : nombre d’expansions, profondeur, agents par tick
budget de sécurité : microsecondes observées, alerte, report du travail restant
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** le premier budget protège la reproductibilité ; le second protège la fluidité et fournit une télémétrie dépendante de la machine.

- **Résultat attendu et conséquences :** **Conséquence :** une mesure trop élevée peut dégrader la fréquence future ou déclencher un diagnostic, mais elle ne change pas rétroactivement le résultat d’une recherche déjà autorisée par son budget logique.

- **Lien avec le moteur :** **Lien moteur :** l’horloge monotone évite les sauts de l’heure système, mais elle ne rend pas deux processeurs aussi rapides.

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

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** cette commande transporte l’identité de la décision, l’action choisie et le contexte minimal nécessaire à l’exécuteur.

- **Corrélation et révisions :** **Corrélation :** `request_id` distingue deux tentatives ; `decision_sequence` ordonne les décisions du même agent ; `snapshot_revision` permet de refuser une requête fondée sur un monde obsolète.

- **Cibles et données optionnelles :** **Cibles :** une action peut utiliser une identité, une position ou aucune cible. L’exécuteur vérifie les champs réellement requis par son contrat.

- **Frontières d’autorité :** **Frontière :** aucune valeur d’effet autoritaire n’est incluse. Une future requête de combat ne transporte pas directement « points de vie après attaque ».

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

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** `AgentDecisionService` constitue le point d’orchestration d’une décision et émet une requête seulement après validation complète.

- **Déroulement ou instructions importantes :** **Ordre :** il valide l’état et ses dépendances, réserve une séquence, construit un snapshot, choisit un but, planifie, recontrôle la révision puis fabrique la requête.

- **Révision concurrente :** **Révision concurrente :** si le monde change pendant le calcul, le plan n’est pas appliqué ; `ERR_BUSY` invite l’ordonnanceur à reprogrammer une décision.

- **Absence de but :** **Absence de but :** retourner `OK` sans signal signifie que l’attente est une issue normale, distincte d’un échec de planification.

- **Effets de bord :** **Effets de bord :** la séquence de l’agent avance et un signal typé peut être émis. Aucun état social, familial, physique ou de combat n’est modifié ici.

- **Dépendances et ports utilisés :** **Ports :** `AgentSnapshotBuilder`, `AgentGoalPolicy`, `AgentGoalConditionCatalog` et `WorldRevisionSource` sont définis par les signatures immédiatement suivantes ; leurs implémentations restent injectées.

### 22.1 Signatures des ports de décision

| Port | Signature minimale | Responsabilité |
|---|---|---|
| `AgentSnapshotBuilder` | `build_snapshot(character_id: StringName, logical_tick: int) -> AgentWorldSnapshot` | agréger des lectures autorisées dans un snapshot détaché |
| `AgentGoalPolicy` | `select_goal(goals: Array[AgentGoal], logical_tick: int) -> AgentGoal` | choisir un but avec un ordre stable |
| `AgentGoalConditionCatalog` | `get_for(goal_type: StringName) -> Array[AgentCondition]` | fournir les conditions validées d’un type de but |
| `WorldRevisionSource` | `current_revision() -> int` | exposer la révision monotone utilisée pour l’invalidation |
| `AgentStateRepository` | `replace_all(states: Array[AgentState]) -> Error` | remplacer atomiquement les états durables |
| `AgentRuntimeRegistry` | `all_character_ids_sorted() -> Array[StringName]` et `get_runtime(character_id: StringName) -> AgentRuntime` | fournir les runtimes transitoires dans un ordre canonique |

Ces ports ne sont pas des Service Locators. Ils sont construits au bootstrap et injectés uniquement dans les services qui en ont besoin.

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

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** ce port impose trois opérations distinctes : prévalidation, démarrage et demande d’annulation.

- **Valeur de retour ou code d’échec :** **Retours :** la classe de base refuse par défaut ; une implémentation doit remplacer chaque méthode qu’elle supporte.

- **Annulation :** **Annulation :** `cancel()` est coopérative. Un mouvement déjà transmis au contrôleur peut nécessiter un tick supplémentaire avant l’arrêt observable.

- **Frontières d’autorité :** **Frontière :** l’exécuteur adapte la requête au service propriétaire. Il ne réimplémente pas les règles du système cible.

- **Point d’explication complémentaire :** Exemples de clés :

> **[LECTURE] Vocabulaire d’exécuteurs — Ne pas saisir.**

```text
agent.executor.wait
agent.executor.move_intent
agent.executor.social_command
agent.executor.family_command
agent.executor.combat_command
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** ces identifiants découplent les `Resource` de conception des classes concrètes composées au bootstrap.

- **Disponibilité et limites :** **Disponibilité :** les deux premières clés peuvent être matérialisées dans ce chapitre ; les exécuteurs de combat restent indisponibles avant le chapitre 18.

- **Refus contrôlé :** **Refus contrôlé :** une clé absente du registre renvoie un échec explicite. Elle ne déclenche jamais le chargement d’une classe ou l’appel dynamique d’une méthode indiquée par les données.

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

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** ce nœud adapte une action autonome au même contrat d’intention que le contrôleur humain, sans appeler directement `Input` ni déplacer le corps.

- **Initialisation :** **Initialisation :** l’identité et le puits d’intention sont obligatoires avant toute requête.

- **Traitement physique :** **Traitement physique :** la direction XZ est recalculée à chaque tick depuis la position actuelle ; le moteur de mouvement reste responsable de la vitesse, des collisions et de `move_and_slide()`.

- **Annulation :** **Annulation :** une intention neutre est envoyée afin d’arrêter la commande précédente ; une requête inconnue ne modifie pas le contrôleur.

- **Limites et réserves :** **Limites :** l’exemple ne traite ni navigation, ni obstacles, ni distance d’arrivée. Une implémentation complète injectera un port de navigation sans déplacer les règles de décision dans `NavigationAgent3D`.

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

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** cette politique associe un mode explicite à une fréquence de décision, sans déduire l’existence métier de la présence dans la scène.

- **Intervalles et cadence :** **Intervalles nominaux :** avec `Engine.physics_ticks_per_second = 60`, le mode `ACTIVE` utilise `6` ticks, soit au plus `10` décisions par seconde ; `BACKGROUND` utilise `60` ticks, soit au plus `1` décision par seconde ; `DORMANT` utilise `600` ticks, soit au plus `1` décision toutes les `10` secondes. Ces équivalences changent si la fréquence physique du projet change. Elles restent nominales : lorsqu’un agent échu est reporté par le budget de l’ordonnanceur, sa décision réelle peut survenir plus tard, mais l’échéance demeure exprimée en ticks logiques.

- **Persistance et mode dormant :** **Mode dormant :** dormant ne signifie pas supprimé ; les buts durables et l’état persistent.

- **Frontières d’autorité :** **Frontière :** le système de partition du monde choisit le mode. Le registre des personnages actifs ne constitue qu’un signal parmi d’autres.

- **Limites et réserves :** Une simulation hors écran ne doit pas reproduire à haute fidélité la physique, la navigation et les animations. Elle produit des transitions logiques autorisées et laisse le chapitre 22 définir la simulation globale du monde vivant.

## 26. Politique de tick

La fréquence de décision est distincte de la fréquence d’exécution d’une action. Un déplacement actif peut produire une intention à chaque tick physique tout en ne replanifiant que toutes les six étapes.

> **[VSC] Visual Studio Code — Créer : `res://src/features/agents/application/agent_tick_policy.gd`.**

```gdscript
class_name AgentTickPolicy
extends RefCounted

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

	var normalized_phase := posmod(phase, interval)
	var remainder := posmod(last_decision_tick + normalized_phase, interval)
	var ticks_until_next_slot := interval - remainder
	var next_due_tick := last_decision_tick + ticks_until_next_slot
	return logical_tick >= next_due_tick
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** la politique calcule la première échéance canonique strictement postérieure à la dernière décision, puis indique si cette échéance est atteinte ou dépassée.

- **Déroulement ou instructions importantes :** **Phase :** `posmod()` ramène `phase` dans l’intervalle positif. La phase est dérivée de manière stable depuis le `CharacterId` ; elle ne provient pas d’un tirage aléatoire au démarrage.

- **Déterminisme et échéances :** **Report conservé :** la comparaison `logical_tick >= next_due_tick` maintient l’agent échu tant que l’ordonnanceur ne l’a pas traité. Avec l’ancien test d’égalité modulo, un agent non visité au tick exact pouvait attendre tout un intervalle supplémentaire.

- **Déroulement ou instructions importantes — complément 2 :** **Rattrapage borné :** après une longue pause, `decide()` n’est appelé qu’une fois pour l’agent et observe le monde courant ; les créneaux manqués ne sont pas rejoués un par un.

- **Résultat attendu et vérification :** **Vérification :** deux agents de phases différentes répartissent leurs échéances, et un agent dépassant son créneau reste dû au tick suivant jusqu’à sa décision.

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

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** ce nœud distribue les décisions sans parcourir indéfiniment tous les agents à chaque tick physique.

- **Ordre autoritaire :** **Ordre autoritaire :** le registre renvoie des identités triées ; le curseur avance du nombre d’entrées visitées, ce qui évite de favoriser toujours les premiers identifiants.

- **Budgets et limites :** **Budget :** `MAX_DECISIONS_PER_PHYSICS_TICK` contrôle le travail déterministe. `WARNING_BUDGET_USEC` ne coupe pas la boucle et sert uniquement à signaler un coût matériel élevé.

- **Temps logique et mesure :** **Temps :** `_logical_tick` est local à cet exemple. Dans le projet complet, il doit provenir de l’horloge de simulation autoritaire utilisée par les autres systèmes.

- **Valeur de retour ou traitement du résultat :** **Traitement du résultat :** le code renvoyé par `decide()` doit être enregistré dans une trace ou un compteur. L’extrait ne le consomme pas afin de rester centré sur l’ordonnancement ; cette omission pédagogique ne signifie pas que l’application finale peut ignorer le résultat.

- **Limites et réserves :** **Limite :** l’ordonnanceur s’exécute sur le thread principal. Une future parallélisation exige des snapshots immuables et interdit tout accès aux nœuds depuis les workers.

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

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** cette séquence évite d’appliquer la suite d’un plan construit pour un monde ancien.

- **Déroulement ou instructions importantes :** **Ordre :** l’annulation est demandée avant d’oublier l’identifiant de la requête active ; sinon l’exécuteur ne pourrait plus être corrélé.

- **Résultat :** **Résultat :** une nouvelle décision repart des données autoritaires, pas de l’état hypothétique du plan abandonné.

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

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** cette valeur résume une décision pour les journaux, tests de reproductibilité et outils Studio.

- **Diagnostic :** **Diagnostic :** `diagnostic_hash` est calculé depuis une représentation canonique des entrées pertinentes et de la sortie ; il ne constitue ni une signature de sécurité ni une preuve de vérité.

- **Données exclues :** **Données exclues :** le texte généré, les prompts complets, les nœuds, les collections mutables et les secrets ne figurent pas dans le record.

- **Persistance :** **Persistance :** la trace de diagnostic peut être conservée dans un journal rotatif séparé, mais elle n’appartient pas au snapshot autoritaire de l’agent.

- **Limites et réserves :** Une trace mémoire de référence est bornée à `64` décisions par agent. Le chapitre 28 approfondira les journaux, corrélations et replays.

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

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** cette fonction choisit une variante dans un ordre canonique puis sauvegarde le nouvel état du générateur.

- **Initialisation :** **Initialisation :** la graine est assignée avant l’état restauré ; l’état doit provenir d’une instance précédente et ne doit pas être inventé arbitrairement.

- **Effet de bord :** **Effet de bord :** `state.random_state` avance exactement une fois après le tirage.

- **Frontières d’autorité :** **Frontière :** un tirage ne départage pas deux actions ayant des conséquences métier différentes dans la politique de référence.

- **Résultat attendu et vérification :** **Vérification :** restaurer le même couple graine/état et le même tableau de variantes doit produire le même choix et le même nouvel état.

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

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** cette politique transforme une sortie externe non fiable en une petite liste d’identifiants déjà présents dans le catalogue local.

- **Filtrage :** **Filtrage :** les doublons, identifiants inconnus et entrées au-delà de la limite sont retirés.

- **Déroulement ou instructions importantes :** **Ordre :** le résultat est trié ; la formulation ou l’ordre de la réponse générative ne devient pas un départage autoritaire implicite.

- **Étape suivante :** **Étape suivante :** le planificateur revalide toujours les préconditions, effets, coûts et budgets.

- **Repli :** **Repli :** en cas d’indisponibilité, de timeout ou de capacité absente, la politique déterministe complète s’exécute sans suggestion.

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
      "target_position": {"x": 12.0, "y": 0.0, "z": -4.0},
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

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** ce document décrit les données nécessaires pour reprendre les motivations durables et la suite pseudo-aléatoire de l’agent.

- **Version :** **Version :** `format` et `version` sont contrôlés avant tout décodage ; une version future est refusée.

- **Vecteur :** **Vecteur :** `target_position` utilise le dictionnaire `{x, y, z}` du `SaveValueCodec` introduit au chapitre 9 ; chaque composante doit être numérique et finie.

- **Statut :** **Statut :** la chaîne `active` est mappée vers l’énumération ; une valeur inconnue n’est pas convertie silencieusement.

- **Données absentes :** **Données absentes :** après chargement, le premier passage reconstruit perceptions et plan depuis le monde restauré.

## 33. Codec strict et section de sauvegarde

Le codec suit les mêmes règles que les chapitres 14 à 16 : clés exactes, types contrôlés, références validées et candidat complet.

> **[LECTURE] Contrat du codec — Structure de référence.**

```gdscript
class_name AgentSnapshotCodec
extends RefCounted

const FORMAT := "project-asteria-agent-state"
const VERSION := 1
const REQUIRED_KEYS := PackedStringArray([
	"format",
	"version",
	"owner_character_id",
	"policy_id",
	"decision_sequence",
	"random_seed",
	"random_state",
	"last_decision_tick",
	"durable_goals",
])

func encode(state: AgentState) -> Dictionary:
	if state == null or state.validate() != OK:
		return {}
	var encoded_goals: Array[Dictionary] = []
	for goal: AgentGoal in state.durable_goals:
		if goal.status != AgentGoal.Status.ACTIVE:
			continue
		encoded_goals.append(_encode_goal(goal))
	return {
		"format": FORMAT,
		"version": VERSION,
		"owner_character_id": String(state.owner_character_id),
		"policy_id": String(state.policy_id),
		"decision_sequence": state.decision_sequence,
		"random_seed": state.random_seed,
		"random_state": state.random_state,
		"last_decision_tick": state.last_decision_tick,
		"durable_goals": encoded_goals,
	}

func decode(
	raw: Dictionary,
	identities: CharacterIdentityIndex,
) -> AgentState:
	if identities == null or not _has_exact_keys(raw, REQUIRED_KEYS):
		return null
	if raw.get("format") != FORMAT or raw.get("version") != VERSION:
		return null
	for key: String in [
		"decision_sequence",
		"random_seed",
		"random_state",
		"last_decision_tick",
	]:
		if not raw[key] is int:
			return null
	if not raw["owner_character_id"] is String:
		return null
	if not raw["policy_id"] is String or not raw["durable_goals"] is Array:
		return null

	var owner_id := StringName(raw["owner_character_id"])
	if not CharacterId.is_valid(owner_id) or not identities.contains(owner_id):
		return null
	var state := AgentState.new()
	state.owner_character_id = owner_id
	state.policy_id = StringName(raw["policy_id"])
	state.decision_sequence = raw["decision_sequence"]
	state.random_seed = raw["random_seed"]
	state.random_state = raw["random_state"]
	state.last_decision_tick = raw["last_decision_tick"]

	var goal_ids: Dictionary[StringName, bool] = {}
	for item: Variant in raw["durable_goals"]:
		if not item is Dictionary:
			return null
		var goal := _decode_goal(item, identities)
		if goal == null or goal_ids.has(goal.goal_id):
			return null
		goal_ids[goal.goal_id] = true
		state.durable_goals.append(goal)
	return state if state.validate() == OK else null

func _encode_goal(goal: AgentGoal) -> Dictionary:
	return {
		"goal_id": String(goal.goal_id),
		"goal_type": String(goal.goal_type),
		"target_character_id": String(goal.target_character_id),
		"target_position": SaveValueCodec.vector3_to_dictionary(goal.target_position),
		"priority": goal.priority,
		"created_tick": goal.created_tick,
		"deadline_tick": goal.deadline_tick,
		"status": "active",
		"provenance": String(goal.provenance),
	}

func _decode_goal(
	raw: Dictionary,
	identities: CharacterIdentityIndex,
) -> AgentGoal:
	var required := PackedStringArray([
		"goal_id", "goal_type", "target_character_id", "target_position",
		"priority", "created_tick", "deadline_tick", "status", "provenance",
	])
	if not _has_exact_keys(raw, required):
		return null
	for key: String in ["goal_id", "goal_type", "target_character_id", "status", "provenance"]:
		if not raw[key] is String:
			return null
	for key: String in ["priority", "created_tick", "deadline_tick"]:
		if not raw[key] is int:
			return null
	if not raw["target_position"] is Dictionary or raw["status"] != "active":
		return null

	var errors := PackedStringArray()
	var goal := AgentGoal.new()
	goal.goal_id = StringName(raw["goal_id"])
	goal.goal_type = StringName(raw["goal_type"])
	goal.target_character_id = StringName(raw["target_character_id"])
	if not goal.target_character_id.is_empty() and not identities.contains(goal.target_character_id):
		return null
	goal.target_position = SaveValueCodec.dictionary_to_vector3(
		raw["target_position"], errors, "durable_goals.target_position"
	)
	if not errors.is_empty():
		return null
	goal.priority = raw["priority"]
	goal.created_tick = raw["created_tick"]
	goal.deadline_tick = raw["deadline_tick"]
	goal.status = AgentGoal.Status.ACTIVE
	goal.provenance = StringName(raw["provenance"])
	return goal if goal.validate() == OK else null

func _has_exact_keys(raw: Dictionary, expected: PackedStringArray) -> bool:
	if raw.size() != expected.size():
		return false
	for key: String in expected:
		if not raw.has(key):
			return false
	return true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** le codec encode les données durables et reconstruit un candidat après contrôle exact du format, de la version, des clés, des types et des identités.

- **Encodage :** **Encodage :** seuls les buts actifs sont écrits ; les positions passent par `SaveValueCodec` et les identifiants deviennent des chaînes JSON.

- **Décodage :** **Décodage :** les entiers sont exigés comme tels dans le dictionnaire déjà normalisé par la chaîne de sauvegarde ; chaque but possède des clés exactes et une cible connue lorsqu’elle est renseignée.

- **Doublons :** **Doublons :** `goal_ids` refuse deux buts portant le même identifiant avant leur insertion dans l’état candidat.

- **Valeur de retour ou code d’échec :** **Retours :** `{}` signale un état source invalide à l’appelant d’encodage ; `null` signale un payload refusé sans mutation du dépôt.

- **Limites et réserves :** **Limite :** l’état interne du RNG ne peut pas être validé par sa forme seule ; il doit provenir d’un snapshot produit par cette version du projet et reste couvert par les tests de reprise.

> **[VSC] Visual Studio Code — Créer : `res://src/features/agents/infrastructure/agent_save_section.gd`.**

```gdscript
class_name AgentSaveSection
extends SaveSection

var _prepared_states: Dictionary[StringName, AgentState] = {}
var _is_prepared: bool = false
var _codec: AgentSnapshotCodec
var _identity_index: CharacterIdentityIndex
var _repository: AgentStateRepository

func prepare_load(raw: Variant) -> Error:
	_prepared_states.clear()
	_is_prepared = false
	if _codec == null or _identity_index == null or _repository == null:
		return ERR_UNCONFIGURED
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
	_is_prepared = true
	return OK

func apply_prepared() -> Error:
	if not _is_prepared:
		return ERR_UNCONFIGURED
	var states: Array[AgentState] = []
	states.assign(_prepared_states.values())
	var result := _repository.replace_all(states)
	if result == OK:
		_prepared_states.clear()
		_is_prepared = false
	return result

func cancel_load() -> void:
	_prepared_states.clear()
	_is_prepared = false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** la section décode tous les agents dans un candidat avant de demander un remplacement global au dépôt.

- **Dépendances et ports utilisés :** **Dépendances :** l’absence du codec, de l’index ou du dépôt produit `ERR_UNCONFIGURED` avant lecture du payload.

- **Échec fermé :** **Échec fermé :** une entrée invalide ou dupliquée vide le candidat et laisse `_is_prepared` à `false`.

- **Conversion typée :** **Conversion typée :** `states.assign()` construit explicitement un `Array[AgentState]` depuis les valeurs du dictionnaire.

- **Application :** **Application :** aucune application n’est possible avant une préparation réussie ; le candidat est consommé seulement après remplacement réussi.

- **Annulation :** **Annulation :** les données préparées et le drapeau sont supprimés sans effet sur le dépôt.

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

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** la scène sépare l’ordonnanceur, la représentation active, une cible spatiale et l’affichage de diagnostic.

- **Résultat attendu :** **Résultat attendu :** l’agent construit une requête de déplacement, le contrôleur produit des intentions, puis une invalidation de cible annule l’action et déclenche une nouvelle décision.

- **Limites et réserves :** **Limite :** la scène ne prouve pas la correction runtime tant qu’elle n’est pas matérialisée et exécutée.

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

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** ce script confirme uniquement les références de scène et affiche la cible initiale.

- **Annotations de scène :** **Annotations de scène :** `@onready` diffère la résolution des nœuds jusqu’à l’entrée dans l’arbre.

- **Sortie :** **Sortie :** trois lignes doivent apparaître dans l’onglet Output ; elles ne constituent pas un test de planification.

- **Réserve :** **Réserve :** le scénario complet sera connecté après matérialisation des contrats du Starter Kit.

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

**Pourquoi cet exemple est fautif :** un plan transitoire devient une propriété de l’état autoritaire du personnage et complique sa sauvegarde.

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var runtime := agent_registry.get_runtime(character_id)
runtime.current_plan = planner.plan(snapshot, goal, conditions, catalog).plan
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** le plan reste dans un runtime d’agent reconstructible et séparé de `CharacterRuntimeState`.

### 37.2 Conserver des nœuds dans la mémoire

**Symptôme ou risque :** un déchargement de scène laisse une référence invalide ou empêche la libération.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
memory[&"target"] = target_node
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la mémoire logique dépend de la durée de vie d’un nœud de présentation.

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
fact.subject_id = target_character_id
fact.position = last_known_position
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** l’identité et la dernière position restent sérialisables et vérifiables hors scène.

### 37.3 Utiliser un dictionnaire libre comme tableau noir

**Symptôme ou risque :** deux graphies créent deux états invisiblement différents.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
blackboard["targte_id"] = target_id
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la faute de frappe devient une nouvelle clé acceptée sans diagnostic.

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var error := blackboard.write(&"agent.bb.target_id", target_id)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** le schéma contrôle l’existence de la clé et le type de la valeur.

### 37.4 Persister le plan

**Symptôme ou risque :** le chargement reprend une suite d’actions calculée pour un monde ancien.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
snapshot["current_plan"] = runtime.current_plan.action_ids
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** les préconditions et cibles du plan peuvent être invalides après restauration.

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
snapshot["durable_goals"] = codec.encode_goals(state.durable_goals)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** les motivations durables sont restaurées, puis un nouveau plan est construit depuis le monde chargé.

### 37.5 Lire directement les dépôts sociaux ou familiaux

**Symptôme ou risque :** le planificateur dépend des structures internes et peut les modifier par alias.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
snapshot.facts = social_repository._states
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** une collection interne devient une entrée mutable du raisonnement.

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var view := social_query.get_mutual_view(actor_id, target_id)
snapshot.boolean_facts[&"agent.fact.target_trusted"] = view != null and view.mutual_trust >= 40
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** un port de lecture produit une valeur dérivée puis une copie simple est placée dans le snapshot.

### 37.6 Dépendre de l’ordre d’un dictionnaire

**Symptôme ou risque :** deux exécutions choisissent des actions différentes avec les mêmes données logiques.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
var selected := actions_by_id.values().front()
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** aucune règle métier ne définit quelle valeur doit apparaître en premier.

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var actions := catalog.all_sorted()
var selected := actions.front() if not actions.is_empty() else null
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** le catalogue applique un ordre canonique documenté avant la sélection.

### 37.7 Utiliser le temps CPU comme seul budget

**Symptôme ou risque :** un ordinateur lent choisit un autre plan qu’un ordinateur rapide.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
while Time.get_ticks_usec() - start < 1000:
	expand_next_node()
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** le nombre de nœuds explorés dépend de la vitesse matérielle et de la charge courante.

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
while expanded < MAX_EXPANSIONS and not frontier.is_empty():
	expand_next_node()
	expanded += 1
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** le même nombre maximal d’expansions est autorisé avec les mêmes entrées.

### 37.8 Rejouer toutes les décisions manquées

**Symptôme ou risque :** le retour d’une pause provoque une pointe de calcul et applique des décisions obsolètes.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
for tick in range(last_tick + 1, current_tick + 1):
	decide(agent, tick)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** chaque décision intermédiaire utilise un monde qui n’existe plus sous cette forme.

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
if tick_policy.is_due(current_tick, last_tick, mode, phase):
	decide(agent, current_tick)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** une seule décision observe le monde autoritaire actuel.

### 37.9 Confondre hors écran et inexistant

**Symptôme ou risque :** les buts disparaissent lorsque le personnage n’a plus de nœud actif.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
if active_registry.get_node(character_id) == null:
	agent_repository.erase(character_id)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la représentation visuelle devient l’autorité de l’existence logique.

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
runtime.mode = AgentSimulationMode.Value.BACKGROUND
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** l’agent reste enregistré et seule sa fréquence de simulation change.

### 37.10 Appliquer la suggestion générative

> **À relire :** [§ 4. Chaîne d’autorité](#ch17-authority-chain).

**Symptôme ou risque :** une sortie non déterministe contourne le catalogue et les systèmes propriétaires.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
executor.start(ai_response)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** le contenu externe est traité comme une commande déjà validée.

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var allowed_ids := suggestion_policy.filter_action_ids(raw_ids, catalog)
var result := planner.plan(snapshot, goal, conditions, catalog)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la suggestion est réduite à des identifiants connus et le planificateur reste l’autorité de sélection.

### 37.11 Oublier la révision du monde

**Symptôme ou risque :** l’agent demande une action sur une cible modifiée pendant la planification.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
action_requested.emit(request)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** aucune vérification ne confirme que le snapshot est encore actuel.

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
if revisions.current_revision() != snapshot.world_revision:
	return ERR_BUSY
action_requested.emit(request)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** une mutation pertinente force une nouvelle observation avant émission.

### 37.12 Annuler sans corrélation

**Symptôme ou risque :** l’exécuteur arrête la mauvaise action ou ignore la demande.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
executor.cancel(&"", &"world_changed")
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** aucun identifiant ne désigne la requête active.

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
executor.cancel(runtime.active_request_id, &"agent.reason.world_changed")
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la demande cible l’opération enregistrée par le runtime de l’agent.

### 37.13 Émettre avant la mutation propriétaire

**Symptôme ou risque :** les observateurs croient qu’une action a réussi avant son refus métier.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
action_completed.emit(request)
var result := social_service.apply_change(command)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** l’événement décrit un succès qui n’a pas encore été obtenu.

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var result := social_service.apply_change(command)
if result == OK:
	action_completed.emit(request)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** l’événement n’est émis qu’après l’acceptation du système autoritaire.

### 37.14 Utiliser un RNG global non restauré

**Symptôme ou risque :** une animation ou un autre système déplace la suite aléatoire de l’agent.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
var selected := variants.pick_random()
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** le choix dépend de l’état aléatoire global et de l’ordre d’autres appels.

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var selected := choose_variant(state, variants)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** un générateur propre à l’agent utilise une graine et un état restaurables.

### 37.15 Créer un exécuteur depuis une chaîne externe

**Symptôme ou risque :** une donnée non fiable choisit une classe ou une méthode arbitraire.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
var executor := load(ai_response["script_path"]).new()
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la sortie externe contrôle un chemin de code chargé au runtime.

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var executor := executor_registry.get(definition.executor_key)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la clé validée sélectionne uniquement un exécuteur composé et autorisé par le projet.

### 37.16 Paralléliser l’accès aux nœuds

**Symptôme ou risque :** un worker lit ou modifie l’arbre de scène pendant le traitement principal.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
worker_pool.add_task(func(): target_node.global_position)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la tâche capture un nœud mutable dont l’accès n’est pas isolé par un snapshot.

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var snapshot := snapshot_builder.build_snapshot(character_id, logical_tick)
worker_pool.add_task(func(): planner.plan(snapshot, goal, conditions, catalog))
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** le worker reçoit des valeurs détachées de la scène ; toute mutation reste renvoyée au thread propriétaire sous forme de résultat.

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

## 44. Synthèse opérationnelle pour Project Asteria

Le système d’agents autonomes de `Project Asteria` repose sur les décisions suivantes :

1. l’état logique d’un agent reste séparé du nœud actif, du personnage, du social et de la famille ;
2. les perceptions deviennent des faits structurés, sourcés, bornés et expirables ;
3. la mémoire et le tableau noir sont limités afin de maîtriser coût, persistance et diagnostic ;
4. les buts durables sont distincts des intentions, des plans et des requêtes d’action transitoires ;
5. le catalogue d’actions constitue un vocabulaire fermé avec préconditions, effets, coûts et exécuteurs autorisés ;
6. le planificateur utilise des snapshots détachés, un ordre canonique et des budgets logiques ;
7. l’ordonnanceur répartit les décisions par phases et conserve une échéance reportée jusqu’au traitement effectif ;
8. les modes actif, arrière-plan et dormant modifient la fréquence de décision sans supprimer l’existence logique ;
9. les plans sont invalidés lorsque la révision du monde ou les préconditions ne correspondent plus ;
10. l’IA générative reste consultative et ses suggestions sont filtrées avant toute décision métier ;
11. seules les données durables sont sauvegardées, puis restaurées dans un candidat validé avant remplacement ;
12. le combat, les compétences, l’économie, le monde vivant, la politique et la narration restent autorités de leurs propres règles.

Cette clôture décrit l’état retenu pour le projet fil rouge. Les instructions concernant le chapitre suivant restent exclusivement dans `CONTINUITE-PROJET.md`.
