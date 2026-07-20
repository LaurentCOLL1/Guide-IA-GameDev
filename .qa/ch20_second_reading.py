from pathlib import Path

path = Path("Livre-II/CHAPITRE-20-Inventaire-et-reputation-des-objets.md")
text = path.read_text(encoding="utf-8")

replacements: list[tuple[str, str]] = [
    (
        "│   ├── inventory_durability_port.gd\n│   ├── item_reputation_policy.gd\n",
        "│   ├── inventory_durability_port.gd\n│   ├── inventory_agent_context_port.gd\n│   ├── item_factory.gd\n│   ├── item_reputation_policy.gd\n",
    ),
    (
        "\tif kind == Kind.NONE:\n\t\treturn OK if owner_id.is_empty() else ERR_INVALID_DATA\n\treturn OK if StableId.is_valid(owner_id) else ERR_INVALID_DATA\n",
        "\tif kind == Kind.NONE:\n\t\treturn OK if owner_id.is_empty() else ERR_INVALID_DATA\n\tif kind == Kind.CHARACTER:\n\t\treturn OK if CharacterId.is_valid(owner_id) else ERR_INVALID_DATA\n\treturn OK if StableId.is_valid(owner_id) else ERR_INVALID_DATA\n",
    ),
    (
        "var lot_id: StringName\nvar quantity: int = 0\nvar revision: int = 0\n",
        "var lot_id: StringName\nvar origin_cause_id: StringName\nvar origin_source_system_id: StringName\nvar created_tick: int = 0\nvar quantity: int = 0\nvar revision: int = 0\n",
    ),
    (
        "\tif not StableId.is_valid(container_id) or not StableId.is_valid(lot_id):\n\t\treturn ERR_INVALID_DATA\n",
        "\tif not StableId.is_valid(container_id) or not StableId.is_valid(lot_id):\n\t\treturn ERR_INVALID_DATA\n\tif not StableId.is_valid(origin_cause_id):\n\t\treturn ERR_INVALID_DATA\n\tif not StableId.is_valid(origin_source_system_id) or created_tick < 0:\n\t\treturn ERR_INVALID_DATA\n",
    ),
    (
        "\tcopy.lot_id = lot_id\n\tcopy.quantity = quantity\n",
        "\tcopy.lot_id = lot_id\n\tcopy.origin_cause_id = origin_cause_id\n\tcopy.origin_source_system_id = origin_source_system_id\n\tcopy.created_tick = created_tick\n\tcopy.quantity = quantity\n",
    ),
    (
        "- `lot_id` conserve une origine commune sans prétendre suivre chaque unité.\n",
        "- `lot_id`, la cause, le système source et le tick conservent l’origine commune sans prétendre suivre chaque unité.\n",
    ),
    (
        "\twhile recent_cause_ids.size() > MAX_RECENT_CAUSES:\n\t\trecent_cause_ids.pop_front()\n\treturn OK\n```\n",
        "\twhile recent_cause_ids.size() > MAX_RECENT_CAUSES:\n\t\trecent_cause_ids.pop_front()\n\treturn OK\n\nfunc duplicate_detached() -> ItemReputationState:\n\tvar copy := ItemReputationState.new()\n\tcopy.instance_id = instance_id\n\tcopy.renown = renown\n\tcopy.significant_event_count = significant_event_count\n\tcopy.last_event_tick = last_event_tick\n\tcopy.recent_cause_ids.assign(recent_cause_ids)\n\tcopy.revision = revision\n\treturn copy\n```\n",
    ),
    (
        "func validate(\n\tinstances: Dictionary[StringName, ItemInstanceState],\n\tcatalog: ItemCatalog,\n) -> Error:\n\tif not CharacterId.is_valid(character_id) or revision < 0:\n\t\treturn ERR_INVALID_DATA\n",
        "func validate_shape() -> Error:\n\tif not CharacterId.is_valid(character_id) or revision < 0:\n\t\treturn ERR_INVALID_DATA\n\tif slots.size() > 64:\n\t\treturn ERR_OUT_OF_MEMORY\n\tvar used_instances: Dictionary[StringName, bool] = {}\n\tfor slot_id: StringName in slots:\n\t\tvar instance_id: StringName = slots[slot_id]\n\t\tif not StableId.is_valid(slot_id) or not StableId.is_valid(instance_id):\n\t\t\treturn ERR_INVALID_DATA\n\t\tif used_instances.has(instance_id):\n\t\t\treturn ERR_ALREADY_EXISTS\n\t\tused_instances[instance_id] = true\n\treturn OK\n\nfunc validate(\n\tinstances: Dictionary[StringName, ItemInstanceState],\n\tcatalog: ItemCatalog,\n) -> Error:\n\tif validate_shape() != OK:\n\t\treturn ERR_INVALID_DATA\n",
    ),
    (
        "\tfor instance: ItemInstanceState in instances.values():\n\t\tvar definition := catalog.get_definition(instance.definition_id)\n\t\tif instance == null or instance.validate(definition) != OK:\n\t\t\treturn ERR_INVALID_DATA\n\tfor stack: ItemStackState in stacks.values():\n\t\tvar definition := catalog.get_definition(stack.definition_id)\n\t\tif stack == null or stack.validate(definition) != OK:\n\t\t\treturn ERR_INVALID_DATA\n\tfor record: ItemProvenanceRecord in provenance_records:\n",
        "\tfor instance: ItemInstanceState in instances.values():\n\t\tif instance == null:\n\t\t\treturn ERR_INVALID_DATA\n\t\tvar definition := catalog.get_definition(instance.definition_id)\n\t\tif instance.validate(definition) != OK:\n\t\t\treturn ERR_INVALID_DATA\n\tfor stack: ItemStackState in stacks.values():\n\t\tif stack == null:\n\t\t\treturn ERR_INVALID_DATA\n\t\tvar definition := catalog.get_definition(stack.definition_id)\n\t\tif stack.validate(definition) != OK:\n\t\t\treturn ERR_INVALID_DATA\n\tfor loadout: EquipmentLoadoutState in loadouts.values():\n\t\tif loadout == null or loadout.validate_shape() != OK:\n\t\t\treturn ERR_INVALID_DATA\n\tfor reputation: ItemReputationState in reputations.values():\n\t\tif reputation == null or not instances.has(reputation.instance_id):\n\t\t\treturn ERR_INVALID_DATA\n\t\tvar reputation_instance: ItemInstanceState = instances[reputation.instance_id]\n\t\tvar reputation_definition := catalog.get_definition(reputation_instance.definition_id)\n\t\tif reputation.validate(reputation_definition) != OK:\n\t\t\treturn ERR_INVALID_DATA\n\tfor record: ItemProvenanceRecord in provenance_records:\n",
    ),
    (
        "\tvar candidate := state.duplicate(true) as ItemReputationState\n",
        "\tvar candidate := state.duplicate_detached()\n",
    ),
    (
        "\tvar definition := _catalog.get_definition(instance.definition_id)\n\tif definition == null or slot_id not in definition.equipment_slot_ids:\n\t\treturn {}\n\tif instance.is_broken(definition):\n",
        "\tvar definition := _catalog.get_definition(instance.definition_id)\n\tif definition == null or slot_id not in definition.equipment_slot_ids:\n\t\treturn {}\n\tif instance.owner == null:\n\t\treturn {}\n\tif instance.owner.kind != ItemOwnerRef.Kind.CHARACTER:\n\t\treturn {}\n\tif instance.owner.owner_id != character_id:\n\t\treturn {}\n\tif not instance.equipped_by_character_id.is_empty():\n\t\treturn {}\n\tif instance.is_broken(definition):\n",
    ),
]

for old, new in replacements:
    if old not in text:
        raise SystemExit(f"replacement missing: {old[:100]!r}")
    text = text.replace(old, new, 1)

factory_anchor = "## 18. Commande de transfert\n"
factory_section = '''### 17.1 Fabrique d’instances et de lots

> **[VSC] Visual Studio Code — Créer : `res://src/features/inventory/application/item_factory.gd`.**

```gdscript
class_name ItemFactory
extends RefCounted

func create_instance(
	definition: ItemDefinition,
	instance_id: StringName,
	container_id: StringName,
	owner: ItemOwnerRef,
) -> ItemInstanceState:
	if definition == null or definition.validate() != OK:
		return null
	if definition.is_stackable():
		return null
	var state := ItemInstanceState.new()
	state.instance_id = instance_id
	state.definition_id = definition.item_id
	state.container_id = container_id
	state.owner = owner.duplicate_detached() if owner != null else null
	state.current_durability = definition.maximum_durability
	return state if state.validate(definition) == OK else null

func create_stack(
	definition: ItemDefinition,
	stack_id: StringName,
	container_id: StringName,
	owner: ItemOwnerRef,
	lot_id: StringName,
	quantity: int,
	origin_cause_id: StringName,
	origin_source_system_id: StringName,
	created_tick: int,
) -> ItemStackState:
	if definition == null or not definition.is_stackable():
		return null
	var state := ItemStackState.new()
	state.stack_id = stack_id
	state.definition_id = definition.item_id
	state.container_id = container_id
	state.owner = owner.duplicate_detached() if owner != null else null
	state.lot_id = lot_id
	state.origin_cause_id = origin_cause_id
	state.origin_source_system_id = origin_source_system_id
	state.created_tick = created_tick
	state.quantity = quantity
	return state if state.validate(definition) == OK else null
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- La fabrique choisit explicitement entre instance et lot.
- Une définition fongible ne peut devenir une instance individualisée sans une conversion métier distincte.
- La durabilité initiale d’une instance prend le maximum de la définition.
- Le lot reçoit immédiatement son origine et son tick logique.
- Chaque état est validé avant d’être renvoyé au service créateur.

'''
if factory_anchor not in text:
    raise SystemExit("factory anchor missing")
text = text.replace(factory_anchor, factory_section + factory_anchor, 1)

text = text.replace(
    "- La définition déclare les emplacements compatibles.\n",
    "- La forme du loadout est validée séparément avant les références croisées.\n- La définition déclare les emplacements compatibles.\n",
    1,
)
text = text.replace(
    "- Les collections contiennent des copies détachées.\n",
    "- Les collections contiennent des copies détachées.\n- Les loadouts sont contrôlés structurellement ; les références complètes sont revalidées par l’unité de travail avec le dépôt frais.\n",
    1,
)
text = text.replace(
    "- L’instance, la définition et le loadout sont relus avant préparation.\n",
    "- L’instance, la définition, la propriété et le loadout sont relus avant préparation.\n",
    1,
)

path.write_text(text, encoding="utf-8")
