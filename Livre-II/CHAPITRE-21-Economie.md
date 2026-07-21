---
title: "Livre II — Chapitre 21 : Économie"
id: "DOC-L2-CH21"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre II"
chapter: 21
last-verified: "2026-07-20T21:13:06+02:00"
audit-status: "complete"
audit-date: "2026-07-20T21:13:06+02:00"
audit-report: "Livre-II/QA/AUDIT-CHAPITRE-21.md"
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

# Économie

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L2-CH21`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Version de référence :** Godot `4.7.1-stable`, édition Standard, GDScript, Forward+  

> **Audit post-création :** terminé au niveau `static-review` — voir `Livre-II/QA/AUDIT-CHAPITRE-21.md`.

## 1. Rôle du chapitre

Le chapitre 20 a établi que l’inventaire possède l’identité, la quantité, la garde, la propriété et le transfert des objets. Il a aussi réservé au présent chapitre les monnaies, les prix, les paiements, les achats et les ventes.

Ce chapitre construit l’autorité **économique** de `Project Asteria` : devises, portefeuilles, soldes, valeurs de référence, offres, devis, taxes, récompenses monétaires et transactions atomiques avec l’inventaire.

Le système doit garantir que :

- aucune somme monétaire n’utilise un `float` ;
- chaque devise possède un identifiant stable et une unité mineure explicite ;
- un portefeuille ne devient jamais négatif dans le modèle pédagogique retenu ;
- toute transaction monétaire est équilibrée par devise ;
- une récompense provient d’un portefeuille émetteur ou d’une trésorerie explicite ;
- une interface, un agent ou une sortie IA ne choisit jamais le montant final autoritaire ;
- l’achat d’un objet ne peut débiter l’acheteur sans transférer l’objet, ni transférer l’objet sans payer le vendeur ;
- un retry d’une même transaction ne peut produire un second débit ;
- le chargement prépare portefeuilles, offres et journal avant de remplacer l’état actif.

## 2. Prérequis

Le lecteur doit avoir parcouru :

- le chapitre 4 pour l’architecture feature-first ;
- le chapitre 5 pour l’injection et les unités de travail ;
- le chapitre 7 pour les `Resource`, catalogues et identifiants ;
- le chapitre 8 pour les transactions et journaux durables ;
- le chapitre 9 pour les sauvegardes strictes ;
- le chapitre 14 pour les identités de personnages ;
- le chapitre 15 pour les relations utilisées comme contexte, jamais comme prix direct ;
- le chapitre 17 pour les actions d’agents ;
- le chapitre 20 pour les objets, conteneurs et transferts.

## 3. Périmètre et frontières

Ce chapitre couvre :

- définitions de devises ;
- montants entiers en unités mineures ;
- parties économiques et portefeuilles ;
- soldes non négatifs et révisions ;
- valeurs de référence séparées des objets ;
- multiplicateurs déterministes en points de base ;
- offres de vente et devis temporaires ;
- achats et ventes comme deux vues d’une même transaction ;
- taxes ou commissions explicites ;
- récompenses monétaires équilibrées ;
- journal d’écritures ;
- idempotence ;
- commit commun avec l’inventaire ;
- agents, présentation et persistance.

Il ne couvre pas :

- les lois fiscales, amendes, confiscations ou sanctions ;
- les factions, gouvernements et budgets politiques ;
- les domaines, bâtiments, chaînes de production et loyers ;
- la simulation écologique de l’offre et de la demande ;
- les récompenses narratives ou de quête non monétaires ;
- les prêts, intérêts, dettes, découverts et marchés financiers ;
- le change automatique entre devises ;
- l’équilibrage final du jeu ;
- le multijoueur.

> **Frontière essentielle :** l’économie possède les devises, soldes, valeurs, offres, devis, paiements et écritures. L’inventaire conserve l’autorité sur les objets et leur transfert. Les systèmes futurs peuvent fournir des taxes, indices ou autorisations, mais ne modifient jamais directement un portefeuille.

## 4. Chaîne d’autorité

> **[LECTURE] Flux d’un achat — Ne pas saisir.**

```text
joueur / agent / scénario
    ↓ PurchaseCommand
EconomyService
    ├── relit offre, portefeuilles et révisions
    ├── relit le contexte de prix autorisé
    ├── recalcule le devis
    ├── prépare débit, crédits et journal
    └── demande à l’inventaire un transfert candidat
            ↓
EconomyTransactionCommitPort
    ├── revalide économie et inventaire
    ├── refuse avant toute mutation si un candidat échoue
    ├── remplace les agrégats comme un même lot
    └── enregistre l’idempotence
            ↓
EconomyResult + événements typés
            ↓
présentation, agents, narration, diagnostic
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- La commande propose une opération et un total attendu ; elle ne fixe pas le prix autoritaire.
- L’économie recalcule le devis depuis l’offre et les politiques actives.
- L’inventaire prépare lui-même l’objet source et le conteneur de destination.
- Le port de commit représente l’adaptateur multi-autorités matérialisé au point de composition.
- Aucun signal n’est émis avant le remplacement réussi de tous les candidats.

## 5. Architecture retenue

> **[LECTURE] Arborescence cible — Ne pas créer depuis un terminal.**

```text
res://src/features/economy/
├── domain/
│   ├── economy_id.gd
│   ├── economy_party_ref.gd
│   ├── currency_definition.gd
│   ├── money_amount.gd
│   ├── wallet_state.gd
│   ├── economy_posting.gd
│   ├── economy_ledger_record.gd
│   ├── item_value_definition.gd
│   ├── pricing_context.gd
│   ├── price_quote.gd
│   ├── trade_offer_state.gd
│   ├── purchase_command.gd
│   ├── reward_command.gd
│   └── economy_result.gd
├── application/
│   ├── currency_catalog.gd
│   ├── item_value_catalog.gd
│   ├── economy_repository.gd
│   ├── economy_access_port.gd
│   ├── pricing_context_port.gd
│   ├── economy_inventory_trade_port.gd
│   ├── economy_transaction_commit_port.gd
│   ├── economy_mutation_candidate.gd
│   ├── money_math.gd
│   ├── pricing_policy.gd
│   ├── trade_offer_factory.gd
│   ├── economy_service.gd
│   ├── reward_service.gd
│   ├── economy_agent_context_port.gd
│   └── economy_agent_action_executor.gd
├── infrastructure/
│   ├── economy_snapshot_codec.gd
│   └── economy_save_section.gd
└── presentation/
    └── economy_presentation_bridge.gd

res://data/economy/
├── currencies/
│   ├── aster_mark.tres
│   └── frontier_token.tres
└── values/
    ├── field_ration_value.tres
    └── ashwood_staff_value.tres

res://scenes/learning/
├── ch21_economy_demo.tscn
└── ch21_economy_demo.gd
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- `domain` contient montants, portefeuilles, offres, commandes et invariants.
- `application` calcule les devis et orchestre les candidats sans toucher aux scènes.
- `infrastructure` encode uniquement les données durables.
- Les valeurs d’objets restent dans une fonctionnalité économique séparée des `ItemDefinition` du chapitre 20.
- Le point de composition fournit l’adaptateur qui commit économie et inventaire ensemble.

## 6. Vocabulaire

Une **devise** définit une unité monétaire stable, son unité mineure et ses bornes.

Un **montant** associe une devise à un nombre entier d’unités mineures. Par exemple, `1234` unités mineures peuvent représenter `12,34` unités majeures lorsque la devise utilise un facteur `100`.

Un **portefeuille** porte des soldes par devise pour une partie économique identifiée.

Une **écriture** est un delta signé appliqué à un portefeuille. Une transaction équilibrée possède, pour chaque devise, une somme de deltas égale à zéro.

Une **valeur de référence** décrit le prix de base économique d’une définition d’objet. Elle n’est pas stockée dans l’objet.

Une **offre** engage un vendeur sur un objet, une quantité maximale, une devise et un prix unitaire pendant un intervalle logique.

Un **devis** est un calcul temporaire. Il peut être affiché au joueur, mais il est recalculé au moment du commit.

L’**idempotence** garantit que la même identité de transaction et le même contenu produisent le même résultat sans recommencer les mutations.

## 7. Identifiants économiques

> **[VSC] Visual Studio Code — Créer : `res://src/features/economy/domain/economy_id.gd`.**

```gdscript
class_name EconomyId
extends RefCounted

const CURRENCY_PREFIX := "economy.currency."
const WALLET_PREFIX := "economy.wallet."
const OFFER_PREFIX := "economy.offer."
const QUOTE_PREFIX := "economy.quote."
const TRANSACTION_PREFIX := "economy.transaction."
const POSTING_PREFIX := "economy.posting."

static func currency(slug: String) -> StringName:
	return _from_slug(CURRENCY_PREFIX, slug)

static func wallet(slug: String) -> StringName:
	return _from_slug(WALLET_PREFIX, slug)

static func offer(uuid_text: String) -> StringName:
	return _from_slug(OFFER_PREFIX, uuid_text)

static func quote(transaction_id: StringName, offer_revision: int) -> StringName:
	if not StableId.is_valid(transaction_id) or offer_revision < 0:
		return &""
	return StringName("%s%s.%d" % [QUOTE_PREFIX, transaction_id, offer_revision])

static func transaction(uuid_text: String) -> StringName:
	return _from_slug(TRANSACTION_PREFIX, uuid_text)

static func posting(transaction_id: StringName, index: int) -> StringName:
	if not StableId.is_valid(transaction_id) or index < 0:
		return &""
	return StringName("%s%s.%d" % [POSTING_PREFIX, transaction_id, index])

static func _from_slug(prefix: String, value: String) -> StringName:
	var normalized := value.strip_edges().to_lower().replace("-", "_")
	if normalized.is_empty():
		return &""
	for character: String in normalized:
		var is_letter := character >= "a" and character <= "z"
		var is_digit := character >= "0" and character <= "9"
		if not is_letter and not is_digit and character != "_":
			return &""
	return StringName(prefix + normalized)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Chaque famille d’identifiants possède un préfixe distinct.
- Les slugs sont normalisés sans dépendre d’un texte localisé.
- Un devis est corrélé à une transaction et à la révision de l’offre.
- Les écritures utilisent un index stable dans le record.
- Une entrée invalide renvoie `&""` plutôt qu’un identifiant partiel.

## 8. Parties économiques

> **[VSC] Visual Studio Code — Créer : `res://src/features/economy/domain/economy_party_ref.gd`.**

```gdscript
class_name EconomyPartyRef
extends RefCounted

enum Kind {
	CHARACTER,
	FACTION,
	DOMAIN,
	SYSTEM,
}

var kind: Kind = Kind.SYSTEM
var party_id: StringName

func validate() -> Error:
	if kind < Kind.CHARACTER or kind > Kind.SYSTEM:
		return ERR_INVALID_DATA
	if kind == Kind.CHARACTER:
		return OK if CharacterId.is_valid(party_id) else ERR_INVALID_DATA
	return OK if StableId.is_valid(party_id) else ERR_INVALID_DATA

func duplicate_detached() -> EconomyPartyRef:
	var copy := EconomyPartyRef.new()
	copy.kind = kind
	copy.party_id = party_id
	return copy

func equals(other: EconomyPartyRef) -> bool:
	return other != null and kind == other.kind and party_id == other.party_id
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- La référence permet d’ouvrir un portefeuille à un personnage, une future faction, un futur domaine ou un système.
- Les chapitres 23 et 24 resteront propriétaires de l’existence des factions et domaines.
- `SYSTEM` représente notamment une trésorerie, un puits ou une source monétaire explicitement configurée.
- La copie détachée évite de partager une référence mutable entre snapshots.
- `equals()` compare l’identité économique, pas un nom affiché.

## 9. Définition d’une devise

> **[VSC] Visual Studio Code — Créer : `res://src/features/economy/domain/currency_definition.gd`.**

```gdscript
class_name CurrencyDefinition
extends Resource

const MAX_SAFE_INTEGER := 9007199254740991

@export var currency_id: StringName
@export var display_name_key: StringName
@export var symbol_key: StringName
@export_range(1, 1000000, 1) var minor_units_per_major: int = 100
@export var maximum_balance_minor: int = 1000000000000
@export var transferable := true

func validate() -> Error:
	if not StableId.is_valid(currency_id):
		return ERR_INVALID_DATA
	if not StableId.is_valid(display_name_key):
		return ERR_INVALID_DATA
	if not StableId.is_valid(symbol_key):
		return ERR_INVALID_DATA
	if minor_units_per_major < 1 or minor_units_per_major > 1000000:
		return ERR_INVALID_DATA
	if maximum_balance_minor < 1 or maximum_balance_minor > MAX_SAFE_INTEGER:
		return ERR_INVALID_DATA
	return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- La devise est une `Resource` de conception partagée et immuable pendant le gameplay.
- `minor_units_per_major` décrit l’affichage, pas un facteur flottant de calcul.
- La borne maximale reste dans la plage entière exacte des snapshots JSON du projet.
- `transferable` permet une monnaie de score ou de progression non échangeable.
- Aucun solde vivant n’est stocké dans cette ressource.

## 10. Montant monétaire

> **[VSC] Visual Studio Code — Créer : `res://src/features/economy/domain/money_amount.gd`.**

```gdscript
class_name MoneyAmount
extends RefCounted

var currency_id: StringName
var minor_units: int = 0

func validate(catalog: CurrencyCatalog) -> Error:
	if catalog == null:
		return ERR_UNCONFIGURED
	if not StableId.is_valid(currency_id):
		return ERR_INVALID_DATA
	var definition := catalog.get_definition(currency_id)
	if definition == null or definition.validate() != OK:
		return ERR_DOES_NOT_EXIST
	if minor_units < 0 or minor_units > definition.maximum_balance_minor:
		return ERR_INVALID_DATA
	return OK

func duplicate_detached() -> MoneyAmount:
	var copy := MoneyAmount.new()
	copy.currency_id = currency_id
	copy.minor_units = minor_units
	return copy

func is_same_currency(other: MoneyAmount) -> bool:
	return other != null and currency_id == other.currency_id
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Un montant positif ou nul sert aux prix, soldes et totaux.
- Les deltas signés appartiennent aux écritures, pas à `MoneyAmount`.
- La devise est validée contre le catalogue avant toute opération.
- La comparaison refuse implicitement tout mélange de devises.
- La copie ne contient ni formatage ni symbole d’interface.

## 11. Arithmétique sûre

> **[VSC] Visual Studio Code — Créer : `res://src/features/economy/application/money_math.gd`.**

```gdscript
class_name MoneyMath
extends RefCounted

const MAX_SAFE_INTEGER := 9007199254740991
const BASIS_POINT_SCALE := 10000

static func checked_add(left: int, right: int) -> Variant:
	if left < -MAX_SAFE_INTEGER or left > MAX_SAFE_INTEGER:
		return null
	if right < -MAX_SAFE_INTEGER or right > MAX_SAFE_INTEGER:
		return null
	if right > 0 and left > MAX_SAFE_INTEGER - right:
		return null
	if right < 0 and left < -MAX_SAFE_INTEGER - right:
		return null
	return left + right

static func checked_multiply(left: int, right: int) -> Variant:
	if left == 0 or right == 0:
		return 0
	if left < 0 or right < 0:
		return null
	if left > MAX_SAFE_INTEGER / right:
		return null
	return left * right

static func multiply_basis_points(value: int, basis_points: int) -> Variant:
	if value < 0 or basis_points < 0 or basis_points > 100000:
		return null
	var product: Variant = checked_multiply(value, basis_points)
	if product == null:
		return null
	var rounded: Variant = checked_add(int(product), BASIS_POINT_SCALE / 2)
	if rounded == null:
		return null
	return int(rounded) / BASIS_POINT_SCALE
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Les opérations refusent un résultat hors de la plage JSON sûre retenue par le guide.
- Les prix et multiplicateurs économiques restent non négatifs.
- `10000` points de base représentent `100 %`.
- L’expression `BASIS_POINT_SCALE / 2` vaut `5000`, puisque l’échelle contient `10000` points de base. Son ajout avant la division par `BASIS_POINT_SCALE` réalise un arrondi à l’entier le plus proche.
- `Variant` permet de distinguer un résultat nul valide d’un dépassement signalé par `null`.

## 12. État d’un portefeuille

> **[VSC] Visual Studio Code — Créer : `res://src/features/economy/domain/wallet_state.gd`.**

```gdscript
class_name WalletState
extends RefCounted

var wallet_id: StringName
var owner: EconomyPartyRef
var balances: Dictionary[StringName, int] = {}
var revision: int = 0
var posting_sequence: int = 0

func validate(catalog: CurrencyCatalog) -> Error:
	if catalog == null:
		return ERR_UNCONFIGURED
	if not StableId.is_valid(wallet_id):
		return ERR_INVALID_DATA
	if owner == null or owner.validate() != OK:
		return ERR_INVALID_DATA
	if revision < 0 or posting_sequence < 0:
		return ERR_INVALID_DATA
	if balances.size() > 64:
		return ERR_OUT_OF_MEMORY
	for currency_id: StringName in balances:
		var definition := catalog.get_definition(currency_id)
		if definition == null or definition.validate() != OK:
			return ERR_DOES_NOT_EXIST
		var balance: int = balances[currency_id]
		if balance < 0 or balance > definition.maximum_balance_minor:
			return ERR_INVALID_DATA
	return OK

func balance_for(currency_id: StringName) -> int:
	return int(balances.get(currency_id, 0))

func duplicate_detached() -> WalletState:
	var copy := WalletState.new()
	copy.wallet_id = wallet_id
	copy.owner = owner.duplicate_detached() if owner != null else null
	copy.balances = balances.duplicate(true)
	copy.revision = revision
	copy.posting_sequence = posting_sequence
	return copy
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Un portefeuille peut contenir plusieurs devises sans les convertir entre elles.
- Un solde absent vaut zéro.
- Les soldes négatifs sont interdits ; crédits et dettes exigeraient un modèle distinct.
- `revision` protège les commandes obsolètes et `posting_sequence` ordonne les écritures du portefeuille.
- La copie profonde du dictionnaire évite de modifier le snapshot source.

## 13. Écriture comptable

> **[VSC] Visual Studio Code — Créer : `res://src/features/economy/domain/economy_posting.gd`.**

```gdscript
class_name EconomyPosting
extends RefCounted

var posting_id: StringName
var wallet_id: StringName
var currency_id: StringName
var delta_minor_units: int = 0
var resulting_balance_minor: int = 0

func validate(catalog: CurrencyCatalog) -> Error:
	if catalog == null:
		return ERR_UNCONFIGURED
	if not StableId.is_valid(posting_id):
		return ERR_INVALID_DATA
	if not StableId.is_valid(wallet_id):
		return ERR_INVALID_DATA
	var definition := catalog.get_definition(currency_id)
	if definition == null or definition.validate() != OK:
		return ERR_DOES_NOT_EXIST
	if delta_minor_units == 0:
		return ERR_INVALID_DATA
	if delta_minor_units < -definition.maximum_balance_minor:
		return ERR_INVALID_DATA
	if delta_minor_units > definition.maximum_balance_minor:
		return ERR_INVALID_DATA
	if resulting_balance_minor < 0:
		return ERR_INVALID_DATA
	if resulting_balance_minor > definition.maximum_balance_minor:
		return ERR_INVALID_DATA
	return OK

func duplicate_detached() -> EconomyPosting:
	var copy := EconomyPosting.new()
	copy.posting_id = posting_id
	copy.wallet_id = wallet_id
	copy.currency_id = currency_id
	copy.delta_minor_units = delta_minor_units
	copy.resulting_balance_minor = resulting_balance_minor
	return copy
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le delta est signé : négatif pour un débit, positif pour un crédit.
- Le solde résultant est enregistré pour faciliter le diagnostic et détecter une divergence lors d’un replay.
- Une écriture n’autorise jamais un solde final négatif.
- Les bornes viennent de la définition de devise.
- La classe ne modifie aucun portefeuille par elle-même.

## 14. Record de transaction équilibré

> **[VSC] Visual Studio Code — Créer : `res://src/features/economy/domain/economy_ledger_record.gd`.**

```gdscript
class_name EconomyLedgerRecord
extends RefCounted

const MAX_POSTINGS := 16

var transaction_id: StringName
var cause_id: StringName
var source_system_id: StringName
var logical_tick: int = 0
var command_fingerprint: String = ""
var postings: Array[EconomyPosting] = []

func validate(catalog: CurrencyCatalog) -> Error:
	if catalog == null:
		return ERR_UNCONFIGURED
	if not StableId.is_valid(transaction_id):
		return ERR_INVALID_DATA
	if not StableId.is_valid(cause_id) or not StableId.is_valid(source_system_id):
		return ERR_INVALID_DATA
	if logical_tick < 0 or command_fingerprint.is_empty():
		return ERR_INVALID_DATA
	if postings.size() < 2 or postings.size() > MAX_POSTINGS:
		return ERR_INVALID_DATA

	var totals: Dictionary[StringName, int] = {}
	var posting_ids: Dictionary[StringName, bool] = {}
	for posting: EconomyPosting in postings:
		if posting == null or posting.validate(catalog) != OK:
			return ERR_INVALID_DATA
		if posting_ids.has(posting.posting_id):
			return ERR_ALREADY_EXISTS
		posting_ids[posting.posting_id] = true
		var current: int = int(totals.get(posting.currency_id, 0))
		var next: Variant = MoneyMath.checked_add(current, posting.delta_minor_units)
		if next == null:
			return ERR_INVALID_DATA
		totals[posting.currency_id] = int(next)

	for currency_id: StringName in totals:
		if totals[currency_id] != 0:
			return ERR_INVALID_DATA
	return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le record exige au moins un débit et un crédit.
- L’équilibre est contrôlé séparément pour chaque devise.
- Une récompense doit donc débiter une trésorerie explicite avant de créditer le bénéficiaire.
- L’empreinte canonique sert à distinguer un retry identique d’une réutilisation conflictuelle du même identifiant.
- Le record est une preuve durable ; il n’exécute pas les écritures.

## 15. Valeur de référence d’un objet

> **[VSC] Visual Studio Code — Créer : `res://src/features/economy/domain/item_value_definition.gd`.**

```gdscript
class_name ItemValueDefinition
extends Resource

@export var value_id: StringName
@export var item_definition_id: StringName
@export var currency_id: StringName
@export var base_unit_price_minor: int = 1
@export var minimum_unit_price_minor: int = 1
@export var maximum_unit_price_minor: int = 1000000000

func validate(currency_catalog: CurrencyCatalog) -> Error:
	if currency_catalog == null:
		return ERR_UNCONFIGURED
	if not StableId.is_valid(value_id):
		return ERR_INVALID_DATA
	if not StableId.is_valid(item_definition_id):
		return ERR_INVALID_DATA
	var currency := currency_catalog.get_definition(currency_id)
	if currency == null or currency.validate() != OK:
		return ERR_DOES_NOT_EXIST
	if not currency.transferable:
		return ERR_UNAVAILABLE
	if minimum_unit_price_minor < 1:
		return ERR_INVALID_DATA
	if base_unit_price_minor < minimum_unit_price_minor:
		return ERR_INVALID_DATA
	if maximum_unit_price_minor < base_unit_price_minor:
		return ERR_INVALID_DATA
	if maximum_unit_price_minor > currency.maximum_balance_minor:
		return ERR_INVALID_DATA
	return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- La valeur économique est séparée de `ItemDefinition` afin que l’inventaire reste indépendant des prix.
- Une même définition d’objet possède une valeur de référence versionnée par l’économie.
- Les bornes empêchent un contexte de prix de produire un montant nul ou excessif.
- Le catalogue de devises valide l’unité utilisée.
- Cette ressource ne contient ni stock, ni vendeur, ni offre active.

## 16. Contexte de prix

> **[VSC] Visual Studio Code — Créer : `res://src/features/economy/domain/pricing_context.gd`.**

```gdscript
class_name PricingContext
extends RefCounted

const MIN_MULTIPLIER_BP := 1000
const MAX_MULTIPLIER_BP := 50000
const MAX_TAX_BP := 10000

var context_id: StringName
var revision: int = 0
var valid_until_tick: int = 0
var supply_multiplier_bp: int = 10000
var demand_multiplier_bp: int = 10000
var seller_multiplier_bp: int = 10000
var relationship_multiplier_bp: int = 10000
var tax_basis_points: int = 0
var tax_wallet_id: StringName

func validate() -> Error:
	if not StableId.is_valid(context_id) or revision < 0 or valid_until_tick < 0:
		return ERR_INVALID_DATA
	for value: int in [
		supply_multiplier_bp,
		demand_multiplier_bp,
		seller_multiplier_bp,
		relationship_multiplier_bp,
	]:
		if value < MIN_MULTIPLIER_BP or value > MAX_MULTIPLIER_BP:
			return ERR_INVALID_DATA
	if tax_basis_points < 0 or tax_basis_points > MAX_TAX_BP:
		return ERR_INVALID_DATA
	if tax_basis_points > 0 and not StableId.is_valid(tax_wallet_id):
		return ERR_INVALID_DATA
	if tax_basis_points == 0 and not tax_wallet_id.is_empty():
		return ERR_INVALID_DATA
	return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Les multiplicateurs sont des points de base, jamais des nombres flottants.
- Les indices d’offre, de demande ou de relation proviennent de ports propriétaires.
- L’économie valide puis applique ces indices sans recalculer leurs règles sociales ou écologiques.
- Une taxe positive exige un portefeuille de destination explicite.
- `valid_until_tick` borne l’utilisation d’un contexte devenu ancien.

## 17. Politique de calcul du prix

> **[VSC] Visual Studio Code — Créer : `res://src/features/economy/application/pricing_policy.gd`.**

```gdscript
class_name PricingPolicy
extends RefCounted

func unit_price(
	definition: ItemValueDefinition,
	context: PricingContext,
	currency_catalog: CurrencyCatalog,
) -> Variant:
	if definition == null or context == null:
		return null
	if definition.validate(currency_catalog) != OK or context.validate() != OK:
		return null

	var value: Variant = definition.base_unit_price_minor
	for multiplier: int in [
		context.supply_multiplier_bp,
		context.demand_multiplier_bp,
		context.seller_multiplier_bp,
		context.relationship_multiplier_bp,
	]:
		value = MoneyMath.multiply_basis_points(int(value), multiplier)
		if value == null:
			return null

	return clampi(
		int(value),
		definition.minimum_unit_price_minor,
		definition.maximum_unit_price_minor,
	)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Les multiplicateurs sont appliqués dans un ordre fixe et documenté.
- Chaque étape utilise l’arithmétique bornée de `MoneyMath`.
- Le résultat final est limité par les bornes de la valeur de référence.
- La fonction renvoie `null` lorsqu’un contrat ou un calcul est invalide.
- Aucun contexte ne modifie la ressource de valeur elle-même.

### 17.1 Créer une offre verrouillée

> **[VSC] Visual Studio Code — Créer : `res://src/features/economy/application/trade_offer_factory.gd`.**

```gdscript
class_name TradeOfferFactory
extends RefCounted

var _pricing_policy := PricingPolicy.new()

func create_sell_offer(
	offer_id: StringName,
	seller_wallet_id: StringName,
	source_container_id: StringName,
	source_entry: InventoryEntryRef,
	value_definition: ItemValueDefinition,
	context: PricingContext,
	quantity: int,
	minimum_quantity: int,
	valid_from_tick: int,
	expires_tick: int,
	currency_catalog: CurrencyCatalog,
) -> TradeOfferState:
	if source_entry == null or source_entry.validate() != OK:
		return null
	if quantity < 1 or minimum_quantity < 1 or minimum_quantity > quantity:
		return null
	var unit_price_value: Variant = _pricing_policy.unit_price(
		value_definition,
		context,
		currency_catalog,
	)
	if unit_price_value == null:
		return null
	var offer := TradeOfferState.new()
	offer.offer_id = offer_id
	offer.seller_wallet_id = seller_wallet_id
	offer.source_container_id = source_container_id
	offer.source_entry = source_entry.duplicate_detached()
	offer.item_definition_id = value_definition.item_definition_id
	offer.currency_id = value_definition.currency_id
	offer.unit_price_minor = int(unit_price_value)
	offer.remaining_quantity = quantity
	offer.minimum_quantity = minimum_quantity
	offer.valid_from_tick = valid_from_tick
	offer.expires_tick = expires_tick
	offer.active = true
	offer.revision = 0
	offer.pricing_revision = context.revision
	return offer if offer.validate(currency_catalog) == OK else null
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- La politique de prix est appliquée lors de la création ou du renouvellement de l’offre.
- L’offre conserve ensuite un prix unitaire verrouillé jusqu’à son expiration ou sa révision.
- L’entrée d’inventaire est copiée comme référence, sans déplacer l’objet.
- La révision du contexte de prix reste traçable dans l’offre.
- Une offre invalide n’est jamais enregistrée dans le dépôt.

## 18. Devis temporaire

> **[VSC] Visual Studio Code — Créer : `res://src/features/economy/domain/price_quote.gd`.**

```gdscript
class_name PriceQuote
extends RefCounted

var quote_id: StringName
var offer_id: StringName
var currency_id: StringName
var quantity: int = 0
var unit_price_minor: int = 0
var subtotal_minor: int = 0
var tax_minor: int = 0
var total_minor: int = 0
var seller_net_minor: int = 0
var expected_offer_revision: int = 0
var pricing_revision: int = 0
var valid_until_tick: int = 0
var tax_wallet_id: StringName

func validate(catalog: CurrencyCatalog) -> Error:
	if catalog == null:
		return ERR_UNCONFIGURED
	if not StableId.is_valid(quote_id) or not StableId.is_valid(offer_id):
		return ERR_INVALID_DATA
	if catalog.get_definition(currency_id) == null:
		return ERR_DOES_NOT_EXIST
	if quantity < 1 or unit_price_minor < 1:
		return ERR_INVALID_DATA
	if subtotal_minor < 1 or seller_net_minor != subtotal_minor:
		return ERR_INVALID_DATA
	if tax_minor < 0:
		return ERR_INVALID_DATA
	var checked_total: Variant = MoneyMath.checked_add(subtotal_minor, tax_minor)
	if checked_total == null or total_minor != int(checked_total):
		return ERR_INVALID_DATA
	if expected_offer_revision < 0 or pricing_revision < 0 or valid_until_tick < 0:
		return ERR_INVALID_DATA
	if tax_minor > 0 and not StableId.is_valid(tax_wallet_id):
		return ERR_INVALID_DATA
	if tax_minor == 0 and not tax_wallet_id.is_empty():
		return ERR_INVALID_DATA
	return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le vendeur reçoit le sous-total ; la taxe éventuelle est créditée séparément.
- Le total payé est exactement la somme du sous-total et de la taxe.
- Le devis porte les révisions utilisées afin de diagnostiquer un refus obsolète.
- Il est temporaire et ne devient jamais la source d’autorité d’une sauvegarde.
- La validation structurelle ne remplace pas le recalcul par le service.

## 19. Offre de vente

> **[VSC] Visual Studio Code — Créer : `res://src/features/economy/domain/trade_offer_state.gd`.**

```gdscript
class_name TradeOfferState
extends RefCounted

var offer_id: StringName
var seller_wallet_id: StringName
var source_container_id: StringName
var source_entry: InventoryEntryRef
var item_definition_id: StringName
var currency_id: StringName
var unit_price_minor: int = 0
var remaining_quantity: int = 0
var minimum_quantity: int = 1
var valid_from_tick: int = 0
var expires_tick: int = 0
var active := true
var revision: int = 0
var pricing_revision: int = 0

func validate(currency_catalog: CurrencyCatalog) -> Error:
	if currency_catalog == null:
		return ERR_UNCONFIGURED
	if not StableId.is_valid(offer_id):
		return ERR_INVALID_DATA
	if not StableId.is_valid(seller_wallet_id):
		return ERR_INVALID_DATA
	if not StableId.is_valid(source_container_id):
		return ERR_INVALID_DATA
	if source_entry == null or source_entry.validate() != OK:
		return ERR_INVALID_DATA
	if not StableId.is_valid(item_definition_id):
		return ERR_INVALID_DATA
	var currency := currency_catalog.get_definition(currency_id)
	if currency == null or currency.validate() != OK:
		return ERR_DOES_NOT_EXIST
	if not currency.transferable:
		return ERR_UNAVAILABLE
	if unit_price_minor < 1 or unit_price_minor > currency.maximum_balance_minor:
		return ERR_INVALID_DATA
	if remaining_quantity < 0 or minimum_quantity < 1:
		return ERR_INVALID_DATA
	if active and remaining_quantity < minimum_quantity:
		return ERR_INVALID_DATA
	if valid_from_tick < 0 or expires_tick < valid_from_tick:
		return ERR_INVALID_DATA
	if revision < 0 or pricing_revision < 0:
		return ERR_INVALID_DATA
	if active and remaining_quantity == 0:
		return ERR_INVALID_DATA
	return OK

func is_available(quantity: int, logical_tick: int) -> bool:
	return (
		active
		and logical_tick >= valid_from_tick
		and logical_tick <= expires_tick
		and quantity >= minimum_quantity
		and quantity <= remaining_quantity
	)

func duplicate_detached() -> TradeOfferState:
	var copy := TradeOfferState.new()
	copy.offer_id = offer_id
	copy.seller_wallet_id = seller_wallet_id
	copy.source_container_id = source_container_id
	copy.source_entry = source_entry.duplicate_detached() if source_entry != null else null
	copy.item_definition_id = item_definition_id
	copy.currency_id = currency_id
	copy.unit_price_minor = unit_price_minor
	copy.remaining_quantity = remaining_quantity
	copy.minimum_quantity = minimum_quantity
	copy.valid_from_tick = valid_from_tick
	copy.expires_tick = expires_tick
	copy.active = active
	copy.revision = revision
	copy.pricing_revision = pricing_revision
	return copy
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- L’offre référence une entrée d’inventaire sans en devenir propriétaire.
- `remaining_quantity` limite l’engagement économique et est revalidé contre le stock réel par l’inventaire.
- Le prix unitaire est verrouillé pour la durée de l’offre.
- L’achat et la vente sont deux points de vue sur cette même opération bilatérale.
- L’expiration utilise des ticks logiques persistables.

## 20. Commande d’achat

> **[VSC] Visual Studio Code — Créer : `res://src/features/economy/domain/purchase_command.gd`.**

```gdscript
class_name PurchaseCommand
extends RefCounted

var transaction_id: StringName
var offer_id: StringName
var buyer_wallet_id: StringName
var buyer_destination_container_id: StringName
var quantity: int = 0
var expected_total_minor: int = 0
var expected_offer_revision: int = 0
var expected_buyer_wallet_revision: int = 0
var expected_seller_wallet_revision: int = 0
var expected_tax_wallet_revision: int = 0
var expected_source_container_revision: int = 0
var expected_destination_container_revision: int = 0
var expected_entry_revision: int = 0
var created_stack_id: StringName
var actor_character_id: StringName
var cause_id: StringName
var source_system_id: StringName
var logical_tick: int = 0
var command_fingerprint: String = ""

func validate() -> Error:
	if not StableId.is_valid(transaction_id) or not StableId.is_valid(offer_id):
		return ERR_INVALID_DATA
	if not StableId.is_valid(buyer_wallet_id):
		return ERR_INVALID_DATA
	if not StableId.is_valid(buyer_destination_container_id):
		return ERR_INVALID_DATA
	if quantity < 1 or quantity > 1000000:
		return ERR_INVALID_DATA
	if expected_total_minor < 1 or expected_total_minor > MoneyMath.MAX_SAFE_INTEGER:
		return ERR_INVALID_DATA
	if expected_offer_revision < 0:
		return ERR_INVALID_DATA
	if expected_buyer_wallet_revision < 0 or expected_seller_wallet_revision < 0:
		return ERR_INVALID_DATA
	if expected_tax_wallet_revision < 0:
		return ERR_INVALID_DATA
	if expected_source_container_revision < 0:
		return ERR_INVALID_DATA
	if expected_destination_container_revision < 0 or expected_entry_revision < 0:
		return ERR_INVALID_DATA
	if not created_stack_id.is_empty() and not StableId.is_valid(created_stack_id):
		return ERR_INVALID_DATA
	if not actor_character_id.is_empty() and not CharacterId.is_valid(actor_character_id):
		return ERR_INVALID_DATA
	if not StableId.is_valid(cause_id) or not StableId.is_valid(source_system_id):
		return ERR_INVALID_DATA
	if logical_tick < 0 or command_fingerprint.is_empty():
		return ERR_INVALID_DATA
	if command_fingerprint.length() > 128:
		return ERR_INVALID_DATA
	return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- La commande contient le total affiché afin que le service puisse refuser un prix changé.
- Elle ne contient ni delta de portefeuille, ni taxe calculée, ni propriété finale de l’objet.
- Les révisions protègent l’offre, chaque portefeuille, les deux conteneurs et l’entrée d’inventaire.
- `created_stack_id` est utilisé uniquement lorsqu’un lot doit être divisé par l’inventaire.
- L’empreinte est calculée depuis une représentation canonique avant l’appel du service.

## 21. Commande de récompense

> **[VSC] Visual Studio Code — Créer : `res://src/features/economy/domain/reward_command.gd`.**

```gdscript
class_name RewardCommand
extends RefCounted

var transaction_id: StringName
var issuer_wallet_id: StringName
var recipient_wallet_id: StringName
var amount: MoneyAmount
var expected_issuer_revision: int = 0
var expected_recipient_revision: int = 0
var cause_id: StringName
var source_system_id: StringName
var logical_tick: int = 0
var command_fingerprint: String = ""

func validate(currency_catalog: CurrencyCatalog) -> Error:
	if not StableId.is_valid(transaction_id):
		return ERR_INVALID_DATA
	if not StableId.is_valid(issuer_wallet_id):
		return ERR_INVALID_DATA
	if not StableId.is_valid(recipient_wallet_id):
		return ERR_INVALID_DATA
	if issuer_wallet_id == recipient_wallet_id:
		return ERR_INVALID_PARAMETER
	if amount == null or amount.validate(currency_catalog) != OK:
		return ERR_INVALID_DATA
	var currency := currency_catalog.get_definition(amount.currency_id)
	if currency == null or not currency.transferable:
		return ERR_UNAVAILABLE
	if amount.minor_units < 1:
		return ERR_INVALID_DATA
	if expected_issuer_revision < 0 or expected_recipient_revision < 0:
		return ERR_INVALID_DATA
	if not StableId.is_valid(cause_id) or not StableId.is_valid(source_system_id):
		return ERR_INVALID_DATA
	if logical_tick < 0 or command_fingerprint.is_empty():
		return ERR_INVALID_DATA
	if command_fingerprint.length() > 128:
		return ERR_INVALID_DATA
	return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Une récompense est un transfert entre deux portefeuilles, pas une augmentation isolée.
- Une trésorerie système peut jouer le rôle d’émetteur lorsqu’une règle crée de la monnaie.
- L’émetteur et le destinataire doivent être différents.
- Les mêmes règles de révision et d’idempotence s’appliquent aux achats et récompenses.
- Les objets de quête restent hors de cette commande.

## 22. Résultat métier

> **[VSC] Visual Studio Code — Créer : `res://src/features/economy/domain/economy_result.gd`.**

```gdscript
class_name EconomyResult
extends RefCounted

enum Status {
	COMMITTED,
	REPLAYED,
	REJECTED_INVALID_COMMAND,
	REJECTED_NOT_FOUND,
	REJECTED_UNAUTHORIZED,
	REJECTED_STALE_REVISION,
	REJECTED_PRICE_CHANGED,
	REJECTED_INSUFFICIENT_FUNDS,
	REJECTED_OFFER,
	REJECTED_INVENTORY,
	REJECTED_IDEMPOTENCY_CONFLICT,
	REJECTED_INTERNAL,
}

var status: Status = Status.REJECTED_INTERNAL
var transaction_id: StringName
var currency_id: StringName
var total_minor: int = 0
var affected_wallet_ids: Array[StringName] = []
var message: String = ""

func is_success() -> bool:
	return status in [Status.COMMITTED, Status.REPLAYED]

func validate() -> Error:
	if status < Status.COMMITTED or status > Status.REJECTED_INTERNAL:
		return ERR_INVALID_DATA
	if not transaction_id.is_empty() and not StableId.is_valid(transaction_id):
		return ERR_INVALID_DATA
	if total_minor < 0 or total_minor > MoneyMath.MAX_SAFE_INTEGER:
		return ERR_INVALID_DATA
	if total_minor > 0 and not StableId.is_valid(currency_id):
		return ERR_INVALID_DATA
	var seen: Dictionary[StringName, bool] = {}
	for wallet_id: StringName in affected_wallet_ids:
		if not StableId.is_valid(wallet_id) or seen.has(wallet_id):
			return ERR_INVALID_DATA
		seen[wallet_id] = true
	return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- `REPLAYED` signifie qu’une transaction identique était déjà committée ; aucun second débit n’est réalisé.
- Un conflit d’idempotence est distinct d’une révision obsolète.
- Le résultat expose seulement les identifiants et montants nécessaires à l’appelant.
- `is_success()` permet de traiter un replay comme un succès fonctionnel.
- Les refus ne contiennent aucun snapshot mutable.

## 23. Catalogues

> **[VSC] Visual Studio Code — Créer : `res://src/features/economy/application/currency_catalog.gd`.**

```gdscript
class_name CurrencyCatalog
extends RefCounted

var _definitions: Dictionary[StringName, CurrencyDefinition] = {}

func register(definition: CurrencyDefinition) -> Error:
	if definition == null or definition.validate() != OK:
		return ERR_INVALID_DATA
	if _definitions.has(definition.currency_id):
		return ERR_ALREADY_EXISTS
	_definitions[definition.currency_id] = definition.duplicate(true) as CurrencyDefinition
	return OK

func get_definition(currency_id: StringName) -> CurrencyDefinition:
	var stored := _definitions.get(currency_id) as CurrencyDefinition
	return null if stored == null else stored.duplicate(true) as CurrencyDefinition

func all_ids_sorted() -> Array[StringName]:
	var ids: Array[StringName] = []
	ids.assign(_definitions.keys())
	ids.sort()
	return ids
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le catalogue conserve des copies de définitions validées.
- Les lectures retournent également des copies afin de préserver l’immuabilité de conception.
- L’ordre trié facilite les snapshots et diagnostics reproductibles.
- Aucun portefeuille ou solde n’est stocké ici.
- Une devise inconnue est refusée avant le calcul d’un prix.

> **[VSC] Visual Studio Code — Créer : `res://src/features/economy/application/item_value_catalog.gd`.**

```gdscript
class_name ItemValueCatalog
extends RefCounted

var _by_item_definition: Dictionary[StringName, ItemValueDefinition] = {}

func register(
	definition: ItemValueDefinition,
	currency_catalog: CurrencyCatalog,
) -> Error:
	if definition == null or definition.validate(currency_catalog) != OK:
		return ERR_INVALID_DATA
	if _by_item_definition.has(definition.item_definition_id):
		return ERR_ALREADY_EXISTS
	_by_item_definition[definition.item_definition_id] = (
		definition.duplicate(true) as ItemValueDefinition
	)
	return OK

func get_for_item(item_definition_id: StringName) -> ItemValueDefinition:
	var stored := _by_item_definition.get(item_definition_id) as ItemValueDefinition
	return null if stored == null else stored.duplicate(true) as ItemValueDefinition
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Une définition d’objet possède au plus une valeur active dans ce catalogue pédagogique.
- Une production plus complexe pourra versionner des marchés sans modifier l’inventaire.
- L’enregistrement vérifie aussi la devise.
- La clé est l’identifiant de définition d’objet, jamais son nom affiché.
- Les copies profondes empêchent une offre de modifier la valeur source.

## 24. Dépôt économique

> **[LECTURE] Contrat du dépôt — Structure de référence.**

```gdscript
class_name EconomyRepository
extends RefCounted

func get_wallet(_wallet_id: StringName) -> WalletState:
	return null

func get_offer(_offer_id: StringName) -> TradeOfferState:
	return null

func find_result(
	_transaction_id: StringName,
	_command_fingerprint: String,
) -> EconomyResult:
	return null

func has_conflicting_fingerprint(
	_transaction_id: StringName,
	_command_fingerprint: String,
) -> bool:
	return false

func replace_prepared(_candidate: EconomyMutationCandidate) -> Error:
	return ERR_UNAVAILABLE

func replace_all(_prepared: Dictionary) -> Error:
	return ERR_UNAVAILABLE
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Les lectures renvoient des copies détachées.
- `find_result()` permet de restituer un résultat déjà committé.
- Un même identifiant associé à une autre empreinte produit un conflit contrôlé.
- Le dépôt ne calcule ni prix ni transfert d’objet.
- `replace_all()` est réservé à une restauration préparée complète.

## 25. Ports d’accès et de contexte

> **[VSC] Visual Studio Code — Créer : `res://src/features/economy/application/economy_access_port.gd`.**

```gdscript
class_name EconomyAccessPort
extends RefCounted

func can_purchase(
	command: PurchaseCommand,
	buyer_wallet: WalletState,
	seller_wallet: WalletState,
	offer: TradeOfferState,
) -> Error:
	return ERR_UNAVAILABLE

func can_reward(
	command: RewardCommand,
	issuer_wallet: WalletState,
	recipient_wallet: WalletState,
) -> Error:
	return ERR_UNAVAILABLE
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le port vérifie que l’acteur et le système source peuvent demander l’opération.
- Il ne modifie aucun solde.
- Une future règle politique ou judiciaire pourra adapter cette frontière.
- L’économie continue de valider prix, fonds, révisions et équilibre après l’autorisation.
- `ERR_UNAUTHORIZED` devient un refus métier, les autres codes inattendus une panne interne.

> **[VSC] Visual Studio Code — Créer : `res://src/features/economy/application/pricing_context_port.gd`.**

```gdscript
class_name PricingContextPort
extends RefCounted

func snapshot_for_offer(
	_offer: TradeOfferState,
	_buyer_wallet: WalletState,
	_logical_tick: int,
) -> PricingContext:
	return null
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le port agrège des indices autorisés sans exposer les dépôts sociaux ou écologiques.
- `null` signifie qu’aucun contexte fiable n’est disponible.
- Le service vérifie la révision et l’échéance du contexte.
- Une sortie IA ne peut pas construire directement ce snapshot.
- Le prix reste calculé par la politique économique.

## 26. Candidat économique

> **[VSC] Visual Studio Code — Créer : `res://src/features/economy/application/economy_mutation_candidate.gd`.**

```gdscript
class_name EconomyMutationCandidate
extends RefCounted

var transaction_id: StringName
var command_fingerprint: String = ""
var wallets: Dictionary[StringName, WalletState] = {}
var offer: TradeOfferState
var ledger_record: EconomyLedgerRecord
var result: EconomyResult
var expected_revisions: Dictionary[StringName, int] = {}

func validate(
	currency_catalog: CurrencyCatalog,
) -> Error:
	if currency_catalog == null:
		return ERR_UNCONFIGURED
	if not StableId.is_valid(transaction_id) or command_fingerprint.is_empty():
		return ERR_INVALID_DATA
	if wallets.size() < 2 or wallets.size() > 16:
		return ERR_INVALID_DATA
	for wallet: WalletState in wallets.values():
		if wallet == null or wallet.validate(currency_catalog) != OK:
			return ERR_INVALID_DATA
	if offer != null and offer.validate(currency_catalog) != OK:
		return ERR_INVALID_DATA
	if ledger_record == null or ledger_record.validate(currency_catalog) != OK:
		return ERR_INVALID_DATA
	if ledger_record.transaction_id != transaction_id:
		return ERR_INVALID_DATA
	if ledger_record.command_fingerprint != command_fingerprint:
		return ERR_INVALID_DATA
	if result == null or result.validate() != OK:
		return ERR_INVALID_DATA
	if result.transaction_id != transaction_id:
		return ERR_INVALID_DATA
	var posted_wallets: Dictionary[StringName, bool] = {}
	for posting: EconomyPosting in ledger_record.postings:
		if not wallets.has(posting.wallet_id):
			return ERR_INVALID_DATA
		var posted_wallet: WalletState = wallets[posting.wallet_id]
		if posted_wallet.balance_for(posting.currency_id) != posting.resulting_balance_minor:
			return ERR_INVALID_DATA
		posted_wallets[posting.wallet_id] = true
	for wallet_id: StringName in wallets:
		if not posted_wallets.has(wallet_id):
			return ERR_INVALID_DATA
		if not expected_revisions.has(wallet_id):
			return ERR_INVALID_DATA
	if offer != null and not expected_revisions.has(offer.offer_id):
		return ERR_INVALID_DATA
	if result.affected_wallet_ids.size() != wallets.size():
		return ERR_INVALID_DATA
	for wallet_id: StringName in result.affected_wallet_ids:
		if not wallets.has(wallet_id):
			return ERR_INVALID_DATA
	for aggregate_id: StringName in expected_revisions:
		if not StableId.is_valid(aggregate_id):
			return ERR_INVALID_DATA
		if expected_revisions[aggregate_id] < 0:
			return ERR_INVALID_DATA
	return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le candidat regroupe portefeuilles, offre, journal, résultat et révisions.
- Le résultat idempotent est enregistré dans le même lot que les mutations.
- Chaque écriture est recoupée avec le solde candidat du portefeuille visé.
- Une récompense peut laisser `offer` à `null`.
- Tous les portefeuilles sont revalidés contre les devises.
- Aucun état actif n’est modifié par la validation.

## 27. Construire les écritures d’un paiement

> **[LECTURE] Préparation monétaire — Fonction interne de `EconomyService`.**

```gdscript
func _prepare_payment(
	command: PurchaseCommand,
	quote: PriceQuote,
	buyer: WalletState,
	seller: WalletState,
	tax_wallet: WalletState,
) -> EconomyMutationCandidate:
	if buyer.wallet_id == seller.wallet_id:
		return null
	if tax_wallet != null and tax_wallet.wallet_id in [buyer.wallet_id, seller.wallet_id]:
		return null
	if buyer.balance_for(quote.currency_id) < quote.total_minor:
		return null

	var buyer_candidate := buyer.duplicate_detached()
	var seller_candidate := seller.duplicate_detached()
	var buyer_balance := buyer.balance_for(quote.currency_id) - quote.total_minor
	var seller_balance_value: Variant = MoneyMath.checked_add(
		seller.balance_for(quote.currency_id),
		quote.seller_net_minor,
	)
	if seller_balance_value == null:
		return null
	buyer_candidate.balances[quote.currency_id] = buyer_balance
	seller_candidate.balances[quote.currency_id] = int(seller_balance_value)
	buyer_candidate.revision += 1
	seller_candidate.revision += 1
	buyer_candidate.posting_sequence += 1
	seller_candidate.posting_sequence += 1

	var candidate := EconomyMutationCandidate.new()
	candidate.transaction_id = command.transaction_id
	candidate.command_fingerprint = command.command_fingerprint
	candidate.wallets[buyer.wallet_id] = buyer_candidate
	candidate.wallets[seller.wallet_id] = seller_candidate
	candidate.expected_revisions[buyer.wallet_id] = command.expected_buyer_wallet_revision
	candidate.expected_revisions[seller.wallet_id] = command.expected_seller_wallet_revision

	var postings: Array[EconomyPosting] = []
	postings.append(_posting(
		command, 0, buyer_candidate, quote.currency_id, -quote.total_minor
	))
	postings.append(_posting(
		command, 1, seller_candidate, quote.currency_id, quote.seller_net_minor
	))
	if quote.tax_minor > 0:
		if tax_wallet == null:
			return null
		var tax_candidate := tax_wallet.duplicate_detached()
		var tax_balance_value: Variant = MoneyMath.checked_add(
			tax_wallet.balance_for(quote.currency_id),
			quote.tax_minor,
		)
		if tax_balance_value == null:
			return null
		tax_candidate.balances[quote.currency_id] = int(tax_balance_value)
		tax_candidate.revision += 1
		tax_candidate.posting_sequence += 1
		candidate.wallets[tax_wallet.wallet_id] = tax_candidate
		candidate.expected_revisions[tax_wallet.wallet_id] = (
			command.expected_tax_wallet_revision
		)
		postings.append(_posting(
			command, 2, tax_candidate, quote.currency_id, quote.tax_minor
		))

	candidate.ledger_record = _ledger_record(command, postings)
	return candidate
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Les soldes sont modifiés uniquement sur des copies.
- Le débit de l’acheteur couvre le sous-total et la taxe.
- Le vendeur reçoit le sous-total, tandis que le portefeuille fiscal reçoit la taxe.
- La somme des écritures reste nulle dans la devise du devis.
- Les révisions attendues sont conservées pour le commit final.

## 28. Construire un devis

> **[LECTURE] Calcul contrôlé — Fonction interne de `EconomyService`.**

```gdscript
func _build_quote(
	command: PurchaseCommand,
	offer: TradeOfferState,
	context: PricingContext,
) -> PriceQuote:
	if not offer.is_available(command.quantity, command.logical_tick):
		return null
	if context == null or context.validate() != OK:
		return null
	if command.logical_tick > context.valid_until_tick:
		return null

	var subtotal_value: Variant = MoneyMath.checked_multiply(
		offer.unit_price_minor,
		command.quantity,
	)
	if subtotal_value == null:
		return null
	var tax_value: Variant = MoneyMath.multiply_basis_points(
		int(subtotal_value),
		context.tax_basis_points,
	)
	if tax_value == null:
		return null
	var total_value: Variant = MoneyMath.checked_add(
		int(subtotal_value),
		int(tax_value),
	)
	if total_value == null:
		return null

	var quote := PriceQuote.new()
	quote.quote_id = EconomyId.quote(command.transaction_id, offer.revision)
	quote.offer_id = offer.offer_id
	quote.currency_id = offer.currency_id
	quote.quantity = command.quantity
	quote.unit_price_minor = offer.unit_price_minor
	quote.subtotal_minor = int(subtotal_value)
	quote.tax_minor = int(tax_value)
	quote.total_minor = int(total_value)
	quote.seller_net_minor = int(subtotal_value)
	quote.expected_offer_revision = offer.revision
	quote.pricing_revision = context.revision
	quote.valid_until_tick = min(offer.expires_tick, context.valid_until_tick)
	quote.tax_wallet_id = context.tax_wallet_id
	return quote
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- L’offre vérifie d’abord quantité et intervalle logique.
- Le sous-total utilise une multiplication entière bornée.
- La taxe est calculée en points de base avec le même arrondi déterministe.
- Le devis expire au premier terme entre l’offre et le contexte.
- Le total attendu de la commande sera comparé à `quote.total_minor` par le service.

## 29. Frontière avec l’inventaire

> **[VSC] Visual Studio Code — Créer : `res://src/features/economy/application/economy_inventory_trade_port.gd`.**

```gdscript
class_name EconomyInventoryTradePort
extends RefCounted

class PreparedTrade:
	extends RefCounted

	var authority_id: StringName = &"inventory"
	var payload: Dictionary = {}

	func validate() -> Error:
		if authority_id != &"inventory":
			return ERR_INVALID_DATA
		return OK if not payload.is_empty() else ERR_INVALID_DATA

func prepare_purchase_transfer(
	_offer: TradeOfferState,
	_command: PurchaseCommand,
) -> PreparedTrade:
	return null
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le port demande à l’inventaire de préparer source, destination, quantité, propriété et éventuelle division de pile.
- Le payload opaque est construit par un adaptateur fiable, jamais par le joueur.
- L’économie ne modifie ni `ItemInstanceState`, ni `ItemStackState`, ni conteneur.
- Les révisions de la source, de la destination et de l’entrée sont portées par la commande puis relues par l’adaptateur.
- `null` représente un refus contrôlé de l’inventaire.

> **[VSC] Visual Studio Code — Créer : `res://src/features/economy/application/economy_transaction_commit_port.gd`.**

```gdscript
class_name EconomyTransactionCommitPort
extends RefCounted

func commit(
	_economy_candidate: EconomyMutationCandidate,
	_inventory_candidate: EconomyInventoryTradePort.PreparedTrade = null,
) -> Error:
	return ERR_UNAVAILABLE
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- L’implémentation se trouve au point de composition et coordonne les dépôts propriétaires.
- Elle peut adapter le candidat d’inventaire à l’unité de travail introduite au chapitre 20.
- Toutes les révisions et absences de collision sont revalidées avant le premier remplacement.
- Une défaillance annule l’ensemble ; aucun débit ou objet partiel ne devient observable.
- Cette atomicité est une exigence à exécuter au chapitre 27, pas une preuve runtime ici.

## 30. Service d’achat

> **[VSC] Visual Studio Code — Créer : `res://src/features/economy/application/economy_service.gd`.**

```gdscript
class_name EconomyService
extends RefCounted

signal transaction_committed(result: EconomyResult)

var _currency_catalog: CurrencyCatalog
var _repository: EconomyRepository
var _access: EconomyAccessPort
var _pricing_context: PricingContextPort
var _inventory: EconomyInventoryTradePort
var _commit_port: EconomyTransactionCommitPort

func purchase(command: PurchaseCommand) -> EconomyResult:
	if command == null or command.validate() != OK:
		return _result(
			EconomyResult.Status.REJECTED_INVALID_COMMAND,
			command,
			"commande invalide",
		)
	if not _is_configured():
		return _result(
			EconomyResult.Status.REJECTED_INTERNAL,
			command,
			"services obligatoires indisponibles",
		)

	var previous := _repository.find_result(
		command.transaction_id,
		command.command_fingerprint,
	)
	if previous != null:
		previous.status = EconomyResult.Status.REPLAYED
		return previous
	if _repository.has_conflicting_fingerprint(
		command.transaction_id,
		command.command_fingerprint,
	):
		return _result(
			EconomyResult.Status.REJECTED_IDEMPOTENCY_CONFLICT,
			command,
			"identifiant réutilisé avec un autre contenu",
		)

	var prepared: Dictionary = _prepare_purchase(command)
	if prepared.is_empty():
		return _result(
			EconomyResult.Status.REJECTED_INTERNAL,
			command,
			"préparation impossible",
		)
	if prepared.has("result"):
		return prepared["result"] as EconomyResult

	var economy_candidate := prepared["economy"] as EconomyMutationCandidate
	var inventory_candidate := (
		prepared["inventory"] as EconomyInventoryTradePort.PreparedTrade
	)
	var commit_code := _commit_port.commit(economy_candidate, inventory_candidate)
	if commit_code != OK:
		return _commit_failure(command, commit_code)

	transaction_committed.emit(economy_candidate.result)
	return economy_candidate.result
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- L’idempotence est vérifiée avant toute lecture coûteuse ou préparation externe.
- Un retry identique renvoie le résultat antérieur en statut `REPLAYED`.
- `_prepare_purchase()` peut renvoyer un refus métier précis dans la clé `result`.
- Le port de commit reçoit les deux candidats préparés.
- Le signal est émis uniquement après succès du commit multi-autorités.

> **[LECTURE] Préparation complète — Suite de `economy_service.gd`.**

```gdscript
func _prepare_purchase(command: PurchaseCommand) -> Dictionary:
	var offer := _repository.get_offer(command.offer_id)
	if offer == null or offer.validate(_currency_catalog) != OK:
		return {"result": _result_not_found(command, "offre absente")}
	if offer.revision != command.expected_offer_revision:
		return {"result": _result_stale(command, "offre obsolète")}
	if not offer.is_available(command.quantity, command.logical_tick):
		return {"result": _result_offer(command, "offre indisponible")}

	var buyer := _repository.get_wallet(command.buyer_wallet_id)
	var seller := _repository.get_wallet(offer.seller_wallet_id)
	if buyer == null or seller == null:
		return {"result": _result_not_found(command, "portefeuille absent")}
	if buyer.revision != command.expected_buyer_wallet_revision:
		return {"result": _result_stale(command, "acheteur obsolète")}
	if seller.revision != command.expected_seller_wallet_revision:
		return {"result": _result_stale(command, "vendeur obsolète")}

	var access_code := _access.can_purchase(command, buyer, seller, offer)
	if access_code == ERR_UNAUTHORIZED:
		return {"result": _result_unauthorized(command)}
	if access_code != OK:
		return {"result": _result_internal(command, error_string(access_code))}

	var context := _pricing_context.snapshot_for_offer(
		offer,
		buyer,
		command.logical_tick,
	)
	var quote := _build_quote(command, offer, context)
	if quote == null or quote.validate(_currency_catalog) != OK:
		return {"result": _result_offer(command, "devis indisponible")}
	if quote.total_minor != command.expected_total_minor:
		return {"result": _result_price_changed(command, quote)}

	var tax_wallet: WalletState = null
	if quote.tax_minor > 0:
		tax_wallet = _repository.get_wallet(quote.tax_wallet_id)
		if tax_wallet == null:
			return {"result": _result_internal(command, "trésorerie absente")}
		if tax_wallet.wallet_id in [buyer.wallet_id, seller.wallet_id]:
			return {"result": _result_internal(command, "trésorerie non distincte")}
		if tax_wallet.revision != command.expected_tax_wallet_revision:
			return {"result": _result_stale(command, "trésorerie obsolète")}

	if buyer.balance_for(quote.currency_id) < quote.total_minor:
		return {"result": _result_insufficient(command, quote)}
	var economy_candidate := _prepare_payment(
		command,
		quote,
		buyer,
		seller,
		tax_wallet,
	)
	if economy_candidate == null:
		return {"result": _result_internal(command, "préparation monétaire invalide")}

	var offer_candidate := offer.duplicate_detached()
	offer_candidate.remaining_quantity -= command.quantity
	offer_candidate.revision += 1
	if offer_candidate.remaining_quantity < offer_candidate.minimum_quantity:
		offer_candidate.active = false
	economy_candidate.offer = offer_candidate
	economy_candidate.expected_revisions[offer.offer_id] = offer.revision
	economy_candidate.result = _committed_result(command, quote, economy_candidate)

	var inventory_candidate := _inventory.prepare_purchase_transfer(
		offer,
		command,
	)
	if inventory_candidate == null or inventory_candidate.validate() != OK:
		return {"result": _result_inventory(command)}
	if economy_candidate.validate(_currency_catalog) != OK:
		return {"result": _result_internal(command, "candidat économique invalide")}
	return {
		"economy": economy_candidate,
		"inventory": inventory_candidate,
	}
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- L’ordre de lecture empêche de préparer un paiement pour une offre inconnue ou obsolète.
- Le service recalcule le devis après autorisation et compare le total affiché.
- Le portefeuille fiscal est facultatif et revalidé seulement lorsqu’une taxe existe.
- L’offre est décrémentée sur une copie et désactivée dès que le reliquat devient inférieur à la quantité minimale.
- Le candidat économique n’atteint le commit qu’après validation du candidat d’inventaire.

### 30.1 Fabriques internes et résultats précis

> **[LECTURE] Helpers de service — Suite de `economy_service.gd`.**

```gdscript
func _is_configured() -> bool:
	return (
		_currency_catalog != null
		and _repository != null
		and _access != null
		and _pricing_context != null
		and _inventory != null
		and _commit_port != null
	)

func _posting(
	command: PurchaseCommand,
	index: int,
	wallet: WalletState,
	currency_id: StringName,
	delta: int,
) -> EconomyPosting:
	var posting := EconomyPosting.new()
	posting.posting_id = EconomyId.posting(command.transaction_id, index)
	posting.wallet_id = wallet.wallet_id
	posting.currency_id = currency_id
	posting.delta_minor_units = delta
	posting.resulting_balance_minor = wallet.balance_for(posting.currency_id)
	return posting

func _ledger_record(
	command: PurchaseCommand,
	postings: Array[EconomyPosting],
) -> EconomyLedgerRecord:
	var record := EconomyLedgerRecord.new()
	record.transaction_id = command.transaction_id
	record.cause_id = command.cause_id
	record.source_system_id = command.source_system_id
	record.logical_tick = command.logical_tick
	record.command_fingerprint = command.command_fingerprint
	for posting: EconomyPosting in postings:
		record.postings.append(posting.duplicate_detached())
	return record

func _result(
	status: EconomyResult.Status,
	command: PurchaseCommand,
	message: String,
	currency_id: StringName = &"",
	total_minor: int = 0,
) -> EconomyResult:
	var result := EconomyResult.new()
	result.status = status
	result.message = message
	result.currency_id = currency_id
	result.total_minor = total_minor
	if command != null:
		result.transaction_id = command.transaction_id
	return result

func _result_not_found(command: PurchaseCommand, message: String) -> EconomyResult:
	return _result(EconomyResult.Status.REJECTED_NOT_FOUND, command, message)

func _result_stale(command: PurchaseCommand, message: String) -> EconomyResult:
	return _result(EconomyResult.Status.REJECTED_STALE_REVISION, command, message)

func _result_offer(command: PurchaseCommand, message: String) -> EconomyResult:
	return _result(EconomyResult.Status.REJECTED_OFFER, command, message)

func _result_unauthorized(command: PurchaseCommand) -> EconomyResult:
	return _result(EconomyResult.Status.REJECTED_UNAUTHORIZED, command, "achat non autorisé")

func _result_internal(command: PurchaseCommand, message: String) -> EconomyResult:
	return _result(EconomyResult.Status.REJECTED_INTERNAL, command, message)

func _result_price_changed(command: PurchaseCommand, quote: PriceQuote) -> EconomyResult:
	return _result(
		EconomyResult.Status.REJECTED_PRICE_CHANGED,
		command,
		"prix modifié",
		quote.currency_id,
		quote.total_minor,
	)

func _result_insufficient(command: PurchaseCommand, quote: PriceQuote) -> EconomyResult:
	return _result(
		EconomyResult.Status.REJECTED_INSUFFICIENT_FUNDS,
		command,
		"fonds insuffisants",
		quote.currency_id,
		quote.total_minor,
	)

func _result_inventory(command: PurchaseCommand) -> EconomyResult:
	return _result(EconomyResult.Status.REJECTED_INVENTORY, command, "transfert refusé")

func _committed_result(
	command: PurchaseCommand,
	quote: PriceQuote,
	candidate: EconomyMutationCandidate,
) -> EconomyResult:
	var result := _result(
		EconomyResult.Status.COMMITTED,
		command,
		"achat committé",
		quote.currency_id,
		quote.total_minor,
	)
	result.affected_wallet_ids.assign(candidate.wallets.keys())
	result.affected_wallet_ids.sort()
	return result

func _commit_failure(command: PurchaseCommand, code: Error) -> EconomyResult:
	var status := EconomyResult.Status.REJECTED_INTERNAL
	if code == ERR_BUSY:
		status = EconomyResult.Status.REJECTED_STALE_REVISION
	elif code == ERR_UNAUTHORIZED:
		status = EconomyResult.Status.REJECTED_UNAUTHORIZED
	return _result(status, command, error_string(code))
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Les helpers centralisent les statuts sans masquer leur signification métier.
- `_posting()` reçoit la devise déjà validée et enregistre le solde candidat résultant sans nouvelle lecture du dépôt.
- Le journal copie les écritures pour ne conserver aucune référence mutable.
- Le résultat committé trie les portefeuilles afin de produire un ordre reproductible.
- `ERR_BUSY` et `ERR_UNAUTHORIZED` restent distingués d’une panne interne.

## 31. Récompenses monétaires

> **[VSC] Visual Studio Code — Créer : `res://src/features/economy/application/reward_service.gd`.**

```gdscript
class_name RewardService
extends RefCounted

signal reward_committed(result: EconomyResult)

var _currency_catalog: CurrencyCatalog
var _repository: EconomyRepository
var _access: EconomyAccessPort
var _commit_port: EconomyTransactionCommitPort

func _is_configured() -> bool:
	return (
		_currency_catalog != null
		and _repository != null
		and _access != null
		and _commit_port != null
	)

func transfer_reward(command: RewardCommand) -> EconomyResult:
	if not _is_configured():
		return _reward_internal(command, "services obligatoires indisponibles")
	if command == null or command.validate(_currency_catalog) != OK:
		return _invalid_reward(command)

	var previous := _repository.find_result(
		command.transaction_id,
		command.command_fingerprint,
	)
	if previous != null:
		previous.status = EconomyResult.Status.REPLAYED
		return previous
	if _repository.has_conflicting_fingerprint(
		command.transaction_id,
		command.command_fingerprint,
	):
		return _idempotency_conflict(command)

	var issuer := _repository.get_wallet(command.issuer_wallet_id)
	var recipient := _repository.get_wallet(command.recipient_wallet_id)
	if issuer == null or recipient == null:
		return _missing_wallet(command)
	if issuer.revision != command.expected_issuer_revision:
		return _stale_reward(command)
	if recipient.revision != command.expected_recipient_revision:
		return _stale_reward(command)
	var access_code := _access.can_reward(command, issuer, recipient)
	if access_code == ERR_UNAUTHORIZED:
		return _unauthorized_reward(command)
	if access_code != OK:
		return _reward_internal(command, error_string(access_code))

	if issuer.balance_for(command.amount.currency_id) < command.amount.minor_units:
		return _insufficient_reward(command)
	var candidate := _prepare_reward_candidate(command, issuer, recipient)
	if candidate == null:
		return _reward_internal(command, "préparation de récompense invalide")
	var code := _commit_port.commit(candidate)
	if code != OK:
		return _reward_commit_failure(command, code)
	reward_committed.emit(candidate.result)
	return candidate.result
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le service réutilise les mêmes contrats d’idempotence et de révision que l’achat.
- Une récompense purement monétaire passe `null` comme candidat d’inventaire.
- Le port de commit doit accepter ce cas sans perdre l’atomicité économique.
- L’émetteur doit disposer des fonds, y compris lorsqu’il s’agit d’une trésorerie système.
- Une récompense d’objet sera orchestrée avec un candidat d’inventaire par le chapitre narratif concerné.

### 31.1 Préparer une récompense équilibrée

> **[LECTURE] Helpers de récompense — Suite de `reward_service.gd`.**

```gdscript
func _prepare_reward_candidate(
	command: RewardCommand,
	issuer: WalletState,
	recipient: WalletState,
) -> EconomyMutationCandidate:
	var currency_id := command.amount.currency_id
	var amount_minor := command.amount.minor_units
	if issuer.balance_for(currency_id) < amount_minor:
		return null
	var issuer_candidate := issuer.duplicate_detached()
	var recipient_candidate := recipient.duplicate_detached()
	issuer_candidate.balances[currency_id] = (
		issuer.balance_for(currency_id) - amount_minor
	)
	var recipient_value: Variant = MoneyMath.checked_add(
		recipient.balance_for(currency_id),
		amount_minor,
	)
	if recipient_value == null:
		return null
	recipient_candidate.balances[currency_id] = int(recipient_value)
	issuer_candidate.revision += 1
	recipient_candidate.revision += 1
	issuer_candidate.posting_sequence += 1
	recipient_candidate.posting_sequence += 1

	var debit := EconomyPosting.new()
	debit.posting_id = EconomyId.posting(command.transaction_id, 0)
	debit.wallet_id = issuer.wallet_id
	debit.currency_id = currency_id
	debit.delta_minor_units = -amount_minor
	debit.resulting_balance_minor = issuer_candidate.balance_for(currency_id)
	var credit := EconomyPosting.new()
	credit.posting_id = EconomyId.posting(command.transaction_id, 1)
	credit.wallet_id = recipient.wallet_id
	credit.currency_id = currency_id
	credit.delta_minor_units = amount_minor
	credit.resulting_balance_minor = recipient_candidate.balance_for(currency_id)

	var record := EconomyLedgerRecord.new()
	record.transaction_id = command.transaction_id
	record.cause_id = command.cause_id
	record.source_system_id = command.source_system_id
	record.logical_tick = command.logical_tick
	record.command_fingerprint = command.command_fingerprint
	record.postings.append(debit)
	record.postings.append(credit)

	var result := EconomyResult.new()
	result.status = EconomyResult.Status.COMMITTED
	result.transaction_id = command.transaction_id
	result.currency_id = currency_id
	result.total_minor = amount_minor
	result.affected_wallet_ids.append(issuer.wallet_id)
	result.affected_wallet_ids.append(recipient.wallet_id)
	result.affected_wallet_ids.sort()
	result.message = "récompense committée"

	var candidate := EconomyMutationCandidate.new()
	candidate.transaction_id = command.transaction_id
	candidate.command_fingerprint = command.command_fingerprint
	candidate.wallets[issuer.wallet_id] = issuer_candidate
	candidate.wallets[recipient.wallet_id] = recipient_candidate
	candidate.ledger_record = record
	candidate.result = result
	candidate.expected_revisions[issuer.wallet_id] = command.expected_issuer_revision
	candidate.expected_revisions[recipient.wallet_id] = command.expected_recipient_revision
	return candidate if candidate.validate(_currency_catalog) == OK else null

func _reward_result(
	status: EconomyResult.Status,
	command: RewardCommand,
	message: String,
) -> EconomyResult:
	var result := EconomyResult.new()
	result.status = status
	result.message = message
	if command != null:
		result.transaction_id = command.transaction_id
		if command.amount != null:
			result.currency_id = command.amount.currency_id
			result.total_minor = command.amount.minor_units
	return result

func _invalid_reward(command: RewardCommand) -> EconomyResult:
	var result := EconomyResult.new()
	result.status = EconomyResult.Status.REJECTED_INVALID_COMMAND
	result.message = "commande invalide"
	if command != null and StableId.is_valid(command.transaction_id):
		result.transaction_id = command.transaction_id
	return result

func _idempotency_conflict(command: RewardCommand) -> EconomyResult:
	return _reward_result(EconomyResult.Status.REJECTED_IDEMPOTENCY_CONFLICT, command, "conflit d’idempotence")

func _missing_wallet(command: RewardCommand) -> EconomyResult:
	return _reward_result(EconomyResult.Status.REJECTED_NOT_FOUND, command, "portefeuille absent")

func _stale_reward(command: RewardCommand) -> EconomyResult:
	return _reward_result(EconomyResult.Status.REJECTED_STALE_REVISION, command, "révision obsolète")

func _unauthorized_reward(command: RewardCommand) -> EconomyResult:
	return _reward_result(EconomyResult.Status.REJECTED_UNAUTHORIZED, command, "récompense non autorisée")

func _insufficient_reward(command: RewardCommand) -> EconomyResult:
	return _reward_result(EconomyResult.Status.REJECTED_INSUFFICIENT_FUNDS, command, "trésorerie insuffisante")

func _reward_internal(command: RewardCommand, message: String) -> EconomyResult:
	return _reward_result(EconomyResult.Status.REJECTED_INTERNAL, command, message)

func _reward_commit_failure(command: RewardCommand, code: Error) -> EconomyResult:
	var status := EconomyResult.Status.REJECTED_INTERNAL
	if code == ERR_BUSY:
		status = EconomyResult.Status.REJECTED_STALE_REVISION
	return _reward_result(status, command, error_string(code))
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- L’émetteur est débité et le destinataire crédité sur des copies détachées.
- Les deux écritures sont égales et opposées dans la même devise.
- Le résultat, le journal et l’empreinte sont inclus dans le candidat idempotent.
- Les helpers conservent des refus précis pour commande, accès, fonds, révision et commit.
- La validation finale recoupe soldes candidats et écritures avant le port de commit.

## 32. Adapter une action d’agent

> **[VSC] Visual Studio Code — Créer : `res://src/features/economy/application/economy_agent_context_port.gd`.**

```gdscript
class_name EconomyAgentContextPort
extends RefCounted

class Context:
	extends RefCounted

	var wallet_id: StringName
	var wallet_revision: int = 0
	var seller_wallet_revision: int = 0
	var tax_wallet_revision: int = 0
	var offer_id: StringName
	var offer_revision: int = 0
	var displayed_total_minor: int = 0
	var destination_container_id: StringName
	var source_container_revision: int = 0
	var destination_container_revision: int = 0
	var entry_revision: int = 0
	var created_stack_id: StringName

	func validate() -> Error:
		if not StableId.is_valid(wallet_id) or wallet_revision < 0:
			return ERR_INVALID_DATA
		if seller_wallet_revision < 0 or tax_wallet_revision < 0:
			return ERR_INVALID_DATA
		if not StableId.is_valid(offer_id) or offer_revision < 0:
			return ERR_INVALID_DATA
		if displayed_total_minor < 1:
			return ERR_INVALID_DATA
		if not StableId.is_valid(destination_container_id):
			return ERR_INVALID_DATA
		if source_container_revision < 0 or destination_container_revision < 0:
			return ERR_INVALID_DATA
		if entry_revision < 0:
			return ERR_INVALID_DATA
		if not created_stack_id.is_empty() and not StableId.is_valid(created_stack_id):
			return ERR_INVALID_DATA
		return OK

func snapshot_for(
	_character_id: StringName,
	_offer_id: StringName,
) -> Context:
	return null
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le contexte fournit uniquement des identifiants, révisions et un total d’affichage.
- Il ne donne pas au planificateur un accès direct aux dépôts.
- L’agent devra encore soumettre une commande au même service que le joueur.
- Le total peut devenir obsolète et être refusé sans débit.
- Les révisions du vendeur, de la trésorerie éventuelle, de la source, de la destination et de l’entrée complètent la révision du portefeuille acheteur.

> **[VSC] Visual Studio Code — Créer : `res://src/features/economy/application/economy_agent_action_executor.gd`.**

```gdscript
class_name EconomyAgentActionExecutor
extends AgentActionExecutor

const EXECUTOR_KEY := &"agent.executor.purchase_offer"

var _service: EconomyService
var _context: EconomyAgentContextPort

func can_execute(request: AgentActionRequest) -> Error:
	if request == null or request.validate() != OK:
		return ERR_INVALID_DATA
	if request.executor_key != EXECUTOR_KEY:
		return ERR_UNAVAILABLE
	if _service == null or _context == null:
		return ERR_UNCONFIGURED
	return OK

func start(request: AgentActionRequest) -> Error:
	var check := can_execute(request)
	if check != OK:
		return check
	var context := _context.snapshot_for(
		request.owner_character_id,
		request.action_id,
	)
	if context == null or context.validate() != OK:
		return ERR_DOES_NOT_EXIST
	var command := _command_from_request(request, context)
	if command == null:
		return ERR_INVALID_DATA
	var result := _service.purchase(command)
	return OK if result.is_success() else ERR_CANT_RESOLVE
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- L’action de l’agent choisit une offre connue, pas un prix arbitraire.
- `_command_from_request()` calcule une identité et une empreinte canoniques à partir du contexte autorisé.
- Le service recalcule ensuite le devis et contrôle les révisions.
- Un refus provoque une nouvelle décision depuis un snapshot frais.
- L’agent ne peut ni créer de monnaie, ni contourner l’inventaire.

## 33. Présentation et interaction du joueur

L’interface peut afficher :

- le nom et le symbole localisés d’une devise ;
- le solde d’un portefeuille ;
- le prix unitaire ;
- la quantité ;
- le sous-total ;
- la taxe ou commission ;
- le total ;
- l’expiration logique d’une offre ;
- un message de prix changé ;
- le résultat committé ou rejoué.

Elle ne doit pas :

- additionner des `float` pour produire le prix ;
- écrire directement dans `balances` ;
- masquer une taxe dans un texte non structuré ;
- considérer un bouton confirmé comme un commit ;
- réutiliser une identité de transaction avec un contenu différent ;
- transférer l’objet avant le résultat économique.

> **[LECTURE] Séparation interface / autorité — Ne pas saisir.**

```text
interface :
- formate les unités mineures ;
- affiche un devis temporaire ;
- construit une commande typée ;
- attend EconomyResult.

service :
- relit offre, portefeuilles et révisions ;
- recalcule sous-total et taxe ;
- prépare les écritures équilibrées ;
- demande le transfert candidat à l’inventaire ;
- commit le lot et enregistre l’idempotence.
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le formatage localisé n’influence jamais les unités mineures stockées.
- Une confirmation visuelle reste une intention jusqu’au commit.
- Le service ne fait confiance ni au total affiché ni à l’état du widget.
- Le résultat de replay est affichable sans produire une seconde animation d’acquisition si la présentation l’a déjà consommé.
- Les règles économiques ne sont pas dupliquées dans l’interface.

## 34. Persistance

Sont persistés :

- portefeuilles, propriétaires, soldes, révisions et séquences ;
- offres actives ou expirées nécessaires au monde sauvegardé ;
- quantités économiques restantes et révisions d’offres ;
- records récents du journal ;
- identifiants, empreintes et résultats nécessaires à l’idempotence ;
- révision globale de l’économie ;
- séquence de transaction du monde.

Ne sont pas persistés :

- définitions de devises `.tres` ;
- valeurs de référence `.tres` ;
- contextes de prix ;
- devis temporaires ;
- formatage localisé ;
- caches de catalogue ;
- commandes en attente ;
- candidats économiques ou d’inventaire ;
- widgets, animations et sons ;
- prix affichés dérivés ;
- données d’objets déjà possédées par l’inventaire.

Le parcours Solo conserve un journal récent borné dans le snapshot. Le Mode Studio peut archiver un journal complet dans SQLite, sans faire de cette archive l’autorité du chargement d’une partie.

## 35. Codec strict

> **[VSC] Visual Studio Code — Créer : `res://src/features/economy/infrastructure/economy_snapshot_codec.gd`.**

```gdscript
class_name EconomySnapshotCodec
extends RefCounted

const FORMAT := "project-asteria-economy"
const VERSION := 1
const ROOT_KEYS := [
	"format",
	"version",
	"economy_revision",
	"transaction_sequence",
	"wallets",
	"offers",
	"ledger_records",
	"idempotency",
]

class DecodeResult:
	extends RefCounted

	var code: Error = FAILED
	var prepared: Dictionary = {}
	var message: String = ""

	func is_success() -> bool:
		return code == OK

func decode(
	document: Dictionary,
	currency_catalog: CurrencyCatalog,
) -> DecodeResult:
	if currency_catalog == null:
		return _failure(ERR_UNCONFIGURED, "catalogue absent")
	if not _has_exact_keys(document, ROOT_KEYS):
		return _failure(ERR_INVALID_DATA, "clés racine invalides")
	if typeof(document.get("format")) != TYPE_STRING:
		return _failure(ERR_INVALID_DATA, "format non textuel")
	if String(document.get("format")) != FORMAT:
		return _failure(ERR_FILE_UNRECOGNIZED, "format inconnu")
	var version_value := _read_int(document.get("version"), 1, VERSION)
	if version_value == null or int(version_value) != VERSION:
		return _failure(ERR_FILE_UNRECOGNIZED, "version inconnue")
	var prepared := _decode_all(document, currency_catalog)
	if prepared == null:
		return _failure(ERR_INVALID_DATA, "état économique invalide")
	if _validate_cross_references(prepared, currency_catalog) != OK:
		return _failure(ERR_INVALID_DATA, "références croisées invalides")
	var result := DecodeResult.new()
	result.code = OK
	result.prepared = prepared
	return result
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le codec exige le format, la version et exactement les clés prévues.
- Les entiers sont lus par la règle JSON sûre du chapitre 9.
- `_decode_all()` vérifie portefeuilles, offres, records et idempotence sans toucher au dépôt actif.
- Les références croisées contrôlent devises, portefeuilles des écritures et offres.
- Un document vide valide reste distinct d’un échec grâce à `DecodeResult`.

## 36. Section de sauvegarde

> **[VSC] Visual Studio Code — Créer : `res://src/features/economy/infrastructure/economy_save_section.gd`.**

```gdscript
class_name EconomySaveSection
extends SaveSection

var _repository: EconomyRepository
var _currency_catalog: CurrencyCatalog
var _codec := EconomySnapshotCodec.new()
var _prepared: Dictionary = {}
var _is_prepared := false

func section_id() -> StringName:
	return &"economy"

func prepare_restore(payload: Dictionary) -> Error:
	_prepared.clear()
	_is_prepared = false
	if _repository == null or _currency_catalog == null:
		return ERR_UNCONFIGURED
	var decoded := _codec.decode(payload, _currency_catalog)
	if not decoded.is_success():
		return decoded.code
	_prepared = decoded.prepared.duplicate(true)
	_is_prepared = true
	return OK

func apply_prepared() -> Error:
	if not _is_prepared:
		return ERR_UNCONFIGURED
	var code := _repository.replace_all(_prepared.duplicate(true))
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

**Explication détaillée du bloc :**

- La préparation décode et valide l’économie entière sans mutation active.
- Les données sont copiées avant stockage et application.
- Un échec d’une autre section permet au coordinateur d’appeler `cancel_restore()`.
- L’idempotence est restaurée avec les soldes afin qu’un retry après chargement reste sûr.
- Les catalogues de conception doivent être disponibles avant l’application.

## 37. Présentation après commit

> **[VSC] Visual Studio Code — Créer : `res://src/features/economy/presentation/economy_presentation_bridge.gd`.**

```gdscript
class_name EconomyPresentationBridge
extends Node

signal wallet_feedback_requested(wallet_id: StringName, total_minor: int)

var _seen_transactions: Dictionary[StringName, bool] = {}

func on_transaction_committed(result: EconomyResult) -> void:
	if result == null or result.validate() != OK or not result.is_success():
		return
	if _seen_transactions.has(result.transaction_id):
		return
	_seen_transactions[result.transaction_id] = true
	for wallet_id: StringName in result.affected_wallet_ids:
		wallet_feedback_requested.emit(wallet_id, result.total_minor)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le pont reçoit uniquement un résultat validé et committé ou rejoué.
- Le cache local évite de rejouer deux fois une animation pour le même identifiant pendant la session.
- Ce cache de présentation n’est pas persistant et n’assure pas l’idempotence métier.
- Le signal transporte des valeurs simples, pas un portefeuille mutable.
- Aucune mutation économique n’est réalisée dans un nœud.

## 38. Scène pédagogique

La scène `ch21_economy_demo.tscn` doit montrer :

1. une devise et deux portefeuilles valides ;
2. une offre de ration avec prix en unités mineures ;
3. un achat réussi qui débite, crédite et transfère l’objet ;
4. une taxe créditée dans une trésorerie ;
5. un solde insuffisant sans transfert d’objet ;
6. un prix modifié refusé avant débit ;
7. une révision d’offre obsolète ;
8. un retry identique renvoyé en `REPLAYED` ;
9. un identifiant réutilisé avec un autre contenu refusé ;
10. une récompense équilibrée depuis une trésorerie ;
11. une sauvegarde restaurant soldes, offres et idempotence.

## 39. Modes Solo et Studio

### 39.1 Mode Solo

- deux ou trois devises maximum ;
- catalogues `.tres` locaux ;
- portefeuilles et offres en mémoire ;
- journal récent borné ;
- politiques de prix déterministes ;
- transaction multi-autorités locale ;
- diagnostics lisibles ;
- aucune dette implicite.

### 39.2 Mode Studio

- catalogue de devises versionné ;
- valeurs et politiques revues par les concepteurs ;
- tests de propriété sur l’équilibre des écritures ;
- journal complet optionnel dans SQLite ;
- télémétrie des refus et changements de prix ;
- migrations explicites ;
- séparation entre équilibrage, domaine et présentation ;
- outils de détection d’inflation et de puits monétaires.

Le Mode Studio renforce l’observabilité. Il n’ajoute ni Service Locator ni Autoload universel.

## 40. Budgets, sécurité et diagnostics

Bornes pédagogiques :

| Élément | Borne |
|---|---:|
| devises actives | 64 |
| devises par portefeuille | 64 |
| écritures par transaction | 16 |
| offres actives | 4 096 |
| records récents dans un snapshot | 2 048 |
| identités d’idempotence récentes | 4 096 |
| multiplicateur de prix | 10 % à 500 % |
| taxe | 0 % à 100 % |

Ces valeurs devront être mesurées au chapitre 27.

Une commande externe doit :

- avoir une taille limitée avant parsing ;
- utiliser une identité de transaction stable ;
- porter une empreinte canonique ;
- référencer uniquement des portefeuilles et offres autorisés ;
- borner quantité, prix attendu et révisions ;
- être recalculée par l’autorité ;
- refuser tout montant flottant ou conversion silencieuse ;
- ne jamais choisir une classe, une méthode ou un chemin de script.

Journaliser :

- identité et empreinte de transaction ;
- cause et système source ;
- offre et quantité ;
- devise, sous-total, taxe et total ;
- révisions attendues et constatées ;
- identifiants des portefeuilles ;
- code de commit ;
- replay ou conflit d’idempotence.

Ne pas journaliser snapshots complets, données personnelles inutiles, secrets, texte génératif brut ou contenu de portefeuille non concerné.

## 41. Erreurs fréquentes et corrections

<!-- qa:error-correction-section -->

### 41.1 Utiliser un `float` pour la monnaie

**Symptôme ou risque :** des additions ou multiplications produisent des centimes fantômes et des résultats différents selon l’ordre des opérations.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
var price := 0.1 + 0.2
wallet.balance -= price
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** un nombre flottant ne représente pas exactement toutes les fractions décimales et le portefeuille perd son unité explicite.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var price_minor: int = 10 + 20
wallet_candidate.balances[currency_id] -= price_minor
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** les unités mineures entières produisent une arithmétique déterministe et sérialisable sans perte.

### 41.2 Modifier directement un portefeuille depuis l’interface

**Symptôme ou risque :** le bouton contourne autorisation, révisions, journal et idempotence.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
func _on_buy_pressed() -> void:
	player_wallet.balances[currency_id] -= displayed_total
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** un nœud de présentation devient une autorité économique mutable.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var result := economy_service.purchase(command)
show_result(result)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** l’interface soumet une commande puis consomme un résultat déjà validé.

### 41.3 Autoriser un solde négatif implicitement

**Symptôme ou risque :** un achat crée une dette sans règle de crédit, limite ou remboursement.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
buyer.balance -= total
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** aucun contrôle n’empêche le solde de passer sous zéro.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
if buyer.balance_for(currency_id) < total_minor:
	return insufficient_funds_result()
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** le modèle sans crédit refuse l’opération avant toute copie candidate.

### 41.4 Créer une récompense sans contrepartie

**Symptôme ou risque :** le journal n’explique pas l’origine de la monnaie et ne peut pas vérifier l’équilibre.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
recipient.balance += reward_minor
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la création monétaire est implicite et aucune écriture de débit ne l’autorise.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var command := build_reward_command(
	treasury_wallet_id,
	recipient_wallet_id,
	reward_amount,
)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** une trésorerie explicite finance la récompense et produit deux écritures équilibrées.

### 41.5 Faire confiance au total envoyé par le client

**Symptôme ou risque :** une commande modifiée achète un objet à un prix inférieur à l’offre.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
var total := command.expected_total_minor
apply_payment(total)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la valeur proposée devient autoritaire sans recalcul.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var quote := _build_quote(command, offer, pricing_context)
if quote.total_minor != command.expected_total_minor:
	return price_changed_result(quote)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** le service recalcule le montant et utilise le total proposé uniquement comme contrôle d’acceptation.

### 41.6 Transférer l’objet avant le paiement

**Symptôme ou risque :** un échec de débit laisse l’objet chez l’acheteur ou exige un rollback incomplet.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
inventory_service.transfer(item_command)
var payment_code := debit_buyer()
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** les deux autorités sont committées séquentiellement et peuvent diverger.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var inventory_candidate := inventory_port.prepare_purchase_transfer(...)
var economy_candidate := prepare_payment(...)
var code := trade_commit_port.commit(economy_candidate, inventory_candidate)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** paiement et transfert sont préparés puis remplacés comme un même lot.

### 41.7 Stocker le prix dans `ItemDefinition`

**Symptôme ou risque :** l’inventaire dépend de l’économie et une ressource partagée mélange identité d’objet et marché.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
item_definition.current_price = market_price
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** une donnée de conception de l’inventaire devient un état économique mutable.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var value_definition := item_value_catalog.get_for_item(
	item_definition.item_id,
)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** les valeurs économiques restent dans un catalogue séparé référencé par identifiant.

### 41.8 Retenter avec une nouvelle identité après un timeout visuel

**Symptôme ou risque :** une transaction déjà committée est débitée une seconde fois.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
if ui_timeout:
	command.transaction_id = EconomyId.transaction(new_uuid())
	economy_service.purchase(command, inventory_revision)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** le retry perd la clé d’idempotence de l’opération initiale.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
if ui_timeout:
	economy_service.purchase(original_command, inventory_revision)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la même identité et la même empreinte renvoient le résultat précédent sans second débit.

### 41.9 Convertir implicitement une devise

**Symptôme ou risque :** des soldes de monnaies différentes sont additionnés comme s’ils avaient la même valeur.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
var wealth := gold_balance + token_balance
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** aucune politique de change, date, taux ou arrondi n’existe.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var gold := MoneyAmount.new()
gold.currency_id = &"economy.currency.aster_mark"
gold.minor_units = gold_balance
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** chaque montant conserve sa devise et aucun total commun n’est calculé sans contrat de conversion explicite.

### 41.10 Laisser une sortie IA fixer un prix ou une récompense

**Symptôme ou risque :** un texte non autoritaire crée de la monnaie ou modifie le marché persistant.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
var price_minor := int(ai_response["fair_price"])
var reward_minor := int(ai_response["reward"])
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** une sortie générative choisit directement deux montants autoritaires.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var unit_price := pricing_policy.unit_price(value_definition, context, catalog)
var reward := reward_table.amount_for(validated_cause_id)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** des politiques déterministes et des causes validées produisent les montants ; l’IA peut seulement proposer un texte ou une catégorie filtrée.

## 42. Tests à préparer

### 42.1 Tests unitaires

- identifiants économiques ;
- définitions de devises ;
- montants et refus de mélange ;
- arithmétique bornée ;
- soldes non négatifs ;
- équilibre des écritures par devise ;
- multiplicateurs et arrondis ;
- validité des offres ;
- construction des devis ;
- idempotence et conflit d’empreinte ;
- codec strict.

### 42.2 Tests d’intégration

- achat simple ;
- achat taxé ;
- fonds insuffisants sans transfert ;
- transfert d’inventaire refusé sans débit ;
- commit atomique économie-inventaire ;
- offre épuisée ;
- prix changé ;
- révision obsolète ;
- retry identique ;
- récompense depuis une trésorerie ;
- action d’agent ;
- sauvegarde et restauration de l’idempotence.

### 42.3 Simulations

- 1, 8 et 64 devises ;
- 1, 1 024 et 4 096 offres actives ;
- 1, 100 et 2 048 records récents ;
- achats concurrents sur la même offre ;
- taxes à plusieurs niveaux ;
- prix aux bornes minimales et maximales ;
- 10 000 transactions avec vérification de l’équilibre ;
- retries après chargement ;
- économie hors écran pour plusieurs marchands.

## 43. Réserves runtime

Cette revue statique ne prouve pas :

- le passage de tous les extraits dans le parseur Godot 4.7.1 ;
- le comportement des dictionnaires typés dans toutes les signatures ;
- l’exactitude runtime des contrôles de dépassement sur toutes les bornes ;
- l’atomicité réelle du commit économie-inventaire ;
- l’adaptateur d’autorisation ;
- l’intégration des taxes futures ;
- l’exécution des actions d’agents ;
- l’instanciation de la scène pédagogique ;
- la tenue des budgets ;
- l’exécution du codec et d’une migration future ;
- le replay entre plateformes ou versions ;
- la génération d’un PDF intermédiaire.

## 44. Sources techniques

- [Godot 4.7 — `Resource`](https://docs.godotengine.org/en/4.7/classes/class_resource.html)
- [Godot 4.7 — `RefCounted`](https://docs.godotengine.org/en/4.7/classes/class_refcounted.html)
- [Godot 4.7 — `Array`](https://docs.godotengine.org/en/4.7/classes/class_array.html)
- [Godot 4.7 — `Dictionary`](https://docs.godotengine.org/en/4.7/classes/class_dictionary.html)
- [Godot 4.7 — `StringName`](https://docs.godotengine.org/en/4.7/classes/class_stringname.html)
- [Godot 4.7 — `Variant`](https://docs.godotengine.org/en/4.7/classes/class_variant.html)
- [Godot 4.7 — signaux](https://docs.godotengine.org/en/4.7/getting_started/step_by_step/signals.html)
- [Godot 4.7 — bases de GDScript et entier 64 bits](https://docs.godotengine.org/en/4.7/tutorials/scripting/gdscript/gdscript_basics.html)
- [Chapitre 7 — Données avec Resources, JSON et configurations](CHAPITRE-07-Donnees-avec-Resources-JSON-et-configurations.md)
- [Chapitre 8 — SQLite, migrations et données persistantes](CHAPITRE-08-SQLite-migrations-et-donnees-persistantes.md)
- [Chapitre 9 — Sauvegardes, chargements et compatibilité](CHAPITRE-09-Sauvegardes-chargements-et-compatibilite-des-versions.md)
- [Chapitre 14 — Personnages](CHAPITRE-14-Personnages.md)
- [Chapitre 15 — Relations sociales](CHAPITRE-15-Relations-sociales.md)
- [Chapitre 17 — Agents IA et comportements autonomes](CHAPITRE-17-Agents-IA-et-comportements-autonomes.md)
- [Chapitre 20 — Inventaire et réputation des objets](CHAPITRE-20-Inventaire-et-reputation-des-objets.md)

## 45. Synthèse opérationnelle pour Project Asteria

Le système économique de `Project Asteria` retient les décisions suivantes :

1. les devises sont des données de conception partagées et immuables ;
2. tous les montants utilisent des unités mineures entières ;
3. les calculs restent dans la plage JSON sûre du projet ;
4. un portefeuille possède des soldes non négatifs par devise ;
5. les écritures d’une transaction sont équilibrées séparément pour chaque devise ;
6. une récompense débite un portefeuille émetteur explicite ;
7. les valeurs d’objets restent séparées des `ItemDefinition` ;
8. les multiplicateurs utilisent des points de base et un ordre déterministe ;
9. une offre verrouille un prix unitaire pendant un intervalle logique ;
10. un devis est temporaire et recalculé au moment de l’achat ;
11. le total proposé par l’appelant n’est jamais autoritaire ;
12. paiement, taxe, offre et transfert d’objet sont préparés avant commit ;
13. l’inventaire conserve l’autorité sur les objets et leurs quantités ;
14. l’idempotence empêche un retry de produire un second débit ;
15. une sortie IA ne crée ni monnaie, ni prix, ni récompense ;
16. devis, contextes, commandes, candidats, caches et présentation sont exclus de la persistance.
