---
title: "Livre IV — Chapitre 1 : Équilibrage et télémétrie locale"
id: "DOC-L4-CH01"
status: "reviewed"
version: "1.0.1"
lang: "fr-FR"
book: "Livre IV"
chapter: 1
last-verified: "2026-07-25T20:33:18+02:00"
audit-status: "complete"
audit-date: "2026-07-25T20:33:18+02:00"
audit-report: "Livre-IV/QA/AUDIT-CHAPITRE-01.md"
audit-level: "static-review"
reference-engine:
  name: "Godot Engine"
  version: "4.7.1-stable"
  edition: "Standard"
  language: "GDScript"
reference-python:
  implementation: "CPython"
  version: "3.14.6"
  fallback-version: "3.13.14"
  qualification-status: "inherited-provisional"
reference-project:
  name: "Project Asteria"
  renderer: "Forward+"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Équilibrage et télémétrie locale

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique nommée, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L4-CH01`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Versions de référence héritées :** Godot `4.7.1-stable`, CPython `3.14.6` avec repli `3.13.14`, GDScript, Forward+

## 1. Rôle du chapitre

Les Livres II et III ont défini des systèmes de jeu, des outils de test, une chaîne d’observabilité et des méthodes de production. Le présent chapitre ne réécrit aucune de ces autorités. Il organise les observations nécessaires pour décider si une règle, une courbe ou un paramètre produit l’expérience voulue.

L’**équilibrage** n’est pas la recherche d’un nombre parfait. C’est une boucle documentée :

1. formuler une question ;
2. identifier les données nécessaires ;
3. produire des observations reproductibles ;
4. comparer une référence et un candidat ;
5. décider, refuser ou demander une nouvelle expérience ;
6. conserver la justification et la possibilité de revenir en arrière.

La **télémétrie locale** désigne ici une collecte exécutée sur la machine de développement, dans un build interne ou dans une session explicitement consentie. Elle reste hors ligne par défaut. Elle n’envoie rien vers un serveur, ne déduit pas l’identité réelle d’une personne et ne devient jamais une autorité de gameplay.

> **[LECTURE] Chaîne de décision d’équilibrage — Ne pas saisir.**

```text
question de conception
    ↓
métriques et scénarios définis avant l’expérience
    ↓
événements committés par les systèmes propriétaires
    ↓
échantillons locaux minimisés
    ↓
agrégats et intervalles de comparaison
    ↓
rapport de décision
    ├── conserver la référence
    ├── adopter le candidat
    ├── demander une nouvelle mesure
    └── abandonner l’hypothèse
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrée :** la question de conception précède le choix des métriques ; on ne collecte pas d’abord pour chercher ensuite une justification.
- **Frontières d’autorité :** les systèmes de combat, économie, écologie ou progression committent leurs propres événements avant toute observation.
- **Transformation :** les échantillons sont agrégés selon une règle versionnée afin de produire des comparaisons interprétables.
- **Sortie :** le rapport conserve une décision humaine, ses preuves et les réserves qui empêchent une conclusion.
- **Invariant :** aucune métrique ne modifie directement un paramètre de gameplay.

## 2. Résultats d’apprentissage

À la fin du chapitre, le lecteur saura :

- distinguer un objectif de conception, une métrique, un indicateur et une décision ;
- écrire un catalogue de métriques avec unités, dimensions, bornes et finalités ;
- séparer événements métier, journaux de diagnostic et échantillons d’équilibrage ;
- produire des compteurs, distributions, ratios et percentiles sans masquer leur dénominateur ;
- comparer une référence et un candidat sur des scénarios identiques ;
- construire des courbes de progression, d’économie, de combat et de difficulté ;
- exécuter des simulations déterministes avec des graines enregistrées ;
- créer un rapport de décision reproductible ;
- minimiser les données locales, définir leur conservation et documenter le consentement ;
- déclarer honnêtement ce qui a été relu, simulé ou réellement exécuté.

## 3. Niveau de preuve et réserves

Le chapitre est accepté au niveau `static-review`. Les classes GDScript, schémas, scripts Python, scénarios et rapports sont des modèles pédagogiques. Aucun projet Godot, collecteur, simulation, corpus de joueurs, benchmark ou campagne d’équilibrage de `Project Asteria` n’est revendiqué comme matérialisé.

> **[LECTURE] État de preuve du chapitre — Ne pas saisir.**

```yaml
evidence_level:
  chapter: static_review
  metric_catalog_materialized: false
  local_recorder_executed: false
  simulation_scenarios_executed: false
  python_analysis_executed: false
  player_data_collected: false
  consent_flow_implemented: false
  balance_decision_approved: false
  runtime_claims: none
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Statut :** `static_review` signifie que les contrats et extraits ont été relus sans devenir une preuve d’exécution.
- **Collecte :** aucune donnée de joueur ou de testeur n’est déclarée recueillie.
- **Simulation :** les scénarios sont préparés, mais leurs résultats ne sont pas inventés.
- **Décision :** aucun changement de paramètre n’est présenté comme approuvé.
- **Limite :** toute valeur mesurée future devra citer une version, un scénario, une graine et un artefact consultable.

## 4. Prérequis et frontières

Le lecteur doit connaître :

- l’architecture feature-first du Livre II, chapitre 4 ;
- les événements typés et les services injectés du chapitre 5 ;
- les données versionnées et identifiants stables du chapitre 7 ;
- les systèmes de personnages, combat, économie et écologie des chapitres 14, 18, 21 et 22 ;
- les simulations déterministes du chapitre 27 ;
- l’observabilité locale du chapitre 28 ;
- l’automatisation Python du chapitre 29.

Le chapitre couvre les métriques d’équilibrage, les scénarios de mesure, les agrégats, les courbes, les comparaisons et les rapports de décision.

Il ne couvre pas :

- la stratégie générale d’assurance qualité du chapitre 2 ;
- les campagnes fonctionnelles et de régression du chapitre 3 ;
- le diagnostic d’anomalies du chapitre 4 ;
- la politique complète de logs, métriques et traces du chapitre 5 ;
- le profilage CPU, GPU ou mémoire des chapitres 6 à 8 ;
- l’autorité des systèmes de gameplay du Livre II ;
- la collecte distante, l’analytique marketing ou le profilage publicitaire ;
- une analyse juridique personnalisée.

> **Frontière essentielle :** l’observabilité du Livre II fournit un port et des événements structurés. Le présent chapitre sélectionne un sous-ensemble minimisé pour répondre à des questions d’équilibrage. Il ne remplace ni les événements métier, ni les journaux de diagnostic, ni les tests.

## 5. Vocabulaire opérationnel

Un **objectif de conception** décrit un effet recherché, par exemple : « un combat d’introduction doit laisser le temps de comprendre la garde ».

Une **métrique** définit précisément une grandeur : identité, unité, source, agrégation, dimensions autorisées et finalité.

Un **échantillon** est une observation unique associée à un scénario et à une version.

Un **indicateur** est une valeur interprétée à partir d’une ou plusieurs métriques, par exemple le taux de victoire sur un scénario donné.

Une **dimension** découpe une métrique selon une catégorie autorisée : difficulté, archétype d’ennemi ou version de règle.

Une **distribution** conserve plusieurs valeurs afin d’étudier leur dispersion. Une moyenne seule ne montre pas les cas extrêmes.

Une **référence** est la configuration actuellement retenue. Un **candidat** est une modification comparée à cette référence.

Une **baseline** est un ensemble de résultats approuvés pour une version et un protocole précis. Elle ne représente pas une vérité universelle.

Un **percentile** est une valeur sous laquelle se trouve une proportion donnée des observations. Le percentile 90 indique qu’environ 90 % des valeurs sont inférieures ou égales à ce seuil selon la méthode retenue.

La **cardinalité** est le nombre de combinaisons possibles des dimensions. Une cardinalité non bornée rend les agrégats coûteux, peu comparables et susceptibles de contenir des identifiants personnels.

## 6. Pilote d’équilibrage de Project Asteria

Le pilote du chapitre est `AST-BALANCE-PILOT-RELAY-EXPEDITION-001`. Il observe une courte expédition vers le relais abandonné déjà utilisé dans le Livre III.

Le pilote pose trois questions indépendantes :

1. le combat d’introduction laisse-t-il au personnage débutant assez de temps pour comprendre la garde ;
2. la récompense économique couvre-t-elle raisonnablement les consommables engagés sans créer de monnaie ;
3. la rareté écologique observée influence-t-elle le contexte économique sans permettre à l’équilibrage d’écrire un prix ou une population.

> **[LECTURE] Contrat du pilote — Ne pas saisir.**

```yaml
asteria_balance_pilot:
  id: AST-BALANCE-PILOT-RELAY-EXPEDITION-001
  revision: 0.1.0-draft
  questions:
    - AST-BAL-Q-COMBAT-GUARD-001
    - AST-BAL-Q-ECONOMY-COST-001
    - AST-BAL-Q-ECOLOGY-SIGNAL-001
  reference_profile: AST-BAL-PROFILE-RELAY-REF-001
  candidate_profiles:
    - AST-BAL-PROFILE-RELAY-CANDIDATE-A-001
  scenario_set: AST-BAL-SCENARIOS-RELAY-001
  player_data_required: false
  materialization_status: not_started
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** le pilote, ses questions, ses profils et son jeu de scénarios possèdent des identifiants distincts.
- **Comparaison :** le candidat A sera évalué contre une référence explicite, pas contre un souvenir de session.
- **Données :** les premières expériences utilisent des simulations et des sessions internes sans donnée personnelle.
- **Frontières :** combat, économie et écologie restent propriétaires de leurs états et résultats.
- **Réserve :** `not_started` interdit de présenter les valeurs d’exemple comme des mesures réelles.

## 7. Formuler une question mesurable

Une question utile relie une population, un contexte, un résultat et une décision possible. « Le combat est-il amusant ? » est trop large pour déterminer une métrique unique.

Une formulation exploitable serait :

> Pour le scénario d’introduction `AST-SCENARIO-COMBAT-GUARD-001`, avec le profil de personnage débutant et la graine enregistrée, quelle proportion de simulations atteint au moins deux occasions de garde avant la fin du combat, et comment cette proportion change-t-elle entre la référence et le candidat A ?

La question nomme le scénario, la population simulée, l’observation et la comparaison. Elle ne décide pas à l’avance qu’une proportion élevée est meilleure : le seuil d’acceptation appartient au protocole de décision.

> **[LECTURE] Fiche de question — Ne pas saisir.**

```yaml
balance_question:
  id: AST-BAL-Q-COMBAT-GUARD-001
  statement: "Le scénario d’introduction offre-t-il au moins deux occasions de garde ?"
  population: simulated_beginner_profile
  scenario_id: AST-SCENARIO-COMBAT-GUARD-001
  primary_metric: combat.guard_opportunity.count
  secondary_metrics:
    - combat.duration.logical_ticks
    - combat.outcome
  comparison: reference_vs_candidate_a
  decision_thresholds:
    source: design_review
    status: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Population :** `simulated_beginner_profile` évite de faire passer une simulation pour un échantillon de joueurs réels.
- **Métrique principale :** le nombre d’occasions de garde répond directement à la question.
- **Métriques secondaires :** la durée et l’issue aident à détecter un gain obtenu au prix d’un combat interminable.
- **Seuil :** son statut `pending` empêche de fabriquer une réussite après avoir vu les résultats.
- **Résultat attendu :** la revue peut refuser la question si elle ne conduit à aucune décision possible.

## 8. Architecture retenue

La fonctionnalité d’équilibrage consomme des événements et résultats déjà committés. Elle produit des artefacts d’analyse hors du runtime autoritaire.

> **[LECTURE] Arborescence cible — Ne pas créer depuis un terminal.**

```text
res://src/features/balancing/
├── domain/
│   ├── balance_metric_kind.gd
│   ├── balance_metric_definition.gd
│   ├── balance_sample.gd
│   ├── balance_run_manifest.gd
│   ├── balance_aggregate.gd
│   └── balance_decision.gd
├── application/
│   ├── balance_metric_catalog.gd
│   ├── balance_event_mapper.gd
│   ├── balance_sample_sink.gd
│   ├── balance_aggregator.gd
│   ├── balance_simulation_runner.gd
│   └── balance_report_builder.gd
└── infrastructure/
    ├── jsonl_balance_sample_sink.gd
    └── balance_manifest_codec.gd

config/balancing/
├── metric-catalog.v1.json
├── retention-policy.v1.json
└── pilots/
    └── relay-expedition.v1.yaml

automation/src/asteria_tools/balancing/
├── aggregate.py
├── compare.py
└── report.py

user://balance-lab/
├── runs/
├── reports/
└── quarantine/
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Domaine :** les définitions, échantillons, agrégats et décisions sont indépendants des scènes Godot.
- **Application :** les mappeurs traduisent des événements autorisés en échantillons minimisés ; ils ne recalculent pas l’issue métier.
- **Infrastructure :** l’écriture locale est remplaçable et reste sous `user://balance-lab`.
- **Python :** l’analyse hors ligne réutilise l’environnement du Livre II, chapitre 29.
- **Séparation :** les rapports publiables ne sont pas confondus avec les runs bruts ou la quarantaine.

## 9. Chaîne d’autorité

> **[LECTURE] Flux d’un échantillon d’équilibrage — Ne pas saisir.**

```text
CombatService / EconomyService / EcologyService
    ↓ événement ou résultat après commit
TelemetryPort et événements typés du Livre II
    ↓ filtre d’équilibrage versionné
BalanceEventMapper
    ├── vérifie l’événement autorisé
    ├── sélectionne les champs minimaux
    ├── ajoute scénario, profil et version
    └── construit BalanceSample
            ↓
BalanceSampleSink local
            ↓
agrégation et rapport hors autorité métier
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Source :** l’échantillon dérive d’un résultat déjà accepté par le système propriétaire.
- **Filtre :** le catalogue ferme les événements et attributs utilisables.
- **Contexte :** scénario, profil et version rendent l’observation comparable.
- **Effet de bord :** seul le sink local écrit un fichier ; le mappeur reste une transformation contrôlée.
- **Interdiction :** le flux ne retourne aucune commande de mutation vers le gameplay.

## 10. Classer les métriques

Le chapitre utilise quatre familles principales.

| Famille | Exemple | Agrégation |
|---|---|---|
| compteur | nombre d’occasions de garde | somme ou distribution par run |
| jauge | réserve écologique à un tick donné | dernière valeur ou série ordonnée |
| distribution | durée d’un combat | médiane, percentiles, dispersion |
| ratio | victoires / combats terminés | numérateur et dénominateur conservés |

Un ratio n’est jamais stocké seul. Conserver `8 / 10` distingue un taux de 80 % fondé sur dix cas d’un taux identique fondé sur dix mille cas.

> **[VSC] Visual Studio Code — Créer `res://src/features/balancing/domain/balance_metric_kind.gd`.**

```gdscript
class_name BalanceMetricKind
extends RefCounted

enum Value {
	COUNTER,
	GAUGE,
	DISTRIBUTION,
	RATIO_NUMERATOR,
	RATIO_DENOMINATOR,
}

static func is_valid(value: int) -> bool:
	return value >= Value.COUNTER and value <= Value.RATIO_DENOMINATOR
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Énumération :** chaque valeur représente une méthode d’agrégation, pas une unité.
- **Paramètre :** `value` est un entier car les valeurs d’énumération GDScript sont numériques.
- **Retour :** `is_valid()` renvoie `true` uniquement pour l’intervalle fermé de l’énumération.
- **Opérateurs :** `>=`, `<=` et `and` vérifient les deux bornes.
- **Limite :** numérateur et dénominateur restent séparés jusqu’au calcul du ratio.

## 11. Définir une métrique comme contrat

Une métrique possède une identité stable, un type, une unité, une source autorisée, une politique d’agrégation, des dimensions et une finalité.

> **[VSC] Visual Studio Code — Créer `res://src/features/balancing/domain/balance_metric_definition.gd`.**

```gdscript
class_name BalanceMetricDefinition
extends RefCounted

var metric_id: StringName
var kind: BalanceMetricKind.Value
var unit_id: StringName
var source_event_id: StringName
var allowed_dimensions: PackedStringArray
var minimum_value: float
var maximum_value: float
var purpose: String

func _init(
	p_metric_id: StringName,
	p_kind: BalanceMetricKind.Value,
	p_unit_id: StringName,
	p_source_event_id: StringName,
	p_allowed_dimensions: PackedStringArray,
	p_minimum_value: float,
	p_maximum_value: float,
	p_purpose: String,
) -> void:
	metric_id = p_metric_id
	kind = p_kind
	unit_id = p_unit_id
	source_event_id = p_source_event_id
	allowed_dimensions = p_allowed_dimensions.duplicate()
	minimum_value = p_minimum_value
	maximum_value = p_maximum_value
	purpose = p_purpose

func is_valid() -> bool:
	return (
		not metric_id.is_empty()
		and BalanceMetricKind.is_valid(kind)
		and not unit_id.is_empty()
		and not source_event_id.is_empty()
		and minimum_value <= maximum_value
		and not purpose.strip_edges().is_empty()
	)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètres :** le préfixe `p_` distingue les arguments des propriétés d’instance.
- **Types :** `StringName` convient aux identifiants stables ; `PackedStringArray` borne une liste de dimensions textuelles.
- **Copie :** `duplicate()` évite que l’appelant modifie ensuite la liste conservée.
- **Bornes :** les valeurs minimales et maximales servent à refuser des échantillons impossibles ou corrompus.
- **Retour :** `is_valid()` combine les gardes et ne modifie aucun état.

## 12. Cataloguer les métriques

Le catalogue est une source versionnée. Ajouter une métrique exige une finalité, une source et une politique de conservation. Une chaîne observée dans un journal ne devient pas automatiquement une métrique.

> **[VSC] Visual Studio Code — Créer `config/balancing/metric-catalog.v1.json`.**

```json
{
  "schema_version": 1,
  "catalog_id": "AST-BAL-METRICS-001",
  "metrics": {
    "combat.guard_opportunity.count": {
      "kind": "COUNTER",
      "unit": "count",
      "source_event": "combat.turn.opportunity_committed",
      "allowed_dimensions": [
        "scenario_id",
        "balance_profile_id",
        "difficulty_id"
      ],
      "minimum": 0,
      "maximum": 100,
      "purpose": "Comparer le temps laissé à l’apprentissage de la garde."
    },
    "combat.duration.logical_ticks": {
      "kind": "DISTRIBUTION",
      "unit": "logical_tick",
      "source_event": "combat.encounter.ended",
      "allowed_dimensions": [
        "scenario_id",
        "balance_profile_id",
        "outcome"
      ],
      "minimum": 1,
      "maximum": 100000,
      "purpose": "Détecter les combats trop courts ou excessivement longs."
    }
  }
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Schéma :** `schema_version` permet une migration explicite du format.
- **Clés :** les identifiants sont stables et indépendants des textes affichés au joueur.
- **Dimensions :** seules trois dimensions fermées sont admises par métrique.
- **Bornes :** elles ne sont pas des objectifs de design ; elles détectent des valeurs incompatibles avec le contrat.
- **Finalité :** `purpose` documente pourquoi la collecte existe et aide à appliquer la minimisation.

## 13. Nommer les unités sans ambiguïté

Une valeur n’est interprétable qu’avec son unité. `duration = 120` peut signifier des millisecondes, des images, des ticks logiques ou des secondes.

Le catalogue utilise des identifiants d’unité fermés :

- `count` pour un dénombrement ;
- `logical_tick` pour l’horloge logique ;
- `minor_currency_unit` pour une monnaie autoritaire ;
- `basis_point` pour un taux entier sur 10 000 ;
- `ratio_part` pour un numérateur ou dénominateur ;
- `resource_unit` pour une quantité écologique définie par son système propriétaire.

Les montants économiques restent des entiers en unités mineures. Une analyse peut afficher une valeur lisible, mais elle conserve l’entier original et l’identité de devise.

> **[LECTURE] Exemple d’unité économique — Ne pas saisir.**

```yaml
economic_sample:
  metric_id: economy.consumable_cost.minor_units
  value: 1250
  unit_id: minor_currency_unit
  currency_id: economy.currency.aster_mark
  rendered_for_report: "12,50 unités majeures"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Valeur :** `1250` reste l’entier autoritaire fourni par l’économie.
- **Unité :** `minor_currency_unit` empêche de traiter la valeur comme un flottant générique.
- **Dimension :** `currency_id` distingue les devises sans conversion implicite.
- **Présentation :** le texte lisible est dérivé pour le rapport et ne remplace pas la valeur source.
- **Invariant :** l’équilibrage n’écrit ni portefeuille, ni prix, ni taux de change.

## 14. Borner les dimensions et la cardinalité

Les dimensions servent à comparer des groupes connus. Elles ne doivent pas contenir :

- un nom de joueur ;
- un identifiant de compte ;
- un chemin de sauvegarde ;
- un texte libre ;
- une position exacte à chaque image ;
- un identifiant d’instance non borné ;
- un prompt ou une réponse IA brute.

Une dimension telle que `difficulty_id` possède quelques valeurs stables. Une dimension `character_instance_id` pourrait produire une série par personnage et devenir un identifiant indirect.

> **[LECTURE] Budget de cardinalité — Ne pas saisir.**

```yaml
dimension_policy:
  scenario_id:
    maximum_distinct_values: 64
    source: versioned_catalog
  balance_profile_id:
    maximum_distinct_values: 16
    source: versioned_catalog
  difficulty_id:
    maximum_distinct_values: 8
    source: versioned_catalog
  free_text:
    allowed: false
  runtime_instance_id:
    allowed: false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Borne :** chaque dimension autorisée possède un maximum contrôlable.
- **Source :** les valeurs proviennent d’un catalogue, pas d’une saisie libre.
- **Confidentialité :** l’absence d’identifiant d’instance réduit les risques de réidentification.
- **Coût :** une cardinalité bornée limite le nombre de séries et la taille des agrégats.
- **Refus :** une valeur inconnue bloque l’échantillon ou rejoint une quarantaine, elle ne crée pas une nouvelle dimension silencieuse.

## 15. Représenter un échantillon

Un échantillon ne copie pas l’événement complet. Il conserve uniquement les champs nécessaires à la métrique et au protocole.

> **[VSC] Visual Studio Code — Créer `res://src/features/balancing/domain/balance_sample.gd`.**

```gdscript
class_name BalanceSample
extends RefCounted

var metric_id: StringName
var run_id: StringName
var logical_tick: int
var value: float
var dimensions: Dictionary

func _init(
	p_metric_id: StringName,
	p_run_id: StringName,
	p_logical_tick: int,
	p_value: float,
	p_dimensions: Dictionary,
) -> void:
	metric_id = p_metric_id
	run_id = p_run_id
	logical_tick = p_logical_tick
	value = p_value
	dimensions = p_dimensions.duplicate(true)

func detached_copy() -> BalanceSample:
	return BalanceSample.new(
		metric_id,
		run_id,
		logical_tick,
		value,
		dimensions,
	)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identités :** `metric_id` choisit le contrat ; `run_id` relie l’observation à une expérience.
- **Temps :** `logical_tick` provient du monde ou du scénario et non de l’horloge système.
- **Valeur :** `float` permet les distributions dérivées, mais les montants monétaires restent convertis sans perte depuis leurs entiers et conservent leur unité.
- **Copie profonde :** `duplicate(true)` détache les dimensions imbriquées de l’appelant.
- **Retour :** `detached_copy()` produit un nouvel objet sans modifier l’échantillon courant.

## 16. Valider un échantillon contre le catalogue

La validation contrôle l’identité, les bornes, les dimensions et les valeurs non finies. Une valeur `NaN` peut contaminer toutes les moyennes si elle n’est pas refusée.

> **[VSC] Visual Studio Code — Créer `res://src/features/balancing/application/balance_metric_catalog.gd`.**

```gdscript
class_name BalanceMetricCatalog
extends RefCounted

var _definitions: Dictionary = {}

func add(definition: BalanceMetricDefinition) -> bool:
	if definition == null or not definition.is_valid():
		return false
	if _definitions.has(definition.metric_id):
		return false
	_definitions[definition.metric_id] = definition
	return true

func validate_sample(sample: BalanceSample) -> StringName:
	if sample == null:
		return &"BALANCE_SAMPLE_NULL"
	var definition: BalanceMetricDefinition = _definitions.get(sample.metric_id)
	if definition == null:
		return &"BALANCE_METRIC_UNKNOWN"
	if is_nan(sample.value) or is_inf(sample.value):
		return &"BALANCE_VALUE_NOT_FINITE"
	if sample.value < definition.minimum_value:
		return &"BALANCE_VALUE_BELOW_MINIMUM"
	if sample.value > definition.maximum_value:
		return &"BALANCE_VALUE_ABOVE_MAXIMUM"
	for key in sample.dimensions:
		if String(key) not in definition.allowed_dimensions:
			return &"BALANCE_DIMENSION_FORBIDDEN"
	return &"OK"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Ajout :** `add()` refuse les définitions invalides et les identités dupliquées.
- **Recherche :** `Dictionary.get()` renvoie `null` lorsqu’aucune définition ne correspond.
- **Nombres :** `is_nan()` et `is_inf()` écartent les valeurs non finies.
- **Boucle :** chaque clé de dimension doit apparaître dans la liste fermée de la définition.
- **Retour :** un `StringName` stable permet au sink et au rapport de distinguer les refus sans lever une exception pour un cas prévu.

## 17. Mapper un événement sans le recopier

Le mappeur connaît les événements autorisés. Il ne sérialise jamais l’objet métier entier.

> **[VSC] Visual Studio Code — Créer `res://src/features/balancing/application/balance_event_mapper.gd`.**

```gdscript
class_name BalanceEventMapper
extends RefCounted

func from_combat_ended(
	event: CombatEvent,
	run_id: StringName,
	scenario_id: StringName,
	balance_profile_id: StringName,
) -> BalanceSample:
	if event == null or event.kind != CombatEvent.Kind.ENCOUNTER_ENDED:
		return null
	return BalanceSample.new(
		&"combat.duration.logical_ticks",
		run_id,
		event.logical_tick,
		float(event.duration_ticks),
		{
			"scenario_id": String(scenario_id),
			"balance_profile_id": String(balance_profile_id),
			"outcome": CombatResult.outcome_name(event.outcome),
		},
	)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Précondition :** seul un événement de fin de combat est accepté.
- **Paramètres :** le run, le scénario et le profil sont fournis par l’expérience, pas déduits de la scène.
- **Conversion :** `float(event.duration_ticks)` adapte un entier à la représentation générique de l’échantillon tout en conservant l’unité `logical_tick` dans le catalogue.
- **Dimensions :** le dictionnaire contient trois catégories bornées et aucun identifiant personnel.
- **Retour :** `null` représente un événement hors contrat ; l’appelant doit l’ignorer ou le diagnostiquer sans créer d’échantillon vide.

## 18. Décrire un run avant sa première mesure

Le manifeste fige la version du jeu, le profil d’équilibrage, les scénarios, les graines et le catalogue.

> **[VSC] Visual Studio Code — Créer `config/balancing/pilots/relay-expedition.v1.yaml`.**

```yaml
balance_run_plan:
  schema_version: 1
  pilot_id: AST-BALANCE-PILOT-RELAY-EXPEDITION-001
  run_id: AST-BAL-RUN-RELAY-0001
  source_revision: "<git-commit>"
  build_id: "<build-id>"
  metric_catalog_id: AST-BAL-METRICS-001
  reference_profile: AST-BAL-PROFILE-RELAY-REF-001
  candidate_profiles:
    - AST-BAL-PROFILE-RELAY-CANDIDATE-A-001
  scenarios:
    - id: AST-SCENARIO-COMBAT-GUARD-001
      seeds: [104729, 130363, 155921, 196613]
  collection_mode: internal_simulation
  network_export: false
  consent_required: false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Révisions :** `source_revision` et `build_id` relient les résultats au code et au build exacts.
- **Catalogue :** l’identité du catalogue empêche de comparer deux runs dont les métriques ont changé silencieusement.
- **Graines :** la liste est écrite avant l’exécution et reste identique entre référence et candidat.
- **Mode :** `internal_simulation` explique pourquoi aucun consentement de testeur n’est requis.
- **Réseau :** `false` confirme l’absence d’envoi distant dans ce protocole.

## 19. Séparer les modes de collecte

Le projet distingue quatre modes :

| Mode | Source | Données personnelles prévues | Usage |
|---|---|---:|---|
| simulation interne | scénarios déterministes | non | comparer des règles |
| session développeur | équipe locale | normalement non | vérifier l’instrumentation |
| playtest consenti | testeur informé | possible, minimisées | observer une tâche réelle |
| production distante | joueurs publiés | hors périmètre du chapitre | exige une gouvernance distincte |

Un build ne doit pas passer silencieusement d’un mode à l’autre. Le mode de collecte est visible, versionné et désactivable.

> **[LECTURE] Politique de mode — Ne pas saisir.**

```yaml
collection_modes:
  internal_simulation:
    enabled_by_default: true
    network_export: false
    personal_data: prohibited
  developer_session:
    enabled_by_default: false
    network_export: false
    personal_data: prohibited
  consented_playtest:
    enabled_by_default: false
    network_export: false
    personal_data: minimized
    consent_record_required: true
  production_remote:
    enabled: false
    status: out_of_scope
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Défaut :** seule la simulation interne est active par défaut.
- **Session développeur :** l’activation explicite évite de remplir le disque pendant une partie ordinaire.
- **Playtest :** le consentement et la minimisation sont deux exigences séparées.
- **Production :** le statut hors périmètre bloque toute extension implicite vers une collecte distante.
- **Résultat attendu :** un rapport peut démontrer quel mode était actif pour chaque run.

## 20. Écrire localement avec une politique de rétention

Le sink local écrit dans un dossier de run identifié. Le chapitre 28 reste l’autorité de l’implémentation générale JSONL et de la rédaction des données sensibles ; le présent chapitre ajoute une racine et une politique propres au laboratoire d’équilibrage.

> **[VSC] Visual Studio Code — Créer `config/balancing/retention-policy.v1.json`.**

```json
{
  "schema_version": 1,
  "policy_id": "AST-BAL-RETENTION-001",
  "roots": [
    "user://balance-lab/runs",
    "user://balance-lab/reports"
  ],
  "raw_run_maximum_count": 20,
  "report_maximum_count": 50,
  "maximum_total_bytes": 536870912,
  "automatic_network_upload": false,
  "delete_oldest_unapproved_raw_runs_first": true,
  "approved_reports_require_manual_deletion": true
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Racines :** seules les zones du laboratoire sont concernées.
- **Bornes :** nombre de runs, rapports et octets évitent une croissance sans limite.
- **Priorité :** les runs bruts non approuvés sont supprimés avant les rapports de décision.
- **Réseau :** l’upload automatique reste interdit.
- **Suppression :** un rapport approuvé exige une action explicite afin de conserver la justification d’une décision.

## 21. Agréger sans perdre le dénominateur

Un agrégat conserve le nombre d’observations, les valeurs triées ou les accumulateurs nécessaires. Pour un ratio, il conserve le numérateur et le dénominateur.

> **[VSC] Visual Studio Code — Créer `res://src/features/balancing/domain/balance_aggregate.gd`.**

```gdscript
class_name BalanceAggregate
extends RefCounted

var metric_id: StringName
var dimensions: Dictionary
var count: int = 0
var total: float = 0.0
var minimum: float = INF
var maximum: float = -INF
var values: PackedFloat64Array = PackedFloat64Array()

func add_value(value: float) -> void:
	count += 1
	total += value
	minimum = minf(minimum, value)
	maximum = maxf(maximum, value)
	values.append(value)

func mean() -> float:
	return total / float(count) if count > 0 else NAN
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Accumulateurs :** `count`, `total`, `minimum` et `maximum` évitent de recalculer les statistiques simples.
- **Sentinelles :** `INF` et `-INF` garantissent que la première valeur devient à la fois minimum et maximum.
- **Distribution :** `PackedFloat64Array` conserve les valeurs nécessaires aux médianes et percentiles du laboratoire.
- **Retour :** `mean()` renvoie `NAN` lorsque l’agrégat est vide ; l’appelant doit traiter ce statut avant publication.
- **Limite :** pour des volumes très élevés, un algorithme de streaming qualifié remplacerait la conservation intégrale.

## 22. Calculer moyenne, médiane et percentiles

La moyenne additionne toutes les valeurs puis divise par leur nombre. Elle est sensible aux valeurs extrêmes.

La médiane sépare une série triée en deux moitiés. Elle décrit mieux un centre lorsque quelques cas sont très longs ou très coûteux.

Un percentile montre la queue de distribution. Pour une durée de combat, la médiane peut être acceptable alors que le percentile 95 révèle quelques combats bloqués.

> **[LECTURE] Exemple de distribution — Ne pas saisir.**

```text
durées en ticks : 40, 42, 43, 45, 47, 49, 52, 54, 58, 240

moyenne              67
médiane               48
maximum              240
lecture              un cas extrême tire fortement la moyenne vers le haut
décision             inspecter le scénario extrême avant de modifier la courbe
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Données :** dix observations sont affichées, ce qui rend le dénominateur visible.
- **Moyenne :** le combat de 240 ticks augmente fortement la valeur centrale arithmétique.
- **Médiane :** elle reste proche des durées ordinaires, mais ne signale pas seule le blocage.
- **Maximum :** il attire l’attention sur le cas à reproduire.
- **Décision :** une distribution ne prescrit pas automatiquement une correction globale.

## 23. Calculer un percentile de manière explicite

Les bibliothèques peuvent utiliser des conventions différentes d’interpolation. Le rapport doit enregistrer la méthode.

> **[VSC] Visual Studio Code — Créer `automation/src/asteria_tools/balancing/aggregate.py`.**

```python
from __future__ import annotations

from math import ceil
from statistics import mean, median


def nearest_rank_percentile(values: list[float], percentile: float) -> float:
    if not values:
        raise ValueError("BALANCE_VALUES_EMPTY")
    if not 0.0 < percentile <= 100.0:
        raise ValueError("BALANCE_PERCENTILE_OUT_OF_RANGE")
    ordered = sorted(values)
    rank = ceil((percentile / 100.0) * len(ordered))
    return ordered[rank - 1]


def summarize(values: list[float]) -> dict[str, float | int]:
    if not values:
        raise ValueError("BALANCE_VALUES_EMPTY")
    return {
        "count": len(values),
        "mean": mean(values),
        "median": median(values),
        "p90_nearest_rank": nearest_rank_percentile(values, 90.0),
        "minimum": min(values),
        "maximum": max(values),
    }
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètres :** `values` contient les observations d’un même groupe ; `percentile` est exprimé entre `0` exclu et `100` inclus.
- **Tri :** `sorted()` produit une nouvelle liste et ne modifie pas l’entrée.
- **Rang :** `ceil()` applique la convention du rang le plus proche ; `rank - 1` convertit le rang humain en indice Python.
- **Retour :** `summarize()` conserve le nombre de cas avec les statistiques.
- **Erreurs :** une liste vide ou un percentile hors intervalle produit un refus stable, jamais une valeur inventée.

## 24. Mesurer la dispersion

Deux candidats peuvent avoir la même moyenne et des comportements très différents. L’écart-type de population décrit la dispersion autour de la moyenne pour l’ensemble observé. Il ne prouve pas que l’échantillon représente tous les joueurs.

Le rapport doit toujours préciser :

- la taille de l’échantillon ;
- la nature simulée ou humaine des observations ;
- les scénarios inclus ;
- les exclusions ;
- la statistique et sa convention ;
- les réserves d’interprétation.

> **[LECTURE] Comparaison de dispersion — Ne pas saisir.**

```yaml
comparison:
  metric_id: combat.duration.logical_ticks
  reference:
    count: 100
    median: 48
    population_standard_deviation: 6.2
  candidate_a:
    count: 100
    median: 48
    population_standard_deviation: 19.7
  interpretation: "Centre identique, variabilité plus forte pour le candidat A."
  decision: REVIEW_REQUIRED
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Taille :** les deux groupes contiennent le même nombre de simulations.
- **Centre :** la médiane identique ne suffit pas à conclure à une équivalence.
- **Dispersion :** l’écart-type plus élevé signale des durées moins stables.
- **Interprétation :** la phrase décrit les données sans attribuer une cause non démontrée.
- **Décision :** `REVIEW_REQUIRED` demande une inspection des scénarios extrêmes.

## 25. Construire une baseline

Une baseline contient une configuration, des scénarios et des résultats approuvés. Elle est immuable : une correction crée une nouvelle version.

> **[LECTURE] Manifeste de baseline — Ne pas saisir.**

```yaml
balance_baseline:
  id: AST-BAL-BASELINE-RELAY-001
  version: 1.0.0
  source_revision: "<git-commit>"
  build_id: "<build-id>"
  metric_catalog_id: AST-BAL-METRICS-001
  scenario_set_id: AST-BAL-SCENARIOS-RELAY-001
  balance_profile_id: AST-BAL-PROFILE-RELAY-REF-001
  result_manifest_sha256: "<sha256>"
  approval:
    status: pending
    reviewer_role: game_design
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Version :** la baseline est identifiée indépendamment du profil de paramètres.
- **Entrées :** code, build, métriques et scénarios sont tous fixés.
- **Intégrité :** l’empreinte relie la baseline à son manifeste de résultats.
- **Approbation :** la baseline n’est pas active tant que la revue reste `pending`.
- **Immutabilité :** une nouvelle campagne n’écrase jamais le manifeste précédent.

## 26. Comparer référence et candidat

Une comparaison valide change une variable ou un ensemble explicitement déclaré. Modifier simultanément dégâts, santé, récompenses et fréquence des ressources empêche d’attribuer l’effet observé.

> **[LECTURE] Profil candidat borné — Ne pas saisir.**

```yaml
balance_candidate:
  id: AST-BAL-PROFILE-RELAY-CANDIDATE-A-001
  based_on: AST-BAL-PROFILE-RELAY-REF-001
  changes:
    combat.guard_window.logical_ticks:
      from: 12
      to: 16
  unchanged_contracts:
    - combat.damage_rules
    - character.health_profile
    - economy.reward_profile
    - ecology.resource_profile
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Héritage :** `based_on` désigne la référence exacte.
- **Modification :** une seule fenêtre logique passe de 12 à 16 ticks.
- **Unités :** le nom du paramètre rappelle qu’il s’agit de ticks logiques.
- **Contrôles :** quatre contrats importants sont explicitement inchangés.
- **Résultat attendu :** une différence de résultat peut être étudiée sans attribuer à tort l’effet à plusieurs changements simultanés.

## 27. Construire une courbe de progression

Une courbe de progression transforme un niveau ou un palier en coût, capacité ou récompense. Avant de choisir une formule, il faut définir :

- la valeur au premier palier ;
- la croissance souhaitée ;
- les plafonds ;
- les ruptures intentionnelles ;
- les unités ;
- les valeurs de contrôle.

Une formule n’est pas meilleure parce qu’elle est complexe. Une table versionnée est souvent plus lisible pour un petit nombre de paliers.

> **[LECTURE] Courbe de coût d’expérience — Ne pas saisir.**

```python
def cumulative_experience_required(level: int) -> int:
    if level < 1 or level > 50:
        raise ValueError("LEVEL_OUT_OF_RANGE")
    base = 100
    linear = 60 * (level - 1)
    quadratic = 15 * (level - 1) * (level - 1)
    return base + linear + quadratic
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètre :** `level` est borné de 1 à 50 afin d’éviter des appels hors design.
- **Termes :** `base` fixe le coût initial, `linear` ajoute une croissance régulière et `quadratic` accélère progressivement.
- **Opérateurs :** `*` multiplie les facteurs ; `(level - 1) * (level - 1)` élève le décalage au carré sans conversion flottante.
- **Retour :** la fonction renvoie un entier cumulatif.
- **Limite :** les coefficients sont des exemples de structure et ne sont pas approuvés pour Project Asteria.

## 28. Inspecter une courbe avec une table

Une table rend visibles les écarts entre paliers et permet de détecter une croissance trop brutale.

> **[PS] PowerShell 7 — Générer une table locale depuis l’environnement Python du projet.**

```powershell
.\.venv\Scripts\python.exe -m asteria_tools.balancing.curve_table `
  --curve experience `
  --from-level 1 `
  --to-level 10 `
  --output work\reports\experience-curve.csv

if ($LASTEXITCODE -ne 0) {
  throw "La génération de la table a échoué."
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Interpréteur :** la commande utilise l’environnement virtuel du projet et non Python global.
- **Arguments :** la courbe, les bornes de niveau et le chemin de sortie sont explicites.
- **Continuation :** l’accent grave PowerShell prolonge la commande sur plusieurs lignes.
- **Code de retour :** `$LASTEXITCODE` doit valoir `0`; sinon le script lève une erreur.
- **Effet de bord :** seul le fichier CSV du répertoire de travail est créé ou remplacé.

## 29. Équilibrer l’économie sans modifier l’autorité économique

L’équilibrage peut comparer :

- coût médian des consommables par expédition ;
- récompense monétaire reçue par scénario ;
- quantité d’objets produits et consommés ;
- fréquence des transactions refusées ;
- dispersion des soldes simulés.

Il ne peut pas :

- écrire directement un portefeuille ;
- faire confiance à un total fourni par l’interface ;
- convertir implicitement deux devises ;
- créer de monnaie pour améliorer une métrique ;
- modifier une `ItemDefinition` partagée.

> **[LECTURE] Tableau d’économie simulée — Ne pas saisir.**

```yaml
economy_balance_summary:
  scenario_id: AST-SCENARIO-RELAY-EXPEDITION-001
  currency_id: economy.currency.aster_mark
  runs: 200
  consumable_cost_minor_units:
    median: 900
    p90_nearest_rank: 1500
  reward_minor_units:
    median: 1200
    p90_nearest_rank: 1200
  net_minor_units:
    median: 300
  authority_mutations_by_analysis: 0
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Devise :** toutes les valeurs utilisent la même identité et les mêmes unités mineures.
- **Runs :** le dénominateur de 200 simulations est visible.
- **Distribution :** coût et récompense conservent médiane et percentile.
- **Net :** la différence est une valeur d’analyse, pas une écriture de portefeuille.
- **Invariant :** `authority_mutations_by_analysis` doit rester à zéro.

## 30. Équilibrer le combat sans recopier sa résolution

Le système de combat possède les dégâts, la garde, l’initiative et les états. Le laboratoire observe ses résultats.

Métriques candidates :

- nombre de tours ou ticks logiques ;
- occasions de garde ;
- dégâts reçus et infligés ;
- fréquence des refus de cible ;
- répartition des issues ;
- consommation de ressources ;
- états appliqués par catégorie.

Une métrique de « dégâts par seconde » doit préciser si la seconde est une durée réelle de présentation ou si le protocole utilise des ticks logiques. Pour comparer des règles déterministes, le pilote préfère les ticks logiques.

> **[LECTURE] Résultat de combat minimisé — Ne pas saisir.**

```yaml
combat_balance_record:
  scenario_id: AST-SCENARIO-COMBAT-GUARD-001
  balance_profile_id: AST-BAL-PROFILE-RELAY-REF-001
  seed: 104729
  logical_ticks: 52
  guard_opportunities: 3
  outcome: PLAYER_SURVIVED
  player_health_remaining_basis_points: 2800
  event_history_included: false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Graine :** elle rend la simulation rejouable dans le même environnement qualifié.
- **Temps :** la durée est exprimée en ticks logiques.
- **Santé :** les points de base décrivent une proportion entière sur 10 000 sans copier l’état complet du personnage.
- **Historique :** le détail des événements reste exclu du record d’équilibrage.
- **Frontière :** l’analyse lit l’issue et ne recalcule ni attaque, ni défense, ni dégâts.

## 31. Observer l’écologie sans fixer les prix

L’écologie possède les populations, réserves et indices de rareté. L’économie possède les prix. L’équilibrage peut étudier la relation entre les deux, mais ne doit pas établir un lien autoritaire direct.

> **[LECTURE] Signal écologique et résultat économique — Ne pas saisir.**

```yaml
cross_system_observation:
  scenario_id: AST-SCENARIO-RELAY-RESOURCE-001
  ecology:
    region_id: ecology.region.relay_delta
    resource_id: ecology.resource.ashwood
    scarcity_basis_points: 7200
  economy:
    currency_id: economy.currency.aster_mark
    quoted_price_minor_units: 1850
  interpretation_status: descriptive_only
  automatic_price_update: false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Écologie :** la rareté est un signal committé par son système propriétaire.
- **Économie :** le prix provient d’un devis autoritaire calculé par l’économie.
- **Observation :** le record permet une analyse de relation sans imposer de causalité.
- **Statut :** `descriptive_only` interdit une conclusion automatique.
- **Frontière :** `automatic_price_update` reste faux ; toute politique de prix doit être modifiée dans l’économie et revue séparément.

## 32. Définir une difficulté observable

La difficulté ne se réduit pas au taux d’échec. Une expérience peut être difficile parce que :

- les règles sont inconnues ;
- les signaux sont illisibles ;
- les décisions sont nombreuses ;
- les sanctions sont fortes ;
- les contrôles sont exigeants ;
- la variance est élevée ;
- une erreur est irrécupérable.

Le pilote associe donc plusieurs indicateurs : issue, ressources restantes, nombre de décisions, temps avant premier dommage, occasions de récupération et abandons contrôlés.

Une option de difficulté ne doit pas modifier silencieusement toutes les dimensions. Chaque profil documente ses paramètres et ses effets attendus.

## 33. Préparer des scénarios déterministes

Un scénario décrit l’état initial, les commandes, les graines et les invariants. Il ne dépend pas de l’ordre du système de fichiers ni de l’heure système.

> **[VSC] Visual Studio Code — Créer `test/simulation/scenarios/balance/relay_guard.v1.json`.**

```json
{
  "schema_version": 1,
  "scenario_id": "AST-SCENARIO-COMBAT-GUARD-001",
  "initial_state_fixture": "AST-FIXTURE-RELAY-GUARD-001",
  "command_script": "AST-COMMANDS-RELAY-GUARD-001",
  "maximum_logical_ticks": 200,
  "seeds": [
    104729,
    130363,
    155921,
    196613
  ],
  "required_invariants": [
    "no_negative_health",
    "no_event_before_commit",
    "all_commands_accounted_for"
  ],
  "observed_metrics": [
    "combat.guard_opportunity.count",
    "combat.duration.logical_ticks",
    "combat.outcome"
  ]
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Fixtures :** l’état initial et les commandes sont référencés par identités versionnées.
- **Borne :** `maximum_logical_ticks` empêche une simulation infinie.
- **Graines :** la même liste sert à tous les profils comparés.
- **Invariants :** un run qui les viole est invalide, même si ses métriques semblent favorables.
- **Observation :** seules les métriques déclarées sont exportées.

## 34. Utiliser un générateur pseudo-aléatoire local

Chaque scénario possède son instance de `RandomNumberGenerator`. Le générateur global n’est pas utilisé, car une autre fonctionnalité pourrait avancer sa séquence.

> **[VSC] Visual Studio Code — Créer `res://src/features/balancing/application/balance_simulation_runner.gd`.**

```gdscript
class_name BalanceSimulationRunner
extends RefCounted

func run_scenario(
	scenario: BalanceScenario,
	profile: BalanceProfile,
	seed_value: int,
) -> BalanceRunResult:
	if scenario == null or profile == null:
		return BalanceRunResult.rejected(&"BALANCE_INPUT_MISSING")

	var rng := RandomNumberGenerator.new()
	rng.seed = seed_value

	var state := scenario.build_initial_state()
	for logical_tick in range(1, scenario.maximum_logical_ticks + 1):
		var step_result := scenario.step(state, profile, rng, logical_tick)
		if not step_result.is_valid():
			return BalanceRunResult.rejected(step_result.code)
		state = step_result.next_state
		if step_result.is_terminal:
			return BalanceRunResult.completed(state, logical_tick, seed_value)

	return BalanceRunResult.rejected(&"BALANCE_MAXIMUM_TICKS_REACHED")
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètres :** le scénario, le profil et la graine sont obligatoires et séparés.
- **Générateur :** une instance locale reçoit `seed_value` avant le premier tirage.
- **Boucle :** `range(1, maximum + 1)` inclut la borne maximale voulue.
- **Validation :** chaque étape produit un résultat contrôlé avant de remplacer l’état candidat.
- **Retours :** le runner distingue entrée absente, étape invalide, fin normale et dépassement de budget.

## 35. Ne pas confondre graine et identité binaire universelle

Une même graine produit une séquence reproductible dans le même contrat qualifié. Elle ne garantit pas des octets identiques entre versions de moteur, algorithmes ou plateformes.

Le manifeste conserve donc :

- version du moteur ;
- révision du code ;
- profil ;
- scénario ;
- graine ;
- état initial ;
- résultats et empreintes.

Une comparaison entre référence et candidat utilise le même environnement et les mêmes graines. Une mise à jour de Godot ou du simulateur crée une nouvelle campagne de qualification.

## 36. Exécuter une matrice de simulations

> **[PS] PowerShell 7 — Lancer une campagne locale bornée.**

```powershell
.\.venv\Scripts\python.exe -m asteria_tools.balancing.run_matrix `
  --plan config\balancing\pilots\relay-expedition.v1.yaml `
  --workspace work\balance-runs\AST-BAL-RUN-RELAY-0001 `
  --max-workers 4

if ($LASTEXITCODE -ne 0) {
  throw "La matrice d’équilibrage a échoué."
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Plan :** le fichier versionné contient profils, scénarios et graines.
- **Workspace :** toutes les sorties restent sous un run isolé.
- **Parallélisme :** `--max-workers 4` borne les tâches ; le résultat final doit être trié par identité.
- **Code de retour :** un échec de scénario, schéma ou invariant produit un code non nul.
- **Limite :** cette commande est un contrat pédagogique et n’est pas déclarée exécutée dans ce chapitre.

## 37. Comparer des paires de résultats

Lorsque les mêmes graines sont utilisées pour la référence et le candidat, chaque graine forme une paire. Cette comparaison réduit le bruit dû aux scénarios aléatoires différents.

> **[VSC] Visual Studio Code — Créer `automation/src/asteria_tools/balancing/compare.py`.**

```python
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class PairedResult:
    seed: int
    reference: float
    candidate: float

    @property
    def delta(self) -> float:
        return self.candidate - self.reference


def paired_deltas(results: list[PairedResult]) -> list[float]:
    if not results:
        raise ValueError("BALANCE_PAIRED_RESULTS_EMPTY")
    seeds = [item.seed for item in results]
    if len(seeds) != len(set(seeds)):
        raise ValueError("BALANCE_SEED_DUPLICATED")
    return [item.delta for item in sorted(results, key=lambda item: item.seed)]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Dataclass :** `frozen=True` rend chaque paire immuable ; `slots=True` ferme les attributs attendus.
- **Propriété :** `delta` calcule candidat moins référence sans stocker une valeur redondante.
- **Validation :** une liste vide ou une graine dupliquée est refusée.
- **Tri :** les deltas sont retournés dans l’ordre croissant des graines.
- **Limite :** un delta ne prouve pas à lui seul une amélioration qualitative.

## 38. Éviter les conclusions sur un échantillon trop petit

Quatre graines peuvent vérifier un flux, mais elles ne suffisent pas à décrire une distribution complexe. Le protocole distingue :

- **smoke set** : quelques cas pour vérifier le pipeline ;
- **design set** : assez de cas pour comparer une hypothèse définie ;
- **stress set** : cas extrêmes et budgets ;
- **playtest set** : sessions humaines consenties.

La taille utile dépend de la variabilité, de la décision et du coût. Le rapport n’emploie pas « significatif » au sens statistique sans méthode et hypothèses explicites.

## 39. Produire un rapport de décision

Un rapport relie la question, les profils, les métriques, les scénarios, les résultats, les limites et la décision.

> **[VSC] Visual Studio Code — Créer `work/reports/AST-BAL-DECISION-RELAY-001.yaml`.**

```yaml
balance_decision_report:
  id: AST-BAL-DECISION-RELAY-001
  question_id: AST-BAL-Q-COMBAT-GUARD-001
  reference_profile: AST-BAL-PROFILE-RELAY-REF-001
  candidate_profile: AST-BAL-PROFILE-RELAY-CANDIDATE-A-001
  run_manifest_sha256: "<sha256>"
  evidence:
    result_manifest_sha256: "<sha256>"
    sample_count: "<measured-value>"
    failed_runs: "<measured-value>"
  observations:
    primary_metric: "<measured-summary>"
    secondary_metrics: []
  limitations:
    - "Simulation interne uniquement."
    - "Aucun playtest humain."
  decision:
    status: PENDING_REVIEW
    selected_profile: null
    rationale: ""
  rollback:
    reference_profile_preserved: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Question :** le rapport répond à une identité de question unique.
- **Preuves :** les manifestes sont référencés par empreinte.
- **Mesures :** les placeholders doivent être remplacés uniquement par des résultats réellement produits.
- **Limites :** simulation et playtest restent clairement distingués.
- **Retour arrière :** la référence est conservée tant que la décision n’est pas approuvée.

## 40. Versionner les paramètres et préparer le retour arrière

Un paramètre retenu appartient à un profil versionné. L’interface ou le rapport ne modifie pas directement une `Resource` partagée.

La promotion suit cette séquence :

1. créer un candidat ;
2. valider son schéma ;
3. exécuter la campagne ;
4. relire les résultats ;
5. approuver la décision ;
6. publier une nouvelle version du profil ;
7. conserver la référence précédente ;
8. exécuter les tests de non-régression pertinents.

Un retour arrière sélectionne une version antérieure approuvée. Il ne réécrit pas l’historique des rapports.

## 41. Distinguer corrélation et causalité

Deux métriques qui évoluent ensemble ne prouvent pas qu’une variable cause l’autre. Une hausse du taux de victoire peut coïncider avec :

- une fenêtre de garde plus large ;
- un changement de dégâts ;
- une modification du scénario ;
- une correction de bug ;
- une sélection différente de graines ;
- un comportement de testeur plus expérimenté.

La causalité demande un protocole : variable isolée, conditions comparables, mécanisme plausible et répétition. Le rapport utilise « associé à » ou « observé avec » lorsqu’aucune causalité n’est démontrée.

## 42. Minimiser les données d’un playtest consenti

Avant un playtest humain, le projet documente :

- la finalité exacte ;
- les métriques nécessaires ;
- les champs interdits ;
- la durée de conservation ;
- l’accès ;
- le retrait ;
- le mécanisme de consentement ;
- la procédure de suppression.

Par défaut, le pilote n’enregistre pas :

- nom, adresse électronique ou compte ;
- voix, vidéo ou chat ;
- adresse IP ;
- identifiant matériel ;
- texte libre ;
- sauvegarde complète ;
- localisation réelle ;
- prompt ou réponse IA brute.

Un identifiant de session aléatoire peut rester une donnée personnelle s’il permet de relier les comportements à une personne. La minimisation ne remplace donc ni l’information, ni la base juridique, ni les droits applicables.

## 43. Documenter le consentement sans le forcer

Le consentement, lorsqu’il constitue la base retenue, doit être libre, spécifique, éclairé et révocable. Refuser la télémétrie facultative ne doit pas bloquer une fonctionnalité qui n’en dépend pas.

> **[LECTURE] État d’une session consentie — Ne pas saisir.**

```yaml
playtest_session:
  session_id: "<random-session-id>"
  collection_mode: consented_playtest
  notice_version: AST-PRIVACY-NOTICE-PLAYTEST-001
  purposes:
    - balance_combat_guard_learning
  optional_metrics:
    accepted: true
  voice_recording:
    accepted: false
  withdrawal_supported: true
  retention_policy_id: AST-BAL-RETENTION-PLAYTEST-001
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Finalité :** la session nomme l’objectif précis de l’observation.
- **Séparation :** métriques et enregistrement vocal possèdent des choix distincts.
- **Révocation :** `withdrawal_supported` impose une procédure de retrait.
- **Rétention :** une politique identifiée détermine la conservation.
- **Limite :** cet exemple ne constitue pas un formulaire juridique prêt à publier.

## 44. Anonymisation, pseudonymisation et agrégation

La **pseudonymisation** remplace ou sépare un identifiant, mais permet encore une réassociation dans certaines conditions. Les données restent alors personnelles.

L’**anonymisation** vise à rendre l’identification irréversible selon les moyens raisonnablement disponibles. Ajouter un hash à une adresse électronique ne suffit pas automatiquement.

L’**agrégation** réduit la granularité, par exemple en conservant un total par scénario plutôt qu’une trace par session. Elle diminue le risque, mais un groupe très petit ou des dimensions rares peuvent encore isoler une personne.

Le chapitre privilégie :

1. simulations sans personne ;
2. agrégats internes ;
3. sessions consenties minimisées seulement lorsque la question l’exige.

## 45. Mode Solo

En Solo, commencer par un seul pilote, trois à cinq métriques et un petit jeu de graines. Écrire la question et les seuils avant la campagne.

Conserver :

- le plan de run ;
- le catalogue de métriques ;
- les profils comparés ;
- les résultats bruts bornés ;
- le rapport ;
- la décision.

Une feuille de calcul peut suffire pour une première lecture, mais les données sources et les formules restent versionnées. Une cellule modifiée manuellement ne devient pas une baseline sans rapport.

Le développeur Solo effectue une revue différée : fermer l’analyse, revenir avec les critères, puis décider sans ajuster simultanément les données et les seuils.

## 46. Mode Studio

En Studio, séparer autant que possible :

- propriétaire de la question ;
- propriétaire des systèmes instrumentés ;
- responsable des métriques ;
- opérateur de simulation ;
- analyste ;
- game designer décisionnaire ;
- responsable confidentialité ;
- QA de non-régression.

Le catalogue de métriques passe par revue. Les dashboards ne deviennent pas des sources canoniques : ils dérivent de manifestes et de requêtes versionnées.

Une expérience possède un propriétaire, une échéance, un coût, une règle d’arrêt et une décision attendue. Les résultats négatifs sont conservés afin d’éviter de répéter une hypothèse déjà réfutée.

## 47. Diagnostics : erreurs fréquentes et corrections

<!-- qa:error-correction-section -->

Les dix cas suivants appliquent la règle sémantique complète : symptôme, exemple fautif, correction et explication de la différence.

### 47.1 Collecter avant de définir la question

**Symptôme ou risque :** Le projet enregistre toutes les actions puis cherche après coup une histoire compatible avec les données.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
telemetry:
  collect_every_event: true
  purpose: "On verra plus tard."
  retention: unlimited
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** La finalité est absente, la collecte n’est pas minimisée et la conservation illimitée rend impossible de justifier chaque champ.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
telemetry:
  question_id: AST-BAL-Q-COMBAT-GUARD-001
  allowed_metrics:
    - combat.guard_opportunity.count
    - combat.duration.logical_ticks
  retention_policy_id: AST-BAL-RETENTION-001
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La question, les deux métriques nécessaires et la politique de conservation bornent la collecte et rendent chaque observation justifiable.

### 47.2 Utiliser une moyenne sans montrer la distribution

**Symptôme ou risque :** Un combat bloqué disparaît dans une moyenne présentée comme représentative.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
combat_duration:
  mean_ticks: 67
  conclusion: balanced
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le nombre de cas, la médiane, les extrêmes et les percentiles sont absents ; la conclusion dépasse les informations disponibles.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
combat_duration:
  count: 10
  mean_ticks: 67
  median_ticks: 48
  p90_nearest_rank_ticks: 240
  conclusion: investigate_tail
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Le dénominateur et la queue de distribution révèlent le cas extrême, ce qui transforme une approbation automatique en investigation ciblée.

### 47.3 Stocker un ratio sans numérateur ni dénominateur

**Symptôme ou risque :** Deux taux de 80 % semblent équivalents alors que l’un repose sur cinq cas et l’autre sur mille.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
win_rate: 0.8
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** La valeur ne permet pas de connaître la taille de l’échantillon ni de recalculer le taux.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
wins: 800
completed_runs: 1000
win_rate: 0.8
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Le numérateur et le dénominateur rendent le ratio vérifiable et distinguent clairement la précision descriptive des deux expériences.

### 47.4 Utiliser un identifiant de joueur comme dimension

**Symptôme ou risque :** Le nombre de séries explose et le fichier permet de suivre une personne session après session.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```json
{
  "metric": "combat.duration.logical_ticks",
  "dimensions": {
    "player_email": "personne@example.invalid"
  }
}
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Une adresse électronique est inutile pour la question d’équilibrage, augmente la cardinalité et introduit une donnée personnelle directe.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```json
{
  "metric": "combat.duration.logical_ticks",
  "dimensions": {
    "scenario_id": "AST-SCENARIO-COMBAT-GUARD-001",
    "difficulty_id": "difficulty.introduction"
  }
}
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Les dimensions proviennent de catalogues bornés, répondent au protocole et ne suivent pas une identité réelle.

### 47.5 Modifier plusieurs variables dans le même candidat

**Symptôme ou risque :** Une amélioration observée ne peut être attribuée à aucun changement précis.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
candidate:
  guard_window: 16
  enemy_damage: 7
  player_health: 140
  reward_minor_units: 1800
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Quatre systèmes ou paramètres évoluent ensemble ; une variation de résultat possède plusieurs explications concurrentes.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
candidate:
  based_on: AST-BAL-PROFILE-RELAY-REF-001
  changes:
    combat.guard_window.logical_ticks:
      from: 12
      to: 16
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Le candidat isole une variable et cite sa référence, ce qui permet une comparaison interprétable et un retour arrière précis.

### 47.6 Utiliser le générateur aléatoire global

**Symptôme ou risque :** Une autre fonctionnalité avance la séquence et change les résultats de simulation.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```gdscript
seed(104729)
var roll := randi_range(1, 100)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le générateur global est partagé ; un appel ajouté ailleurs peut modifier l’ordre des tirages et casser la comparaison.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```gdscript
var rng := RandomNumberGenerator.new()
rng.seed = 104729
var roll := rng.randi_range(1, 100)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** L’instance locale possède sa propre graine et son propre état, isolés des tirages effectués par les autres systèmes.

### 47.7 Laisser l’analyse modifier le gameplay

**Symptôme ou risque :** Un dashboard augmente automatiquement la récompense lorsqu’un indicateur passe sous un seuil.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```gdscript
if dashboard.win_rate < 0.5:
	EconomyService.set_reward_minor_units(1800)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Une vue dérivée obtient une autorité économique et modifie un paramètre sans profil versionné, revue ni tests de régression.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```gdscript
var proposal := BalanceDecision.propose(
	&"AST-BAL-Q-ECONOMY-COST-001",
	&"AST-BAL-PROFILE-RELAY-CANDIDATE-B-001",
)
decision_repository.save_pending(proposal)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** L’analyse crée une proposition en attente ; la modification réelle reste un profil versionné soumis aux propriétaires et aux portes qualité.

### 47.8 Confondre corrélation et causalité

**Symptôme ou risque :** Le rapport affirme que la rareté cause un prix élevé sans isoler les politiques économiques.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
observation:
  scarcity_basis_points: 7200
  price_minor_units: 1850
conclusion: "La rareté a causé ce prix."
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Une coïncidence de deux valeurs n’exclut ni taxes, ni offre, ni réputation, ni autre politique de prix.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
observation:
  scarcity_basis_points: 7200
  price_minor_units: 1850
interpretation: "Valeurs associées dans ce scénario."
causal_claim: not_demonstrated
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La formulation reste descriptive et enregistre explicitement que le mécanisme causal n’a pas été démontré.

### 47.9 Conserver les runs bruts sans limite

**Symptôme ou risque :** Le laboratoire remplit le disque et conserve des sessions plus longtemps que nécessaire.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
retention:
  raw_runs: forever
  maximum_bytes: null
  deletion: disabled
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Aucune borne de volume, de durée ou de priorité de suppression ne protège le poste ni les personnes concernées.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
retention:
  raw_run_maximum_count: 20
  maximum_total_bytes: 536870912
  delete_oldest_unapproved_raw_runs_first: true
  approved_reports_require_manual_deletion: true
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Les runs bruts sont bornés et supprimés selon une priorité explicite, tandis que les rapports approuvés restent protégés de l’effacement automatique.

### 47.10 Présenter une simulation comme un résultat joueur

**Symptôme ou risque :** Un rapport annonce que « 80 % des joueurs réussissent » alors qu’il contient seulement des agents simulés.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
source: simulation
runs: 1000
statement: "80 % des joueurs réussissent."
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** La population observée n’est pas composée de joueurs et la formulation généralise au-delà du protocole.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
source: deterministic_simulation
runs: 1000
statement: "800 simulations sur 1000 terminent avec l’issue attendue."
player_generalization: prohibited
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La phrase nomme la source, le numérateur et le dénominateur, puis interdit explicitement l’extrapolation vers des personnes réelles.

## 48. Checklist de production et d’acceptation

- [ ] question de conception écrite avant la collecte ;
- [ ] décision possible et seuils définis ou déclarés en attente ;
- [ ] métriques dotées d’identités, unités, finalités et sources ;
- [ ] dimensions fermées et cardinalité bornée ;
- [ ] événements observés uniquement après commit ;
- [ ] aucune autorité gameplay accordée au laboratoire ;
- [ ] scénario, fixture, profil et graines versionnés ;
- [ ] référence et candidat comparés sur les mêmes entrées ;
- [ ] numérateurs, dénominateurs et tailles d’échantillon conservés ;
- [ ] moyenne complétée par médiane, dispersion ou percentiles pertinents ;
- [ ] valeurs extrêmes inspectées et non supprimées sans justification ;
- [ ] manifestes et empreintes produits ;
- [ ] données personnelles absentes ou strictement minimisées ;
- [ ] consentement et retrait documentés lorsque nécessaires ;
- [ ] rétention et purge bornées ;
- [ ] rapport de décision relu par le rôle autorisé ;
- [ ] référence précédente conservée pour le retour arrière ;
- [ ] tests de non-régression identifiés ;
- [ ] aucune mesure runtime revendiquée sans exécution réelle ;
- [ ] aucune sortie de campagne n’est publiée hors du workspace déclaré.

## 49. Critère d’acceptation du pilote

Le pilote `AST-BALANCE-PILOT-RELAY-EXPEDITION-001` pourra être déclaré matérialisé seulement lorsque :

- le catalogue réel est versionné ;
- les scénarios et profils existent ;
- une campagne de référence et une campagne candidate ont été exécutées ;
- les mêmes graines et invariants ont été utilisés ;
- les manifestes et résultats sont conservés ;
- les agrégats peuvent être reproduits ;
- les runs invalides sont séparés ;
- un rapport nomme les limites ;
- une décision humaine est signée ;
- le profil précédent reste restaurable.

Le présent chapitre ne coche aucune de ces conditions d’exécution.

## 50. Références techniques officielles

- [Godot 4.7 — `RandomNumberGenerator`](https://docs.godotengine.org/en/4.7/classes/class_randomnumbergenerator.html)
- [Godot 4.7 — Génération de nombres aléatoires](https://docs.godotengine.org/en/4.7/tutorials/math/random_number_generation.html)
- [Godot 4.7 — `JSON`](https://docs.godotengine.org/en/4.7/classes/class_json.html)
- [Python 3.14 — Module `statistics`](https://docs.python.org/3.14/library/statistics.html)
- [Python 3.14 — Module `csv`](https://docs.python.org/3.14/library/csv.html)
- [Python 3.14 — Module `json`](https://docs.python.org/3.14/library/json.html)
- [CNIL — Minimiser les données collectées](https://www.cnil.fr/fr/minimiser-les-donnees-collectees)
- [Commission européenne — Principes du RGPD](https://commission.europa.eu/law/law-topic/data-protection/data-protection-eu_fr)
- [Livre II — Chapitre 18 : Combat](../Livre-II/CHAPITRE-18-Combat.md)
- [Livre II — Chapitre 21 : Économie](../Livre-II/CHAPITRE-21-Economie.md)
- [Livre II — Chapitre 22 : Monde vivant et simulation écologique](../Livre-II/CHAPITRE-22-Monde-vivant-et-simulation-ecologique.md)
- [Livre II — Chapitre 27 : Tests unitaires, tests d’intégration et simulations](../Livre-II/CHAPITRE-27-Tests-unitaires-tests-d-integration-et-simulations.md)
- [Livre II — Chapitre 28 : Journalisation, diagnostic et reproductibilité](../Livre-II/CHAPITRE-28-Journalisation-diagnostic-et-reproductibilite.md)
- [Livre II — Chapitre 29 : Automatisation Python et génération de données](../Livre-II/CHAPITRE-29-Automatisation-Python-et-generation-de-donnees.md)

## 51. Synthèse opérationnelle pour Project Asteria

Project Asteria retient `AST-BALANCE-PILOT-RELAY-EXPEDITION-001` comme premier laboratoire d’équilibrage du Livre IV.

Les décisions permanentes sont :

- l’équilibrage observe des résultats committés et ne possède aucune autorité gameplay ;
- la collecte reste locale et hors ligne par défaut ;
- chaque métrique possède identité, unité, source, finalité, bornes et dimensions autorisées ;
- les ratios conservent numérateur et dénominateur ;
- les distributions ne sont pas réduites à une moyenne ;
- les simulations utilisent scénarios, profils et graines versionnés ;
- une graine ne prouve pas une identité binaire entre environnements différents ;
- référence et candidat utilisent les mêmes scénarios et entrées ;
- les montants économiques restent des entiers en unités mineures ;
- l’écologie fournit des signaux sans fixer les prix ;
- les données humaines sont évitées lorsque des simulations suffisent ;
- consentement, minimisation, rétention et retrait restent explicites lorsqu’un playtest les exige ;
- les rapports proposent une décision, mais ne modifient jamais directement les paramètres ;
- toute promotion conserve la référence précédente et une procédure de retour arrière ;
- aucune mesure runtime, conclusion joueur ou efficacité réelle n’est revendiquée sans campagne exécutée.

> **[LECTURE] Décisions du pilote — Ne pas saisir.**

```yaml
asteria_balance_decisions:
  pilot_id: AST-BALANCE-PILOT-RELAY-EXPEDITION-001
  metric_catalog_id: AST-BAL-METRICS-001
  local_by_default: true
  network_export: false
  gameplay_authority: none
  source_events_after_commit_only: true
  deterministic_scenarios: required
  paired_reference_candidate_seeds: required
  personal_data_default: prohibited
  human_playtest_requires_governance: true
  decision_authority: human_review
  rollback_profile_preserved: true
  materialization_status: not_started
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Catalogue :** l’ensemble de métriques possède une identité stable.
- **Collecte :** le réseau reste désactivé et les données personnelles interdites par défaut.
- **Simulation :** référence et candidat partagent scénarios et graines.
- **Autorité :** la revue humaine sélectionne un profil ; le laboratoire ne modifie pas les systèmes.
- **Réserve :** `not_started` confirme qu’aucun run ni résultat n’est présenté comme exécuté.
