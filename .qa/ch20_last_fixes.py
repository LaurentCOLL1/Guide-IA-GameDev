from collections import Counter
from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise SystemExit(f"missing {label}: {old[:100]!r}")
    return text.replace(old, new, 1)


chapter_path = Path("Livre-II/CHAPITRE-20-Inventaire-et-reputation-des-objets.md")
chapter = chapter_path.read_text(encoding="utf-8")

# Create a reputation state alongside reputation-enabled instances.
chapter = replace_once(
    chapter,
    '''\tstate.quantity = quantity
\treturn state if state.validate(definition) == OK else null
```
''',
    '''\tstate.quantity = quantity
\treturn state if state.validate(definition) == OK else null

func create_reputation_state(
\tdefinition: ItemDefinition,
\tinstance_id: StringName,
) -> ItemReputationState:
\tif definition == null or definition.validate() != OK:
\t\treturn null
\tif not definition.reputation_enabled or not StableId.is_valid(instance_id):
\t\treturn null
\tvar state := ItemReputationState.new()
\tstate.instance_id = instance_id
\treturn state if state.validate(definition) == OK else null
```
''',
    "factory reputation state",
)
chapter = replace_once(
    chapter,
    "- Le lot reçoit immédiatement son origine et son tick logique.\n- Chaque état est validé avant d’être renvoyé au service créateur.\n",
    "- Le lot reçoit immédiatement son origine et son tick logique.\n- Une instance dont la réputation est activée reçoit un état de renommée séparé, initialisé à zéro.\n- Chaque état est validé avant d’être renvoyé au service créateur.\n",
    "factory reputation explanation",
)

# Distinguish stack failures before building the candidate.
old_stack_branch = '''\t\tInventoryEntryRef.Kind.STACK:
\t\t\tprepared.candidate = _prepare_stack_transfer(
\t\t\t\tcommand,
\t\t\t\tsource,
\t\t\t\tdestination,
\t\t\t)
'''
new_stack_branch = '''\t\tInventoryEntryRef.Kind.STACK:
\t\t\tvar stack := _repository.get_stack(command.entry.entry_id)
\t\t\tif stack == null or not source.contains(stack.stack_id):
\t\t\t\tprepared.status = InventoryResult.Status.REJECTED_NOT_FOUND
\t\t\t\tprepared.message = "pile absente de la source"
\t\t\t\treturn prepared
\t\t\tif stack.revision != command.expected_entry_revision:
\t\t\t\tprepared.status = InventoryResult.Status.REJECTED_STALE_REVISION
\t\t\t\tprepared.message = "révision de pile obsolète"
\t\t\t\treturn prepared
\t\t\tif command.quantity > stack.quantity:
\t\t\t\tprepared.status = InventoryResult.Status.REJECTED_STACK_RULE
\t\t\t\tprepared.message = "quantité supérieure à la pile"
\t\t\t\treturn prepared
\t\t\tvar is_partial := command.quantity < stack.quantity
\t\t\tif is_partial and not StableId.is_valid(command.created_stack_id):
\t\t\t\tprepared.status = InventoryResult.Status.REJECTED_STACK_RULE
\t\t\t\tprepared.message = "identifiant de division absent"
\t\t\t\treturn prepared
\t\t\tif not is_partial and not command.created_stack_id.is_empty():
\t\t\t\tprepared.status = InventoryResult.Status.REJECTED_STACK_RULE
\t\t\t\tprepared.message = "identifiant de division inattendu"
\t\t\t\treturn prepared
\t\t\tprepared.candidate = _prepare_stack_transfer(
\t\t\t\tcommand,
\t\t\t\tsource,
\t\t\t\tdestination,
\t\t\t)
'''
chapter = replace_once(chapter, old_stack_branch, new_stack_branch, "stack rejection statuses")
chapter = replace_once(
    chapter,
    "- `TransferPreparation` conserve un statut précis sans traiter tous les refus comme une absence.\n",
    "- `TransferPreparation` conserve un statut précis sans traiter tous les refus comme une absence ; les piles distinguent absence, révision, quantité et identifiant de division.\n",
    "stack status explanation",
)

# Build the destination-shaped instance before capacity validation.
old_instance_order = '''\tvar source_candidate := source.duplicate_detached()
\tvar destination_candidate := destination.duplicate_detached()
\tif not _remove_entry(source_candidate, instance.instance_id):
\t\treturn null
\tif not _append_instance(destination_candidate, instance):
\t\treturn null
\tsource_candidate.revision += 1
\tdestination_candidate.revision += 1

\tvar instance_candidate := instance.duplicate_detached()
\tvar previous_owner := instance_candidate.owner.duplicate_detached()
\tinstance_candidate.container_id = destination.container_id
\tinstance_candidate.owner = command.requested_owner.duplicate_detached()
\tinstance_candidate.revision += 1
\tinstance_candidate.provenance_sequence += 1
'''
new_instance_order = '''\tvar source_candidate := source.duplicate_detached()
\tvar destination_candidate := destination.duplicate_detached()
\tvar instance_candidate := instance.duplicate_detached()
\tvar previous_owner := instance_candidate.owner.duplicate_detached()
\tinstance_candidate.container_id = destination.container_id
\tinstance_candidate.owner = command.requested_owner.duplicate_detached()
\tinstance_candidate.revision += 1
\tinstance_candidate.provenance_sequence += 1

\tif not _remove_entry(source_candidate, instance.instance_id):
\t\treturn null
\tif not _append_instance(destination_candidate, instance_candidate):
\t\treturn null
\tsource_candidate.revision += 1
\tdestination_candidate.revision += 1
'''
chapter = replace_once(chapter, old_instance_order, new_instance_order, "destination-shaped instance")
chapter = replace_once(
    chapter,
    "- La destination est validée avant de modifier l’instance candidate.\n",
    "- La destination valide l’instance candidate déjà configurée avec sa nouvelle garde et sa nouvelle propriété.\n",
    "instance destination explanation",
)

# Build the moved stack before passing it to the destination helper.
old_full_stack = '''\tif command.quantity == stack.quantity:
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
'''
new_full_stack = '''\tif command.quantity == stack.quantity:
\t\tif not command.created_stack_id.is_empty():
\t\t\treturn null
\t\tvar moved := stack.duplicate_detached()
\t\tmoved.container_id = destination.container_id
\t\tmoved.owner = command.requested_owner.duplicate_detached()
\t\tmoved.revision += 1
\t\tif not _remove_entry(source_candidate, stack.stack_id):
\t\t\treturn null
\t\tif not _append_stack(destination_candidate, moved, definition):
\t\t\treturn null
\t\tcandidate.stacks[moved.stack_id] = moved
'''
chapter = replace_once(chapter, old_full_stack, new_full_stack, "destination-shaped moved stack")
chapter = replace_once(
    chapter,
    "- La capacité de destination est contrôlée avant toute mutation active.\n",
    "- La capacité de destination est contrôlée avec la pile candidate déjà configurée pour cette destination, avant toute mutation active.\n",
    "stack destination explanation",
)

# Validate merge definition ownership as well as stack compatibility.
chapter = replace_once(
    chapter,
    '''\tif destination == null or source == null or definition == null:
\t\treturn ERR_INVALID_PARAMETER
\tif not destination.can_merge_with(source):
''',
    '''\tif destination == null or source == null or definition == null:
\t\treturn ERR_INVALID_PARAMETER
\tif definition.validate() != OK or not definition.is_stackable():
\t\treturn ERR_INVALID_DATA
\tif destination.definition_id != definition.item_id:
\t\treturn ERR_INVALID_DATA
\tif source.definition_id != definition.item_id:
\t\treturn ERR_INVALID_DATA
\tif not destination.can_merge_with(source):
''',
    "merge definition validation",
)
chapter = replace_once(
    chapter,
    "- La fusion exige une compatibilité stricte et une capacité suffisante.\n",
    "- La fusion exige une définition empilable correspondante, une compatibilité stricte et une capacité suffisante.\n",
    "merge explanation",
)

# Use an explicitly typed empty external candidate list.
chapter = replace_once(
    chapter,
    "\tvar commit_code := _unit_of_work.commit(prepared.candidate, [])\n",
    "\tvar external_candidates: Array[InventoryMutationUnitOfWork.ExternalCandidate] = []\n\tvar commit_code := _unit_of_work.commit(\n\t\tprepared.candidate,\n\t\texternal_candidates,\n\t)\n",
    "typed empty external candidates",
)
chapter = replace_once(
    chapter,
    "- Le candidat est validé avant le commit.\n",
    "- Le candidat est validé avant le commit et la liste externe vide conserve un type explicite.\n",
    "typed external list explanation",
)

# Add the symmetric unequip preparation.
unequip_section = '''
### 24.1 Déséquiper et retirer uniquement le grant source

> **[LECTURE] Préparation d’un déséquipement — Structure de référence.**

```gdscript
func prepare_unequip(
\tcharacter_id: StringName,
\tslot_id: StringName,
\texpected_instance_revision: int,
\texpected_loadout_revision: int,
\texpected_ability_revision: int,
) -> Dictionary:
\tvar loadout := _repository.get_loadout(character_id)
\tif loadout == null or loadout.revision != expected_loadout_revision:
\t\treturn {}
\tif not loadout.slots.has(slot_id):
\t\treturn {}
\tvar instance_id: StringName = loadout.slots[slot_id]
\tvar instance := _repository.get_instance(instance_id)
\tif instance == null or instance.revision != expected_instance_revision:
\t\treturn {}
\tif instance.equipped_by_character_id != character_id:
\t\treturn {}
\tvar definition := _catalog.get_definition(instance.definition_id)
\tif definition == null:
\t\treturn {}

\tvar instance_candidate := instance.duplicate_detached()
\tvar loadout_candidate := loadout.duplicate_detached()
\tinstance_candidate.equipped_by_character_id = &""
\tinstance_candidate.revision += 1
\tloadout_candidate.slots.erase(slot_id)
\tloadout_candidate.revision += 1

\tvar grant_candidate := _ability_grant_port.prepare_grant_set(
\t\tcharacter_id,
\t\tinstance_id,
\t\tdefinition.granted_ability_ids,
\t\tfalse,
\t\texpected_ability_revision,
\t)
\tif not definition.granted_ability_ids.is_empty() and grant_candidate == null:
\t\treturn {}
\treturn {
\t\t"instance": instance_candidate,
\t\t"loadout": loadout_candidate,
\t\t"grant": grant_candidate,
\t\t"expected_instance_revision": expected_instance_revision,
\t\t"expected_loadout_revision": expected_loadout_revision,
\t}
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le slot détermine l’instance réellement équipée ; l’appelant ne peut pas substituer un autre identifiant.
- Les révisions d’instance, de loadout et de compétences restent séparées.
- Le candidat efface seulement le lien d’équipement et prépare le retrait du grant provenant de cette instance.
- Une compétence durablement apprise ou accordée par une autre source reste sous la décision du système de compétences.
- Instance, loadout et retrait de grant doivent être committés dans le même lot.

'''
chapter = replace_once(chapter, "## 25. Durabilité demandée par le combat\n", unequip_section + "## 25. Durabilité demandée par le combat\n", "unequip section")

chapter_path.write_text(chapter, encoding="utf-8")

# Recompute metrics and patch audit/proof.
lines = chapter.splitlines()
headings = [line.strip() for line in lines if line.startswith("#")]
blocks = sum(1 for line in lines if line.startswith("```")) // 2
markers = chapter.count("<!-- qa:code-explanation -->")
errors = chapter.count("**Symptôme ou risque :**")
faulty = chapter.count("**Pourquoi cet exemple est fautif :**")
corrected = chapter.count("**Pourquoi la correction fonctionne :**")
duplicates = sum(count - 1 for count in Counter(headings).values() if count > 1)
if blocks != markers or errors != 10 or faulty != 10 or corrected != 10 or duplicates != 0:
    raise SystemExit("metric invariant failed")

audit_path = Path("Livre-II/QA/AUDIT-CHAPITRE-20.md")
audit = audit_path.read_text(encoding="utf-8")
audit = audit.replace("Deux lectures statiques distinctes", "Plusieurs lectures statiques distinctes", 1)
for old, new in [
    ("- lignes finales : **2584** ;", f"- lignes finales : **{len(lines)}** ;"),
    ("- titres Markdown : **58** ;", f"- titres Markdown : **{len(headings)}** ;"),
    ("- blocs de code ou de données : **55** ;", f"- blocs de code ou de données : **{blocks}** ;"),
    ("- marqueurs d’explication : **55** ;", f"- marqueurs d’explication : **{markers}** ;"),
    ("Les **55** blocs possèdent chacun", f"Les **{blocks}** blocs possèdent chacun"),
]:
    if old not in audit:
        raise SystemExit(f"audit metric missing: {old}")
    audit = audit.replace(old, new, 1)
audit = replace_once(
    audit,
    "16. matérialisé le port de contexte utilisé par l’adaptateur d’agent.\n",
    "16. matérialisé le port de contexte utilisé par l’adaptateur d’agent ;\n17. validé les états candidats avec leur conteneur de destination ;\n18. distingué les refus propres aux piles avant construction ;\n19. ajouté le déséquipement symétrique et le retrait du seul grant source ;\n20. ajouté l’initialisation séparée de la réputation des instances concernées.\n",
    "audit final corrections",
)
audit_path.write_text(audit, encoding="utf-8")

proof_path = Path("Livre-II/QA/VALIDATION-FINALE-CHAPITRE-20.yaml")
proof = proof_path.read_text(encoding="utf-8")
for old, new in [
    ("  chapter-lines: 2584", f"  chapter-lines: {len(lines)}"),
    ("  chapter-headings: 58", f"  chapter-headings: {len(headings)}"),
    ("  chapter-code-and-data-blocks: 55", f"  chapter-code-and-data-blocks: {blocks}"),
    ("  code-explanation-markers: 55", f"  code-explanation-markers: {markers}"),
]:
    if old not in proof:
        raise SystemExit(f"proof metric missing: {old}")
    proof = proof.replace(old, new, 1)
proof_path.write_text(proof, encoding="utf-8")
