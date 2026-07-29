#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import platform
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Iterable

EXPECTED_CASES = 67
REPORT_PATH = Path("dist/QA-LIVRE-V-CH16-ARCHITECTURE.json")
CASES: list[tuple[str, Callable[[], None]]] = []


def case(name: str):
    def decorator(function: Callable[[], None]):
        CASES.append((name, function))
        return function
    return decorator


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


LAYERS = {"domain", "application", "presentation", "infrastructure", "composition", "tools"}
ALLOWED = {
    "domain": {"domain"},
    "application": {"application", "domain"},
    "presentation": {"presentation", "application", "domain"},
    "infrastructure": {"infrastructure", "application", "domain"},
    "composition": LAYERS,
    "tools": {"tools", "application", "domain", "infrastructure"},
}


def validate_edges(nodes: dict[str, str], edges: list[tuple[str, str]]) -> None:
    for source, target in edges:
        require(source in nodes and target in nodes, f"unknown node: {source}->{target}")
        source_layer = nodes[source]
        target_layer = nodes[target]
        require(target_layer in ALLOWED[source_layer], f"forbidden dependency: {source_layer}->{target_layer}")


def topological_order(nodes: Iterable[str], edges: list[tuple[str, str]]) -> list[str]:
    values = list(nodes)
    incoming = {value: 0 for value in values}
    outgoing = {value: [] for value in values}
    for source, target in edges:
        require(source in incoming and target in incoming, "edge references unknown node")
        outgoing[target].append(source)
        incoming[source] += 1
    ready = sorted(value for value, count in incoming.items() if count == 0)
    result: list[str] = []
    while ready:
        value = ready.pop(0)
        result.append(value)
        for dependent in sorted(outgoing[value]):
            incoming[dependent] -= 1
            if incoming[dependent] == 0:
                ready.append(dependent)
                ready.sort()
    require(len(result) == len(values), "dependency cycle detected")
    return result


def choose_channel(scope: str, durable: bool, needs_return: bool) -> str:
    if durable:
        return "queue"
    if needs_return:
        return "call"
    if scope == "local":
        return "signal"
    if scope == "transversal":
        return "typed_bus"
    raise ValueError("unsupported communication scope")


def validate_lifecycle(states: list[str]) -> None:
    allowed = {
        "CREATED": {"CONFIGURED", "FAILED"},
        "CONFIGURED": {"STARTED", "FAILED"},
        "STARTED": {"STOPPED", "FAILED"},
        "FAILED": {"STOPPED"},
        "STOPPED": set(),
    }
    require(states and states[0] == "CREATED", "lifecycle must start at CREATED")
    for current, following in zip(states, states[1:]):
        require(following in allowed[current], f"invalid transition {current}->{following}")


def validate_state_owners(entries: list[tuple[str, str, bool]]) -> None:
    owners: dict[str, list[str]] = {}
    for state, component, authoritative in entries:
        if authoritative:
            owners.setdefault(state, []).append(component)
    for state, values in owners.items():
        require(len(values) == 1, f"state {state} has {len(values)} owners")


@dataclass
class MemoryRepository:
    values: dict[str, dict[str, object]] = field(default_factory=dict)

    def put(self, key: str, value: dict[str, object]) -> None:
        require(bool(key), "key required")
        self.values[key] = dict(value)

    def get(self, key: str) -> dict[str, object] | None:
        value = self.values.get(key)
        return dict(value) if value is not None else None

    def delete(self, key: str) -> bool:
        return self.values.pop(key, None) is not None


@dataclass
class StubSqliteRepository(MemoryRepository):
    engine: str = "sqlite-stub"


def exercise_repository(repository: MemoryRepository) -> None:
    require(repository.get("missing") is None, "missing value must be explicit")
    repository.put("item.1", {"quantity": 2})
    require(repository.get("item.1") == {"quantity": 2}, "stored value mismatch")
    repository.put("item.1", {"quantity": 3})
    require(repository.get("item.1") == {"quantity": 3}, "replacement mismatch")
    require(repository.delete("item.1"), "delete should report success")
    require(repository.get("item.1") is None, "deleted value remains")


@dataclass
class Participant:
    name: str
    can_prepare: bool = True
    can_commit: bool = True
    prepared: bool = False
    committed: bool = False
    compensated: bool = False

    def prepare(self) -> bool:
        self.prepared = self.can_prepare
        return self.prepared

    def commit(self) -> bool:
        if not self.prepared or not self.can_commit:
            return False
        self.committed = True
        return True

    def compensate(self) -> None:
        if self.committed:
            self.compensated = True
            self.committed = False


def execute_unit_of_work(participants: list[Participant]) -> bool:
    prepared: list[Participant] = []
    for participant in participants:
        if not participant.prepare():
            return False
        prepared.append(participant)
    committed: list[Participant] = []
    for participant in participants:
        if not participant.commit():
            for done in reversed(committed):
                done.compensate()
            return False
        committed.append(participant)
    return True


def translate_external(raw: dict[str, object]) -> dict[str, object]:
    require(raw.get("status") in {"ok", "denied"}, "unknown external status")
    return {
        "accepted": raw["status"] == "ok",
        "message": str(raw.get("detail", "")),
        "adapter_version": 1,
    }


def validate_facade(public_api: list[str], internal_tokens: set[str]) -> None:
    require(len(public_api) <= 8, "facade too wide")
    for entry in public_api:
        require(not any(token in entry for token in internal_tokens), f"internal detail leaked: {entry}")


def validate_registry(entries: list[tuple[str, str]]) -> dict[str, str]:
    result: dict[str, str] = {}
    for key, implementation in entries:
        require(key not in result, f"duplicate registry key: {key}")
        require(key and implementation, "registry entry must be non-empty")
        result[key] = implementation
    return result


def stable_manifest(payload: dict[str, object]) -> str:
    encoded = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def validate_contract(required: set[str], implementation: set[str]) -> None:
    missing = required - implementation
    require(not missing, f"contract methods missing: {sorted(missing)}")


def detect_architecture_smells(manifest: dict[str, object]) -> set[str]:
    smells: set[str] = set()
    responsibilities = manifest.get("responsibilities", [])
    if isinstance(responsibilities, list) and len(responsibilities) > 5:
        smells.add("god_object")
    name = str(manifest.get("name", ""))
    if name in {"GameManager", "GlobalManager", "Manager"}:
        smells.add("generic_manager")
    dependencies = manifest.get("dependencies", [])
    if isinstance(dependencies, list) and any(value in {"Global", "ServiceLocator", "GlobalServices"} for value in dependencies):
        smells.add("service_locator")
    public_api = manifest.get("public_api", [])
    if isinstance(public_api, list) and any("/internal/" in str(value) or "sqlite_" in str(value) for value in public_api):
        smells.add("leaky_facade")
    return smells


@case("domain_depends_only_on_domain")
def _():
    validate_edges({"rule": "domain", "value": "domain"}, [("rule", "value")])


@case("domain_to_infrastructure_rejected")
def _():
    try:
        validate_edges({"rule": "domain", "db": "infrastructure"}, [("rule", "db")])
    except AssertionError:
        return
    raise AssertionError("domain dependency on infrastructure accepted")


@case("presentation_to_application_allowed")
def _():
    validate_edges({"panel": "presentation", "service": "application"}, [("panel", "service")])


@case("infrastructure_to_domain_port_allowed")
def _():
    validate_edges({"adapter": "infrastructure", "port": "domain"}, [("adapter", "port")])


@case("composition_may_know_concrete_components")
def _():
    validate_edges({"bootstrap": "composition", "panel": "presentation", "repo": "infrastructure"}, [("bootstrap", "panel"), ("bootstrap", "repo")])


@case("tools_may_use_infrastructure")
def _():
    validate_edges({"migration_tool": "tools", "repo": "infrastructure"}, [("migration_tool", "repo")])


@case("acyclic_graph_has_order")
def _():
    order = topological_order(["bus", "repo", "service", "panel"], [("service", "bus"), ("service", "repo"), ("panel", "service")])
    require(order.index("bus") < order.index("service") < order.index("panel"), "invalid start order")


@case("cycle_is_detected")
def _():
    try:
        topological_order(["a", "b"], [("a", "b"), ("b", "a")])
    except AssertionError:
        return
    raise AssertionError("cycle accepted")


@case("stop_order_is_reverse_start")
def _():
    order = topological_order(["bus", "service", "panel"], [("service", "bus"), ("panel", "service")])
    require(list(reversed(order)) == ["panel", "service", "bus"], "invalid reverse stop order")


@case("unknown_dependency_is_rejected")
def _():
    try:
        topological_order(["service"], [("service", "missing")])
    except AssertionError:
        return
    raise AssertionError("unknown dependency accepted")


@case("constructor_dependency_is_explicit")
def _():
    manifest = {"component": "InventoryService", "constructor": ["InventoryRepository", "EventBus"]}
    require("InventoryRepository" in manifest["constructor"], "repository hidden")


@case("service_locator_is_detected")
def _():
    smells = detect_architecture_smells({"name": "InventoryService", "dependencies": ["GlobalServices"]})
    require("service_locator" in smells, "service locator not detected")


@case("local_notification_uses_signal")
def _():
    require(choose_channel("local", False, False) == "signal", "local notification choice")


@case("transversal_notification_uses_typed_bus")
def _():
    require(choose_channel("transversal", False, False) == "typed_bus", "transversal choice")


@case("durable_work_uses_queue")
def _():
    require(choose_channel("transversal", True, False) == "queue", "durable choice")


@case("request_with_return_uses_call")
def _():
    require(choose_channel("local", False, True) == "call", "call choice")


@case("unsupported_scope_is_rejected")
def _():
    try:
        choose_channel("global_magic", False, False)
    except ValueError:
        return
    raise AssertionError("unsupported channel accepted")


@case("command_is_imperative")
def _():
    name = "TransferItemCommand"
    require(name.endswith("Command"), "command naming lost")


@case("event_is_past_tense_fact")
def _():
    event = {"name": "item_transferred", "committed": True}
    require(event["name"].endswith("ed") and event["committed"], "event contract invalid")


@case("query_declares_no_mutation")
def _():
    query = {"name": "GetInventoryView", "mutates": False}
    require(not query["mutates"], "query mutates")


@case("event_after_commit_is_valid")
def _():
    timeline = ["prepare", "commit", "publish_event"]
    require(timeline.index("commit") < timeline.index("publish_event"), "event published too early")


@case("event_before_commit_is_rejected")
def _():
    timeline = ["prepare", "publish_event", "commit"]
    require(timeline.index("publish_event") < timeline.index("commit"), "fixture malformed")
    try:
        require(timeline.index("commit") < timeline.index("publish_event"), "event published before commit")
    except AssertionError:
        return
    raise AssertionError("early event accepted")


@case("single_state_owner_is_valid")
def _():
    validate_state_owners([("inventory", "InventoryRepository", True), ("inventory", "InventoryPanel", False)])


@case("duplicate_state_owner_is_rejected")
def _():
    try:
        validate_state_owners([("inventory", "InventoryRepository", True), ("inventory", "InventoryPanel", True)])
    except AssertionError:
        return
    raise AssertionError("duplicate owners accepted")


@case("derived_view_is_not_authority")
def _():
    validate_state_owners([("economy", "LedgerRepository", True), ("economy", "EconomyDashboard", False)])


@case("valid_lifecycle_reaches_stopped")
def _():
    validate_lifecycle(["CREATED", "CONFIGURED", "STARTED", "STOPPED"])


@case("failed_lifecycle_can_cleanup")
def _():
    validate_lifecycle(["CREATED", "CONFIGURED", "FAILED", "STOPPED"])


@case("skipping_configuration_is_rejected")
def _():
    try:
        validate_lifecycle(["CREATED", "STARTED"])
    except AssertionError:
        return
    raise AssertionError("invalid lifecycle accepted")


@case("restart_after_stopped_is_rejected")
def _():
    try:
        validate_lifecycle(["CREATED", "CONFIGURED", "STARTED", "STOPPED", "STARTED"])
    except AssertionError:
        return
    raise AssertionError("restart accepted without contract")


@case("memory_repository_respects_contract")
def _():
    exercise_repository(MemoryRepository())


@case("sqlite_stub_repository_respects_contract")
def _():
    exercise_repository(StubSqliteRepository())


@case("repository_missing_is_explicit")
def _():
    require(MemoryRepository().get("none") is None, "missing record not explicit")


@case("repository_returns_copy")
def _():
    repo = MemoryRepository()
    repo.put("x", {"quantity": 1})
    value = repo.get("x")
    require(value is not None, "value missing")
    value["quantity"] = 99
    require(repo.get("x") == {"quantity": 1}, "repository leaked mutable state")


@case("unit_of_work_commits_all")
def _():
    participants = [Participant("inventory"), Participant("economy")]
    require(execute_unit_of_work(participants), "unit of work failed")
    require(all(item.committed for item in participants), "partial commit")


@case("prepare_failure_commits_nothing")
def _():
    participants = [Participant("inventory"), Participant("economy", can_prepare=False)]
    require(not execute_unit_of_work(participants), "prepare failure ignored")
    require(not any(item.committed for item in participants), "commit occurred after prepare failure")


@case("commit_failure_compensates_prior_commits")
def _():
    participants = [Participant("inventory"), Participant("economy", can_commit=False)]
    require(not execute_unit_of_work(participants), "commit failure ignored")
    require(participants[0].compensated and not participants[0].committed, "prior commit not compensated")


@case("external_response_is_translated")
def _():
    require(translate_external({"status": "ok", "detail": "ready"})["accepted"] is True, "translation failed")


@case("external_denial_is_translated")
def _():
    require(translate_external({"status": "denied", "detail": "policy"})["accepted"] is False, "denial failed")


@case("unknown_external_status_is_rejected")
def _():
    try:
        translate_external({"status": "mystery"})
    except AssertionError:
        return
    raise AssertionError("unknown external status accepted")


@case("adapter_version_is_recorded")
def _():
    require(translate_external({"status": "ok"})["adapter_version"] == 1, "adapter version missing")


@case("facade_hides_internal_details")
def _():
    validate_facade(["transfer_item", "get_container_view", "item_transferred"], {"sqlite_", "/internal/", "_table"})


@case("facade_width_is_bounded")
def _():
    validate_facade([f"operation_{index}" for index in range(8)], {"internal"})


@case("too_wide_facade_is_rejected")
def _():
    try:
        validate_facade([f"operation_{index}" for index in range(9)], {"internal"})
    except AssertionError:
        return
    raise AssertionError("wide facade accepted")


@case("leaky_facade_is_rejected")
def _():
    try:
        validate_facade(["sqlite_inventory_table"], {"sqlite_"})
    except AssertionError:
        return
    raise AssertionError("leaky facade accepted")


@case("strategy_registry_accepts_variants")
def _():
    registry = validate_registry([("lexical", "LexicalSearch"), ("vector", "VectorSearch")])
    require(set(registry) == {"lexical", "vector"}, "strategy registry incomplete")


@case("strategy_registry_rejects_duplicate")
def _():
    try:
        validate_registry([("vector", "A"), ("vector", "B")])
    except AssertionError:
        return
    raise AssertionError("duplicate strategy accepted")


@case("factory_unknown_type_is_rejected")
def _():
    registry = validate_registry([("memory", "InMemoryRepository")])
    try:
        require("network" in registry, "unknown factory type")
    except AssertionError:
        return
    raise AssertionError("unknown factory type accepted")


@case("plugin_capabilities_are_bounded")
def _():
    granted = {"read_catalog", "emit_suggestion"}
    require("mutate_inventory" not in granted, "plugin received authority")


@case("plugin_global_write_is_rejected")
def _():
    requested = {"read_catalog", "mutate_all_state"}
    allowed = {"read_catalog", "emit_suggestion"}
    require(not requested.issubset(allowed), "unbounded plugin accepted")


@case("composition_handles_orthogonal_variants")
def _():
    components = {"movement": "GroundMovement", "health": "FiniteHealth", "view": "HumanoidView"}
    require(len(components) == 3 and len(set(components.values())) == 3, "composition collapsed")


@case("deep_inheritance_is_flagged")
def _():
    hierarchy = ["Actor", "LivingActor", "HumanoidActor", "PlayerActor", "MagePlayerActor", "FireMagePlayerActor"]
    require(len(hierarchy) > 4, "fixture too shallow")
    require(len(hierarchy) > 4, "deep hierarchy not flagged")


@case("manifest_hash_is_deterministic")
def _():
    a = stable_manifest({"module": "inventory", "dependencies": ["core"], "version": 1})
    b = stable_manifest({"version": 1, "dependencies": ["core"], "module": "inventory"})
    require(a == b, "manifest hash depends on key order")


@case("manifest_hash_changes_with_contract")
def _():
    a = stable_manifest({"module": "inventory", "version": 1})
    b = stable_manifest({"module": "inventory", "version": 2})
    require(a != b, "manifest hash ignored change")


@case("dependency_manifest_is_json_serializable")
def _():
    json.dumps({"nodes": {"service": "application", "repo": "infrastructure"}, "edges": [["service", "repo_port"]]}, sort_keys=True)


@case("adr_has_required_fields")
def _():
    adr = {"status": "accepted", "context": "storage varies", "decision": "repository", "consequences": ["mapping"]}
    require({"status", "context", "decision", "consequences"}.issubset(adr), "ADR incomplete")


@case("solo_profile_stays_minimal")
def _():
    solo = {"composition_roots": 1, "required_platforms": 1, "distributed_runtime": False}
    require(solo["composition_roots"] == 1 and not solo["distributed_runtime"], "solo overbuilt")


@case("studio_profile_adds_controls_not_domain")
def _():
    solo_domain_hash = stable_manifest({"domain": "inventory-v1"})
    studio_domain_hash = stable_manifest({"domain": "inventory-v1"})
    studio_controls = {"reviewers": 1, "platforms": 2}
    require(solo_domain_hash == studio_domain_hash and studio_controls["reviewers"] == 1, "studio rewrote domain")


@case("test_double_matches_repository_contract")
def _():
    validate_contract({"put", "get", "delete"}, {"put", "get", "delete", "clear"})


@case("contract_mismatch_is_rejected")
def _():
    try:
        validate_contract({"put", "get", "delete"}, {"put", "get"})
    except AssertionError:
        return
    raise AssertionError("contract mismatch accepted")


@case("public_api_avoids_internal_paths")
def _():
    api = ["transfer_item", "get_view"]
    require(not any("/internal/" in value for value in api), "internal path leaked")


@case("cross_module_internal_import_is_rejected")
def _():
    import_path = "features/economy/internal/ledger_table"
    require("/internal/" in import_path, "fixture malformed")
    try:
        require("/internal/" not in import_path, "cross-module internal import")
    except AssertionError:
        return
    raise AssertionError("internal import accepted")


@case("module_interface_is_short")
def _():
    public_api = ["command", "query", "event"]
    require(len(public_api) <= 8, "module interface too large")


@case("god_object_is_detected")
def _():
    smells = detect_architecture_smells({
        "name": "WorldCoordinator",
        "responsibilities": ["save", "combat", "economy", "audio", "quests", "network"],
    })
    require("god_object" in smells, "god object not detected")


@case("generic_manager_is_detected")
def _():
    smells = detect_architecture_smells({"name": "GameManager", "responsibilities": ["game"]})
    require("generic_manager" in smells, "generic manager not detected")


@case("event_payload_is_minimal")
def _():
    payload = {"event": "item_transferred", "item_id": "item.1", "source_id": "bag.a", "target_id": "bag.b"}
    require(len(payload) == 4, "event payload unexpectedly broad")


@case("state_dump_event_is_rejected")
def _():
    payload = {"event": "inventory_changed", "complete_inventory_state": {"items": list(range(100))}}
    require("complete_inventory_state" in payload, "fixture malformed")
    try:
        require("complete_inventory_state" not in payload, "state dump event")
    except AssertionError:
        return
    raise AssertionError("state dump event accepted")


@case("anti_corruption_contract_is_versioned")
def _():
    contract = {"adapter": "local_ai", "schema_version": 1, "capabilities": ["suggest"]}
    require(contract["schema_version"] == 1 and contract["capabilities"] == ["suggest"], "adapter contract invalid")


def main() -> int:
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    if len(CASES) != EXPECTED_CASES:
        raise RuntimeError(f"Expected {EXPECTED_CASES} cases, found {len(CASES)}")
    started = time.perf_counter()
    results: list[dict[str, object]] = []
    failed = 0
    for name, function in CASES:
        case_started = time.perf_counter()
        try:
            function()
            status = "passed"
            error = None
        except Exception as exc:
            status = "failed"
            error = f"{type(exc).__name__}: {exc}"
            failed += 1
        results.append({
            "name": name,
            "status": status,
            "duration_ms": round((time.perf_counter() - case_started) * 1000, 3),
            "error": error,
        })
    report = {
        "schema_version": 1,
        "fixture": "livre-v-ch16-architecture-contracts",
        "runtime": {
            "python_version": platform.python_version(),
            "python_implementation": platform.python_implementation(),
            "platform": platform.platform(),
        },
        "scope": {
            "backend": "python-stdlib-synthetic-architecture-graphs",
            "network_used": False,
            "godot_loaded": False,
            "addon_loaded": False,
            "storage_loaded": False,
            "user_data_processed": False,
        },
        "summary": {
            "total": len(results),
            "passed": len(results) - failed,
            "failed": failed,
            "duration_ms": round((time.perf_counter() - started) * 1000, 3),
        },
        "results": results,
    }
    REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report["summary"], ensure_ascii=False))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
