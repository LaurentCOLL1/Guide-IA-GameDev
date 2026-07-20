---
title: "Livre II — Chapitre 17 : Agents IA et comportements autonomes"
id: "DOC-L2-CH17"
status: "draft"
version: "0.9.0"
lang: "fr-FR"
book: "Livre II"
chapter: 17
last-verified: "2026-07-20"
audit-status: "pending"
audit-date: null
audit-report: "Livre-II/QA/AUDIT-CHAPITRE-17.md"
audit-level: "not-audited"
reference-engine:
  name: "Godot Engine"
  version: "4.7.1-stable"
  edition: "Standard"
  language: "GDScript"
reference-project:
  name: "Project Asteria"
  renderer: "Forward+"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
recommended-reasoning: "GPT-5.6 Sol — Élevée"
---

# Agents IA et comportements autonomes

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L2-CH17`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Version de référence :** Godot `4.7.1-stable`, édition Standard, GDScript, Forward+  
> **Niveau de raisonnement conseillé :** GPT-5.6 Sol — Élevée  
> **Audit post-création :** en attente — le premier commit constitue la porte de brouillon `0.9.0`.

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

**Explication détaillée du bloc :**

- **Rôle :** ce schéma sépare le raisonnement de l’écriture autoritaire ; aucune étape de perception ou de planification ne modifie directement le monde.
- **Entrées et sorties :** les requêtes de lecture produisent un snapshot ; le planificateur produit une proposition ; le système propriétaire retourne un succès ou un refus.
- **Invariant protégé :** une conclusion de l’agent, même cohérente, ne devient pas automatiquement un fait du jeu.
- **Vérification :** une action sociale passe par `SocialRelationshipService`, une action familiale par `FamilyGraphService`, et les futures actions de combat par le service du chapitre 18.

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

**Explication détaillée du bloc :**

- **Rôle :** l’arborescence place les règles pures dans `domain`, l’orchestration dans `application`, la persistance dans `infrastructure` et l’adaptation au personnage actif dans `presentation`.
- **Dépendances :** `domain` ne dépend ni d’un nœud, ni d’un transport IA, ni d’une scène ; `presentation` peut dépendre des contrats de mouvement du chapitre 6.
- **Résultat attendu :** une simulation hors écran peut utiliser le même domaine et le même service de décision sans instancier `autonomous_character_controller.gd`.

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

**Explication détaillée du bloc :**

- **Rôle :** `AgentState` conserve uniquement les données durables nécessaires à la continuité et à la reproductibilité de l’agent.
- **Données importantes :** `owner_character_id` relie l’agent à une identité métier ; `policy_id` sélectionne sa politique ; `durable_goals` est borné ; `decision_sequence` ordonne les décisions ; `random_seed` et `random_state` permettent de restaurer une suite pseudo-aléatoire lorsqu’une variation autorisée l’exige.
- **Retours et erreurs :** `validate()` renvoie un code `Error` ; `next_sequence()` renvoie `-1` lorsque le tick régresse et n’altère alors aucun compteur.
- **Effets de bord :** `next_sequence()` incrémente la séquence et mémorise le tick uniquement après la vérification d’ordre.
- **Invariants protégés :** identité stable, nombre de buts borné, séquence croissante et temps logique non décroissant.
- **Résultat attendu :** deux exécutions restaurées avec le même snapshot, les mêmes observations et le même ordre de ticks commencent avec le même état de décision.

La mémoire, le tableau noir, l’intention et le plan ne figurent pas dans cette classe. Ils sont reconstruits ou invalidés.

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

**Explication détaillée du bloc :**

- **Rôle :** cette valeur transporte une observation structurée avec sa provenance, sa confiance et sa durée de validité.
- **Types et sentinelle :** `Kind` ferme le vocabulaire initial ; `confidence` utilise un entier de `0` à `1000` pour éviter les comparaisons flottantes ambiguës ; `NO_EXPIRATION` signifie que seule une invalidation explicite retire le fait.
- **Validation :** une position non finie, un tick négatif ou une expiration antérieure à l’observation rendent le fait invalide.
- **Sémantique temporelle :** un fait reste valide au tick `expires_at_tick` et devient expiré au tick suivant.
- **Limite :** `confidence` exprime la confiance du modèle de jeu, pas une probabilité scientifique de vérité.

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

**Explication détaillée du bloc :**

- **Rôle :** `AgentMemory` maintient un ensemble borné de faits récents sans exposer son dictionnaire interne.
- **Entrées :** `remember()` reçoit un fait déjà structuré et le tick logique courant ; `read_all()` utilise le tick pour nettoyer avant lecture.
- **Effets de bord :** mémoriser peut supprimer les faits expirés, évincer un fait ancien puis insérer ou remplacer une entrée.
- **Ordre déterministe :** les lectures trient d’abord par récence décroissante, puis par `fact_id` ; l’éviction départage deux faits du même tick par leur identifiant.
- **Copie défensive :** le tableau retourné est nouveau, mais les objets `AgentFact` restent partagés et doivent être traités comme immuables après insertion.
- **Limite :** pour autoriser la mutation d’un fait, il faudrait retourner des duplications profondes ou remplacer systématiquement l’objet complet.

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

**Explication détaillée du bloc :**

- **Rôle :** ce contrat limite les clés et le type `Variant.Type` accepté pour chacune d’elles.
- **Configuration :** `configure()` copie le schéma afin que l’appelant ne puisse pas modifier ultérieurement la liste autorisée par alias de dictionnaire.
- **Erreurs :** une clé inconnue produit `ERR_DOES_NOT_EXIST` ; un type incorrect produit `ERR_INVALID_DATA`.
- **Effets de bord :** reconfigurer efface les anciennes valeurs ; écrire remplace la valeur associée à une clé valide.
- **Copie profonde :** `snapshot()` duplique aussi les tableaux et dictionnaires imbriqués, mais une `Resource` imbriquée resterait partagée ; le schéma de référence n’autorise donc que des scalaires, `StringName`, `Vector3` et petites collections de valeurs.
- **Persistance :** le tableau noir n’est pas sauvegardé ; il décrit le contexte de la décision courante.

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

**Explication détaillée du bloc :**

- **Rôle :** `AgentGoal` porte une motivation durable, sa priorité, sa provenance et son éventuelle échéance.
- **Bornes :** la priorité signée permet de désactiver temporairement un but sans inventer une valeur infinie ; les politiques peuvent néanmoins filtrer les priorités négatives.
- **États terminaux :** un but satisfait, échoué ou annulé n’est plus actionnable et doit être archivé ou retiré par le service applicatif.
- **Temps logique :** l’échéance est inclusive ; le but reste actionnable au tick de sa deadline.
- **Séparation :** aucune référence vers `AgentPlan` n’est stockée, car un plan est une hypothèse transitoire invalidée par le monde.

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

**Explication détaillée du bloc :**

- **Rôle :** cette fonction choisit le but actif le plus prioritaire avec deux critères de départage reproductibles.
- **Ordre :** une priorité élevée gagne ; à priorité égale, le but le plus ancien gagne ; une égalité restante est résolue par l’identifiant.
- **Retour :** l’absence de candidat produit `null` et doit conduire l’agent à une intention d’attente explicite, pas à une réutilisation silencieuse du plan précédent.
- **Effets de bord :** le tableau d’entrée n’est pas trié ; seul `candidates` est modifié.
- **Vérification :** permuter l’ordre initial des mêmes buts doit produire le même `goal_id` sélectionné.
