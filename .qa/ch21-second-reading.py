from pathlib import Path

path = Path("Livre-II/CHAPITRE-21-Economie.md")
text = path.read_text(encoding="utf-8")


def replace_once(old: str, new: str) -> None:
    global text
    if old not in text:
        raise SystemExit(f"missing replacement anchor: {old[:120]!r}")
    text = text.replace(old, new, 1)


def insert_before(anchor: str, addition: str) -> None:
    global text
    if anchor not in text:
        raise SystemExit(f"missing insertion anchor: {anchor[:120]!r}")
    text = text.replace(anchor, addition + anchor, 1)


replace_once(
    "│   ├── economy_trade_commit_port.gd\n",
    "│   ├── economy_transaction_commit_port.gd\n",
)
replace_once(
    "@export_range(1, 9007199254740991, 1) var maximum_balance_minor: int = 1000000000000",
    "@export var maximum_balance_minor: int = 1000000000000",
)
replace_once(
    "@export_range(1, 9007199254740991, 1) var base_unit_price_minor: int = 1\n@export_range(1, 9007199254740991, 1) var minimum_unit_price_minor: int = 1\n@export_range(1, 9007199254740991, 1) var maximum_unit_price_minor: int = 1000000000",
    "@export var base_unit_price_minor: int = 1\n@export var minimum_unit_price_minor: int = 1\n@export var maximum_unit_price_minor: int = 1000000000",
)
replace_once(
    "func validate(catalog: CurrencyCatalog) -> Error:\n\tif catalog == null or not StableId.is_valid(currency_id):\n\t\treturn ERR_UNCONFIGURED",
    "func validate(catalog: CurrencyCatalog) -> Error:\n\tif catalog == null:\n\t\treturn ERR_UNCONFIGURED\n\tif not StableId.is_valid(currency_id):\n\t\treturn ERR_INVALID_DATA",
)
replace_once(
    "\tif abs(delta_minor_units) > definition.maximum_balance_minor:\n\t\treturn ERR_INVALID_DATA",
    "\tif delta_minor_units < -definition.maximum_balance_minor:\n\t\treturn ERR_INVALID_DATA\n\tif delta_minor_units > definition.maximum_balance_minor:\n\t\treturn ERR_INVALID_DATA",
)
replace_once(
    "\tif subtotal_minor < 1 or seller_net_minor != subtotal_minor:\n\t\treturn ERR_INVALID_DATA\n\tif tax_minor < 0 or total_minor != subtotal_minor + tax_minor:\n\t\treturn ERR_INVALID_DATA",
    "\tif subtotal_minor < 1 or seller_net_minor != subtotal_minor:\n\t\treturn ERR_INVALID_DATA\n\tif tax_minor < 0:\n\t\treturn ERR_INVALID_DATA\n\tvar checked_total: Variant = MoneyMath.checked_add(subtotal_minor, tax_minor)\n\tif checked_total == null or total_minor != int(checked_total):\n\t\treturn ERR_INVALID_DATA",
)
replace_once(
    "\tif unit_price_minor < 1 or remaining_quantity < 0 or minimum_quantity < 1:\n\t\treturn ERR_INVALID_DATA\n\tif minimum_quantity > max(remaining_quantity, 1):\n\t\treturn ERR_INVALID_DATA",
    "\tif unit_price_minor < 1 or remaining_quantity < 0 or minimum_quantity < 1:\n\t\treturn ERR_INVALID_DATA\n\tif active and remaining_quantity < minimum_quantity:\n\t\treturn ERR_INVALID_DATA",
)
replace_once(
    "var expected_tax_wallet_revision: int = 0\nvar created_stack_id: StringName",
    "var expected_tax_wallet_revision: int = 0\nvar expected_source_container_revision: int = 0\nvar expected_destination_container_revision: int = 0\nvar expected_entry_revision: int = 0\nvar created_stack_id: StringName",
)
replace_once(
    "\tif expected_tax_wallet_revision < 0:\n\t\treturn ERR_INVALID_DATA\n\tif not created_stack_id.is_empty()",
    "\tif expected_tax_wallet_revision < 0:\n\t\treturn ERR_INVALID_DATA\n\tif expected_source_container_revision < 0:\n\t\treturn ERR_INVALID_DATA\n\tif expected_destination_container_revision < 0 or expected_entry_revision < 0:\n\t\treturn ERR_INVALID_DATA\n\tif not created_stack_id.is_empty()",
)
replace_once(
    "- Les révisions protègent l’offre et chaque portefeuille concerné.\n- `created_stack_id`",
    "- Les révisions protègent l’offre, chaque portefeuille, les deux conteneurs et l’entrée d’inventaire.\n- `created_stack_id`",
)
replace_once(
    "\tif total_minor < 0:\n\t\treturn ERR_INVALID_DATA\n\tvar seen:",
    "\tif total_minor < 0:\n\t\treturn ERR_INVALID_DATA\n\tif total_minor > 0 and not StableId.is_valid(currency_id):\n\t\treturn ERR_INVALID_DATA\n\tvar seen:",
)

factory = r'''### 17.1 Créer une offre verrouillée

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

'''
insert_before("## 18. Devis temporaire\n", factory)

replace_once(
    "\tif result == null or result.validate() != OK:\n\t\treturn ERR_INVALID_DATA\n\tfor aggregate_id:",
    "\tif result == null or result.validate() != OK:\n\t\treturn ERR_INVALID_DATA\n\tif result.transaction_id != transaction_id:\n\t\treturn ERR_INVALID_DATA\n\tvar posted_wallets: Dictionary[StringName, bool] = {}\n\tfor posting: EconomyPosting in ledger_record.postings:\n\t\tif not wallets.has(posting.wallet_id):\n\t\t\treturn ERR_INVALID_DATA\n\t\tvar posted_wallet: WalletState = wallets[posting.wallet_id]\n\t\tif posted_wallet.balance_for(posting.currency_id) != posting.resulting_balance_minor:\n\t\t\treturn ERR_INVALID_DATA\n\t\tposted_wallets[posting.wallet_id] = true\n\tfor wallet_id: StringName in wallets:\n\t\tif not posted_wallets.has(wallet_id):\n\t\t\treturn ERR_INVALID_DATA\n\tfor aggregate_id:",
)
replace_once(
    "- Le résultat idempotent est enregistré dans le même lot que les mutations.\n- Une récompense",
    "- Le résultat idempotent est enregistré dans le même lot que les mutations.\n- Chaque écriture est recoupée avec le solde candidat du portefeuille visé.\n- Une récompense",
)
replace_once(
    "\tif buyer.balance_for(quote.currency_id) < quote.total_minor:\n\t\treturn null\n\n\tvar buyer_candidate",
    "\tif buyer.wallet_id == seller.wallet_id:\n\t\treturn null\n\tif tax_wallet != null and tax_wallet.wallet_id in [buyer.wallet_id, seller.wallet_id]:\n\t\treturn null\n\tif buyer.balance_for(quote.currency_id) < quote.total_minor:\n\t\treturn null\n\n\tvar buyer_candidate",
)

old_port = r'''> **[VSC] Visual Studio Code — Créer : `res://src/features/economy/application/economy_inventory_trade_port.gd`.**

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
	_expected_inventory_revision: int,
) -> PreparedTrade:
	return null
```
'''
new_port = r'''> **[VSC] Visual Studio Code — Créer : `res://src/features/economy/application/economy_inventory_trade_port.gd`.**

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
'''
replace_once(old_port, new_port)
replace_once(
    "- La révision d’inventaire est relue par l’adaptateur avant la préparation.",
    "- Les révisions de la source, de la destination et de l’entrée sont portées par la commande puis relues par l’adaptateur.",
)
replace_once(
    "> **[VSC] Visual Studio Code — Créer : `res://src/features/economy/application/economy_trade_commit_port.gd`.**\n\n```gdscript\nclass_name EconomyTradeCommitPort",
    "> **[VSC] Visual Studio Code — Créer : `res://src/features/economy/application/economy_transaction_commit_port.gd`.**\n\n```gdscript\nclass_name EconomyTransactionCommitPort",
)
text = text.replace("EconomyTradeCommitPort", "EconomyTransactionCommitPort")

replace_once(
    "func purchase(\n\tcommand: PurchaseCommand,\n\texpected_inventory_revision: int,\n) -> EconomyResult:",
    "func purchase(command: PurchaseCommand) -> EconomyResult:",
)
replace_once(
    "\tvar prepared: Dictionary = _prepare_purchase(\n\t\tcommand,\n\t\texpected_inventory_revision,\n\t)",
    "\tvar prepared: Dictionary = _prepare_purchase(command)",
)
replace_once(
    "func _prepare_purchase(\n\tcommand: PurchaseCommand,\n\texpected_inventory_revision: int,\n) -> Dictionary:",
    "func _prepare_purchase(command: PurchaseCommand) -> Dictionary:",
)
replace_once(
    "\tvar inventory_candidate := _inventory.prepare_purchase_transfer(\n\t\toffer,\n\t\tcommand,\n\t\texpected_inventory_revision,\n\t)",
    "\tvar inventory_candidate := _inventory.prepare_purchase_transfer(\n\t\toffer,\n\t\tcommand,\n\t)",
)
replace_once(
    "\tif offer_candidate.remaining_quantity == 0:\n\t\toffer_candidate.active = false",
    "\tif offer_candidate.remaining_quantity < offer_candidate.minimum_quantity:\n\t\toffer_candidate.active = false",
)
replace_once(
    "\t\tif tax_wallet == null:\n\t\t\treturn {\"result\": _result_internal(command, \"trésorerie absente\")}\n\t\tif tax_wallet.revision",
    "\t\tif tax_wallet == null:\n\t\t\treturn {\"result\": _result_internal(command, \"trésorerie absente\")}\n\t\tif tax_wallet.wallet_id in [buyer.wallet_id, seller.wallet_id]:\n\t\t\treturn {\"result\": _result_internal(command, \"trésorerie non distincte\")}\n\t\tif tax_wallet.revision",
)

helpers = r'''### 30.1 Fabriques internes et résultats précis

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
	delta: int,
) -> EconomyPosting:
	var posting := EconomyPosting.new()
	posting.posting_id = EconomyId.posting(command.transaction_id, index)
	posting.wallet_id = wallet.wallet_id
	posting.currency_id = _repository.get_offer(command.offer_id).currency_id
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
- `_posting()` relit la devise de l’offre et enregistre le solde candidat résultant.
- Le journal copie les écritures pour ne conserver aucune référence mutable.
- Le résultat committé trie les portefeuilles afin de produire un ordre reproductible.
- `ERR_BUSY` et `ERR_UNAUTHORIZED` restent distingués d’une panne interne.

'''
insert_before("## 31. Récompenses monétaires\n", helpers)

replace_once(
    "\tif _access.can_reward(command, issuer, recipient) != OK:\n\t\treturn _unauthorized_reward(command)",
    "\tvar access_code := _access.can_reward(command, issuer, recipient)\n\tif access_code == ERR_UNAUTHORIZED:\n\t\treturn _unauthorized_reward(command)\n\tif access_code != OK:\n\t\treturn _reward_internal(command, error_string(access_code))",
)

reward_helpers = r'''### 31.1 Préparer une récompense équilibrée

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
	record.postings = [debit, credit]

	var result := EconomyResult.new()
	result.status = EconomyResult.Status.COMMITTED
	result.transaction_id = command.transaction_id
	result.currency_id = currency_id
	result.total_minor = amount_minor
	result.affected_wallet_ids = [issuer.wallet_id, recipient.wallet_id]
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
	return _reward_result(EconomyResult.Status.REJECTED_INVALID_COMMAND, command, "commande invalide")

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

'''
insert_before("## 32. Adapter une action d’agent\n", reward_helpers)

replace_once(
    "\tvar destination_container_id: StringName\n\tvar inventory_revision: int = 0",
    "\tvar destination_container_id: StringName\n\tvar source_container_revision: int = 0\n\tvar destination_container_revision: int = 0\n\tvar entry_revision: int = 0",
)
replace_once(
    "\t\tif not StableId.is_valid(destination_container_id):\n\t\t\treturn ERR_INVALID_DATA\n\t\treturn OK if inventory_revision >= 0 else ERR_INVALID_DATA",
    "\t\tif not StableId.is_valid(destination_container_id):\n\t\t\treturn ERR_INVALID_DATA\n\t\tif source_container_revision < 0 or destination_container_revision < 0:\n\t\t\treturn ERR_INVALID_DATA\n\t\treturn OK if entry_revision >= 0 else ERR_INVALID_DATA",
)
replace_once(
    "\tvar result := _service.purchase(command, context.inventory_revision)",
    "\tvar result := _service.purchase(command)",
)
replace_once(
    "- La révision d’inventaire protège le conteneur de destination.",
    "- Les trois révisions d’inventaire protègent la source, la destination et l’entrée.",
)
replace_once(
    "var result := economy_service.purchase(command, inventory_revision)",
    "var result := economy_service.purchase(command)",
)

path.write_text(text, encoding="utf-8")
