from collections import Counter
from pathlib import Path

TIMESTAMP = "2026-07-20T17:50:09+02:00"
BASE_COMMIT = "ce4e5e48e3659f0de2ffcfffede4b9c2dbe7ecd4"
CHAPTER_PATH = Path("Livre-II/CHAPITRE-20-Inventaire-et-reputation-des-objets.md")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise SystemExit(f"missing replacement for {label}: {old[:120]!r}")
    return text.replace(old, new, 1)


chapter = CHAPTER_PATH.read_text(encoding="utf-8")
chapter = replace_once(
    chapter,
    'last-verified: "2026-07-20T17:32:42+02:00"',
    f'last-verified: "{TIMESTAMP}"',
    "chapter last verified",
)
chapter = replace_once(
    chapter,
    'audit-date: "2026-07-20T17:32:42+02:00"',
    f'audit-date: "{TIMESTAMP}"',
    "chapter audit date",
)
chapter = replace_once(
    chapter,
    "│   ├── inventory_mutation_unit_of_work.gd\n│   ├── inventory_ability_grant_port.gd\n",
    "│   ├── inventory_mutation_unit_of_work.gd\n│   ├── inventory_access_port.gd\n│   ├── inventory_ability_grant_port.gd\n",
    "architecture access port",
)
chapter = replace_once(
    chapter,
    "var quantity: int = 1\nvar source_container_id: StringName\n",
    "var quantity: int = 1\nvar created_stack_id: StringName\nvar source_container_id: StringName\n",
    "created stack id field",
)
chapter = replace_once(
    chapter,
    "\tif quantity < 1:\n\t\treturn ERR_INVALID_DATA\n\tif not StableId.is_valid(source_container_id):\n",
    "\tif quantity < 1:\n\t\treturn ERR_INVALID_DATA\n\tif not created_stack_id.is_empty() and not StableId.is_valid(created_stack_id):\n\t\treturn ERR_INVALID_DATA\n\tif not StableId.is_valid(source_container_id):\n",
    "created stack id validation",
)
chapter = replace_once(
    chapter,
    "- La commande identifie explicitement source, destination, entrée et quantité.\n",
    "- La commande identifie explicitement source, destination, entrée et quantité.\n- `created_stack_id` est fourni par l’appelant uniquement lorsqu’un transfert partiel doit créer une nouvelle pile.\n",
    "command explanation",
)

old_merge = '''func can_merge_with(other: ItemStackState) -> bool:
\tif other == null:
\t\treturn false
\treturn (
\t\tdefinition_id == other.definition_id
\t\tand lot_id == other.lot_id
\t\tand owner.kind == other.owner.kind
\t\tand owner.owner_id == other.owner.owner_id
\t)
'''
new_merge = '''func can_merge_with(other: ItemStackState) -> bool:
\tif other == null or owner == null or other.owner == null:
\t\treturn false
\treturn (
\t\tdefinition_id == other.definition_id
\t\tand lot_id == other.lot_id
\t\tand origin_cause_id == other.origin_cause_id
\t\tand origin_source_system_id == other.origin_source_system_id
\t\tand created_tick == other.created_tick
\t\tand owner.kind == other.owner.kind
\t\tand owner.owner_id == other.owner.owner_id
\t)
'''
chapter = replace_once(chapter, old_merge, new_merge, "stack merge compatibility")
chapter = replace_once(
    chapter,
    "- Deux piles ne fusionnent que si définition, lot et propriétaire correspondent.\n",
    "- Deux piles ne fusionnent que si définition, origine complète et propriétaire correspondent.\n",
    "stack merge explanation",
)
chapter = replace_once(
    chapter,
    "\tif definition == null or not definition.is_stackable():\n\t\treturn null\n",
    "\tif definition == null or definition.validate() != OK:\n\t\treturn null\n\tif not definition.is_stackable():\n\t\treturn null\n",
    "factory validates stack definition",
)

loadout_owner_anchor = '''\t\tif instance.is_broken(definition):
\t\t\treturn ERR_UNAVAILABLE
\t\tif instance.equipped_by_character_id != character_id:
'''
loadout_owner_replacement = '''\t\tif instance.is_broken(definition):
\t\t\treturn ERR_UNAVAILABLE
\t\tif instance.owner == null:
\t\t\treturn ERR_INVALID_DATA
\t\tif instance.owner.kind != ItemOwnerRef.Kind.CHARACTER:
\t\t\treturn ERR_INVALID_DATA
\t\tif instance.owner.owner_id != character_id:
\t\t\treturn ERR_INVALID_DATA
\t\tif instance.equipped_by_character_id != character_id:
'''
chapter = replace_once(chapter, loadout_owner_anchor, loadout_owner_replacement, "loadout owner checks")
chapter = replace_once(
    chapter,
    "- L’état d’instance et le loadout doivent se confirmer mutuellement.\n",
    "- L’état d’instance, sa propriété et le loadout doivent se confirmer mutuellement.\n",
    "loadout explanation",
)

access_section = '''### 20.1 Autoriser un transfert

> **[VSC] Visual Studio Code — Créer : `res://src/features/inventory/application/inventory_access_port.gd`.**

```gdscript
class_name InventoryAccessPort
extends RefCounted

func can_transfer(
\tcommand: InventoryTransferCommand,
\tcurrent_owner: ItemOwnerRef,
\tsource_custodian: ItemOwnerRef,
) -> Error:
\treturn ERR_UNAVAILABLE
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le port décide si l’acteur et le système source peuvent demander ce transfert.
- `OK` autorise la préparation ; `ERR_UNAUTHORIZED` produit un refus de propriété.
- Le propriétaire courant et le gardien matériel sont fournis séparément.
- Une transaction économique, une quête ou une future règle de justice pourra adapter ce port sans écrire directement le dépôt.
- L’inventaire conserve le dernier mot sur ses invariants même après autorisation.

'''
chapter = replace_once(chapter, "## 21. Préparer un transfert\n", access_section + "## 21. Préparer un transfert\n", "access section")

old_service = '''class_name InventoryService
extends RefCounted

signal inventory_committed(result: InventoryResult)

var _catalog: ItemCatalog
var _repository: InventoryRepository
var _unit_of_work: InventoryMutationUnitOfWork

func transfer(command: InventoryTransferCommand) -> InventoryResult:
\tif command == null or command.validate() != OK:
\t\treturn _result(
\t\t\tInventoryResult.Status.REJECTED_INVALID_COMMAND,
\t\t\tcommand,
\t\t\t"commande invalide",
\t\t)
\tif _catalog == null or _repository == null or _unit_of_work == null:
\t\treturn _result(
\t\t\tInventoryResult.Status.REJECTED_INTERNAL,
\t\t\tcommand,
\t\t\t"services obligatoires indisponibles",
\t\t)
\tvar candidate := _prepare_transfer(command)
\tif candidate == null:
\t\treturn _result(
\t\t\tInventoryResult.Status.REJECTED_NOT_FOUND,
\t\t\tcommand,
\t\t\t"entrée ou conteneur absent",
\t\t)
\tif candidate.validate(_catalog) != OK:
\t\treturn _result(
\t\t\tInventoryResult.Status.REJECTED_INTERNAL,
\t\t\tcommand,
\t\t\t"candidat invalide",
\t\t)
\tvar commit_code := _unit_of_work.commit(candidate)
\tif commit_code != OK:
\t\tvar status := InventoryResult.Status.REJECTED_INTERNAL
\t\tif commit_code == ERR_BUSY:
\t\t\tstatus = InventoryResult.Status.REJECTED_STALE_REVISION
\t\telif commit_code == ERR_OUT_OF_MEMORY:
\t\t\tstatus = InventoryResult.Status.REJECTED_CAPACITY
\t\treturn _result(status, command, error_string(commit_code))
\tvar result := _result(
\t\tInventoryResult.Status.COMMITTED,
\t\tcommand,
\t\t"transfert committé",
\t)
\tresult.affected_entry_ids.assign(_affected_ids(candidate))
\tinventory_committed.emit(result)
\treturn result
'''
new_service = '''class_name InventoryService
extends RefCounted

signal inventory_committed(result: InventoryResult)

class TransferPreparation:
\textends RefCounted

\tvar candidate: InventoryMutationCandidate
\tvar status := InventoryResult.Status.REJECTED_INTERNAL
\tvar message: String = ""

\tfunc is_ready() -> bool:
\t\treturn candidate != null

var _catalog: ItemCatalog
var _repository: InventoryRepository
var _access: InventoryAccessPort
var _unit_of_work: InventoryMutationUnitOfWork

func transfer(command: InventoryTransferCommand) -> InventoryResult:
\tif command == null or command.validate() != OK:
\t\treturn _result(
\t\t\tInventoryResult.Status.REJECTED_INVALID_COMMAND,
\t\t\tcommand,
\t\t\t"commande invalide",
\t\t)
\tif (
\t\t_catalog == null
\t\tor _repository == null
\t\tor _access == null
\t\tor _unit_of_work == null
\t):
\t\treturn _result(
\t\t\tInventoryResult.Status.REJECTED_INTERNAL,
\t\t\tcommand,
\t\t\t"services obligatoires indisponibles",
\t\t)

\tvar prepared := _prepare_transfer(command)
\tif not prepared.is_ready():
\t\treturn _result(prepared.status, command, prepared.message)
\tif prepared.candidate.validate(_catalog) != OK:
\t\treturn _result(
\t\t\tInventoryResult.Status.REJECTED_INTERNAL,
\t\t\tcommand,
\t\t\t"candidat invalide",
\t\t)

\tvar commit_code := _unit_of_work.commit(prepared.candidate, [])
\tif commit_code != OK:
\t\tvar status := InventoryResult.Status.REJECTED_INTERNAL
\t\tif commit_code == ERR_BUSY:
\t\t\tstatus = InventoryResult.Status.REJECTED_STALE_REVISION
\t\telif commit_code == ERR_OUT_OF_MEMORY:
\t\t\tstatus = InventoryResult.Status.REJECTED_CAPACITY
\t\treturn _result(status, command, error_string(commit_code))

\tvar result := _result(
\t\tInventoryResult.Status.COMMITTED,
\t\tcommand,
\t\t"transfert committé",
\t)
\tresult.affected_entry_ids.assign(_affected_ids(prepared.candidate))
\tinventory_committed.emit(result)
\treturn result

func _prepare_transfer(command: InventoryTransferCommand) -> TransferPreparation:
\tvar prepared := TransferPreparation.new()
\tvar source := _repository.get_container(command.source_container_id)
\tvar destination := _repository.get_container(command.destination_container_id)
\tif source == null or destination == null:
\t\tprepared.status = InventoryResult.Status.REJECTED_NOT_FOUND
\t\tprepared.message = "conteneur absent"
\t\treturn prepared
\tif source.revision != command.expected_source_revision:
\t\tprepared.status = InventoryResult.Status.REJECTED_STALE_REVISION
\t\tprepared.message = "révision source obsolète"
\t\treturn prepared
\tif destination.revision != command.expected_destination_revision:
\t\tprepared.status = InventoryResult.Status.REJECTED_STALE_REVISION
\t\tprepared.message = "révision destination obsolète"
\t\treturn prepared

\tvar current_owner := _owner_for_entry(command.entry)
\tif current_owner == null:
\t\tprepared.status = InventoryResult.Status.REJECTED_NOT_FOUND
\t\tprepared.message = "entrée absente"
\t\treturn prepared
\tvar access_code := _access.can_transfer(
\t\tcommand,
\t\tcurrent_owner,
\t\tsource.custodian,
\t)
\tif access_code == ERR_UNAUTHORIZED:
\t\tprepared.status = InventoryResult.Status.REJECTED_OWNERSHIP
\t\tprepared.message = "transfert non autorisé"
\t\treturn prepared
\tif access_code != OK:
\t\tprepared.status = InventoryResult.Status.REJECTED_INTERNAL
\t\tprepared.message = error_string(access_code)
\t\treturn prepared

\tmatch command.entry.kind:
\t\tInventoryEntryRef.Kind.INSTANCE:
\t\t\tvar instance := _repository.get_instance(command.entry.entry_id)
\t\t\tif instance == null or not source.contains(instance.instance_id):
\t\t\t\tprepared.status = InventoryResult.Status.REJECTED_NOT_FOUND
\t\t\t\tprepared.message = "instance absente de la source"
\t\t\t\treturn prepared
\t\t\tif instance.revision != command.expected_entry_revision:
\t\t\t\tprepared.status = InventoryResult.Status.REJECTED_STALE_REVISION
\t\t\t\tprepared.message = "révision d’instance obsolète"
\t\t\t\treturn prepared
\t\t\tif command.quantity != 1 or not command.created_stack_id.is_empty():
\t\t\t\tprepared.status = InventoryResult.Status.REJECTED_STACK_RULE
\t\t\t\tprepared.message = "forme de transfert d’instance invalide"
\t\t\t\treturn prepared
\t\t\tif not instance.equipped_by_character_id.is_empty():
\t\t\t\tprepared.status = InventoryResult.Status.REJECTED_EQUIPMENT
\t\t\t\tprepared.message = "objet encore équipé"
\t\t\t\treturn prepared
\t\t\tprepared.candidate = _prepare_instance_transfer(
\t\t\t\tcommand,
\t\t\t\tsource,
\t\t\t\tdestination,
\t\t\t)
\t\tInventoryEntryRef.Kind.STACK:
\t\t\tprepared.candidate = _prepare_stack_transfer(
\t\t\t\tcommand,
\t\t\t\tsource,
\t\t\t\tdestination,
\t\t\t)
\t\t_:
\t\t\tprepared.status = InventoryResult.Status.REJECTED_INVALID_COMMAND
\t\t\tprepared.message = "type d’entrée inconnu"
\t\t\treturn prepared

\tif prepared.candidate == null:
\t\tprepared.status = InventoryResult.Status.REJECTED_CAPACITY
\t\tprepared.message = "destination ou règle de pile refusée"
\t\treturn prepared
\tprepared.message = "transfert préparé"
\treturn prepared
'''
chapter = replace_once(chapter, old_service, new_service, "inventory service and preparation statuses")
chapter = replace_once(
    chapter,
    "- `_prepare_transfer()` construit des copies de source, destination et entrée.\n- Le candidat est validé avant le commit.\n",
    "- `TransferPreparation` conserve un statut précis sans traiter tous les refus comme une absence.\n- `_prepare_transfer()` relit conteneurs, révisions, propriété et autorisation avant les copies.\n- Le candidat est validé avant le commit.\n",
    "service explanation",
)

chapter = replace_once(
    chapter,
    "\tif not source.contains(instance.instance_id):\n\t\treturn null\n\n\tvar source_candidate := source.duplicate_detached()\n",
    "\tif not source.contains(instance.instance_id):\n\t\treturn null\n\tif not instance.equipped_by_character_id.is_empty():\n\t\treturn null\n\n\tvar source_candidate := source.duplicate_detached()\n",
    "equipped transfer refusal",
)
chapter = replace_once(
    chapter,
    "\tif not _append_instance(destination_candidate, instance):\n\t\treturn null\n\n\tvar instance_candidate := instance.duplicate_detached()\n",
    "\tif not _append_instance(destination_candidate, instance):\n\t\treturn null\n\tsource_candidate.revision += 1\n\tdestination_candidate.revision += 1\n\n\tvar instance_candidate := instance.duplicate_detached()\n",
    "container revisions on instance transfer",
)
chapter = replace_once(
    chapter,
    "- La source est vérifiée à la fois dans l’instance et dans le conteneur.\n",
    "- La source est vérifiée à la fois dans l’instance et dans le conteneur ; un objet équipé doit d’abord être déséquipé.\n",
    "instance transfer explanation",
)
chapter = replace_once(
    chapter,
    "- Propriété, garde, révision et séquence de provenance changent dans le même candidat.\n",
    "- Propriété, garde, révisions des conteneurs, révision d’instance et séquence de provenance changent dans le même candidat.\n",
    "instance revisions explanation",
)

stack_transfer_section = '''
> **[LECTURE] Préparation interne d’un lot — Suite de `inventory_service.gd`.**

```gdscript
func _prepare_stack_transfer(
\tcommand: InventoryTransferCommand,
\tsource: InventoryContainerState,
\tdestination: InventoryContainerState,
) -> InventoryMutationCandidate:
\tvar stack := _repository.get_stack(command.entry.entry_id)
\tif stack == null or stack.container_id != source.container_id:
\t\treturn null
\tif stack.revision != command.expected_entry_revision:
\t\treturn null
\tif not source.contains(stack.stack_id):
\t\treturn null
\tif command.quantity > stack.quantity:
\t\treturn null
\tvar definition := _catalog.get_definition(stack.definition_id)
\tif definition == null or stack.validate(definition) != OK:
\t\treturn null

\tvar source_candidate := source.duplicate_detached()
\tvar destination_candidate := destination.duplicate_detached()
\tvar candidate := InventoryMutationCandidate.new()
\tcandidate.command_id = command.command_id

\tif command.quantity == stack.quantity:
\t\tif not command.created_stack_id.is_empty():
\t\t\treturn null
\t\tif not _remove_entry(source_candidate, stack.stack_id):
\t\t\treturn null
\t\tif not _append_stack(destination_candidate, stack, definition):
\t\t\treturn null
\t\tvar moved := stack.duplicate_detached()
\t\tmoved.container_id = destination.container_id
\t\tmoved.owner = command.requested_owner.duplicate_detached()
\t\tmoved.revision += 1
\t\tcandidate.stacks[moved.stack_id] = moved
\telse:
\t\tif not StableId.is_valid(command.created_stack_id):
\t\t\treturn null
\t\tvar split := _prepare_stack_split(
\t\t\tstack,
\t\t\tcommand.quantity,
\t\t\tcommand.created_stack_id,
\t\t)
\t\tif split.is_empty():
\t\t\treturn null
\t\tvar remaining: ItemStackState = split["source"]
\t\tvar created: ItemStackState = split["created"]
\t\tcreated.container_id = destination.container_id
\t\tcreated.owner = command.requested_owner.duplicate_detached()
\t\tif not _append_stack(destination_candidate, created, definition):
\t\t\treturn null
\t\tcandidate.stacks[remaining.stack_id] = remaining
\t\tcandidate.stacks[created.stack_id] = created

\tsource_candidate.revision += 1
\tdestination_candidate.revision += 1
\tcandidate.containers[source.container_id] = source_candidate
\tcandidate.containers[destination.container_id] = destination_candidate
\tcandidate.expected_revisions[source.container_id] = command.expected_source_revision
\tcandidate.expected_revisions[destination.container_id] = command.expected_destination_revision
\tcandidate.expected_revisions[stack.stack_id] = command.expected_entry_revision
\treturn candidate
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Un transfert total conserve l’identifiant de pile et exige `created_stack_id` vide.
- Un transfert partiel exige un nouvel identifiant préparé par l’appelant.
- La pile restante et la pile créée conservent la même origine de lot.
- La capacité de destination est contrôlée avant toute mutation active.
- La nouvelle pile n’a pas de révision attendue puisqu’elle n’existe pas encore ; l’unité de travail doit aussi vérifier l’absence de collision d’identifiant.

'''
chapter = replace_once(chapter, "## 22. Diviser et fusionner un lot\n", stack_transfer_section + "## 22. Diviser et fusionner un lot\n", "stack transfer section")

old_split = '''func _split_stack(
\tstack: ItemStackState,
\tquantity: int,
\tnew_stack_id: StringName,
) -> ItemStackState:
\tif stack == null or quantity < 1 or quantity >= stack.quantity:
\t\treturn null
\tif not StableId.is_valid(new_stack_id):
\t\treturn null
\tvar created := stack.duplicate_detached()
\tcreated.stack_id = new_stack_id
\tcreated.quantity = quantity
\tcreated.revision = 0
\treturn created
'''
new_split = '''func _prepare_stack_split(
\tstack: ItemStackState,
\tquantity: int,
\tnew_stack_id: StringName,
) -> Dictionary:
\tif stack == null or quantity < 1 or quantity >= stack.quantity:
\t\treturn {}
\tif not StableId.is_valid(new_stack_id) or new_stack_id == stack.stack_id:
\t\treturn {}
\tvar source_candidate := stack.duplicate_detached()
\tvar created := stack.duplicate_detached()
\tsource_candidate.quantity -= quantity
\tsource_candidate.revision += 1
\tcreated.stack_id = new_stack_id
\tcreated.quantity = quantity
\tcreated.revision = 0
\treturn {
\t\t"source": source_candidate,
\t\t"created": created,
\t}
'''
chapter = replace_once(chapter, old_split, new_split, "complete stack split")
chapter = replace_once(
    chapter,
    "- Une division partielle crée une nouvelle pile avec le même `lot_id`.\n- La pile source réelle n’est modifiée que sur une copie préparée par l’appelant.\n",
    "- Une division partielle renvoie la pile source décrémentée et la nouvelle pile avec le même `lot_id`.\n- Les deux résultats sont des copies préparées ; la source active reste intacte avant commit.\n",
    "split explanation",
)
chapter = replace_once(
    chapter,
    "\texternal_candidates: Array[ExternalCandidate] = [],\n",
    "\texternal_candidates: Array[ExternalCandidate],\n",
    "no mutable default external candidates",
)
chapter = replace_once(
    chapter,
    "- Le contrat reçoit le candidat d’inventaire et les candidats des autorités externes.\n",
    "- Le contrat reçoit toujours explicitement le candidat d’inventaire et la liste des candidats des autorités externes, même vide.\n",
    "unit of work explanation",
)

old_equip_signature = '''func prepare_equip(
\tcharacter_id: StringName,
\tslot_id: StringName,
\tinstance_id: StringName,
\texpected_inventory_revision: int,
\texpected_ability_revision: int,
) -> Dictionary:
\tvar instance := _repository.get_instance(instance_id)
\tif instance == null:
\t\treturn {}
'''
new_equip_signature = '''func prepare_equip(
\tcharacter_id: StringName,
\tslot_id: StringName,
\tinstance_id: StringName,
\texpected_instance_revision: int,
\texpected_loadout_revision: int,
\texpected_ability_revision: int,
) -> Dictionary:
\tvar instance := _repository.get_instance(instance_id)
\tif instance == null or instance.revision != expected_instance_revision:
\t\treturn {}
'''
chapter = replace_once(chapter, old_equip_signature, new_equip_signature, "equip revisions signature")
chapter = replace_once(
    chapter,
    "\tif loadout == null or loadout.revision != expected_inventory_revision:\n",
    "\tif loadout == null or loadout.revision != expected_loadout_revision:\n",
    "equip loadout revision",
)
chapter = replace_once(
    chapter,
    '''\treturn {
\t\t"instance": instance_candidate,
\t\t"loadout": loadout_candidate,
\t\t"grant": grant_candidate,
\t}
''',
    '''\treturn {
\t\t"instance": instance_candidate,
\t\t"loadout": loadout_candidate,
\t\t"grant": grant_candidate,
\t\t"expected_instance_revision": expected_instance_revision,
\t\t"expected_loadout_revision": expected_loadout_revision,
\t}
''',
    "equip returned revisions",
)
chapter = replace_once(
    chapter,
    "- L’instance, la définition, la propriété et le loadout sont relus avant préparation.\n",
    "- L’instance, sa révision, la définition, la propriété et la révision du loadout sont relues avant préparation.\n",
    "equip explanation revisions",
)

agent_context = '''### 27.1 Contexte d’inventaire pour un agent

> **[VSC] Visual Studio Code — Créer : `res://src/features/inventory/application/inventory_agent_context_port.gd`.**

```gdscript
class_name InventoryAgentContextPort
extends RefCounted

class Context:
\textends RefCounted

\tvar owner_character_id: StringName
\tvar snapshot_revision: int = 0

\tfunc validate() -> Error:
\t\tif not CharacterId.is_valid(owner_character_id):
\t\t\treturn ERR_INVALID_DATA
\t\treturn OK if snapshot_revision >= 0 else ERR_INVALID_DATA

\tfunc build_transfer_command(
\t\t_request: AgentActionRequest,
\t) -> InventoryTransferCommand:
\t\treturn null

func snapshot_for(_character_id: StringName) -> Context:
\treturn null
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le contexte est un snapshot détaché et révisionné des choix autorisés pour l’agent.
- L’adaptateur concret construit une commande seulement depuis les conteneurs, entrées et destinations exposés par ce snapshot.
- Le stub ne fournit aucune collection interne mutable.
- Le service d’inventaire relit ensuite toutes les révisions et l’autorisation.

'''
chapter = replace_once(chapter, "## 27. Adapter une action d’agent\n", agent_context + "## 27. Adapter une action d’agent\n", "agent context section")
chapter = replace_once(
    chapter,
    "- Le contexte fournit les conteneurs, l’entrée et les révisions autorisées.\n",
    "- Le contexte fournit uniquement les choix autorisés et une révision de snapshot ; la commande reste revalidée par le service.\n",
    "agent context explanation",
)

CHAPTER_PATH.write_text(chapter, encoding="utf-8")

# Metrics after all corrections.
lines = chapter.splitlines()
headings = [line.strip() for line in lines if line.startswith("#")]
heading_duplicates = sum(count - 1 for count in Counter(headings).values() if count > 1)
fence_lines = sum(1 for line in lines if line.startswith("```"))
if fence_lines % 2 != 0:
    raise SystemExit("unbalanced fenced blocks")
blocks = fence_lines // 2
markers = chapter.count("<!-- qa:code-explanation -->")
error_cases = chapter.count("**Symptôme ou risque :**")
faulty = chapter.count("**Pourquoi cet exemple est fautif :**")
corrected = chapter.count("**Pourquoi la correction fonctionne :**")
if blocks != markers:
    raise SystemExit(f"block/marker mismatch: {blocks} != {markers}")
if not (error_cases == faulty == corrected == 10):
    raise SystemExit(f"error correction mismatch: {error_cases}, {faulty}, {corrected}")
if heading_duplicates != 0:
    raise SystemExit(f"duplicate headings: {heading_duplicates}")
if "Validation légère sans PDF" in chapter:
    raise SystemExit("reader chapter contains QA validation procedure")
if "Prochaine étape" in chapter:
    raise SystemExit("reader chapter contains next-step heading")
if "## 39. Synthèse opérationnelle pour Project Asteria" not in chapter:
    raise SystemExit("missing final Project Asteria synthesis")

# Audit.
audit = f'''---
title: "Audit du Livre II — Chapitre 20"
id: "DOC-L2-QA-AUDIT-CH20"
status: "complete"
version: "1.0.0"
chapter-id: "DOC-L2-CH20"
chapter-version: "1.0.0"
audit-level: "static-review"
audit-date: "{TIMESTAMP}"
last-verified: "{TIMESTAMP}"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit du chapitre 20 — Inventaire et réputation des objets

## 1. Porte de brouillon

Le chapitre a été matérialisé sur une branche dédiée et dans une pull request en brouillon. Deux lectures statiques distinctes ont ensuite corrigé les contrats avant la présente clôture `1.0.0`.

## 2. Résultats

- lignes finales : **{len(lines)}** ;
- titres Markdown : **{len(headings)}** ;
- blocs de code ou de données : **{blocks}** ;
- marqueurs d’explication : **{markers}** ;
- cas d’erreurs détaillés : **{error_cases}** ;
- contre-exemples expliqués : **{faulty}** ;
- corrections expliquées : **{corrected}** ;
- doublons de titres : **{heading_duplicates}** ;
- blocs significatifs sans explication : **0** ;
- commandes de validation QA dans le chapitre lecteur : **0** ;
- instruction `Prochaine étape` dans le chapitre : **0** ;
- synthèse finale `Project Asteria` : **présente**.

## 3. Complétude et périmètre

Le chapitre couvre :

- définitions partagées et instances uniques ;
- lots fongibles, division, fusion et transfert ;
- conteneurs, capacités et masse dérivée ;
- équipement et compétences accordées ;
- durabilité demandée par le combat ;
- propriété distincte de la garde matérielle ;
- autorisation de transfert ;
- provenance des instances et origine des lots ;
- réputation globale d’un objet identifié ;
- actions d’agents et présentation ;
- codec strict et restauration préparée.

Les frontières sont respectées :

- le combat conserve ses calculs et prépare seulement une demande de durabilité ;
- les compétences conservent progression, charges, recharges, coûts et effets ;
- l’économie du chapitre 21 conservera monnaies, prix, paiements et contrats de transaction ;
- la justice future pourra adapter l’autorisation sans muter directement l’inventaire ;
- la présentation consomme uniquement des résultats committés.

## 4. Corrections issues des lectures statiques

Les lectures distinctes ont notamment :

1. ajouté une copie détachée explicite pour `ItemReputationState` ;
2. validé les valeurs nulles avant toute lecture d’instance ou de pile ;
3. séparé validation de forme et références croisées des loadouts ;
4. ajouté l’origine complète des lots avec cause, système source et tick logique ;
5. ajouté une fabrique validée pour instances et lots ;
6. vérifié propriété, état brisé et révisions avant équipement ;
7. comparé toute l’origine et protégé les propriétaires lors d’une fusion ;
8. ajouté `InventoryAccessPort` afin d’interdire les transferts non autorisés ;
9. distingué les statuts de préparation au lieu de transformer tous les refus en absence ;
10. interdit le transfert direct d’un objet encore équipé ;
11. incrémenté les révisions des deux conteneurs préparés ;
12. matérialisé le transfert total et partiel des piles ;
13. rendu la division complète en renvoyant source décrémentée et pile créée ;
14. supprimé le tableau mutable par défaut du contrat d’unité de travail ;
15. séparé les révisions d’instance, de loadout et de compétences ;
16. matérialisé le port de contexte utilisé par l’adaptateur d’agent.

## 5. Revue statique du code

Les extraits ont été relus pour vérifier :

- les signatures, types, paramètres et valeurs de retour ;
- les sentinelles `null`, `{{}}`, `&""` et `-1` ;
- les codes `Error` et refus métier ;
- les bornes de masse, quantité, durabilité, réputation et historiques ;
- les copies détachées et candidats ;
- les révisions des conteneurs, entrées, loadouts, réputations et compétences ;
- les identifiants des nouvelles piles ;
- l’ordre de préparation avant commit ;
- l’absence de mutation active par le combat, les agents ou la présentation ;
- l’absence de chargement dynamique de classes depuis les données.

Cette revue ne constitue pas une exécution du parseur GDScript.

## 6. Explications pédagogiques

Les **{blocks}** blocs possèdent chacun un marqueur `<!-- qa:code-explanation -->` et une explication proportionnée portant, selon le besoin, sur les entrées, types, paramètres, retours, effets, invariants, déroulement, résultat attendu et frontières.

Aucune rubrique ne justifie un extrait en répétant seulement le titre de sa section.

## 7. Règle sémantique des erreurs

La section `Erreurs fréquentes et corrections` porte le marqueur `<!-- qa:error-correction-section -->`.

Chacun des dix cas contient un symptôme ou risque, un exemple fautif expliqué, puis un exemple corrigé expliqué. Les cas couvrent les définitions partagées mutées, noms affichés comme identités, empilements invalides, inventaire stocké dans un nœud, source retirée trop tôt, pile équipée, combat écrivant la durabilité, inventaire écrivant une compétence, valeurs dérivées persistées et sortie IA modifiant la réputation.

## 8. Contextes d’utilisation

Les fichiers à créer utilisent `[VSC]`. Les flux, contrats, résultats et contre-exemples utilisent `[LECTURE]`. Les autres repères restent déclarés dans l’en-tête sans être ajoutés artificiellement à des procédures absentes.

Le chapitre ne contient aucune commande de workflow ou procédure de validation documentaire destinée à l’équipe éditoriale.

## 9. Sources et exactitude technique

Les API et types moteur renvoient aux pages officielles Godot 4.7 concernant `Resource`, `RefCounted`, `Array`, `Dictionary`, `StringName`, `Variant` et les signaux.

Les dépendances internes renvoient aux chapitres 7, 9, 14, 17, 18 et 19. La version de référence reste Godot `4.7.1-stable`.

## 10. Clôture éditoriale

La dernière section du chapitre est une synthèse opérationnelle des décisions retenues pour `Project Asteria`. Elle ne contient ni chemin du chapitre suivant, ni niveau GPT futur, ni instruction de production.

## 11. Réserves

- le parseur Godot 4.7.1 n’a pas été exécuté ;
- les dictionnaires typés n’ont pas été vérifiés dans toutes les signatures présentées ;
- l’atomicité runtime de `InventoryMutationUnitOfWork` n’a pas été exécutée ;
- l’autorisation de transfert n’a pas été matérialisée ;
- le grant de compétences et son retrait n’ont pas été exécutés ;
- l’intégration combat-durabilité n’a pas été exécutée ;
- la scène pédagogique n’a pas été instanciée ;
- les budgets n’ont pas été mesurés ;
- le codec et une future migration n’ont pas été exécutés ;
- le replay interplateforme n’a pas été vérifié ;
- aucun PDF n’a été construit.

## 12. Décision

Le chapitre 20 est **accepté au niveau `static-review`**, sous les réserves runtime et PDF de fin de Livre indiquées ci-dessus.
'''
Path("Livre-II/QA/AUDIT-CHAPITRE-20.md").write_text(audit, encoding="utf-8")

proof = f'''schema-version: 1
evidence-id: DOC-L2-QA-EVIDENCE-CH20
status: pending
validation-date: 2026-07-20
validated-base-commit: {BASE_COMMIT}
validated-head-commit: pending
chapter:
  id: DOC-L2-CH20
  path: Livre-II/CHAPITRE-20-Inventaire-et-reputation-des-objets.md
  version: 1.0.0
  audit-level: static-review
results:
  blocking-errors: pending
  warnings: pending
  chapter-lines: {len(lines)}
  chapter-headings: {len(headings)}
  chapter-code-and-data-blocks: {blocks}
  code-explanation-markers: {markers}
  detailed-error-cases: {error_cases}
  faulty-examples-explained: {faulty}
  corrected-examples-explained: {corrected}
  duplicate-headings: {heading_duplicates}
  reader-qa-procedure-absent: true
  next-step-absent-from-reader-chapter: true
  project-asteria-final-synthesis: true
  definitions-instances-stacks-separated: true
  ownership-custody-separated: true
  strict-stack-compatibility: true
  transfer-authorization-port: true
  multi-aggregate-unit-of-work-contract: true
  external-authorities-preserved: true
  save-prepared-before-replacement: true
  pdf-produced: false
  runtime-executed: false
ci:
  validate-chapters-without-pdf:
    run-id: pending
    conclusion: pending
  validate-usage-contexts:
    run-id: pending
    conclusion: pending
reservations:
  - Godot parser not executed.
  - Typed Dictionary signatures not runtime-verified.
  - Inventory unit of work not run.
  - Transfer authorization adapter not materialized.
  - Ability grant integration not run.
  - Combat durability integration not run.
  - Demo scene not instantiated.
  - Performance budgets not measured.
  - Save restoration not executed.
  - Cross-platform replay not verified.
  - PDF deferred until end of Livre II.
'''
Path("Livre-II/QA/VALIDATION-FINALE-CHAPITRE-20.yaml").write_text(proof, encoding="utf-8")

# Active index.
index_path = Path("Livre-II/index.md")
index = index_path.read_text(encoding="utf-8")
index = replace_once(index, 'version: "1.12.6"', 'version: "1.13.0"', "index version")
index = replace_once(
    index,
    "20. Inventaire et réputation des objets — à rédiger",
    "20. [Inventaire et réputation des objets](CHAPITRE-20-Inventaire-et-reputation-des-objets.md) — **rédigé, repéré, expliqué bloc par bloc, transferts multi-agrégats préparés, clôturé par les décisions Project Asteria et audité au niveau static-review**",
    "index chapter 20",
)
index = replace_once(
    index,
    "- [audit du chapitre 19](QA/AUDIT-CHAPITRE-19.md) ;\n",
    "- [audit du chapitre 19](QA/AUDIT-CHAPITRE-19.md) ;\n- [audit du chapitre 20](QA/AUDIT-CHAPITRE-20.md) ;\n",
    "index audit 20",
)
index = replace_once(
    index,
    "Les chapitres 3 à 19 utilisent **Élevée**.",
    "Les chapitres 3 à 20 utilisent **Élevée**.",
    "index reasoning range",
)
index_path.write_text(index, encoding="utf-8")

# Roadmap.
roadmap_path = Path("ROADMAP.md")
roadmap = roadmap_path.read_text(encoding="utf-8")
roadmap = replace_once(
    roadmap,
    "- [ ] Douze grands systèmes de jeu — 6 chapitres rédigés, repérés et audités sur 12.",
    "- [ ] Douze grands systèmes de jeu — 7 chapitres rédigés, repérés et audités sur 12.",
    "roadmap gameplay count",
)
roadmap = replace_once(
    roadmap,
    "- [x] Convention des outils et contextes appliquée aux chapitres 1 à 19.",
    "- [x] Convention des outils et contextes appliquée aux chapitres 1 à 20.",
    "roadmap context range",
)
roadmap = replace_once(
    roadmap,
    "- [x] Chapitre 19 — définitions de compétences, coûts, ciblages, effets composables, progression, charges, recharges, unité de travail commune et sauvegarde stricte — rédigé et audité au niveau `static-review`.\n",
    "- [x] Chapitre 19 — définitions de compétences, coûts, ciblages, effets composables, progression, charges, recharges, unité de travail commune et sauvegarde stricte — rédigé et audité au niveau `static-review`.\n- [x] Chapitre 20 — définitions et instances d’objets, lots fongibles, conteneurs, transferts autorisés, équipement, durabilité, propriété, provenance, réputation et sauvegarde stricte — rédigé et audité au niveau `static-review`.\n",
    "roadmap chapter 20",
)
roadmap_path.write_text(roadmap, encoding="utf-8")

# Compilation order.
contents_path = Path("contents.txt")
contents = contents_path.read_text(encoding="utf-8")
contents = replace_once(
    contents,
    "Livre-II/CHAPITRE-19-Competences-et-pouvoirs.md\n",
    "Livre-II/CHAPITRE-19-Competences-et-pouvoirs.md\nLivre-II/CHAPITRE-20-Inventaire-et-reputation-des-objets.md\n",
    "contents chapter 20",
)
contents = replace_once(
    contents,
    "Livre-II/QA/AUDIT-CHAPITRE-19.md\n",
    "Livre-II/QA/AUDIT-CHAPITRE-19.md\nLivre-II/QA/AUDIT-CHAPITRE-20.md\n",
    "contents audit 20",
)
contents = replace_once(
    contents,
    "Livre-II/QA/VALIDATION-FINALE-CHAPITRE-19.yaml\n",
    "Livre-II/QA/VALIDATION-FINALE-CHAPITRE-19.yaml\nLivre-II/QA/VALIDATION-FINALE-CHAPITRE-20.yaml\n",
    "contents proof 20",
)
contents_path.write_text(contents, encoding="utf-8")

# Continuity.
continuity_path = Path("CONTINUITE-PROJET.md")
continuity = continuity_path.read_text(encoding="utf-8")
continuity = replace_once(continuity, 'version: "3.19.1"', 'version: "3.20.0"', "continuity version")
continuity = replace_once(
    continuity,
    'last-updated: "2026-07-20T16:52:26+02:00"',
    f'last-updated: "{TIMESTAMP}"',
    "continuity timestamp",
)
continuity = replace_once(
    continuity,
    "Chapitres 3 à 19 : **Élevée**.",
    "Chapitres 3 à 20 : **Élevée**.",
    "continuity reasoning range",
)
architecture = '''### 11.15 Inventaire et réputation des objets

- `ItemDefinition` constitue une `Resource` de conception partagée et immuable ;
- instances uniques et lots fongibles possèdent des états distincts ;
- une définition empilable exclut durabilité, équipement, compétence accordée et réputation individuelle ;
- propriété métier et garde matérielle sont séparées ;
- les conteneurs référencent des entrées par identifiants stables et la masse totale reste dérivée ;
- l’origine complète d’un lot comprend `lot_id`, cause, système source et tick logique ;
- les fusions exigent définition, origine complète et propriétaire identiques ;
- source, destination et entrée sont préparées sur des copies avec révisions séparées ;
- `InventoryAccessPort` autorise la demande sans contourner les invariants d’inventaire ;
- un objet équipé doit être déséquipé avant transfert ;
- seuls les objets uniques compatibles et non brisés peuvent être équipés ;
- les compétences accordées restent sous l’autorité du système de compétences ;
- le combat prépare une demande de durabilité sans écrire l’inventaire ;
- provenance et réputation utilisent des causes validées et des ticks logiques ;
- `InventoryMutationUnitOfWork` reçoit les candidats d’inventaire et des autorités externes avant tout événement ;
- définitions, masse dérivée, commandes, candidats, caches et présentation sont exclus de la persistance ;
- prix, monnaies, paiements, achats et ventes restent réservés au chapitre 21.

'''
continuity = replace_once(continuity, "## 12. Chapitre 5 — état résumé\n", architecture + "## 12. Chapitre 5 — état résumé\n", "continuity architecture 11.15")
error_anchor = "- ne pas utiliser un nom affiché comme identité de compétence ;\n"
new_errors = '''- ne pas utiliser un nom affiché comme identité de compétence ;
- ne pas modifier une `ItemDefinition` partagée comme état d’instance ;
- ne pas confondre propriété métier et garde matérielle ;
- ne pas fusionner des objets individualisés ou des lots d’origines différentes ;
- ne pas retirer une entrée de la source avant validation complète de la destination ;
- ne pas autoriser un transfert sans politique d’accès explicite ;
- ne pas transférer directement un objet encore équipé ;
- ne pas laisser le combat écrire directement la durabilité ;
- ne pas laisser l’inventaire écrire progression, charges ou recharge d’une compétence ;
- ne pas persister masse dérivée, tris, filtres ou sélection d’interface ;
- ne pas laisser une sortie IA modifier directement la réputation d’un objet ;
'''
continuity = replace_once(continuity, error_anchor, new_errors, "continuity inventory errors")
continuity = replace_once(
    continuity,
    "- progression : 19 chapitres sur 30 ;",
    "- progression : 20 chapitres sur 30 ;",
    "continuity chapter count",
)
continuity = replace_once(
    continuity,
    "- chapitre 19 : version `1.0.1` ;\n",
    "- chapitre 19 : version `1.0.1` ;\n- chapitre 20 : version `1.0.0` ;\n",
    "continuity chapter 20 version",
)
old_next = '''Le chapitre 19 est terminé au niveau `static-review`. Les compétences séparent définitions, progression et état runtime, préparent coûts et effets derrière leurs autorités propriétaires et exigent un commit commun avant tout événement.

Chapitre suivant :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-II/CHAPITRE-20-Inventaire-et-reputation-des-objets.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Périmètre attendu : définitions et instances d’objets, conteneurs d’inventaire, empilement, équipement, durabilité, propriété, provenance et réputation des objets, en réutilisant les contrats des personnages, du combat et des compétences sans déplacer leurs autorités.
'''
new_next = '''Le chapitre 20 est terminé au niveau `static-review`. L’inventaire sépare définitions, instances et lots, prépare les transferts sur des copies révisionnées, distingue propriété et garde, et conserve combat, compétences et économie derrière leurs autorités.

Chapitre suivant :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-II/CHAPITRE-21-Economie.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Périmètre attendu : monnaies et portefeuilles, valeurs et politiques de prix, offres, achats, ventes, récompenses, paiements et transactions atomiques avec l’inventaire, sans déplacer l’identité, la quantité, la propriété ou le transfert des objets hors du système du chapitre 20.
'''
continuity = replace_once(continuity, old_next, new_next, "continuity next action")
journal_anchor = "## 27. Journal\n\n"
journal = f'''### {TIMESTAMP} — version 3.20.0

- chapitre 20 créé, relu, corrigé et audité au niveau `static-review` ;
- définitions, instances, lots, conteneurs, équipement, durabilité, propriété, provenance et réputation documentés ;
- autorisation des transferts, statuts de préparation et révisions multi-agrégats explicités ;
- frontières avec combat, compétences, agents, justice future et économie maintenues ;
- index, roadmap, `contents.txt`, audit et preuve QA mis à jour ;
- prochaine action déplacée vers le chapitre 21 — Économie, niveau Élevée ;
- aucun test runtime revendiqué et aucun PDF construit.

'''
continuity = replace_once(continuity, journal_anchor, journal_anchor + journal, "continuity journal")
continuity_path.write_text(continuity, encoding="utf-8")
