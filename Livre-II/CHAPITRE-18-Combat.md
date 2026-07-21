---
title: "Livre II — Chapitre 18 : Combat"
id: "DOC-L2-CH18"
status: "reviewed"
version: "1.0.2"
lang: "fr-FR"
book: "Livre II"
chapter: 18
last-verified: "2026-07-21T19:59:30+02:00"
audit-status: "complete"
audit-date: "2026-07-21T19:59:30+02:00"
audit-report: "Livre-II/QA/AUDIT-CHAPITRE-18.md"
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

# Combat

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L2-CH18`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Version de référence :** Godot `4.7.1-stable`, édition Standard, GDScript, Forward+  

> **Audit post-création :** terminé au niveau `static-review` — voir `Livre-II/QA/AUDIT-CHAPITRE-18.md`.
> **Explications de code :** structurées bloc par bloc ; les informations pédagogiques antérieures sont conservées dans des rubriques explicites, complétées seulement lorsque le bloc l’exige.

## 1. Rôle du chapitre

Le chapitre 17 a établi une frontière essentielle : un agent autonome peut demander une action, mais il ne décide jamais lui-même des dégâts, de la portée, de la défense, de l’initiative ou de la mort d’un personnage.

Ce chapitre construit l’autorité de combat de `Project Asteria`. Elle doit :

- recevoir des commandes typées provenant d’un joueur, d’un agent ou d’un script de scénario ;
- vérifier l’identité de la source et de la cible ;
- contrôler l’engagement, l’initiative, la disponibilité et la portée ;
- résoudre la visibilité et les obstacles sans confondre présentation physique et règle métier ;
- calculer les chances de toucher et les dégâts avec des entiers bornés ;
- appliquer défense, résistances, garde et états temporaires dans un ordre déterministe ;
- produire des événements consultables et un historique borné ;
- conserver une simulation logique hors écran ;
- sauvegarder seulement l’état autoritaire nécessaire à la reprise ;
- rester indépendant des animations, sons, effets visuels et services d’IA générative.

À la fin, le lecteur saura distinguer quatre responsabilités :

| Responsabilité | Autorité |
|---|---|
| choisir une action souhaitée | joueur, agent ou scénario |
| vérifier si elle est actuellement autorisée | service de combat |
| appliquer santé, endurance et état de vie | règles de personnage coordonnées par le combat |
| représenter l’action à l’écran | scène, animation, audio et VFX |

## 2. Prérequis

Le lecteur doit avoir parcouru :

- le chapitre 4 pour l’architecture feature-first et les dépendances orientées vers les contrats ;
- le chapitre 5 pour les services injectés, les événements typés et le point de composition ;
- le chapitre 6 pour la chaîne entrée → intention → contrôleur et le traitement physique ;
- le chapitre 7 pour les `Resource` de conception et les identifiants stables ;
- le chapitre 9 pour les sections de sauvegarde préparées avant application ;
- le chapitre 14 pour `CharacterId`, `CharacterRuntimeState`, `CharacterStatistics` et `CharacterRules` ;
- le chapitre 17 pour `AgentActionRequest`, les exécuteurs autorisés et les révisions du monde.

## 3. Périmètre et frontières

Ce chapitre définit :

- les identifiants d’affrontement et de commande ;
- l’état logique d’un affrontement ;
- les participants et leur disponibilité ;
- la chronologie d’initiative ;
- les commandes de base : attaquer, garder, attendre et se désengager ;
- la validation des cibles ;
- la distance, la portée et la ligne de vue ;
- la résolution d’une attaque de base ;
- les paquets de dégâts, défense et résistances ;
- la garde et les états temporaires ;
- les événements, résultats et historiques ;
- l’adaptation des requêtes d’agents ;
- la simulation active et hors écran ;
- les budgets logiques ;
- la persistance et la restauration.

Il ne définit pas :

- les compétences, pouvoirs, coûts en mana, temps de recharge ou arbres d’aptitudes du chapitre 19 ;
- l’équipement, les armes possédées et leur durabilité du chapitre 20 ;
- les prix, récompenses et transactions du chapitre 21 ;
- les rencontres écologiques à grande échelle du chapitre 22 ;
- les crimes, lois, factions et sanctions du chapitre 23 ;
- les quêtes et conséquences narratives du chapitre 25 ;
- le multijoueur, l’autorité réseau et la prédiction du Livre IV.

> **Frontière essentielle :** le combat décide si une commande produit un impact. Il ne décide ni pourquoi l’agent l’a choisie, ni quelle animation doit la représenter.

<a id="ch18-authority-chain"></a>

## 4. Chaîne d’autorité

> **[LECTURE] Flux d’autorité du combat — Ne pas saisir.**

```text
joueur / agent / scénario
    ↓ commande souhaitée
adaptateur d’entrée
    ↓ CombatCommand validée
CombatService
    ├── vérifie identité, engagement et disponibilité
    ├── vérifie cible, portée et ligne de vue
    ├── résout toucher, défense, dégâts et états
    ├── prépare les candidats de mutation
    └── valide puis commit
        ↓
CharacterRuntimeState + CombatantState
        ↓ événements typés
présentation, journal, narration, IA
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** ce flux place toute mutation autoritaire derrière `CombatService` et un commit validé.

- **Paramètres et types importants :** **Entrée :** l’adaptateur fournit une intention structurée, jamais une nouvelle valeur de santé.

- **Sorties :** **Sorties :** le service renvoie un résultat métier et publie des événements ; la présentation les consomme sans recalculer l’issue.

- **Invariants protégés :** **Invariant protégé :** ni l’agent, ni l’animation, ni le raycast n’écrivent directement dans l’état de personnage.

## 5. Architecture retenue

La fonctionnalité `combat` reste séparée des personnages, des agents et des futures compétences.

> **[LECTURE] Arborescence cible — Ne pas créer depuis un terminal.**

```text
res://src/features/combat/
├── domain/
│   ├── combat_id.gd
│   ├── combat_rules.gd
│   ├── combat_action_kind.gd
│   ├── combat_command.gd
│   ├── combatant_state.gd
│   ├── combat_encounter_state.gd
│   ├── active_status.gd
│   ├── damage_packet.gd
│   ├── defense_profile.gd
│   ├── combat_event.gd
│   ├── combat_history.gd
│   └── combat_result.gd
├── application/
│   ├── combat_repository.gd
│   ├── combat_mutation_unit_of_work.gd
│   ├── combat_encounter_factory.gd
│   ├── combat_service.gd
│   ├── combat_snapshot.gd
│   ├── combat_snapshot_builder.gd
│   ├── combat_context_port.gd
│   ├── initiative_policy.gd
│   ├── target_validator.gd
│   ├── line_of_sight_port.gd
│   ├── hit_resolver.gd
│   ├── damage_resolver.gd
│   ├── status_policy.gd
│   ├── combat_command_queue.gd
│   ├── combat_scheduler.gd
│   └── combat_agent_action_executor.gd
├── infrastructure/
│   ├── physics_line_of_sight_adapter.gd
│   ├── combat_snapshot_codec.gd
│   └── combat_save_section.gd
└── presentation/
    └── combat_presentation_bridge.gd

res://data/combat/
└── default_combat_rules.tres

res://scenes/learning/
├── ch18_combat_demo.tscn
└── ch18_combat_demo.gd
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** l’arborescence sépare règles pures, orchestration, accès moteur, persistance et présentation.

- **Dépendances et ports utilisés :** **Dépendances :** `domain` ne dépend d’aucun nœud ; l’adaptateur physique reste dans `infrastructure` ; les animations restent dans `presentation`.

- **Frontière avec les personnages :** **Frontière avec les personnages :** la santé et l’endurance demeurent dans `CharacterRuntimeState`; le combat coordonne leur mutation sans les dupliquer.

- **Frontière avec les compétences :** **Frontière avec les compétences :** le chapitre 19 pourra produire des requêtes d’impact ou enrichir les définitions, sans déplacer la validation de cible et l’application des dégâts.

## 6. Vocabulaire du cycle de combat

Un **affrontement** regroupe des participants et une chronologie logique. Il peut représenter un duel, une escarmouche ou un combat hors écran.

Une **commande** est une demande ponctuelle corrélée par un identifiant unique.

Une **résolution** est le calcul autoritaire qui transforme une commande acceptée en résultat : raté, impact nul, dégâts, état appliqué, désengagement ou refus.

Un **participant** est un personnage engagé. Sa santé reste dans le système de personnages ; son initiative, sa garde et ses états de combat restent dans `CombatantState`.

Un **tick logique** ordonne les décisions. Il ne représente pas une heure murale et ne dépend pas de la vitesse du processeur.

## 7. Identifiants stables de combat

Les identifiants ne sont ni des noms affichés ni des chemins de scène.

> **[VSC] Visual Studio Code — Créer : `res://src/features/combat/domain/combat_id.gd`.**

```gdscript
class_name CombatId
extends RefCounted

const ENCOUNTER_PREFIX := "combat.encounter."
const COMMAND_PREFIX := "combat.command."
const EVENT_PREFIX := "combat.event."

static func encounter(character_seed: StringName, sequence: int) -> StringName:
	if not CharacterId.is_valid(character_seed) or sequence <= 0:
		return &""
	return StringName(
		"%s%s.%d" % [ENCOUNTER_PREFIX, String(character_seed), sequence]
	)

static func command(
	encounter_id: StringName,
	issuer_id: StringName,
	sequence: int,
) -> StringName:
	if not StableId.is_valid(encounter_id):
		return &""
	if not CharacterId.is_valid(issuer_id) or sequence <= 0:
		return &""
	return StringName(
		"%s%s.%s.%d"
		% [
			COMMAND_PREFIX,
			String(encounter_id),
			String(issuer_id),
			sequence,
		]
	)

static func event(encounter_id: StringName, sequence: int) -> StringName:
	if not StableId.is_valid(encounter_id) or sequence <= 0:
		return &""
	return StringName(
		"%s%s.%d" % [EVENT_PREFIX, String(encounter_id), sequence]
	)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** ces fabriques produisent les identifiants d’affrontement, de commande et d’événement à partir d’identités métier et de séquences croissantes.

- **Valeur de retour ou code d’échec :** **Valeurs de retour :** une entrée invalide produit la sentinelle `&""`; aucun identifiant partiel n’est construit.

- **Déterminisme :** **Déterminisme :** avec les mêmes arguments, la chaîne produite est identique ; aucune heure système ni valeur aléatoire globale n’intervient.

- **Limites et réserves :** **Limite :** l’unicité dépend du maintien des séquences par l’autorité de l’affrontement.

## 8. Règles de conception comme `Resource`

Les paramètres d’équilibrage sont des données de conception partagées. Ils ne contiennent aucun état de partie.

> **[VSC] Visual Studio Code — Créer : `res://src/features/combat/domain/combat_rules.gd`.**

```gdscript
class_name CombatRules
extends Resource

@export_range(1, 4096, 1) var max_encounters := 512
@export_range(1, 64, 1) var max_participants := 64
@export_range(1, 512, 1) var max_queued_commands := 256
@export_range(1, 64, 1) var max_statuses_per_combatant := 16
@export_range(1, 4096, 1) var max_history_events := 512

@export_range(1, 600, 1) var base_action_delay_ticks := 60
@export_range(1, 600, 1) var minimum_action_delay_ticks := 12
@export_range(1, 128, 1) var commands_per_physics_tick := 16
@export_range(0, 100000, 1) var base_guard_gain := 25
@export var allow_friendly_fire := false

@export_range(0, 1000, 1) var minimum_hit_chance_permille := 50
@export_range(0, 1000, 1) var maximum_hit_chance_permille := 950
@export_range(0, 1000, 1) var maximum_resistance_permille := 900
@export_range(0.1, 100.0, 0.1) var basic_attack_range_m := 2.25

func validate() -> Error:
	if max_encounters < 1 or max_encounters > 4096:
		return ERR_INVALID_DATA
	if max_participants < 1 or max_participants > 64:
		return ERR_INVALID_DATA
	if max_queued_commands < 1 or max_queued_commands > 512:
		return ERR_INVALID_DATA
	if max_statuses_per_combatant < 1 or max_statuses_per_combatant > 64:
		return ERR_INVALID_DATA
	if max_history_events < 1 or max_history_events > 4096:
		return ERR_INVALID_DATA
	if base_action_delay_ticks < 1 or base_action_delay_ticks > 600:
		return ERR_INVALID_DATA
	if minimum_action_delay_ticks < 1:
		return ERR_INVALID_DATA
	if minimum_action_delay_ticks > base_action_delay_ticks:
		return ERR_INVALID_DATA
	if commands_per_physics_tick < 1 or commands_per_physics_tick > 128:
		return ERR_INVALID_DATA
	if base_guard_gain < 0 or base_guard_gain > CombatantState.MAX_GUARD:
		return ERR_INVALID_DATA
	if minimum_hit_chance_permille < 0:
		return ERR_INVALID_DATA
	if maximum_hit_chance_permille > 1000:
		return ERR_INVALID_DATA
	if minimum_hit_chance_permille > maximum_hit_chance_permille:
		return ERR_INVALID_DATA
	if maximum_resistance_permille < 0 or maximum_resistance_permille > 1000:
		return ERR_INVALID_DATA
	if basic_attack_range_m <= 0.0 or not is_finite(basic_attack_range_m):
		return ERR_INVALID_DATA
	return OK
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** cette `Resource` centralise les bornes et valeurs d’équilibrage communes à un profil de combat.

- **Paramètres et types importants :** **Types :** les probabilités utilisent des millièmes entiers, la garde des entiers bornés et les distances des mètres Godot ; `allow_friendly_fire` rend la politique d’alliance explicite.

- **Valeur de retour ou code d’échec :** **Codes de retour :** `validate()` revérifie aussi les bornes `@export_range`, puis renvoie `OK` ou `ERR_INVALID_DATA` sans corriger silencieusement une ressource incohérente.

- **Partage :** **Partage :** la ressource est considérée comme immuable pendant le gameplay ; les compteurs courants restent dans les états runtime.

> **[APP] Godot — Créer `res://data/combat/default_combat_rules.tres` depuis `CombatRules`, puis renseigner les valeurs de référence.**

Le bootstrap charge et valide cette ressource avant de construire les services. Un fichier invalide bloque l’activation du système au lieu de créer un combat avec des bornes inconnues.

## 9. Actions de base

Le chapitre fournit seulement un vocabulaire minimal. Les compétences du chapitre 19 ne sont pas codées comme de nouveaux `match` dans le service.

> **[VSC] Visual Studio Code — Créer : `res://src/features/combat/domain/combat_action_kind.gd`.**

```gdscript
class_name CombatActionKind
extends RefCounted

enum Value {
	BASIC_ATTACK,
	GUARD,
	WAIT,
	DISENGAGE,
}

static func is_valid(value: int) -> bool:
	return value >= Value.BASIC_ATTACK and value <= Value.DISENGAGE
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** l’énumération décrit les opérations fondamentales prises en charge directement par le combat.

- **Frontières d’autorité :** **Frontière :** une compétence future reste une définition du chapitre 19 qui demande ensuite au combat de valider et d’appliquer ses impacts.

- **Valeur de retour :** **Valeur de retour :** `is_valid()` protège les données décodées avant leur conversion vers l’énumération.

## 10. Commande typée

Une commande décrit ce que l’émetteur demande. Elle ne transporte jamais la santé finale, le résultat du jet ou le nombre de dégâts déjà décidé.

> **[VSC] Visual Studio Code — Créer : `res://src/features/combat/domain/combat_command.gd`.**

```gdscript
class_name CombatCommand
extends RefCounted

var command_id: StringName
var encounter_id: StringName
var issuer_character_id: StringName
var target_character_id: StringName = &""
var action_kind: CombatActionKind.Value
var action_id: StringName
var requested_tick: int = 0
var issuer_sequence: int = 0
var expected_combat_revision: int = 0
var expected_world_revision: int = 0

func validate() -> Error:
	if not StableId.is_valid(command_id):
		return ERR_INVALID_DATA
	if not StableId.is_valid(encounter_id):
		return ERR_INVALID_DATA
	if not CharacterId.is_valid(issuer_character_id):
		return ERR_INVALID_DATA
	if not CombatActionKind.is_valid(action_kind):
		return ERR_INVALID_DATA
	if not StableId.is_valid(action_id):
		return ERR_INVALID_DATA
	if requested_tick < 0 or issuer_sequence <= 0:
		return ERR_INVALID_DATA
	if expected_combat_revision < 0 or expected_world_revision < 0:
		return ERR_INVALID_DATA
	if action_kind == CombatActionKind.Value.BASIC_ATTACK:
		if not CharacterId.is_valid(target_character_id):
			return ERR_INVALID_DATA
	elif not target_character_id.is_empty():
		return ERR_INVALID_DATA
	return OK

func duplicate_detached() -> CombatCommand:
	var copy := CombatCommand.new()
	copy.command_id = command_id
	copy.encounter_id = encounter_id
	copy.issuer_character_id = issuer_character_id
	copy.target_character_id = target_character_id
	copy.action_kind = action_kind
	copy.action_id = action_id
	copy.requested_tick = requested_tick
	copy.issuer_sequence = issuer_sequence
	copy.expected_combat_revision = expected_combat_revision
	copy.expected_world_revision = expected_world_revision
	return copy
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** la commande transporte identité, action, cible et révisions attendues sans embarquer un effet déjà calculé.

- **Corrélation et révisions :** **Corrélation :** `command_id` identifie une tentative ; `issuer_sequence` ordonne les commandes d’un même personnage ; seules les actions qui exigent une cible peuvent porter `target_character_id`.

- **Concurrence :** **Concurrence :** les deux révisions rendent explicites un monde ou un affrontement devenus obsolètes.

- **Effet de bord :** **Effet de bord :** `duplicate_detached()` crée une copie indépendante destinée à une file ; aucune collection mutable n’est partagée.

## 11. État d’un participant

`CombatantState` complète `CharacterRuntimeState`; il ne recopie ni santé, ni endurance, ni position.

> **[VSC] Visual Studio Code — Créer : `res://src/features/combat/domain/combatant_state.gd`.**

```gdscript
class_name CombatantState
extends RefCounted

const MAX_GUARD := 100000

var character_id: StringName
var side_id: StringName
var next_ready_tick: int = 0
var initiative_rank: int = 0
var guard_points: int = 0
var command_sequence: int = 0
var active_statuses: Array[ActiveStatus] = []
var disengaged := false

func validate(rules: CombatRules) -> Error:
	if rules == null or rules.validate() != OK:
		return ERR_UNCONFIGURED
	if not CharacterId.is_valid(character_id):
		return ERR_INVALID_DATA
	if not StableId.is_valid(side_id):
		return ERR_INVALID_DATA
	if next_ready_tick < 0 or command_sequence < 0:
		return ERR_INVALID_DATA
	if initiative_rank < -100000 or initiative_rank > 100000:
		return ERR_INVALID_DATA
	if guard_points < 0 or guard_points > MAX_GUARD:
		return ERR_INVALID_DATA
	if active_statuses.size() > rules.max_statuses_per_combatant:
		return ERR_OUT_OF_MEMORY
	var seen: Dictionary[StringName, bool] = {}
	for status: ActiveStatus in active_statuses:
		if status == null or status.validate() != OK:
			return ERR_INVALID_DATA
		if seen.has(status.status_id):
			return ERR_ALREADY_EXISTS
		seen[status.status_id] = true
	return OK

func next_command_sequence() -> int:
	command_sequence += 1
	return command_sequence

func duplicate_detached() -> CombatantState:
	var copy := CombatantState.new()
	copy.character_id = character_id
	copy.side_id = side_id
	copy.next_ready_tick = next_ready_tick
	copy.initiative_rank = initiative_rank
	copy.guard_points = guard_points
	copy.command_sequence = command_sequence
	copy.disengaged = disengaged
	for status: ActiveStatus in active_statuses:
		copy.active_statuses.append(status.duplicate_detached())
	return copy
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** l’objet conserve uniquement l’état spécifique au combat d’un participant.

- **Séparation :** **Séparation :** santé, endurance, position et `is_alive` restent dans `CharacterRuntimeState`; `side_id` appartient à l’engagement courant et sert au ciblage ainsi qu’à la fermeture de l’affrontement.

- **Valeur de retour ou code d’échec :** **Codes de retour :** dépassement du nombre d’états produit `ERR_OUT_OF_MEMORY`; un doublon produit `ERR_ALREADY_EXISTS`.

- **Effets de bord :** **Effets de bord :** `next_command_sequence()` réserve une séquence croissante ; `duplicate_detached()` recopie aussi chaque état temporaire afin qu’un candidat ne partage aucun objet mutable avec l’état actif.

## 12. État d’un affrontement

L’affrontement agrège les participants et la source pseudo-aléatoire locale. Les files dérivées peuvent être reconstruites.

> **[VSC] Visual Studio Code — Créer : `res://src/features/combat/domain/combat_encounter_state.gd`.**

```gdscript
class_name CombatEncounterState
extends RefCounted

var encounter_id: StringName
var logical_tick: int = 0
var revision: int = 0
var event_sequence: int = 0
var rng_seed: int = 0
var rng_state: int = 0
var participants: Dictionary[StringName, CombatantState] = {}
var processed_command_ids: Array[StringName] = []
var history := CombatHistory.new()
var closed := false

func validate(rules: CombatRules) -> Error:
	if rules == null or rules.validate() != OK:
		return ERR_UNCONFIGURED
	if not StableId.is_valid(encounter_id):
		return ERR_INVALID_DATA
	if logical_tick < 0 or revision < 0 or event_sequence < 0:
		return ERR_INVALID_DATA
	if participants.is_empty() or participants.size() > rules.max_participants:
		return ERR_OUT_OF_MEMORY
	var ids: Array[StringName] = []
	ids.assign(participants.keys())
	ids.sort()
	for character_id: StringName in ids:
		var participant := participants[character_id]
		if participant == null or participant.character_id != character_id:
			return ERR_INVALID_DATA
		if participant.validate(rules) != OK:
			return ERR_INVALID_DATA
	if processed_command_ids.size() > rules.max_history_events:
		return ERR_OUT_OF_MEMORY
	var seen_commands: Dictionary[StringName, bool] = {}
	for command_id: StringName in processed_command_ids:
		if not StableId.is_valid(command_id) or seen_commands.has(command_id):
			return ERR_INVALID_DATA
		seen_commands[command_id] = true
	if history == null or history.validate(rules.max_history_events) != OK:
		return ERR_INVALID_DATA
	for event: CombatEvent in history.snapshot():
		if event.encounter_id != encounter_id:
			return ERR_INVALID_DATA
		if event.sequence > event_sequence:
			return ERR_INVALID_DATA
	return OK

func initialize_rng(seed_value: int) -> void:
	var rng := RandomNumberGenerator.new()
	rng.seed = seed_value
	rng_seed = seed_value
	rng_state = rng.state

func advance_to(new_tick: int) -> Error:
	if new_tick < logical_tick:
		return ERR_INVALID_DATA
	logical_tick = new_tick
	return OK

func next_event_sequence() -> int:
	event_sequence += 1
	return event_sequence

func contains(character_id: StringName) -> bool:
	return participants.has(character_id)

func get_participant(character_id: StringName) -> CombatantState:
	return participants.get(character_id) as CombatantState

func duplicate_detached() -> CombatEncounterState:
	var copy := CombatEncounterState.new()
	copy.encounter_id = encounter_id
	copy.logical_tick = logical_tick
	copy.revision = revision
	copy.event_sequence = event_sequence
	copy.rng_seed = rng_seed
	copy.rng_state = rng_state
	copy.closed = closed
	var ids: Array[StringName] = []
	ids.assign(participants.keys())
	ids.sort()
	for character_id: StringName in ids:
		copy.participants[character_id] = participants[character_id].duplicate_detached()
	copy.processed_command_ids.assign(processed_command_ids)
	copy.history = history.duplicate_detached()
	return copy
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** l’affrontement constitue la racine autoritaire du domaine de combat.

- **Déroulement ou instructions importantes :** **Ordre :** les identifiants sont triés avant validation afin que les diagnostics et traitements ultérieurs ne dépendent pas de l’ordre d’un dictionnaire.

- **Idempotence :** **Idempotence :** `processed_command_ids` mémorise un historique borné des commandes déjà consommées.

- **RNG :** **RNG :** `initialize_rng()` définit d’abord `seed`, puis conserve uniquement un `state` réellement produit par le générateur ; la reprise vise la même version de moteur, pas un algorithme futur différent.

- **Copies :** **Copies :** `duplicate_detached()` recopie participants, états, commandes traitées et historique ; le tick ne peut avancer que par `advance_to()`.

### 12.1 Construire un affrontement valide

> **[VSC] Visual Studio Code — Créer : `res://src/features/combat/application/combat_encounter_factory.gd`.**

```gdscript
class_name CombatEncounterFactory
extends RefCounted

func create(
	encounter_id: StringName,
	participants: Array[CombatantState],
	rng_seed: int,
	rules: CombatRules,
) -> CombatEncounterState:
	if not StableId.is_valid(encounter_id):
		return null
	if rules == null or rules.validate() != OK:
		return null
	if participants.size() < 2:
		return null
	if participants.size() > rules.max_participants:
		return null

	var encounter := CombatEncounterState.new()
	encounter.encounter_id = encounter_id
	var sides: Dictionary[StringName, bool] = {}
	for participant: CombatantState in participants:
		if participant == null or participant.validate(rules) != OK:
			return null
		if encounter.participants.has(participant.character_id):
			return null
		encounter.participants[participant.character_id] = (
			participant.duplicate_detached()
		)
		sides[participant.side_id] = true
	if sides.size() < 2:
		return null

	encounter.initialize_rng(rng_seed)
	var started := CombatEvent.new()
	started.sequence = encounter.next_event_sequence()
	started.event_id = CombatId.event(encounter_id, started.sequence)
	started.encounter_id = encounter_id
	started.kind = CombatEvent.Kind.ENCOUNTER_STARTED
	started.logical_tick = 0
	started.detail_id = &"combat.event.encounter_started"
	if encounter.history.append(started, rules.max_history_events) != OK:
		return null
	return encounter if encounter.validate(rules) == OK else null
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** la fabrique refuse doublons, participants invalides et affrontement sans deux côtés opposés avant de publier un état utilisable.

- **RNG :** **RNG :** `initialize_rng()` applique la graine puis capture le `state` produit par Godot ; aucune valeur arbitraire n’est affectée directement à `state`.

- **Copies :** **Copies :** chaque participant est dupliqué, états temporaires compris. La liste fournie par l’appelant ne partage donc aucune autorité mutable avec l’affrontement.

- **Historique :** **Historique :** l’événement de démarrage reçoit la première séquence avant validation finale.

## 13. Définir l’initiative

L’initiative n’est pas un tri effectué une seule fois au début. Chaque participant possède un `next_ready_tick`. Après une action, son prochain tick disponible est recalculé.

> **[VSC] Visual Studio Code — Créer : `res://src/features/combat/application/initiative_policy.gd`.**

```gdscript
class_name InitiativePolicy
extends RefCounted

func initial_rank(agility: int) -> int:
	return clampi(agility, -1000, 1000)

func recovery_ticks(
	rules: CombatRules,
	agility: int,
	action_delay_modifier: int = 0,
) -> int:
	if rules == null or rules.validate() != OK:
		return 0
	var reduction := clampi(agility + action_delay_modifier, -500, 500)
	var computed := rules.base_action_delay_ticks - reduction
	return maxi(rules.minimum_action_delay_ticks, computed)

func compare_ready(a: CombatantState, b: CombatantState) -> bool:
	if a.next_ready_tick != b.next_ready_tick:
		return a.next_ready_tick < b.next_ready_tick
	if a.initiative_rank != b.initiative_rank:
		return a.initiative_rank > b.initiative_rank
	return String(a.character_id) < String(b.character_id)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** cette politique calcule le rang initial, le délai de récupération et l’ordre total des participants prêts.

- **Départage :** **Départage :** tick, agilité bornée puis identité donnent un ordre total stable sans dépendre de `hash()` ni d’une valeur aléatoire.

- **Bornes :** **Bornes :** l’agilité et les modificateurs sont limités avant le calcul ; le délai ne descend jamais sous `minimum_action_delay_ticks`.

- **Persistance :** **Persistance :** le rang peut être sauvegardé, mais il reste reconstructible depuis l’agilité autoritaire tant qu’aucun modificateur durable ne s’y ajoute.

- **Frontières d’autorité :** La collection prête est copiée puis triée. Elle n’est pas conservée comme autorité dans la sauvegarde.

## 14. États temporaires

Le combat possède le cycle de vie et les règles d’empilement des états. Le chapitre 19 définira comment une compétence demande leur application.

> **[VSC] Visual Studio Code — Créer : `res://src/features/combat/domain/active_status.gd`.**

```gdscript
class_name ActiveStatus
extends RefCounted

enum StackRule {
	REPLACE,
	REFRESH,
	ADD_STACK,
}

var status_id: StringName
var source_character_id: StringName
var stack_rule: StackRule
var stacks: int = 1
var max_stacks: int = 1
var applied_tick: int = 0
var expires_at_tick: int = 0
var accuracy_modifier_permille: int = 0
var evasion_modifier_permille: int = 0
var defense_modifier: int = 0
var initiative_modifier: int = 0

func validate() -> Error:
	if not StableId.is_valid(status_id):
		return ERR_INVALID_DATA
	if not CharacterId.is_valid(source_character_id):
		return ERR_INVALID_DATA
	if stack_rule < StackRule.REPLACE or stack_rule > StackRule.ADD_STACK:
		return ERR_INVALID_DATA
	if stacks < 1 or max_stacks < 1 or stacks > max_stacks:
		return ERR_INVALID_DATA
	if applied_tick < 0 or expires_at_tick <= applied_tick:
		return ERR_INVALID_DATA
	for modifier: int in [
		accuracy_modifier_permille,
		evasion_modifier_permille,
		defense_modifier,
		initiative_modifier,
	]:
		if modifier < -100000 or modifier > 100000:
			return ERR_INVALID_DATA
	return OK

func is_expired(logical_tick: int) -> bool:
	return logical_tick >= expires_at_tick

func duplicate_detached() -> ActiveStatus:
	var copy := ActiveStatus.new()
	copy.status_id = status_id
	copy.source_character_id = source_character_id
	copy.stack_rule = stack_rule
	copy.stacks = stacks
	copy.max_stacks = max_stacks
	copy.applied_tick = applied_tick
	copy.expires_at_tick = expires_at_tick
	copy.accuracy_modifier_permille = accuracy_modifier_permille
	copy.evasion_modifier_permille = evasion_modifier_permille
	copy.defense_modifier = defense_modifier
	copy.initiative_modifier = initiative_modifier
	return copy
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** l’état actif contient une durée logique et des modificateurs déjà validés.

- **Durée :** **Durée :** l’expiration est exclusive : l’état cesse d’être actif lorsque `logical_tick >= expires_at_tick`.

- **Frontières d’autorité :** **Frontière :** le combat sait appliquer et expirer l’état ; la compétence ou l’objet qui le produit appartient à son système d’origine.

- **Valeur de retour ou code d’échec :** **Codes de retour :** règle d’empilement, piles et intervalles incohérents sont refusés ; `duplicate_detached()` empêche le partage d’un état mutable entre candidat et autorité active.

> **[VSC] Visual Studio Code — Créer : `res://src/features/combat/application/status_policy.gd`.**

```gdscript
class_name StatusPolicy
extends RefCounted

func apply_status(
	statuses: Array[ActiveStatus],
	incoming: ActiveStatus,
	max_statuses: int,
) -> Error:
	if incoming == null or incoming.validate() != OK:
		return ERR_INVALID_DATA
	if max_statuses < 1:
		return ERR_INVALID_PARAMETER

	var detached := incoming.duplicate_detached()
	var existing_index := -1
	for index in statuses.size():
		if statuses[index] == null or statuses[index].validate() != OK:
			return ERR_INVALID_DATA
		if statuses[index].status_id == incoming.status_id:
			existing_index = index
			break

	if existing_index < 0:
		if statuses.size() >= max_statuses:
			return ERR_OUT_OF_MEMORY
		statuses.append(detached)
		_sort(statuses)
		return OK

	var existing := statuses[existing_index]
	match detached.stack_rule:
		ActiveStatus.StackRule.REPLACE:
			statuses[existing_index] = detached
		ActiveStatus.StackRule.REFRESH:
			existing.expires_at_tick = maxi(
				existing.expires_at_tick,
				detached.expires_at_tick,
			)
		ActiveStatus.StackRule.ADD_STACK:
			existing.stacks = mini(
				existing.max_stacks,
				existing.stacks + detached.stacks,
			)
			existing.expires_at_tick = maxi(
				existing.expires_at_tick,
				detached.expires_at_tick,
			)
		_:
			return ERR_INVALID_DATA
	_sort(statuses)
	return OK

func remove_expired(
	statuses: Array[ActiveStatus],
	logical_tick: int,
) -> Array[StringName]:
	var removed: Array[StringName] = []
	for index in range(statuses.size() - 1, -1, -1):
		if statuses[index].is_expired(logical_tick):
			removed.append(statuses[index].status_id)
			statuses.remove_at(index)
	removed.sort()
	return removed

func _sort(statuses: Array[ActiveStatus]) -> void:
	statuses.sort_custom(
		func(a: ActiveStatus, b: ActiveStatus) -> bool:
			return String(a.status_id) < String(b.status_id)
	)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** la politique applique une règle d’empilement explicite puis maintient un ordre canonique.

- **Mutation :** **Mutation :** la liste reçue est modifiée seulement après validation ; l’état entrant est d’abord dupliqué afin que l’appelant ne puisse pas altérer ultérieurement le candidat.

- **Expiration :** **Expiration :** l’itération inverse évite de décaler les index encore à visiter lors des suppressions.

- **Valeur de retour :** **Valeur de retour :** `remove_expired()` renvoie les identifiants triés afin de produire des événements reproductibles.

## 15. Snapshot de résolution

Une résolution ne lit pas directement plusieurs dépôts pendant ses calculs. Un snapshot détaché agrège les valeurs autorisées au début de la commande.

> **[VSC] Visual Studio Code — Créer : `res://src/features/combat/application/combat_snapshot.gd`.**

```gdscript
class_name CombatSnapshot
extends RefCounted

var encounter_id: StringName
var combat_revision: int = 0
var world_revision: int = 0
var logical_tick: int = 0
var issuer_id: StringName
var target_id: StringName
var issuer_side_id: StringName
var target_side_id: StringName
var issuer_position := Vector3.ZERO
var target_position := Vector3.ZERO
var issuer_alive := false
var target_alive := false
var issuer_stamina: int = 0
var issuer_accuracy_permille: int = 0
var target_evasion_permille: int = 0
var target_defense: int = 0
var target_resistance_permille: int = 0
var line_of_sight := false

func validate() -> Error:
	if not StableId.is_valid(encounter_id):
		return ERR_INVALID_DATA
	if combat_revision < 0 or world_revision < 0 or logical_tick < 0:
		return ERR_INVALID_DATA
	if not CharacterId.is_valid(issuer_id):
		return ERR_INVALID_DATA
	if not CharacterId.is_valid(target_id):
		return ERR_INVALID_DATA
	if not StableId.is_valid(issuer_side_id):
		return ERR_INVALID_DATA
	if not StableId.is_valid(target_side_id):
		return ERR_INVALID_DATA
	if not issuer_position.is_finite() or not target_position.is_finite():
		return ERR_INVALID_DATA
	for value: int in [
		issuer_accuracy_permille,
		target_evasion_permille,
	]:
		if value < -100000 or value > 100000:
			return ERR_INVALID_DATA
	if target_resistance_permille < -1000 or target_resistance_permille > 1000:
		return ERR_INVALID_DATA
	if issuer_stamina < 0 or target_defense < 0:
		return ERR_INVALID_DATA
	return OK

func distance_squared() -> float:
	return issuer_position.distance_squared_to(target_position)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** le snapshot fige les lectures nécessaires à une résolution unique.

- **Données dérivées :** **Données dérivées :** précision, esquive, défense et résistance peuvent agréger attributs et états ; les côtés proviennent des participants engagés et permettent de refuser un allié lorsque la règle l’exige.

- **Distance :** **Distance :** le carré de la distance évite une racine carrée lors d’une simple comparaison de portée.

- **Invariant :** **Invariant :** après sa construction, le service traite cet objet comme immuable et recontrôle les révisions avant le commit.

### 15.1 Port de construction des lectures dérivées

> **[VSC] Visual Studio Code — Créer : `res://src/features/combat/application/combat_snapshot_builder.gd`.**

```gdscript
class_name CombatSnapshotBuilder
extends RefCounted

func build_for_basic_attack(
	command: CombatCommand,
	encounter: CombatEncounterState,
) -> CombatSnapshot:
	return null

func build_defense_profile(snapshot: CombatSnapshot) -> DefenseProfile:
	return null

func build_basic_attack_packet(
	command: CombatCommand,
	snapshot: CombatSnapshot,
) -> DamagePacket:
	return null

func definition_for(character_id: StringName) -> CharacterDefinition:
	return null
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** ce port rassemble les lectures des personnages, des positions et des données de conception sans permettre au service de parcourir directement plusieurs dépôts pendant le calcul.

- **Copies :** **Copies :** les objets retournés sont détachés ou dérivés ; le paquet et le profil peuvent être abandonnés sans modifier leurs sources.

- **Frontières :** **Frontières :** l’implémentation connaît les catalogues et ports de lecture, mais ne commit aucune santé, garde ou révision.

- **Refus contrôlé :** **Refus contrôlé :** `null` indique qu’une lecture obligatoire manque ; `CombatService` transforme ce cas en `REJECTED_RESOURCE`.

## 16. Port de ligne de vue

Le domaine demande une réponse booléenne et ignore comment elle est obtenue.

> **[VSC] Visual Studio Code — Créer : `res://src/features/combat/application/line_of_sight_port.gd`.**

```gdscript
class_name LineOfSightPort
extends RefCounted

func has_line_of_sight(
	from_position: Vector3,
	to_position: Vector3,
	excluded_rids: Array[RID],
	collision_mask: int,
) -> bool:
	return false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** le port isole la dépendance au moteur physique.

- **Valeur de retour :** **Valeur de retour :** la classe de base refuse par défaut ; un adaptateur actif ou hors écran doit être injecté.

- **Paramètres et types importants :** **Paramètres :** les positions, exceptions et masque sont des données déjà validées par l’application.

- **Frontières d’autorité :** **Frontière :** le booléen participe à la validation, mais ne choisit jamais la cible.

## 17. Adaptateur physique actif

Dans une scène active, une requête de rayon peut vérifier qu’aucun obstacle du masque de couverture ne coupe le segment.

> **[VSC] Visual Studio Code — Créer : `res://src/features/combat/infrastructure/physics_line_of_sight_adapter.gd`.**

```gdscript
class_name PhysicsLineOfSightAdapter
extends Node

var _space_state: PhysicsDirectSpaceState3D

func capture_space_state() -> void:
	_space_state = get_world_3d().direct_space_state

func has_line_of_sight(
	from_position: Vector3,
	to_position: Vector3,
	excluded_rids: Array[RID],
	collision_mask: int,
) -> bool:
	if _space_state == null:
		return false
	if not from_position.is_finite() or not to_position.is_finite():
		return false
	if from_position.is_equal_approx(to_position):
		return true

	var query := PhysicsRayQueryParameters3D.create(
		from_position,
		to_position,
		collision_mask,
		excluded_rids,
	)
	query.collide_with_areas = false
	query.collide_with_bodies = true
	var hit := _space_state.intersect_ray(query)
	return hit.is_empty()
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** cet adaptateur traduit le port en `PhysicsRayQueryParameters3D` puis appelle `intersect_ray()`.

- **Cycle moteur :** **Cycle moteur :** `capture_space_state()` doit être appelé depuis la phase physique qui orchestre le combat actif ; l’exemple ne conserve pas l’espace entre deux mondes.

- **Exceptions :** **Exceptions :** les corps de la source et de la cible peuvent être exclus afin que leurs propres collisions ne bloquent pas le segment.

- **Refus conservateur :** **Refus conservateur :** absence d’espace ou position non finie produit `false`; le service ne transforme pas une incapacité de mesure en visibilité.

- **Limites et réserves :** **Limite :** un rayon représente une ligne. Les projectiles volumineux peuvent nécessiter une requête de forme ou plusieurs échantillons.

- **Persistance et restauration :** `Area3D` peut détecter une zone persistante et `ShapeCast3D` balayer un volume. Ils ne remplacent pas automatiquement la règle de portée : les couches, exceptions et instants d’échantillonnage doivent rester explicites.

- **Dépendances et ports utilisés :** Hors écran, un autre adaptateur utilise les données logiques de partition, les pièces, portes ou cellules d’occlusion. Il ne lance pas un rayon dans une scène inexistante.

## 18. Validation de cible et de portée

> **[VSC] Visual Studio Code — Créer : `res://src/features/combat/application/target_validator.gd`.**

```gdscript
class_name TargetValidator
extends RefCounted

enum Status {
	VALID,
	INVALID_SOURCE,
	INVALID_TARGET,
	SAME_CHARACTER,
	SAME_SIDE,
	DEAD_SOURCE,
	DEAD_TARGET,
	OUT_OF_RANGE,
	NO_LINE_OF_SIGHT,
}

func validate_basic_attack(
	snapshot: CombatSnapshot,
	rules: CombatRules,
) -> Status:
	if snapshot == null or snapshot.validate() != OK:
		return Status.INVALID_TARGET
	if rules == null or rules.validate() != OK:
		return Status.INVALID_SOURCE
	if snapshot.issuer_id == snapshot.target_id:
		return Status.SAME_CHARACTER
	if not rules.allow_friendly_fire:
		if snapshot.issuer_side_id == snapshot.target_side_id:
			return Status.SAME_SIDE
	if not snapshot.issuer_alive:
		return Status.DEAD_SOURCE
	if not snapshot.target_alive:
		return Status.DEAD_TARGET
	var range_squared := rules.basic_attack_range_m * rules.basic_attack_range_m
	if snapshot.distance_squared() > range_squared:
		return Status.OUT_OF_RANGE
	if not snapshot.line_of_sight:
		return Status.NO_LINE_OF_SIGHT
	return Status.VALID
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** la méthode transforme plusieurs préconditions en un statut métier précis.

- **Déroulement ou instructions importantes :** **Ordre :** identité, politique de tir allié et vie sont vérifiées avant la distance ; la ligne de vue n’est consultée qu’après une portée valide.

- **Statuts à distinguer :** **Statuts à distinguer :** `SAME_SIDE` applique la politique d’alliance ; `OUT_OF_RANGE` refuse par géométrie ; `NO_LINE_OF_SIGHT` signifie qu’un obstacle autoritaire subsiste malgré une distance acceptable.

- **Effet de bord :** **Effet de bord :** aucun ; cette validation peut être rejouée sur le même snapshot.

## 19. Résoudre la chance de toucher

Les probabilités utilisent des entiers en millièmes. Un tirage de `0` à `999` est comparé à une chance bornée.

> **[VSC] Visual Studio Code — Créer : `res://src/features/combat/application/hit_resolver.gd`.**

```gdscript
class_name HitResolver
extends RefCounted

class HitOutcome:
	extends RefCounted

	var chance_permille: int = 0
	var roll: int = 0
	var hit := false

func resolve(
	rules: CombatRules,
	accuracy_permille: int,
	evasion_permille: int,
	rng: RandomNumberGenerator,
) -> HitOutcome:
	if rules == null or rules.validate() != OK or rng == null:
		return null
	var chance := clampi(
		accuracy_permille - evasion_permille,
		rules.minimum_hit_chance_permille,
		rules.maximum_hit_chance_permille,
	)
	var outcome := HitOutcome.new()
	outcome.chance_permille = chance
	outcome.roll = rng.randi_range(0, 999)
	outcome.hit = outcome.roll < chance
	return outcome
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** le résolveur borne la chance, consomme exactement un tirage et expose les valeurs utiles au diagnostic.

- **Probabilité :** **Probabilité :** une chance de `750` signifie 750 résultats gagnants parmi les 1 000 valeurs possibles.

- **RNG local :** **RNG local :** l’appelant fournit l’instance liée à l’affrontement et persiste son `state` après la résolution.

- **Limite de reproductibilité :** **Limite de reproductibilité :** Godot documente l’algorithme sous-jacent comme détail d’implémentation ; la restauration vise la même version de moteur, pas une garantie éternelle inter-version.

## 20. Paquet de dégâts

Un paquet décrit une demande de dégâts avant défense. Il reste distinct du résultat final.

> **[VSC] Visual Studio Code — Créer : `res://src/features/combat/domain/damage_packet.gd`.**

```gdscript
class_name DamagePacket
extends RefCounted

enum DamageType {
	PHYSICAL,
	FIRE,
	COLD,
	LIGHTNING,
	ARCANE,
}

var source_character_id: StringName
var target_character_id: StringName
var damage_type: DamageType
var base_amount: int = 0
var armor_penetration_permille: int = 0
var tags: Array[StringName] = []

func validate() -> Error:
	if not CharacterId.is_valid(source_character_id):
		return ERR_INVALID_DATA
	if not CharacterId.is_valid(target_character_id):
		return ERR_INVALID_DATA
	if damage_type < DamageType.PHYSICAL or damage_type > DamageType.ARCANE:
		return ERR_INVALID_DATA
	if base_amount < 0 or base_amount > 100000000:
		return ERR_INVALID_DATA
	if armor_penetration_permille < 0 or armor_penetration_permille > 1000:
		return ERR_INVALID_DATA
	var seen: Dictionary[StringName, bool] = {}
	for tag: StringName in tags:
		if not StableId.is_valid(tag) or seen.has(tag):
			return ERR_INVALID_DATA
		seen[tag] = true
	return OK
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** le paquet transporte une quantité brute, un type et une pénétration, sans modifier la cible.

- **Bornes :** **Bornes :** les montants restent entiers et limités afin d’éviter valeurs négatives, dépassements accidentels et données hostiles.

- **Tags :** **Tags :** ils permettent à des systèmes futurs de reconnaître une provenance sans charger dynamiquement une classe depuis une chaîne.

- **Frontières d’autorité :** **Frontière :** les armes et compétences construisent éventuellement le paquet ; le combat conserve l’autorité de résolution.

## 21. Profil de défense

Le profil est un snapshot dérivé depuis le personnage, ses états de combat et, plus tard, son équipement.

> **[VSC] Visual Studio Code — Créer : `res://src/features/combat/domain/defense_profile.gd`.**

```gdscript
class_name DefenseProfile
extends RefCounted

var flat_defense: int = 0
var resistance_by_type: Dictionary[int, int] = {}

func validate(maximum_resistance_permille: int) -> Error:
	if flat_defense < 0 or flat_defense > 100000000:
		return ERR_INVALID_DATA
	for key: int in resistance_by_type:
		if key < DamagePacket.DamageType.PHYSICAL:
			return ERR_INVALID_DATA
		if key > DamagePacket.DamageType.ARCANE:
			return ERR_INVALID_DATA
		var resistance: int = resistance_by_type[key]
		if resistance < -1000 or resistance > maximum_resistance_permille:
			return ERR_INVALID_DATA
	return OK

func resistance_for(damage_type: DamagePacket.DamageType) -> int:
	return resistance_by_type.get(int(damage_type), 0)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** ce profil rassemble les valeurs défensives nécessaires à un calcul sans référencer directement une ressource d’équipement.

- **Défense fixe :** **Défense fixe :** elle reste positive ou nulle ; les vulnérabilités sont représentées uniquement par une résistance négative afin de conserver un ordre de calcul non ambigu.

- **Valeur par défaut :** **Valeur par défaut :** un type absent utilise zéro résistance.

- **Persistance :** **Persistance :** le profil est recalculé et n’est pas sauvegardé tant que ses sources restent autoritaires ailleurs.

## 22. Ordre de calcul des dégâts

L’ordre choisi est : pénétration de l’armure, défense fixe, résistance, puis garde. Cette séquence doit être documentée car changer l’ordre modifie l’équilibrage.

> **[VSC] Visual Studio Code — Créer : `res://src/features/combat/application/damage_resolver.gd`.**

```gdscript
class_name DamageResolver
extends RefCounted

class DamageOutcome:
	extends RefCounted

	var raw_amount: int = 0
	var defense_after_penetration: int = 0
	var after_defense: int = 0
	var resistance_permille: int = 0
	var after_resistance: int = 0
	var absorbed_by_guard: int = 0
	var health_damage: int = 0

func resolve(
	packet: DamagePacket,
	profile: DefenseProfile,
	available_guard: int,
	maximum_resistance_permille: int,
) -> DamageOutcome:
	if packet == null or packet.validate() != OK:
		return null
	if profile == null:
		return null
	if profile.validate(maximum_resistance_permille) != OK:
		return null
	if available_guard < 0:
		return null

	var outcome := DamageOutcome.new()
	outcome.raw_amount = packet.base_amount

	var kept_defense_permille := 1000 - packet.armor_penetration_permille
	outcome.defense_after_penetration = maxi(
		0,
		(profile.flat_defense * kept_defense_permille) / 1000,
	)
	outcome.after_defense = maxi(
		0,
		packet.base_amount - outcome.defense_after_penetration,
	)

	outcome.resistance_permille = profile.resistance_for(
		packet.damage_type
	)
	var kept_damage_permille := 1000 - outcome.resistance_permille
	outcome.after_resistance = maxi(
		0,
		(outcome.after_defense * kept_damage_permille) / 1000,
	)

	outcome.absorbed_by_guard = mini(
		available_guard,
		outcome.after_resistance,
	)
	outcome.health_damage = outcome.after_resistance - outcome.absorbed_by_guard
	return outcome
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** le calcul produit une trace complète de chaque étape sans modifier la cible.

- **Arithmétique :** **Arithmétique :** la division entière arrondit vers zéro ; cette règle fait partie du contrat d’équilibrage.

- **Pénétration :** **Pénétration :** `1000` ignore toute défense fixe positive ; elle ne supprime pas la résistance du type.

- **Garde :** **Garde :** elle absorbe en dernier et ne peut jamais dépasser le montant restant.

- **Résultat nul :** **Résultat nul :** zéro dégât est une issue valide, distincte d’une commande invalide.

## 23. Résultats métier

Le résultat sépare le code d’exécution technique du statut de combat.

> **[VSC] Visual Studio Code — Créer : `res://src/features/combat/domain/combat_result.gd`.**

```gdscript
class_name CombatResult
extends RefCounted

enum Status {
	RESOLVED,
	MISSED,
	NO_EFFECT,
	REJECTED_INVALID_COMMAND,
	REJECTED_UNKNOWN_ENCOUNTER,
	REJECTED_DUPLICATE_COMMAND,
	REJECTED_STALE_REVISION,
	REJECTED_STALE_TICK,
	REJECTED_NOT_PARTICIPANT,
	REJECTED_NOT_READY,
	REJECTED_TARGET,
	REJECTED_RESOURCE,
	REJECTED_CLOSED,
	BUDGET_EXCEEDED,
}

var status: Status
var command_id: StringName
var encounter_id: StringName
var issuer_id: StringName
var target_id: StringName = &""
var health_delta: int = 0
var guard_delta: int = 0
var message: String = ""

func is_success() -> bool:
	return status in [
		Status.RESOLVED,
		Status.MISSED,
		Status.NO_EFFECT,
	]

func validate() -> Error:
	if status < Status.RESOLVED or status > Status.BUDGET_EXCEEDED:
		return ERR_INVALID_DATA
	if not command_id.is_empty() and not StableId.is_valid(command_id):
		return ERR_INVALID_DATA
	if not encounter_id.is_empty() and not StableId.is_valid(encounter_id):
		return ERR_INVALID_DATA
	return OK
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** l’objet transporte un statut métier stable et les deltas réellement appliqués.

- **Statuts à distinguer :** **Statuts à distinguer :** `MISSED` est une commande valide ayant consommé sa résolution ; `REJECTED_TARGET` signifie qu’aucune attaque n’a été autorisée.

- **Deltas :** **Deltas :** un dégât de santé est négatif ; une absorption de garde peut aussi être représentée par un delta négatif.

- **Valeur de retour :** **Valeur de retour :** `is_success()` inclut les issues valides sans effet, car elles ne doivent pas être retentées comme des erreurs techniques.

## 24. Événements et historique borné

> **[VSC] Visual Studio Code — Créer : `res://src/features/combat/domain/combat_event.gd`.**

```gdscript
class_name CombatEvent
extends RefCounted

enum Kind {
	ENCOUNTER_STARTED,
	PARTICIPANT_JOINED,
	COMMAND_ACCEPTED,
	ATTACK_MISSED,
	DAMAGE_APPLIED,
	GUARD_CHANGED,
	STATUS_APPLIED,
	STATUS_EXPIRED,
	PARTICIPANT_DEFEATED,
	PARTICIPANT_DISENGAGED,
	ENCOUNTER_CLOSED,
}

var event_id: StringName
var encounter_id: StringName
var kind: Kind
var logical_tick: int = 0
var sequence: int = 0
var source_character_id: StringName = &""
var target_character_id: StringName = &""
var amount: int = 0
var detail_id: StringName = &""

func validate() -> Error:
	if not StableId.is_valid(event_id):
		return ERR_INVALID_DATA
	if not StableId.is_valid(encounter_id):
		return ERR_INVALID_DATA
	if kind < Kind.ENCOUNTER_STARTED or kind > Kind.ENCOUNTER_CLOSED:
		return ERR_INVALID_DATA
	if logical_tick < 0 or sequence <= 0:
		return ERR_INVALID_DATA
	if not source_character_id.is_empty():
		if not CharacterId.is_valid(source_character_id):
			return ERR_INVALID_DATA
	if not target_character_id.is_empty():
		if not CharacterId.is_valid(target_character_id):
			return ERR_INVALID_DATA
	if amount < -100000000 or amount > 100000000:
		return ERR_INVALID_DATA
	if not detail_id.is_empty() and not StableId.is_valid(detail_id):
		return ERR_INVALID_DATA
	return OK

func duplicate_detached() -> CombatEvent:
	var copy := CombatEvent.new()
	copy.event_id = event_id
	copy.encounter_id = encounter_id
	copy.kind = kind
	copy.logical_tick = logical_tick
	copy.sequence = sequence
	copy.source_character_id = source_character_id
	copy.target_character_id = target_character_id
	copy.amount = amount
	copy.detail_id = detail_id
	return copy
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** l’événement décrit un fait déjà accepté par l’autorité de combat.

- **Déroulement ou instructions importantes :** **Ordre :** `logical_tick` puis `sequence` donnent une chronologie indépendante de l’heure système.

- **Données :** **Données :** les montants et identifiants de détail restent compacts ; un texte localisé n’est pas utilisé comme donnée métier.

- **Consommateurs :** **Consommateurs :** présentation, journal et narration peuvent écouter ces événements sans pouvoir annuler rétroactivement la résolution.

> **[VSC] Visual Studio Code — Créer : `res://src/features/combat/domain/combat_history.gd`.**

```gdscript
class_name CombatHistory
extends RefCounted

var _events: Array[CombatEvent] = []

func append(event: CombatEvent, maximum: int) -> Error:
	if event == null or event.validate() != OK:
		return ERR_INVALID_DATA
	if maximum < 1:
		return ERR_INVALID_PARAMETER
	_events.append(event.duplicate_detached())
	while _events.size() > maximum:
		_events.pop_front()
	return OK

func snapshot() -> Array[CombatEvent]:
	var copy: Array[CombatEvent] = []
	for event: CombatEvent in _events:
		copy.append(event.duplicate_detached())
	return copy

func validate(maximum: int) -> Error:
	if maximum < 1 or _events.size() > maximum:
		return ERR_OUT_OF_MEMORY
	var previous_tick := -1
	var previous_sequence := -1
	for event: CombatEvent in _events:
		if event == null or event.validate() != OK:
			return ERR_INVALID_DATA
		if event.logical_tick < previous_tick:
			return ERR_INVALID_DATA
		if event.logical_tick == previous_tick:
			if event.sequence <= previous_sequence:
				return ERR_INVALID_DATA
		previous_tick = event.logical_tick
		previous_sequence = event.sequence
	return OK

func duplicate_detached() -> CombatHistory:
	var copy := CombatHistory.new()
	for event: CombatEvent in _events:
		copy._events.append(event.duplicate_detached())
	return copy
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** l’historique conserve une fenêtre bornée d’événements autoritaires.

- **Bornage :** **Bornage :** les plus anciens événements sont retirés après l’ajout lorsque la capacité est dépassée.

- **Copie :** **Copie :** `append()`, `snapshot()` et `duplicate_detached()` recopient les événements ; aucun consommateur ne reçoit une référence mutable conservée par l’historique.

- **Invariants protégés :** **Validation :** l’ordre doit être croissant par tick puis séquence ; un chargement désordonné est refusé.

## 25. Dépôt d’affrontements

Le dépôt ne dépend ni des scènes ni des contrôleurs actifs.

> **[LECTURE] Contrat de dépôt — Structure de référence.**

```gdscript
class_name CombatRepository
extends RefCounted

func get_encounter(encounter_id: StringName) -> CombatEncounterState:
	return null

func replace_encounter(
	expected_revision: int,
	candidate: CombatEncounterState,
) -> Error:
	return ERR_UNAVAILABLE

func replace_all(candidates: Array[CombatEncounterState]) -> Error:
	return ERR_UNAVAILABLE

func all_encounter_ids_sorted() -> Array[StringName]:
	return []
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** le contrat impose une lecture détachée, un remplacement conditionnel, un remplacement complet préparé pour la restauration et un ordre canonique.

- **Concurrence :** **Concurrence :** `expected_revision` évite d’écraser un état modifié depuis la construction du candidat.

- **Refus contrôlé :** **Refus contrôlé :** la base renvoie `ERR_UNAVAILABLE`; l’implémentation doit remplacer explicitement les méthodes prises en charge.

- **Copies :** **Copies :** `get_encounter()` ne rend jamais l’objet mutable interne ; `replace_all()` valide l’ensemble avant de remplacer le contenu actif.

- **Frontières d’autorité :** **Frontière :** le dépôt ne calcule ni initiative ni dégâts.

## 26. Port de mutation des personnages

Le combat prépare un candidat de santé et d’endurance, puis demande au système des personnages de le valider et de le remplacer.

> **[VSC] Visual Studio Code — Créer : `res://src/features/combat/application/combat_mutation_unit_of_work.gd`.**

```gdscript
class_name CombatMutationUnitOfWork
extends RefCounted

func prepare_character_candidate(
	character_id: StringName,
) -> CharacterRuntimeState:
	return null

func prepare_combat_candidate(
	encounter_id: StringName,
) -> CombatEncounterState:
	return null

func commit(
	character_candidates: Array[CharacterRuntimeState],
	combat_candidates: Array[CombatEncounterState],
	expected_world_revision: int,
	expected_combat_revisions: Dictionary[StringName, int],
) -> Error:
	return ERR_UNAVAILABLE
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** ce port coordonne les candidats de plusieurs autorités sans déplacer leurs invariants dans le combat.

- **Préparation :** **Préparation :** les méthodes retournent des copies détachées ; aucune mutation active n’a encore eu lieu.

- **Commit :** **Commit :** les deux collections sont strictement typées ; l’implémentation revalide tous les candidats et toutes les révisions avant des swaps qui ne peuvent plus échouer individuellement.

- **Atomicité attendue :** **Atomicité attendue :** l’unité de travail possède les deux dépôts ou une transaction applicative commune ; elle n’effectue jamais un premier remplacement réversible suivi d’un second susceptible d’échouer. Cette propriété reste à tester au runtime.

## 27. Résoudre une attaque de base

Le service construit d’abord les candidats, puis calcule. Aucun effet n’est émis avant le commit.

> **[VSC] Visual Studio Code — Créer : `res://src/features/combat/application/combat_service.gd`.**

```gdscript
class_name CombatService
extends RefCounted

signal combat_resolved(result: CombatResult)
signal combat_event_emitted(event: CombatEvent)

var _rules: CombatRules
var _repository: CombatRepository
var _unit_of_work: CombatMutationUnitOfWork
var _snapshot_builder: CombatSnapshotBuilder
var _target_validator := TargetValidator.new()
var _initiative_policy := InitiativePolicy.new()
var _hit_resolver := HitResolver.new()
var _damage_resolver := DamageResolver.new()

func execute(command: CombatCommand) -> CombatResult:
	if command == null or command.validate() != OK:
		return _result(
			CombatResult.Status.REJECTED_INVALID_COMMAND,
			command,
			"commande invalide",
		)
	if _rules == null or _rules.validate() != OK:
		return _result(
			CombatResult.Status.REJECTED_RESOURCE,
			command,
			"règles indisponibles",
		)
	if _repository == null or _unit_of_work == null:
		return _result(
			CombatResult.Status.REJECTED_RESOURCE,
			command,
			"ports de mutation indisponibles",
		)
	if _snapshot_builder == null:
		return _result(
			CombatResult.Status.REJECTED_RESOURCE,
			command,
			"constructeur de snapshot indisponible",
		)

	var active := _repository.get_encounter(command.encounter_id)
	if active == null:
		return _result(
			CombatResult.Status.REJECTED_UNKNOWN_ENCOUNTER,
			command,
			"affrontement inconnu",
		)
	if active.closed:
		return _result(
			CombatResult.Status.REJECTED_CLOSED,
			command,
			"affrontement fermé",
		)
	if active.processed_command_ids.has(command.command_id):
		return _result(
			CombatResult.Status.REJECTED_DUPLICATE_COMMAND,
			command,
			"commande déjà traitée",
		)
	if active.revision != command.expected_combat_revision:
		return _result(
			CombatResult.Status.REJECTED_STALE_REVISION,
			command,
			"révision de combat obsolète",
		)
	if command.requested_tick < active.logical_tick:
		return _result(
			CombatResult.Status.REJECTED_STALE_TICK,
			command,
			"tick de commande antérieur à l’affrontement",
		)

	var issuer := active.get_participant(command.issuer_character_id)
	if issuer == null or issuer.disengaged:
		return _result(
			CombatResult.Status.REJECTED_NOT_PARTICIPANT,
			command,
			"émetteur non engagé",
		)
	if command.requested_tick < issuer.next_ready_tick:
		return _result(
			CombatResult.Status.REJECTED_NOT_READY,
			command,
			"participant indisponible",
		)

	match command.action_kind:
		CombatActionKind.Value.BASIC_ATTACK:
			return _execute_basic_attack(command)
		CombatActionKind.Value.GUARD:
			return _execute_guard(command)
		CombatActionKind.Value.WAIT:
			return _execute_wait(command)
		CombatActionKind.Value.DISENGAGE:
			return _execute_disengage(command)
		_:
			return _result(
				CombatResult.Status.REJECTED_INVALID_COMMAND,
				command,
				"action inconnue",
			)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** `execute()` constitue l’entrée unique du service et refuse les commandes invalides, anciennes, dupliquées ou prématurées.

- **Déroulement ou instructions importantes :** **Ordre :** les vérifications communes précèdent le `match`; aucune branche ne contourne identité, fermeture, idempotence ou initiative.

- **Statuts à distinguer :** **Statuts à distinguer :** une commande obsolète peut être reconstruite depuis un nouveau snapshot ; une commande dupliquée ne doit jamais être rejouée.

- **Effet de bord :** **Effet de bord :** ce premier niveau n’émet encore aucun événement ; il vérifie aussi les ports obligatoires, le tick et l’initiative avant de déléguer à une branche.

> **[LECTURE] Cœur de l’attaque — Suite du même fichier.**

```gdscript
func _execute_basic_attack(command: CombatCommand) -> CombatResult:
	var character_candidate := _unit_of_work.prepare_character_candidate(
		command.target_character_id
	)
	var combat_candidate := _unit_of_work.prepare_combat_candidate(
		command.encounter_id
	)
	if character_candidate == null or combat_candidate == null:
		return _result(
			CombatResult.Status.REJECTED_RESOURCE,
			command,
			"candidat indisponible",
		)
	if combat_candidate.advance_to(command.requested_tick) != OK:
		return _result(
			CombatResult.Status.REJECTED_STALE_TICK,
			command,
			"tick de résolution obsolète",
		)

	var snapshot := _snapshot_builder.build_for_basic_attack(
		command,
		combat_candidate,
	)
	if snapshot == null or snapshot.validate() != OK:
		return _result(
			CombatResult.Status.REJECTED_RESOURCE,
			command,
			"snapshot invalide",
		)

	var target_status := _target_validator.validate_basic_attack(
		snapshot,
		_rules,
	)
	if target_status != TargetValidator.Status.VALID:
		return _result(
			CombatResult.Status.REJECTED_TARGET,
			command,
			"cible refusée : %s" % target_status,
		)

	var rng := RandomNumberGenerator.new()
	rng.seed = combat_candidate.rng_seed
	rng.state = combat_candidate.rng_state
	var hit := _hit_resolver.resolve(
		_rules,
		snapshot.issuer_accuracy_permille,
		snapshot.target_evasion_permille,
		rng,
	)
	if hit == null:
		return _result(
			CombatResult.Status.REJECTED_RESOURCE,
			command,
			"résolution du toucher impossible",
		)
	combat_candidate.rng_state = rng.state

	var issuer_candidate := combat_candidate.get_participant(
		command.issuer_character_id
	)
	if issuer_candidate == null:
		return _result(
			CombatResult.Status.REJECTED_NOT_PARTICIPANT,
			command,
			"émetteur absent du candidat",
		)
	var delay := _initiative_policy.recovery_ticks(
		_rules,
		issuer_candidate.initiative_rank,
	)
	issuer_candidate.next_ready_tick = combat_candidate.logical_tick + delay
	_record_processed(combat_candidate, command.command_id)

	if not hit.hit:
		var no_character_candidates: Array[CharacterRuntimeState] = []
		return _commit_outcome(
			command,
			combat_candidate,
			no_character_candidates,
			CombatResult.Status.MISSED,
			0,
			0,
			false,
			"attaque manquée",
		)

	var packet := _snapshot_builder.build_basic_attack_packet(
		command,
		snapshot,
	)
	var profile := _snapshot_builder.build_defense_profile(snapshot)
	var target_definition := _snapshot_builder.definition_for(
		command.target_character_id
	)
	var target_combatant := combat_candidate.get_participant(
		command.target_character_id
	)
	if packet == null or profile == null:
		return _result(
			CombatResult.Status.REJECTED_RESOURCE,
			command,
			"données de dégâts indisponibles",
		)
	if target_definition == null or target_combatant == null:
		return _result(
			CombatResult.Status.REJECTED_RESOURCE,
			command,
			"cible autoritaire indisponible",
		)
	var damage := _damage_resolver.resolve(
		packet,
		profile,
		target_combatant.guard_points,
		_rules.maximum_resistance_permille,
	)
	if damage == null:
		return _result(
			CombatResult.Status.REJECTED_RESOURCE,
			command,
			"résolution des dégâts impossible",
		)

	target_combatant.guard_points -= damage.absorbed_by_guard
	var actual_health_delta := CharacterRules.apply_health_delta(
		character_candidate,
		target_definition,
		-damage.health_damage,
	)
	var status := CombatResult.Status.RESOLVED
	if damage.health_damage == 0 and damage.absorbed_by_guard == 0:
		status = CombatResult.Status.NO_EFFECT
	var character_candidates: Array[CharacterRuntimeState] = []
	character_candidates.append(character_candidate)
	return _commit_outcome(
		command,
		combat_candidate,
		character_candidates,
		status,
		actual_health_delta,
		-damage.absorbed_by_guard,
		not character_candidate.is_alive,
		"attaque résolue",
	)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** cette méthode prépare des copies, valide la cible, consomme un tirage, calcule les dégâts et tente un commit.

- **RNG :** **RNG :** le nouvel état est enregistré dans le candidat même si l’attaque manque ; une commande valide consomme exactement un tirage.

- **Initiative :** **Initiative :** le délai est appliqué aux attaques manquées comme réussies, empêchant un retry gratuit après un échec.

- **Santé :** **Santé :** `CharacterRules.apply_health_delta()` reste l’autorité de bornage et de cohérence avec `is_alive`.

- **Atomicité :** **Atomicité :** les deltas ne deviennent actifs que dans `_commit_outcome()`; un échec antérieur abandonne les candidats.

- **Port de données :** **Port de données :** le paquet, le profil et la définition viennent de `CombatSnapshotBuilder`; aucun chemin ou nom de classe fourni par la commande n’est chargé dynamiquement.

> **[LECTURE] Commit et résultat — Suite du même fichier.**

```gdscript
func _commit_outcome(
	command: CombatCommand,
	combat_candidate: CombatEncounterState,
	character_candidates: Array[CharacterRuntimeState],
	status: CombatResult.Status,
	health_delta: int,
	guard_delta: int,
	target_defeated: bool,
	message: String,
) -> CombatResult:
	var events := _build_outcome_events(
		command,
		combat_candidate,
		status,
		health_delta,
		guard_delta,
		target_defeated,
	)
	for event: CombatEvent in events:
		var history_code := combat_candidate.history.append(
			event,
			_rules.max_history_events,
		)
		if history_code != OK:
			return _result(
				CombatResult.Status.REJECTED_RESOURCE,
				command,
				"historique refusé : %s" % error_string(history_code),
			)

	combat_candidate.revision += 1
	var combat_candidates: Array[CombatEncounterState] = []
	combat_candidates.append(combat_candidate)
	var expected_revisions: Dictionary[StringName, int] = {
		command.encounter_id: command.expected_combat_revision,
	}
	var commit_code := _unit_of_work.commit(
		character_candidates,
		combat_candidates,
		command.expected_world_revision,
		expected_revisions,
	)
	if commit_code != OK:
		var rejected_status := CombatResult.Status.REJECTED_RESOURCE
		if commit_code == ERR_BUSY:
			rejected_status = CombatResult.Status.REJECTED_STALE_REVISION
		return _result(
			rejected_status,
			command,
			"commit refusé : %s" % error_string(commit_code),
		)

	var result := _result(status, command, message)
	result.health_delta = health_delta
	result.guard_delta = guard_delta
	combat_resolved.emit(result)
	for event: CombatEvent in events:
		combat_event_emitted.emit(event.duplicate_detached())
	return result

func _build_outcome_events(
	command: CombatCommand,
	encounter: CombatEncounterState,
	status: CombatResult.Status,
	health_delta: int,
	guard_delta: int,
	target_defeated: bool,
) -> Array[CombatEvent]:
	var events: Array[CombatEvent] = []
	events.append(_make_event(
		encounter,
		CombatEvent.Kind.COMMAND_ACCEPTED,
		command.issuer_character_id,
		command.target_character_id,
		0,
		command.action_id,
	))
	if status == CombatResult.Status.MISSED:
		events.append(_make_event(
			encounter,
			CombatEvent.Kind.ATTACK_MISSED,
			command.issuer_character_id,
			command.target_character_id,
			0,
			command.action_id,
		))
	elif health_delta < 0:
		events.append(_make_event(
			encounter,
			CombatEvent.Kind.DAMAGE_APPLIED,
			command.issuer_character_id,
			command.target_character_id,
			-health_delta,
			command.action_id,
		))
	if guard_delta != 0:
		var guard_target := command.target_character_id
		if guard_target.is_empty():
			guard_target = command.issuer_character_id
		events.append(_make_event(
			encounter,
			CombatEvent.Kind.GUARD_CHANGED,
			command.issuer_character_id,
			guard_target,
			guard_delta,
			command.action_id,
		))
	if command.action_kind == CombatActionKind.Value.DISENGAGE:
		events.append(_make_event(
			encounter,
			CombatEvent.Kind.PARTICIPANT_DISENGAGED,
			command.issuer_character_id,
			&"",
			0,
			command.action_id,
		))
	if target_defeated:
		events.append(_make_event(
			encounter,
			CombatEvent.Kind.PARTICIPANT_DEFEATED,
			command.issuer_character_id,
			command.target_character_id,
			0,
			command.action_id,
		))
	if encounter.closed:
		events.append(_make_event(
			encounter,
			CombatEvent.Kind.ENCOUNTER_CLOSED,
			command.issuer_character_id,
			&"",
			0,
			&"combat.event.encounter_closed",
		))
	return events

func _make_event(
	encounter: CombatEncounterState,
	kind: CombatEvent.Kind,
	source_id: StringName,
	target_id: StringName,
	amount: int,
	detail_id: StringName,
) -> CombatEvent:
	var event := CombatEvent.new()
	event.sequence = encounter.next_event_sequence()
	event.event_id = CombatId.event(encounter.encounter_id, event.sequence)
	event.encounter_id = encounter.encounter_id
	event.kind = kind
	event.logical_tick = encounter.logical_tick
	event.source_character_id = source_id
	event.target_character_id = target_id
	event.amount = amount
	event.detail_id = detail_id
	return event

func _record_processed(
	encounter: CombatEncounterState,
	command_id: StringName,
) -> void:
	encounter.processed_command_ids.append(command_id)
	while encounter.processed_command_ids.size() > _rules.max_history_events:
		encounter.processed_command_ids.pop_front()

func _result(
	status: CombatResult.Status,
	command: CombatCommand,
	message: String,
) -> CombatResult:
	var result := CombatResult.new()
	result.status = status
	result.message = message
	if command != null:
		result.command_id = command.command_id
		result.encounter_id = command.encounter_id
		result.issuer_id = command.issuer_character_id
		result.target_id = command.target_character_id
	return result
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** le commit précède toujours l’émission du résultat et des événements.

- **Concurrence :** **Concurrence :** `ERR_BUSY` signale une révision obsolète ; un autre code de commit devient un refus de ressource. Dans tous les cas, les candidats et événements préparés sont abandonnés.

- **Idempotence :** **Idempotence :** l’identifiant traité est ajouté au candidat avant commit et la liste reste bornée.

- **Historique et signaux :** **Historique et signaux :** les événements sont ajoutés au candidat avant le commit, puis des copies sont émises après succès ; l’historique persistant et la présentation décrivent ainsi le même résultat.

- **Limites et réserves :** Les branches `GUARD`, `WAIT` et `DISENGAGE` suivent la même discipline : candidat, validation, nouveau `next_ready_tick`, identifiant traité, commit, puis événements.

## 28. Garde, attente et désengagement

> **[LECTURE] Règles minimales des actions non offensives — Ne pas saisir.**

```text
GUARD
- exige un participant vivant et prêt
- ajoute une garde bornée issue du profil de base
- consomme un délai d'action
- ne restaure pas la santé

WAIT
- n'ajoute aucun effet
- avance uniquement next_ready_tick
- consomme la commande pour éviter les retries

DISENGAGE
- refuse si une règle de verrouillage l'interdit
- marque le participant disengaged dans le candidat
- retire ses commandes en attente lors du commit
- ferme l'affrontement s'il ne reste plus deux camps opposés
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** ce tableau fixe les invariants communs sans anticiper les postures ou compétences du chapitre 19.

- **Garde :** **Garde :** elle constitue une réserve temporaire distincte de la santé et ne peut pas dépasser la borne du domaine.

- **Attente :** **Attente :** elle est une action valide, utile pour la chronologie et la simulation hors écran.

- **Désengagement :** **Désengagement :** il modifie l’appartenance à l’affrontement, pas l’existence du personnage.

> **[LECTURE] Implémentation des trois branches — Suite de `combat_service.gd`.**

```gdscript
func _execute_guard(command: CombatCommand) -> CombatResult:
	var candidate := _prepare_non_offensive_candidate(command)
	if candidate == null:
		return _result(
			CombatResult.Status.REJECTED_RESOURCE,
			command,
			"candidat de garde indisponible",
		)
	var issuer := candidate.get_participant(command.issuer_character_id)
	var previous_guard := issuer.guard_points
	issuer.guard_points = mini(
		CombatantState.MAX_GUARD,
		issuer.guard_points + _rules.base_guard_gain,
	)
	_apply_recovery(issuer, candidate.logical_tick)
	_record_processed(candidate, command.command_id)
	var characters: Array[CharacterRuntimeState] = []
	return _commit_outcome(
		command, candidate, characters, CombatResult.Status.RESOLVED,
		0, issuer.guard_points - previous_guard, false, "garde appliquée",
	)

func _execute_wait(command: CombatCommand) -> CombatResult:
	var candidate := _prepare_non_offensive_candidate(command)
	if candidate == null:
		return _result(
			CombatResult.Status.REJECTED_RESOURCE,
			command,
			"candidat d’attente indisponible",
		)
	var issuer := candidate.get_participant(command.issuer_character_id)
	_apply_recovery(issuer, candidate.logical_tick)
	_record_processed(candidate, command.command_id)
	var characters: Array[CharacterRuntimeState] = []
	return _commit_outcome(
		command, candidate, characters, CombatResult.Status.RESOLVED,
		0, 0, false, "attente résolue",
	)

func _execute_disengage(command: CombatCommand) -> CombatResult:
	var candidate := _prepare_non_offensive_candidate(command)
	if candidate == null:
		return _result(
			CombatResult.Status.REJECTED_RESOURCE,
			command,
			"candidat de désengagement indisponible",
		)
	var issuer := candidate.get_participant(command.issuer_character_id)
	issuer.disengaged = true
	_apply_recovery(issuer, candidate.logical_tick)
	_record_processed(candidate, command.command_id)
	candidate.closed = not _has_two_active_sides(candidate)
	var characters: Array[CharacterRuntimeState] = []
	return _commit_outcome(
		command, candidate, characters, CombatResult.Status.RESOLVED,
		0, 0, false, "désengagement résolu",
	)

func _prepare_non_offensive_candidate(
	command: CombatCommand,
) -> CombatEncounterState:
	var candidate := _unit_of_work.prepare_combat_candidate(
		command.encounter_id
	)
	if candidate == null:
		return null
	if candidate.advance_to(command.requested_tick) != OK:
		return null
	var issuer := candidate.get_participant(command.issuer_character_id)
	if issuer == null or issuer.disengaged:
		return null
	return candidate

func _apply_recovery(issuer: CombatantState, logical_tick: int) -> void:
	var delay := _initiative_policy.recovery_ticks(
		_rules,
		issuer.initiative_rank,
	)
	issuer.next_ready_tick = logical_tick + delay

func _has_two_active_sides(encounter: CombatEncounterState) -> bool:
	var sides: Dictionary[StringName, bool] = {}
	for value: Variant in encounter.participants.values():
		var participant := value as CombatantState
		if participant == null or participant.disengaged:
			continue
		sides[participant.side_id] = true
		if sides.size() >= 2:
			return true
	return false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Discipline commune :** **Discipline commune :** chaque branche prépare un candidat détaché, avance le tick sans régression, applique le délai, enregistre l’idempotence et utilise le même commit typé.

- **Garde :** **Garde :** le delta renvoyé correspond à l’augmentation réelle après la borne `MAX_GUARD`.

- **Attente :** **Attente :** aucun autre état ne change, mais la commande et le délai sont consommés.

- **Désengagement :** **Désengagement :** les côtés actifs sont recalculés depuis `side_id`; l’affrontement se ferme lorsqu’il ne reste plus deux côtés engagés.

## 29. Adapter une requête d’agent

L’exécuteur du chapitre 17 transforme `AgentActionRequest` en `CombatCommand`. Il ne recopie pas une valeur de dégâts proposée par l’agent.

> **[VSC] Visual Studio Code — Créer : `res://src/features/combat/application/combat_context_port.gd`.**

```gdscript
class_name CombatContextPort
extends RefCounted

class Context:
	extends RefCounted

	var encounter_id: StringName
	var combat_revision: int = 0

	func validate() -> Error:
		if not StableId.is_valid(encounter_id):
			return ERR_INVALID_DATA
		if combat_revision < 0:
			return ERR_INVALID_DATA
		return OK

func snapshot_for(
	issuer_id: StringName,
	target_id: StringName,
) -> Context:
	return null
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** ce port localise l’affrontement commun et sa révision sans donner à l’agent un accès au dépôt de combat.

- **Paramètres et types importants :** **Entrées :** les deux identités proviennent d’une requête déjà validée ; l’implémentation refuse les personnages non engagés dans un même affrontement.

- **Valeur de retour :** **Valeur de retour :** `null` signifie qu’aucun contexte exécutable n’existe ; un objet retourné doit réussir `validate()`.

> **[VSC] Visual Studio Code — Créer : `res://src/features/combat/application/combat_agent_action_executor.gd`.**

```gdscript
class_name CombatAgentActionExecutor
extends AgentActionExecutor

const EXECUTOR_KEY := &"agent.executor.combat_command"
const BASIC_ATTACK_ACTION := &"agent.action.combat.basic_attack"

var _combat_context: CombatContextPort
var _combat_service: CombatService

func can_execute(request: AgentActionRequest) -> Error:
	if request == null or request.validate() != OK:
		return ERR_INVALID_DATA
	if request.executor_key != EXECUTOR_KEY:
		return ERR_UNAVAILABLE
	if request.action_id != BASIC_ATTACK_ACTION:
		return ERR_UNAVAILABLE
	if not CharacterId.is_valid(request.target_character_id):
		return ERR_INVALID_DATA
	if _combat_context == null or _combat_service == null:
		return ERR_UNCONFIGURED
	return OK

func start(request: AgentActionRequest) -> Error:
	var check := can_execute(request)
	if check != OK:
		return check
	var context := _combat_context.snapshot_for(
		request.owner_character_id,
		request.target_character_id,
	)
	if context == null or context.validate() != OK:
		return ERR_DOES_NOT_EXIST
	var command := CombatCommand.new()
	command.command_id = CombatId.command(
		context.encounter_id,
		request.owner_character_id,
		request.decision_sequence,
	)
	command.encounter_id = context.encounter_id
	command.issuer_character_id = request.owner_character_id
	command.target_character_id = request.target_character_id
	command.action_kind = CombatActionKind.Value.BASIC_ATTACK
	command.action_id = &"combat.action.basic_attack"
	command.requested_tick = request.logical_tick
	command.issuer_sequence = request.decision_sequence
	command.expected_combat_revision = context.combat_revision
	command.expected_world_revision = request.snapshot_revision
	var result := _combat_service.execute(command)
	return OK if result.is_success() else ERR_CANT_RESOLVE

func cancel(_request_id: StringName, _reason: StringName) -> Error:
	return ERR_UNAVAILABLE
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** l’adaptateur convertit le vocabulaire de l’agent vers celui du combat puis appelle l’autorité.

- **Invariants protégés :** **Validation :** seules la clé et l’action explicitement enregistrées sont acceptées ; aucune classe n’est chargée depuis les données.

- **Révisions :** **Révisions :** la révision du monde vient de la décision d’agent et la révision du combat vient d’un contexte relu au démarrage.

- **Annulation :** **Annulation :** une résolution atomique déjà exécutée n’est pas annulable ; les actions longues futures devront être représentées par une phase préparatoire distincte.

- **Valeur de retour ou traitement du résultat :** **Traitement du résultat :** `OK` signifie que la commande a été valablement consommée, y compris lors d’un raté ; un refus métier produit `ERR_CANT_RESOLVE`.

## 30. Adapter l’entrée du joueur

Le contrôleur du joueur produit la même `CombatCommand`. Il peut choisir une cible depuis l’interface, mais la sélection visuelle ne vaut pas validation autoritaire.

La présentation peut afficher une prévisualisation de portée calculée localement. Le service répète toujours la vérification sur son snapshot au moment de l’exécution.

## 31. File de commandes

Une file bornée absorbe les demandes arrivées entre deux ticks physiques.

> **[VSC] Visual Studio Code — Créer : `res://src/features/combat/application/combat_command_queue.gd`.**

```gdscript
class_name CombatCommandQueue
extends RefCounted

var _commands: Array[CombatCommand] = []

func enqueue(command: CombatCommand, maximum: int) -> Error:
	if command == null or command.validate() != OK:
		return ERR_INVALID_DATA
	if maximum < 1:
		return ERR_INVALID_PARAMETER
	if _commands.size() >= maximum:
		return ERR_BUSY
	for existing: CombatCommand in _commands:
		if existing.command_id == command.command_id:
			return ERR_ALREADY_EXISTS
	_commands.append(command.duplicate_detached())
	_commands.sort_custom(_comes_before)
	return OK

func pop_front() -> CombatCommand:
	if _commands.is_empty():
		return null
	return _commands.pop_front()

func size() -> int:
	return _commands.size()

func remove_for_character(character_id: StringName) -> int:
	var removed := 0
	for index in range(_commands.size() - 1, -1, -1):
		var command := _commands[index]
		if command.issuer_character_id == character_id:
			_commands.remove_at(index)
			removed += 1
	return removed

func clear() -> void:
	_commands.clear()

func _comes_before(a: CombatCommand, b: CombatCommand) -> bool:
	if a.requested_tick != b.requested_tick:
		return a.requested_tick < b.requested_tick
	if a.issuer_sequence != b.issuer_sequence:
		return a.issuer_sequence < b.issuer_sequence
	return String(a.command_id) < String(b.command_id)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** la file conserve des copies triées et refuse surcharge ou doublon.

- **Déroulement ou instructions importantes :** **Ordre :** tick demandé, séquence de l’émetteur puis identifiant forment un ordre total.

- **Refus contrôlé :** **Refus contrôlé :** `ERR_BUSY` signale une capacité atteinte ; l’appelant peut reporter une décision sans agrandir la mémoire.

- **Annulation et persistance :** **Annulation et persistance :** `remove_for_character()` retire les demandes d’un participant désengagé ; `clear()` est utilisé par la barrière de sauvegarde. La file reste transitoire et n’est jamais encodée.

## 32. Ordonnanceur borné

L’ordonnanceur traite un nombre maximal de commandes par tick physique. Les microsecondes servent à la télémétrie, pas à décider quelles commandes gagnent.

> **[VSC] Visual Studio Code — Créer : `res://src/features/combat/application/combat_scheduler.gd`.**

```gdscript
class_name CombatScheduler
extends Node

signal queue_backlogged(remaining: int)
signal command_completed(result: CombatResult)

var _rules: CombatRules
var _queue := CombatCommandQueue.new()
var _service: CombatService

func submit(command: CombatCommand) -> Error:
	if _rules == null or _rules.validate() != OK:
		return ERR_UNCONFIGURED
	return _queue.enqueue(command, _rules.max_queued_commands)

func _physics_process(_delta: float) -> void:
	if _rules == null or _service == null:
		return
	var processed := 0
	while processed < _rules.commands_per_physics_tick:
		var command := _queue.pop_front()
		if command == null:
			break
		var result := _service.execute(command)
		if result.is_success():
			if command.action_kind == CombatActionKind.Value.DISENGAGE:
				_queue.remove_for_character(command.issuer_character_id)
		command_completed.emit(result)
		processed += 1
	if _queue.size() > 0:
		queue_backlogged.emit(_queue.size())
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** le nœud relie la file logique au rythme physique sans rendre la vitesse du processeur autoritaire.

- **Budgets et limites :** **Budget :** au plus `commands_per_physics_tick` commandes sont consommées ; les autres restent dans leur ordre canonique.

- **Effets de bord :** **Effets de bord :** chaque résultat est émis après l’appel du service ; un désengagement committé retire les commandes restantes de son émetteur, sans calcul de dégâts dans le nœud.

- **Diagnostic :** **Diagnostic :** `queue_backlogged` expose la pression de la file sans supprimer ni réordonner les commandes.

## 33. Combat actif et simulation hors écran

Le même domaine est utilisé dans deux modes.

### 33.1 Mode actif

- positions lues depuis les états de personnages synchronisés ;
- ligne de vue fournie par l’adaptateur physique ;
- commandes traitées dans `_physics_process()` ;
- animations et audio déclenchés après événement.

### 33.2 Mode hors écran

- positions représentées par cellules, zones ou coordonnées logiques ;
- ligne de vue calculée depuis les connexions et obstacles de la partition ;
- nombre de résolutions réduit par tick ;
- aucun `CharacterBody3D`, `Area3D`, rayon ou animation requis.

La simulation hors écran ne doit pas inventer une seconde formule de dégâts. Elle change les entrées spatiales et la fréquence, pas l’autorité métier.

## 34. Révisions et invalidation

Une commande est refusée lorsque :

- `expected_world_revision` ne correspond plus au monde ;
- `expected_combat_revision` ne correspond plus à l’affrontement ;
- `requested_tick` est antérieur au tick logique déjà committé ;
- la cible est morte, sortie, du même côté lorsque le tir allié est interdit, déplacée hors portée ou masquée ;
- l’émetteur n’est plus prêt ;
- l’identifiant a déjà été traité.

Le refus n’est pas automatiquement un bug. Il peut être la conséquence normale d’un monde qui évolue entre planification et exécution.

## 35. Sauvegarder à une frontière stable

Une sauvegarde n’enregistre pas une animation à 43 %, un rayon déjà lancé ou une commande au milieu de son commit.

La coordination suit cette séquence :

> **[LECTURE] Barrière de sauvegarde — Ne pas saisir.**

```text
1. arrêter temporairement l'acceptation de nouvelles commandes
2. terminer ou abandonner la commande atomique courante
3. vérifier que la file transitoire est vide
4. copier les affrontements autoritaires
5. encoder et valider toutes les sections
6. écrire le document de sauvegarde
7. rouvrir l'acceptation des commandes
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** la barrière produit un snapshot cohérent sans sérialiser une mutation partielle.

- **File :** **File :** les commandes non commencées sont abandonnées et pourront être reconstruites par le joueur ou l’agent après reprise.

- **Atomicité :** **Atomicité :** aucun affrontement n’est encodé pendant que son commit est en cours.

- **Limites et réserves :** **Limite :** la coordination runtime avec les autres sections sera testée au chapitre 27.

## 36. Snapshot persistant

Sont persistés :

- identifiant, tick, révision, séquence d’événement et fermeture de l’affrontement ;
- graine et état du RNG local ;
- participants, côté, disponibilité, initiative, garde, séquence et désengagement ;
- états actifs avec leurs intervalles ;
- identifiants de commandes récemment traitées ;
- historique borné si le produit exige une reprise du journal.

Ne sont pas persistés :

- snapshots de résolution ;
- profil de défense dérivé ;
- ligne de vue ;
- résultats de raycast ;
- file de commandes ;
- animations, sons et VFX ;
- listes prêtes ou caches triés.

## 37. Codec strict

> **[VSC] Visual Studio Code — Créer : `res://src/features/combat/infrastructure/combat_snapshot_codec.gd`.**

```gdscript
class_name CombatSnapshotCodec
extends RefCounted

class DecodeResult:
	extends RefCounted

	var code: Error = FAILED
	var encounters: Array[CombatEncounterState] = []
	var message: String = ""

	func is_success() -> bool:
		return code == OK

const FORMAT := "project-asteria-combat"
const VERSION := 1
const JSON_SAFE_INT_MAX := 9007199254740991
const INT32_MIN := -2147483648
const INT32_MAX := 2147483647
const UINT32_MAX := 4294967295

const ROOT_KEYS := ["format", "version", "encounters"]
const ENCOUNTER_KEYS := [
	"encounter_id",
	"logical_tick",
	"revision",
	"event_sequence",
	"rng_seed_hi",
	"rng_seed_lo",
	"rng_state_hi",
	"rng_state_lo",
	"closed",
	"participants",
	"processed_command_ids",
	"history",
]
const PARTICIPANT_KEYS := [
	"character_id",
	"side_id",
	"next_ready_tick",
	"initiative_rank",
	"guard_points",
	"command_sequence",
	"disengaged",
	"active_statuses",
]
const STATUS_KEYS := [
	"status_id",
	"source_character_id",
	"stack_rule",
	"stacks",
	"max_stacks",
	"applied_tick",
	"expires_at_tick",
	"accuracy_modifier_permille",
	"evasion_modifier_permille",
	"defense_modifier",
	"initiative_modifier",
]
const EVENT_KEYS := [
	"event_id",
	"encounter_id",
	"kind",
	"logical_tick",
	"sequence",
	"source_character_id",
	"target_character_id",
	"amount",
	"detail_id",
]

func encode(
	encounters: Array[CombatEncounterState],
	rules: CombatRules,
) -> Dictionary:
	if rules == null or rules.validate() != OK:
		return {}
	if encounters.size() > rules.max_encounters:
		return {}
	var sorted: Array[CombatEncounterState] = []
	for encounter: CombatEncounterState in encounters:
		if encounter == null or encounter.validate(rules) != OK:
			return {}
		sorted.append(encounter.duplicate_detached())
	sorted.sort_custom(
		func(a: CombatEncounterState, b: CombatEncounterState) -> bool:
			return String(a.encounter_id) < String(b.encounter_id)
	)
	var encoded: Array[Dictionary] = []
	for encounter: CombatEncounterState in sorted:
		encoded.append(_encode_encounter(encounter))
	return {
		"format": FORMAT,
		"version": VERSION,
		"encounters": encoded,
	}

func decode(document: Dictionary, rules: CombatRules) -> DecodeResult:
	if rules == null or rules.validate() != OK:
		return _failure(ERR_UNCONFIGURED, "règles invalides")
	if not _has_exact_keys(document, ROOT_KEYS):
		return _failure(ERR_INVALID_DATA, "clés racine invalides")
	if typeof(document.get("format")) != TYPE_STRING:
		return _failure(ERR_INVALID_DATA, "format non textuel")
	if String(document.get("format")) != FORMAT:
		return _failure(ERR_FILE_UNRECOGNIZED, "format inconnu")
	var version_value: Variant = _read_int(document.get("version"), 1, VERSION)
	if version_value == null or int(version_value) != VERSION:
		return _failure(ERR_FILE_UNRECOGNIZED, "version inconnue")
	var raw_encounters: Variant = document.get("encounters")
	if typeof(raw_encounters) != TYPE_ARRAY:
		return _failure(ERR_INVALID_DATA, "encounters non tabulaire")
	var raw_array := raw_encounters as Array
	if raw_array.size() > rules.max_encounters:
		return _failure(ERR_OUT_OF_MEMORY, "trop d’affrontements")

	var decoded: Array[CombatEncounterState] = []
	var seen: Dictionary[StringName, bool] = {}
	for raw: Variant in raw_array:
		if typeof(raw) != TYPE_DICTIONARY:
			return _failure(ERR_INVALID_DATA, "affrontement non objet")
		var encounter := _decode_encounter(raw as Dictionary, rules)
		if encounter == null:
			return _failure(ERR_INVALID_DATA, "affrontement invalide")
		if seen.has(encounter.encounter_id):
			return _failure(ERR_ALREADY_EXISTS, "affrontement dupliqué")
		seen[encounter.encounter_id] = true
		decoded.append(encounter)
	decoded.sort_custom(
		func(a: CombatEncounterState, b: CombatEncounterState) -> bool:
			return String(a.encounter_id) < String(b.encounter_id)
	)
	var result := DecodeResult.new()
	result.code = OK
	result.encounters = decoded
	return result

func _encode_encounter(encounter: CombatEncounterState) -> Dictionary:
	var participant_ids: Array[StringName] = []
	participant_ids.assign(encounter.participants.keys())
	participant_ids.sort()
	var participants: Array[Dictionary] = []
	for character_id: StringName in participant_ids:
		participants.append(_encode_participant(encounter.participants[character_id]))

	var processed: Array[String] = []
	for command_id: StringName in encounter.processed_command_ids:
		processed.append(String(command_id))

	var history: Array[Dictionary] = []
	for event: CombatEvent in encounter.history.snapshot():
		history.append(_encode_event(event))
	var seed_parts := _split_int64(encounter.rng_seed)
	var state_parts := _split_int64(encounter.rng_state)
	return {
		"encounter_id": String(encounter.encounter_id),
		"logical_tick": encounter.logical_tick,
		"revision": encounter.revision,
		"event_sequence": encounter.event_sequence,
		"rng_seed_hi": seed_parts[0],
		"rng_seed_lo": seed_parts[1],
		"rng_state_hi": state_parts[0],
		"rng_state_lo": state_parts[1],
		"closed": encounter.closed,
		"participants": participants,
		"processed_command_ids": processed,
		"history": history,
	}

func _decode_encounter(
	raw: Dictionary,
	rules: CombatRules,
) -> CombatEncounterState:
	if not _has_exact_keys(raw, ENCOUNTER_KEYS):
		return null
	var encounter_id := _required_stable_id(raw.get("encounter_id"))
	if encounter_id.is_empty():
		return null
	var logical_tick: Variant = _read_int(
		raw.get("logical_tick"), 0, JSON_SAFE_INT_MAX
	)
	var revision: Variant = _read_int(raw.get("revision"), 0, JSON_SAFE_INT_MAX)
	var event_sequence: Variant = _read_int(
		raw.get("event_sequence"), 0, JSON_SAFE_INT_MAX
	)
	var seed_hi: Variant = _read_int(raw.get("rng_seed_hi"), INT32_MIN, INT32_MAX)
	var seed_lo: Variant = _read_int(raw.get("rng_seed_lo"), 0, UINT32_MAX)
	var state_hi: Variant = _read_int(raw.get("rng_state_hi"), INT32_MIN, INT32_MAX)
	var state_lo: Variant = _read_int(raw.get("rng_state_lo"), 0, UINT32_MAX)
	if null in [
		logical_tick, revision, event_sequence,
		seed_hi, seed_lo, state_hi, state_lo,
	]:
		return null
	if typeof(raw.get("closed")) != TYPE_BOOL:
		return null
	if typeof(raw.get("participants")) != TYPE_ARRAY:
		return null
	if typeof(raw.get("processed_command_ids")) != TYPE_ARRAY:
		return null
	if typeof(raw.get("history")) != TYPE_ARRAY:
		return null

	var encounter := CombatEncounterState.new()
	encounter.encounter_id = encounter_id
	encounter.logical_tick = int(logical_tick)
	encounter.revision = int(revision)
	encounter.event_sequence = int(event_sequence)
	encounter.rng_seed = _join_int64(int(seed_hi), int(seed_lo))
	encounter.rng_state = _join_int64(int(state_hi), int(state_lo))
	encounter.closed = bool(raw.get("closed"))

	var raw_participants := raw.get("participants") as Array
	if raw_participants.is_empty():
		return null
	if raw_participants.size() > rules.max_participants:
		return null
	for raw_participant: Variant in raw_participants:
		if typeof(raw_participant) != TYPE_DICTIONARY:
			return null
		var participant := _decode_participant(
			raw_participant as Dictionary,
			rules,
		)
		if participant == null:
			return null
		if encounter.participants.has(participant.character_id):
			return null
		encounter.participants[participant.character_id] = participant

	var raw_processed := raw.get("processed_command_ids") as Array
	if raw_processed.size() > rules.max_history_events:
		return null
	var seen_commands: Dictionary[StringName, bool] = {}
	for raw_command_id: Variant in raw_processed:
		var command_id := _required_stable_id(raw_command_id)
		if command_id.is_empty() or seen_commands.has(command_id):
			return null
		seen_commands[command_id] = true
		encounter.processed_command_ids.append(command_id)

	var raw_history := raw.get("history") as Array
	if raw_history.size() > rules.max_history_events:
		return null
	var maximum_sequence := 0
	for raw_event: Variant in raw_history:
		if typeof(raw_event) != TYPE_DICTIONARY:
			return null
		var event := _decode_event(raw_event as Dictionary)
		if event == null or event.encounter_id != encounter_id:
			return null
		if event.event_id != CombatId.event(encounter_id, event.sequence):
			return null
		if encounter.history.append(event, rules.max_history_events) != OK:
			return null
		maximum_sequence = maxi(maximum_sequence, event.sequence)
	if maximum_sequence > encounter.event_sequence:
		return null
	if encounter.validate(rules) != OK:
		return null
	return encounter

func _encode_participant(participant: CombatantState) -> Dictionary:
	var statuses: Array[ActiveStatus] = []
	for status: ActiveStatus in participant.active_statuses:
		statuses.append(status.duplicate_detached())
	statuses.sort_custom(
		func(a: ActiveStatus, b: ActiveStatus) -> bool:
			return String(a.status_id) < String(b.status_id)
	)
	var encoded_statuses: Array[Dictionary] = []
	for status: ActiveStatus in statuses:
		encoded_statuses.append(_encode_status(status))
	return {
		"character_id": String(participant.character_id),
		"side_id": String(participant.side_id),
		"next_ready_tick": participant.next_ready_tick,
		"initiative_rank": participant.initiative_rank,
		"guard_points": participant.guard_points,
		"command_sequence": participant.command_sequence,
		"disengaged": participant.disengaged,
		"active_statuses": encoded_statuses,
	}

func _decode_participant(
	raw: Dictionary,
	rules: CombatRules,
) -> CombatantState:
	if not _has_exact_keys(raw, PARTICIPANT_KEYS):
		return null
	var character_id := _required_character_id(raw.get("character_id"))
	var side_id := _required_stable_id(raw.get("side_id"))
	if character_id.is_empty() or side_id.is_empty():
		return null
	var next_ready: Variant = _read_int(
		raw.get("next_ready_tick"), 0, JSON_SAFE_INT_MAX
	)
	var initiative: Variant = _read_int(raw.get("initiative_rank"), -100000, 100000)
	var guard: Variant = _read_int(raw.get("guard_points"), 0, CombatantState.MAX_GUARD)
	var sequence: Variant = _read_int(
		raw.get("command_sequence"), 0, JSON_SAFE_INT_MAX
	)
	if null in [next_ready, initiative, guard, sequence]:
		return null
	if typeof(raw.get("disengaged")) != TYPE_BOOL:
		return null
	if typeof(raw.get("active_statuses")) != TYPE_ARRAY:
		return null
	var raw_statuses := raw.get("active_statuses") as Array
	if raw_statuses.size() > rules.max_statuses_per_combatant:
		return null

	var participant := CombatantState.new()
	participant.character_id = character_id
	participant.side_id = side_id
	participant.next_ready_tick = int(next_ready)
	participant.initiative_rank = int(initiative)
	participant.guard_points = int(guard)
	participant.command_sequence = int(sequence)
	participant.disengaged = bool(raw.get("disengaged"))
	var seen_statuses: Dictionary[StringName, bool] = {}
	for raw_status: Variant in raw_statuses:
		if typeof(raw_status) != TYPE_DICTIONARY:
			return null
		var status := _decode_status(raw_status as Dictionary)
		if status == null or seen_statuses.has(status.status_id):
			return null
		seen_statuses[status.status_id] = true
		participant.active_statuses.append(status)
	participant.active_statuses.sort_custom(
		func(a: ActiveStatus, b: ActiveStatus) -> bool:
			return String(a.status_id) < String(b.status_id)
	)
	if participant.validate(rules) != OK:
		return null
	return participant

func _encode_status(status: ActiveStatus) -> Dictionary:
	return {
		"status_id": String(status.status_id),
		"source_character_id": String(status.source_character_id),
		"stack_rule": int(status.stack_rule),
		"stacks": status.stacks,
		"max_stacks": status.max_stacks,
		"applied_tick": status.applied_tick,
		"expires_at_tick": status.expires_at_tick,
		"accuracy_modifier_permille": status.accuracy_modifier_permille,
		"evasion_modifier_permille": status.evasion_modifier_permille,
		"defense_modifier": status.defense_modifier,
		"initiative_modifier": status.initiative_modifier,
	}

func _decode_status(raw: Dictionary) -> ActiveStatus:
	if not _has_exact_keys(raw, STATUS_KEYS):
		return null
	var status_id := _required_stable_id(raw.get("status_id"))
	var source_id := _required_character_id(raw.get("source_character_id"))
	if status_id.is_empty() or source_id.is_empty():
		return null
	var stack_rule: Variant = _read_int(
		raw.get("stack_rule"),
		ActiveStatus.StackRule.REPLACE,
		ActiveStatus.StackRule.ADD_STACK,
	)
	var stacks: Variant = _read_int(raw.get("stacks"), 1, 100000)
	var max_stacks: Variant = _read_int(raw.get("max_stacks"), 1, 100000)
	var applied: Variant = _read_int(raw.get("applied_tick"), 0, JSON_SAFE_INT_MAX)
	var expires: Variant = _read_int(raw.get("expires_at_tick"), 1, JSON_SAFE_INT_MAX)
	var accuracy: Variant = _read_int(
		raw.get("accuracy_modifier_permille"), -100000, 100000
	)
	var evasion: Variant = _read_int(
		raw.get("evasion_modifier_permille"), -100000, 100000
	)
	var defense: Variant = _read_int(raw.get("defense_modifier"), -100000, 100000)
	var initiative: Variant = _read_int(
		raw.get("initiative_modifier"), -100000, 100000
	)
	if null in [
		stack_rule, stacks, max_stacks, applied, expires,
		accuracy, evasion, defense, initiative,
	]:
		return null
	var status := ActiveStatus.new()
	status.status_id = status_id
	status.source_character_id = source_id
	status.stack_rule = int(stack_rule)
	status.stacks = int(stacks)
	status.max_stacks = int(max_stacks)
	status.applied_tick = int(applied)
	status.expires_at_tick = int(expires)
	status.accuracy_modifier_permille = int(accuracy)
	status.evasion_modifier_permille = int(evasion)
	status.defense_modifier = int(defense)
	status.initiative_modifier = int(initiative)
	return status if status.validate() == OK else null

func _encode_event(event: CombatEvent) -> Dictionary:
	return {
		"event_id": String(event.event_id),
		"encounter_id": String(event.encounter_id),
		"kind": int(event.kind),
		"logical_tick": event.logical_tick,
		"sequence": event.sequence,
		"source_character_id": String(event.source_character_id),
		"target_character_id": String(event.target_character_id),
		"amount": event.amount,
		"detail_id": String(event.detail_id),
	}

func _decode_event(raw: Dictionary) -> CombatEvent:
	if not _has_exact_keys(raw, EVENT_KEYS):
		return null
	var event_id := _required_stable_id(raw.get("event_id"))
	var encounter_id := _required_stable_id(raw.get("encounter_id"))
	if event_id.is_empty() or encounter_id.is_empty():
		return null
	var kind: Variant = _read_int(
		raw.get("kind"), CombatEvent.Kind.ENCOUNTER_STARTED,
		CombatEvent.Kind.ENCOUNTER_CLOSED,
	)
	var logical_tick: Variant = _read_int(
		raw.get("logical_tick"), 0, JSON_SAFE_INT_MAX
	)
	var sequence: Variant = _read_int(raw.get("sequence"), 1, JSON_SAFE_INT_MAX)
	var amount: Variant = _read_int(
		raw.get("amount"), -JSON_SAFE_INT_MAX, JSON_SAFE_INT_MAX
	)
	if null in [kind, logical_tick, sequence, amount]:
		return null
	var source_id := _optional_character_id(raw.get("source_character_id"))
	var target_id := _optional_character_id(raw.get("target_character_id"))
	var detail_id := _optional_stable_id(raw.get("detail_id"))
	if source_id == null or target_id == null or detail_id == null:
		return null
	var event := CombatEvent.new()
	event.event_id = event_id
	event.encounter_id = encounter_id
	event.kind = int(kind)
	event.logical_tick = int(logical_tick)
	event.sequence = int(sequence)
	event.source_character_id = StringName(String(source_id))
	event.target_character_id = StringName(String(target_id))
	event.amount = int(amount)
	event.detail_id = StringName(String(detail_id))
	return event if event.validate() == OK else null

func _read_int(value: Variant, minimum: int, maximum: int) -> Variant:
	var parsed: int
	if typeof(value) == TYPE_INT:
		parsed = int(value)
	elif typeof(value) == TYPE_FLOAT:
		var number := float(value)
		if not is_finite(number) or number != floor(number):
			return null
		if absf(number) > float(JSON_SAFE_INT_MAX):
			return null
		parsed = int(number)
	else:
		return null
	if parsed < minimum or parsed > maximum:
		return null
	return parsed

func _required_stable_id(value: Variant) -> StringName:
	if typeof(value) != TYPE_STRING:
		return &""
	var result := StringName(String(value))
	return result if StableId.is_valid(result) else &""

func _required_character_id(value: Variant) -> StringName:
	if typeof(value) != TYPE_STRING:
		return &""
	var result := StringName(String(value))
	return result if CharacterId.is_valid(result) else &""

func _optional_stable_id(value: Variant) -> Variant:
	if typeof(value) != TYPE_STRING:
		return null
	var result := StringName(String(value))
	if result.is_empty() or StableId.is_valid(result):
		return result
	return null

func _optional_character_id(value: Variant) -> Variant:
	if typeof(value) != TYPE_STRING:
		return null
	var result := StringName(String(value))
	if result.is_empty() or CharacterId.is_valid(result):
		return result
	return null

func _split_int64(value: int) -> Array[int]:
	var parts: Array[int] = []
	parts.append(value >> 32)
	parts.append(value & UINT32_MAX)
	return parts

func _join_int64(high: int, low: int) -> int:
	return (high << 32) | low

func _has_exact_keys(value: Dictionary, expected: Array) -> bool:
	if value.size() != expected.size():
		return false
	for key: Variant in expected:
		if not value.has(key):
			return false
	return true

func _failure(code: Error, message: String) -> DecodeResult:
	var result := DecodeResult.new()
	result.code = code
	result.message = message
	return result
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** le codec matérialise format, version, clés exactes, limites, types, identifiants et absence de doublons pour tous les objets imbriqués.

- **Résultat structuré :** **Résultat structuré :** `DecodeResult.code` distingue un document vide valide d’un refus ; aucune sentinelle de tableau vide n’est ambiguë.

- **Nombres JSON :** **Nombres JSON :** `_read_int()` accepte un `int` ou un `float` exactement entier dans la plage sûre de 53 bits. Les deux valeurs RNG de 64 bits sont divisées en parties haute et basse de 32 bits pour éviter toute perte de précision.

- **Copies et ordre :** **Copies et ordre :** l’encodage travaille sur des copies détachées ; affrontements, participants et états sont triés, tandis que commandes récentes et événements conservent leur ordre historique.

- **Validation croisée :** **Validation croisée :** l’identifiant d’événement doit être reconstructible depuis l’affrontement et la séquence ; la plus grande séquence conservée ne peut pas dépasser le compteur autoritaire.

- **Refus conservateur :** **Refus conservateur :** une clé inconnue, un nombre fractionnaire, une borne dépassée, une référence mal typée ou un doublon invalide tout le candidat avant application.

## 38. Section de sauvegarde

> **[VSC] Visual Studio Code — Créer : `res://src/features/combat/infrastructure/combat_save_section.gd`.**

```gdscript
class_name CombatSaveSection
extends SaveSection

var _repository: CombatRepository
var _codec := CombatSnapshotCodec.new()
var _rules: CombatRules
var _prepared: Array[CombatEncounterState] = []
var _is_prepared := false

func section_id() -> StringName:
	return &"combat"

func capture() -> Dictionary:
	if _repository == null or _rules == null:
		return {}
	if _rules.validate() != OK:
		return {}
	var encounters: Array[CombatEncounterState] = []
	for encounter_id: StringName in _repository.all_encounter_ids_sorted():
		var encounter := _repository.get_encounter(encounter_id)
		if encounter == null:
			return {}
		encounters.append(encounter.duplicate_detached())
	return _codec.encode(encounters, _rules)

func prepare_restore(payload: Dictionary) -> Error:
	_prepared.clear()
	_is_prepared = false
	if _repository == null or _rules == null:
		return ERR_UNCONFIGURED
	var decoded := _codec.decode(payload, _rules)
	if not decoded.is_success():
		return decoded.code
	for encounter: CombatEncounterState in decoded.encounters:
		_prepared.append(encounter.duplicate_detached())
	_is_prepared = true
	return OK

func apply_prepared() -> Error:
	if not _is_prepared:
		return ERR_UNCONFIGURED
	var candidates: Array[CombatEncounterState] = []
	for encounter: CombatEncounterState in _prepared:
		candidates.append(encounter.duplicate_detached())
	var code := _repository.replace_all(candidates)
	if code != OK:
		return code
	_prepared.clear()
	_is_prepared = false
	return OK

func cancel_restore() -> void:
	_prepared.clear()
	_is_prepared = false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** la section capture des copies dans un ordre stable, prépare un ensemble complet puis l’applique seulement sur demande du coordinateur.

- **Cas vide :** **Cas vide :** `DecodeResult` permet d’accepter explicitement zéro affrontement sans confondre ce cas avec une erreur de format.

- **Copies :** **Copies :** capture, préparation et application ne partagent aucun `CombatEncounterState`, `CombatantState`, `ActiveStatus` ou `CombatEvent` mutable avec l’appelant.

- **Effets de bord :** **Effets de bord :** `prepare_restore()` ne touche pas au dépôt actif ; `apply_prepared()` ne vide la préparation qu’après `replace_all()` réussi.

- **Annulation :** **Annulation :** le coordinateur peut libérer le candidat sans mutation lorsque toute autre section échoue.

## 39. Présentation et événements moteur

La présentation écoute les événements de combat et déclenche animation, audio, VFX, caméra et interface.

> **[VSC] Visual Studio Code — Créer : `res://src/features/combat/presentation/combat_presentation_bridge.gd`.**

```gdscript
class_name CombatPresentationBridge
extends Node

var _actor_registry: ActiveCharacterRegistry

func on_combat_event(event: CombatEvent) -> void:
	if event == null or event.validate() != OK:
		return
	match event.kind:
		CombatEvent.Kind.ATTACK_MISSED:
			_play_animation(event.source_character_id, &"attack")
		CombatEvent.Kind.DAMAGE_APPLIED:
			_play_animation(event.source_character_id, &"attack")
			_play_animation(event.target_character_id, &"hit")
		CombatEvent.Kind.PARTICIPANT_DEFEATED:
			_play_animation(event.target_character_id, &"defeated")
		_:
			pass

func _play_animation(
	character_id: StringName,
	animation_id: StringName,
) -> void:
	var actor := _actor_registry.find_active(character_id)
	if actor == null:
		return
	actor.request_animation(animation_id)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Rôle :** le pont transforme des événements déjà validés en demandes de présentation.

- **Absence d’acteur :** **Absence d’acteur :** un personnage hors écran ne produit pas d’erreur ; l’événement autoritaire reste valable.

- **Frontières d’autorité :** **Frontière :** l’animation n’appelle jamais `CharacterRules` et ne décide pas si le coup touche.

- **Limites et réserves :** **Limite :** `request_animation()` représente un port de présentation défini par la scène de personnage ; les noms concrets d’animations restent des données de contenu.

## 40. Scène pédagogique

La scène de démonstration contient :

- deux personnages du chapitre 14 ;
- un nœud `CombatScheduler` ;
- un adaptateur de ligne de vue actif ;
- une interface minimale pour choisir attaque, garde, attente ou désengagement ;
- un panneau de résultats et d’événements ;
- aucun service IA obligatoire.

La démonstration doit permettre de constater :

1. qu’une cible hors portée est refusée sans changement de santé ;
2. qu’un obstacle bloque la ligne de vue ;
3. qu’un raté consomme le délai d’action ;
4. que la garde absorbe avant la santé ;
5. qu’une commande dupliquée ne produit pas un second effet ;
6. qu’un participant hors écran peut être résolu avec un adaptateur logique.

## 41. Modes Solo et Studio

### 41.1 Mode Solo

- dépôt en mémoire ;
- règles uniques dans `default_combat_rules.tres` ;
- ordonnanceur local ;
- historique borné ;
- une seule unité de travail applicative.

### 41.2 Mode Studio

- plusieurs profils de règles versionnés ;
- tests de propriété sur les formules ;
- catalogues de dégâts et d’états validés par pipeline ;
- télémétrie de file, refus et temps de résolution ;
- migrations de sauvegarde explicitement revues ;
- séparation stricte entre équilibrage, contenu, moteur et présentation.

Le mode Studio n’ajoute pas un bus universel ni un service global. Il renforce les contrats, la génération contrôlée et les validations.

## 42. Diagnostics

Journaliser au minimum :

- `encounter_id`, `command_id`, source et cible ;
- révisions attendues et observées ;
- statut de validation de cible ;
- chance et jet de toucher ;
- montant brut, défense, résistance, garde et santé ;
- nouveau `next_ready_tick` ;
- profondeur de file ;
- code du commit.

Ne pas journaliser :

- un objet complet de sauvegarde ;
- des références de nœuds ;
- des données personnelles ou secrets ;
- un texte génératif non filtré ;
- des centaines d’événements sans rotation.

## 43. Budgets et performance

Les bornes de référence sont :

| Élément | Borne |
|---|---:|
| participants par affrontement | 64 |
| commandes en attente | 256 |
| commandes traitées par tick physique | 16 |
| états par participant | 16 |
| événements d’historique | 512 |
| identifiants traités conservés | 512 |

Ces valeurs sont des limites pédagogiques, pas des mesures garanties. Le chapitre 27 devra les tester sur la configuration AMD de référence.

L’horloge monotone peut mesurer la durée d’une résolution. Elle ne doit pas décider qu’une commande placée plus tôt perd son tour parce qu’un processeur a été plus lent.

## 44. Sécurité et données externes

Une commande provenant d’un fichier, d’un mod ou d’un service local doit être :

- limitée en taille avant parsing ;
- décodée vers des types explicites ;
- vérifiée contre un catalogue d’actions autorisées ;
- privée de chemins, classes ou méthodes dynamiques ;
- refusée si son identifiant, sa cible ou sa révision est invalide.

Une suggestion générative peut proposer « attaquer cette cible ». Elle ne fournit jamais :

- le jet de toucher ;
- le nombre de dégâts ;
- le nouvel état de santé ;
- un identifiant d’exécuteur arbitraire ;
- une méthode à appeler.

## 45. Erreurs fréquentes et corrections

<!-- qa:error-correction-section -->

### 45.1 Laisser l’agent écrire les dégâts

**Symptôme ou risque :** une sortie de planification devient autorité et contourne portée, défense, garde et révisions.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
target.current_health -= agent_result.damage
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** `agent_result` n’est pas une source autoritaire et le bornage de `CharacterRules` est contourné.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var command := map_agent_request_to_combat_command(request)
var result := combat_service.execute(command)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** l’agent ne fournit qu’une commande ; le service relit le monde et calcule lui-même l’impact.

### 45.2 Dupliquer la santé dans `CombatantState`

**Symptôme ou risque :** la santé du personnage et celle du combat divergent après chargement ou soin.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
combatant.current_health -= damage
character.current_health -= damage
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** deux autorités doivent rester synchronisées et peuvent être modifiées partiellement.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
CharacterRules.apply_health_delta(
	character_candidate,
	definition,
	-damage,
)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** une seule valeur autoritaire est modifiée par les règles du personnage.

### 45.3 Utiliser l’heure système pour l’initiative

**Symptôme ou risque :** pause, changement d’horloge ou différence de machine réordonne les participants.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
participant.ready_at = Time.get_unix_time_from_system() + cooldown
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** une heure civile n’est pas une étape de simulation et n’est pas restaurée comme chronologie métier.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
participant.next_ready_tick = logical_tick + recovery_ticks
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la disponibilité dépend uniquement de ticks logiques sauvegardables.

### 45.4 Comparer une distance après une racine inutile

**Symptôme ou risque :** des milliers de vérifications effectuent un calcul plus coûteux sans bénéfice.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
if source.distance_to(target) <= max_range:
	pass
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** `distance_to()` calcule une racine alors qu’une comparaison de carrés suffit.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
if source.distance_squared_to(target) <= max_range * max_range:
	pass
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** les deux côtés sont comparés dans la même unité carrée sans racine.

### 45.5 Considérer un `Area3D` comme vérité instantanée universelle

**Symptôme ou risque :** une commande est acceptée avant que la détection d’overlap ne soit mise à jour.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
if attack_area.has_overlapping_bodies():
	apply_damage()
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la collection d’overlaps dépend du cycle physique et ne valide ni identité, ni cible choisie, ni révision.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var snapshot := snapshot_builder.build_for_basic_attack(command, encounter)
var status := target_validator.validate_basic_attack(snapshot, range_m)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la zone peut aider à construire le snapshot, mais le service applique toutes les préconditions.

### 45.6 Émettre l’animation avant le commit

**Symptôme ou risque :** l’écran montre un impact alors que la révision a rendu la commande invalide.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
hit_animation.play()
var code := unit_of_work.commit(...)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** un effet visuel observable précède une mutation qui peut encore être refusée.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var code := unit_of_work.commit(...)
if code == OK:
	combat_event_emitted.emit(event)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la présentation reçoit uniquement des faits déjà committés.

### 45.7 Retenter gratuitement une attaque manquée

**Symptôme ou risque :** l’attaquant peut lancer plusieurs jets au même tick jusqu’à obtenir un succès.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
if not hit:
	return ERR_CANT_RESOLVE
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** le raté est traité comme une commande non consommée et peut être rejoué.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
issuer.next_ready_tick = logical_tick + recovery_ticks
record_processed(command.command_id)
return commit_miss()
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** le raté consomme le tirage, le délai et l’identifiant comme toute résolution valide.

### 45.8 Utiliser le RNG global

**Symptôme ou risque :** un son, un effet visuel ou une autre fonctionnalité change les résultats de combat.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
var hit := randi_range(0, 999) < chance
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** le flux pseudo-aléatoire global est partagé avec des appels sans rapport.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var rng := RandomNumberGenerator.new()
rng.seed = encounter.rng_seed
rng.state = encounter.rng_state
var roll := rng.randi_range(0, 999)
encounter.rng_state = rng.state
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** chaque affrontement possède une suite locale restaurable et indépendante.

### 45.9 Oublier l’idempotence

**Symptôme ou risque :** un double clic, un retry réseau futur ou un signal dupliqué inflige deux impacts.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
queue.append(command)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** aucun contrôle ne distingue une nouvelle commande d’une répétition.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
if encounter.processed_command_ids.has(command.command_id):
	return duplicate_result(command)
return command_queue.enqueue(command, maximum)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** les commandes traitées et en attente sont toutes deux protégées contre les doublons.

### 45.10 Modifier l’état actif avant toutes les validations

**Symptôme ou risque :** la garde baisse alors qu’une cible invalide empêche l’application de la santé.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
active_target.guard_points -= absorbed
if target_is_invalid:
	return ERR_INVALID_DATA
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** un refus tardif laisse une mutation partielle dans l’état actif.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var candidate := unit_of_work.prepare_combat_candidate(encounter_id)
candidate_target.guard_points -= absorbed
var code := unit_of_work.commit(...)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** l’état actif n’est remplacé qu’après validation complète.

### 45.11 Persister la ligne de vue

**Symptôme ou risque :** après chargement, un booléen ancien contredit les obstacles et positions actuels.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```json
{
  "target_visible": true
}
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la visibilité est un résultat dérivé d’un instant et d’un monde précis.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```json
{
  "next_ready_tick": 420,
  "guard_points": 15,
  "statuses": []
}
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** seules les données durables de combat sont restaurées ; la ligne de vue sera recalculée.

### 45.12 Confondre zéro dégât et commande invalide

**Symptôme ou risque :** une attaque entièrement absorbée est retentée ou signalée comme panne.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
if damage == 0:
	return ERR_INVALID_DATA
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** défense, résistance ou garde peuvent légitimement réduire l’impact à zéro.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
result.status = CombatResult.Status.NO_EFFECT
result.health_delta = 0
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** l’issue est valide, consommée et distinguée d’une donnée mal formée.

### 45.13 Sauvegarder une file transitoire

**Symptôme ou risque :** une commande est rejouée au chargement alors que son émetteur ou sa cible a changé.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
payload["queued_commands"] = queue.snapshot()
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la commande a été construite depuis des révisions qui ne seront plus nécessairement valides.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
save_barrier.pause_acceptance()
save_barrier.drain_or_cancel_queue()
payload["encounters"] = combat_save_section.capture()
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** le snapshot est pris sur une frontière stable et les demandes seront reconstruites après reprise.

### 45.14 Utiliser un `Timer` comme initiative autoritaire

**Symptôme ou risque :** `time_scale`, pause et fréquence de traitement changent l’ordre métier.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
attack_timer.start(0.5)
await attack_timer.timeout
apply_attack()
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** le délai en secondes et le signal moteur deviennent la source de l’ordre de combat.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
participant.next_ready_tick = logical_tick + recovery_ticks
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la règle autoritaire reste en ticks ; un `Timer` peut seulement piloter une présentation non autoritaire.

## 46. Tests à préparer

### 46.1 Tests unitaires

- validation des identifiants, commandes, côtés et création d’affrontement ;
- bornes de `CombatRules` ;
- ordre total de l’initiative et départage lexical ;
- refus d’une cible du même côté lorsque le tir allié est désactivé ;
- portée par distance carrée ;
- chance minimale et maximale ;
- consommation exacte d’un tirage ;
- pénétration, défense, résistance et garde ;
- vulnérabilité négative ;
- résultat `NO_EFFECT` ;
- règles d’empilement et expiration ;
- historique borné et ordonné ;
- doublon de commande ;
- tick ou révision obsolète ;
- codec complet avec document vide valide, clés inconnues, types incorrects, nombres non entiers et doublons ;
- copies profondes des participants, états temporaires et événements.

### 46.2 Tests d’intégration

- requête d’agent vers commande de combat ;
- entrée joueur vers la même commande ;
- obstacle physique puis refus de ligne de vue ;
- commit coordonné entre personnage et combat ;
- refus de commit sans émission d’événement ;
- mort puis événement `PARTICIPANT_DEFEATED` ;
- sauvegarde à file vide puis restauration ;
- personnage hors scène dans un affrontement logique ;
- désengagement et fermeture d’affrontement.

### 46.3 Simulations

- 1, 10 et 100 affrontements simultanés ;
- 2, 16 et 64 participants ;
- file proche de 256 commandes ;
- 16 états par participant ;
- 512 événements d’historique ;
- deux exécutions depuis le même snapshot et le même état RNG ;
- comparaison actif/hors écran avec les mêmes entrées logiques ;
- mesure des microsecondes sans modification de l’ordre métier.

## 47. Réserves runtime

Cette rédaction est une revue statique. Elle ne prouve pas :

- que tous les scripts passent le parseur Godot 4.7.1 ;
- que les tableaux typés et classes imbriquées se convertissent comme attendu ;
- que l’adaptateur de ligne de vue est appelé au bon moment du tick physique ;
- que l’unité de travail commit réellement deux dépôts sans état partiel ;
- que les animations consomment correctement les événements ;
- que le RNG produit un replay identique entre plateformes ou versions ;
- que les bornes tiennent sur la configuration de référence ;
- que le codec complet, ses conversions JSON et une future migration sont exécutables ;
- que la scène pédagogique est instanciable ;
- que le packaging inclut toutes les `Resource`;
- qu’un multijoueur futur peut réutiliser cette autorité sans adaptation ;
- qu’un PDF intermédiaire a été produit.

## 48. Résumé

Le combat est un système d’autorité, pas une animation et pas une extension du planificateur. Une commande typée est relue contre un snapshot, les révisions, l’initiative, la cible, la portée et la ligne de vue. Le toucher et les dégâts sont calculés avec des règles bornées, puis des candidats sont committés avant tout événement de présentation.

La santé reste dans le système des personnages. L’initiative, la garde et les états de combat restent dans l’affrontement. Les compétences, objets, économie, politique et narration consomment les contrats sans déplacer leurs propres règles.

## 49. Sources techniques

- [Godot 4.7 — `CharacterBody3D` et `move_and_slide()`](https://docs.godotengine.org/en/4.7/classes/class_characterbody3d.html)
- [Godot 4.7 — `PhysicsDirectSpaceState3D`](https://docs.godotengine.org/en/4.7/classes/class_physicsdirectspacestate3d.html)
- [Godot 4.7 — `PhysicsRayQueryParameters3D`](https://docs.godotengine.org/en/4.7/classes/class_physicsrayqueryparameters3d.html)
- [Godot 4.7 — lancer de rayons](https://docs.godotengine.org/en/4.7/tutorials/physics/ray-casting.html)
- [Godot 4.7 — `Area3D`](https://docs.godotengine.org/en/4.7/classes/class_area3d.html)
- [Godot 4.7 — `ShapeCast3D`](https://docs.godotengine.org/en/4.7/classes/class_shapecast3d.html)
- [Godot 4.7 — `CollisionObject3D`](https://docs.godotengine.org/en/4.7/classes/class_collisionobject3d.html)
- [Godot 4.7 — `RandomNumberGenerator`](https://docs.godotengine.org/en/4.7/classes/class_randomnumbergenerator.html)
- [Godot 4.7 — génération de nombres pseudo-aléatoires](https://docs.godotengine.org/en/4.7/tutorials/math/random_number_generation.html)
- [Godot 4.7 — `Resource`](https://docs.godotengine.org/en/4.7/classes/class_resource.html)
- [Godot 4.7 — `RefCounted`](https://docs.godotengine.org/en/4.7/classes/class_refcounted.html)
- [Godot 4.7 — signaux](https://docs.godotengine.org/en/4.7/getting_started/step_by_step/signals.html)
- [Godot 4.7 — `Timer`](https://docs.godotengine.org/en/4.7/classes/class_timer.html)
- [Godot 4.7 — `Time`](https://docs.godotengine.org/en/4.7/classes/class_time.html)
- [Godot 4.7 — `Engine`](https://docs.godotengine.org/en/4.7/classes/class_engine.html)
- [Godot 4.7 — `JSON`](https://docs.godotengine.org/en/4.7/classes/class_json.html)
- [Godot 4.7 — `Dictionary`](https://docs.godotengine.org/en/4.7/classes/class_dictionary.html)
- [Godot 4.7 — `Array`](https://docs.godotengine.org/en/4.7/classes/class_array.html)
- [Godot 4.7 — `StringName`](https://docs.godotengine.org/en/4.7/classes/class_stringname.html)
- [Godot 4.7 — `Variant`](https://docs.godotengine.org/en/4.7/classes/class_variant.html)
- [Chapitre 9 — Sauvegardes, chargements et compatibilité](CHAPITRE-09-Sauvegardes-chargements-et-compatibilite-des-versions.md)
- [Chapitre 14 — Personnages](CHAPITRE-14-Personnages.md)
- [Chapitre 17 — Agents IA et comportements autonomes](CHAPITRE-17-Agents-IA-et-comportements-autonomes.md)

## 50. Synthèse opérationnelle pour Project Asteria

Le système de combat de `Project Asteria` repose sur les décisions suivantes :

1. toute source produit une `CombatCommand` et aucune ne fournit directement les dégâts ;
2. `CombatService` constitue l’entrée autoritaire unique ;
3. la santé et l’endurance restent dans `CharacterRuntimeState` ;
4. côtés, initiative, garde, états et révision restent dans `CombatEncounterState` ;
5. les commandes sont corrélées, ordonnées, bornées et idempotentes ;
6. les snapshots figent les lectures et les révisions sont recontrôlées avant commit ;
7. portée logique et ligne de vue sont deux validations distinctes ;
8. la physique active est isolée derrière `LineOfSightPort` ;
9. toucher, défense, résistance et garde utilisent une arithmétique entière documentée ;
10. un raté ou un impact nul est une résolution valide qui consomme l’action ;
11. les mutations sont préparées sur des candidats puis committées avant tout événement ;
12. la simulation hors écran réutilise les mêmes règles avec un adaptateur spatial logique ;
13. la file de commandes, les raycasts et la présentation ne sont pas persistés ;
14. le RNG est local à l’affrontement, initialisé par sa graine et sauvegardé sans perte via deux mots de 32 bits ;
15. les compétences, objets, économie, politique et narration restent autorités de leurs propres règles.
