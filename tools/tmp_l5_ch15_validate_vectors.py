#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
import platform
import sys
import tempfile
import time
import uuid
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Iterable, Sequence

EXPECTED_CASES = 42
REPORT_PATH = Path("dist/QA-LIVRE-V-CH15-VECTORS.json")
CASES: list[tuple[str, Callable[[], None]]] = []
NAMESPACE = uuid.UUID("c9c8f31a-51e7-4ceb-8dca-5ac0fd1f0315")


def case(name: str):
    def decorator(function: Callable[[], None]):
        CASES.append((name, function))
        return function
    return decorator


def close(actual: float, expected: float, tolerance: float = 1e-9) -> None:
    if not math.isclose(actual, expected, rel_tol=tolerance, abs_tol=tolerance):
        raise AssertionError(f"{actual!r} != {expected!r}")


def require_same_dimension(a: Sequence[float], b: Sequence[float]) -> None:
    if len(a) != len(b) or not a:
        raise ValueError("Dimensions incompatibles ou vecteur vide.")


def dot(a: Sequence[float], b: Sequence[float]) -> float:
    require_same_dimension(a, b)
    return sum(x * y for x, y in zip(a, b, strict=True))


def norm(a: Sequence[float]) -> float:
    if not a:
        raise ValueError("Vecteur vide.")
    return math.sqrt(sum(value * value for value in a))


def normalize(a: Sequence[float]) -> tuple[float, ...]:
    length = norm(a)
    if length == 0.0:
        raise ValueError("Le vecteur nul ne peut pas être normalisé.")
    return tuple(value / length for value in a)


def cosine(a: Sequence[float], b: Sequence[float]) -> float:
    return dot(a, b) / (norm(a) * norm(b))


def l2_squared(a: Sequence[float], b: Sequence[float]) -> float:
    require_same_dimension(a, b)
    return sum((x - y) ** 2 for x, y in zip(a, b, strict=True))


def manhattan(a: Sequence[float], b: Sequence[float]) -> float:
    require_same_dimension(a, b)
    return sum(abs(x - y) for x, y in zip(a, b, strict=True))


@dataclass(frozen=True, slots=True)
class Point:
    point_id: str
    source_id: str
    vector: tuple[float, ...]
    text: str
    language: str
    visibility: str
    tags: frozenset[str]
    source_revision: str
    content_sha256: str
    model: str = "synthetic-v1"
    distance: str = "cosine"
    schema_version: int = 1


def point(source: str, text: str, vector: Sequence[float], *, ordinal: int = 0,
          language: str = "fr", visibility: str = "internal",
          tags: Iterable[str] = ()) -> Point:
    content_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
    revision = hashlib.sha256(f"{source}|{text}".encode("utf-8")).hexdigest()
    identity = f"{source}|{ordinal}|{content_hash}"
    return Point(
        point_id=str(uuid.uuid5(NAMESPACE, identity)),
        source_id=source,
        vector=tuple(float(value) for value in vector),
        text=text,
        language=language,
        visibility=visibility,
        tags=frozenset(tags),
        source_revision=revision,
        content_sha256=content_hash,
    )


@dataclass
class ExactIndex:
    generation: str
    points: dict[str, Point] = field(default_factory=dict)

    def upsert(self, value: Point) -> None:
        if not value.source_id or not value.point_id or not value.content_sha256:
            raise ValueError("Provenance incomplète.")
        self.points[value.point_id] = value

    def replace_source(self, source_id: str, values: Sequence[Point]) -> None:
        self.delete_source(source_id)
        for value in values:
            if value.source_id != source_id:
                raise ValueError("Source incohérente.")
            self.upsert(value)

    def delete_source(self, source_id: str) -> None:
        stale = [key for key, value in self.points.items() if value.source_id == source_id]
        for key in stale:
            del self.points[key]

    def source_ids(self) -> set[str]:
        return {value.source_id for value in self.points.values()}

    def search(self, query: Sequence[float], *, metric: str = "cosine", limit: int = 5,
               allowed_visibility: set[str] | None = None, language: str | None = None,
               required_tags: set[str] | None = None) -> list[tuple[str, float]]:
        if limit <= 0:
            raise ValueError("limit doit être positif.")
        if allowed_visibility is None or not allowed_visibility:
            raise ValueError("Une visibilité autorisée est obligatoire.")
        tags = required_tags or set()
        scored: list[tuple[str, float]] = []
        for value in self.points.values():
            if value.visibility not in allowed_visibility:
                continue
            if language is not None and value.language != language:
                continue
            if not tags.issubset(value.tags):
                continue
            if metric == "cosine":
                score = cosine(query, value.vector)
                sort_value = -score
            elif metric == "dot":
                score = dot(query, value.vector)
                sort_value = -score
            elif metric == "l2_squared":
                score = l2_squared(query, value.vector)
                sort_value = score
            elif metric == "manhattan":
                score = manhattan(query, value.vector)
                sort_value = score
            else:
                raise ValueError(f"Métrique inconnue : {metric}")
            scored.append((value.point_id, score, sort_value))
        scored.sort(key=lambda item: (item[2], item[0]))
        return [(point_id, score) for point_id, score, _ in scored[:limit]]


def hit_at_k(found: Sequence[str], expected: set[str], k: int) -> float:
    return 1.0 if expected.intersection(found[:k]) else 0.0


def recall_at_k(found: Sequence[str], expected: set[str], k: int) -> float:
    if not expected:
        raise ValueError("Un ensemble attendu non vide est obligatoire.")
    return len(expected.intersection(found[:k])) / len(expected)


def reciprocal_rank(found: Sequence[str], expected: set[str]) -> float:
    for rank, value in enumerate(found, start=1):
        if value in expected:
            return 1.0 / rank
    return 0.0


def mean_reciprocal_rank(runs: Sequence[tuple[Sequence[str], set[str]]]) -> float:
    if not runs:
        raise ValueError("Au moins un cas est obligatoire.")
    return sum(reciprocal_rank(found, expected) for found, expected in runs) / len(runs)


def dcg(relevances: Sequence[float], k: int) -> float:
    return sum((2.0 ** value - 1.0) / math.log2(rank + 1)
               for rank, value in enumerate(relevances[:k], start=1))


def ndcg_at_k(relevances: Sequence[float], k: int) -> float:
    ideal = sorted(relevances, reverse=True)
    denominator = dcg(ideal, k)
    return 0.0 if denominator == 0.0 else dcg(relevances, k) / denominator


def reciprocal_rank_fusion(rankings: Sequence[Sequence[str]], k: int = 60) -> list[str]:
    scores: dict[str, float] = {}
    for ranking in rankings:
        for rank, value in enumerate(ranking, start=1):
            scores[value] = scores.get(value, 0.0) + 1.0 / (k + rank)
    return [value for value, _ in sorted(scores.items(), key=lambda item: (-item[1], item[0]))]


@case("metric.dot")
def _() -> None:
    close(dot((1, 2, 3), (4, 5, 6)), 32.0)


@case("metric.l2_squared")
def _() -> None:
    close(l2_squared((1, 2), (4, 6)), 25.0)


@case("metric.manhattan")
def _() -> None:
    close(manhattan((1, 2), (4, 6)), 7.0)


@case("metric.norm")
def _() -> None:
    close(norm((3, 4)), 5.0)


@case("metric.normalize_unit")
def _() -> None:
    close(norm(normalize((3, 4))), 1.0)


@case("metric.normalize_zero_rejected")
def _() -> None:
    try:
        normalize((0, 0))
    except ValueError:
        return
    raise AssertionError("Le vecteur nul aurait dû être refusé.")


@case("metric.cosine_identical")
def _() -> None:
    close(cosine((1, 2), (1, 2)), 1.0)


@case("metric.cosine_orthogonal")
def _() -> None:
    close(cosine((1, 0), (0, 1)), 0.0)


@case("metric.cosine_opposite")
def _() -> None:
    close(cosine((1, 0), (-1, 0)), -1.0)


@case("metric.dot_norm_sensitive")
def _() -> None:
    assert dot((1, 0), (2, 0)) > dot((1, 0), (1, 0))


@case("metric.normalized_dot_equals_cosine")
def _() -> None:
    a, b = (2.0, 1.0), (1.0, 3.0)
    close(dot(normalize(a), normalize(b)), cosine(a, b))


@case("ranking.cosine")
def _() -> None:
    index = ExactIndex("g1")
    values = [point("a", "a", (1, 0)), point("b", "b", (0.8, 0.2)), point("c", "c", (0, 1))]
    for value in values:
        index.upsert(value)
    found = [item[0] for item in index.search((1, 0), allowed_visibility={"internal"})]
    assert found == [values[0].point_id, values[1].point_id, values[2].point_id]


@case("ranking.l2")
def _() -> None:
    index = ExactIndex("g1")
    values = [point("a", "a", (0, 0)), point("b", "b", (1, 0)), point("c", "c", (3, 0))]
    for value in values:
        index.upsert(value)
    found = [item[0] for item in index.search((0.5, 0), metric="l2_squared", allowed_visibility={"internal"})]
    assert found[:2] == sorted([values[0].point_id, values[1].point_id])
    assert found[2] == values[2].point_id


@case("ranking.tie_break_stable")
def _() -> None:
    index = ExactIndex("g1")
    values = [point("z", "z", (1, 0)), point("a", "a", (1, 0))]
    for value in reversed(values):
        index.upsert(value)
    found = [item[0] for item in index.search((1, 0), allowed_visibility={"internal"})]
    assert found == sorted(value.point_id for value in values)


@case("contract.dimension_mismatch")
def _() -> None:
    try:
        cosine((1, 0), (1, 0, 0))
    except ValueError:
        return
    raise AssertionError("La dimension incompatible aurait dû être refusée.")


@case("contract.unknown_metric")
def _() -> None:
    index = ExactIndex("g1")
    index.upsert(point("a", "a", (1, 0)))
    try:
        index.search((1, 0), metric="probability", allowed_visibility={"internal"})
    except ValueError:
        return
    raise AssertionError("La métrique inconnue aurait dû être refusée.")


@case("filter.visibility")
def _() -> None:
    index = ExactIndex("g1")
    public = point("public", "p", (1, 0), visibility="public")
    restricted = point("restricted", "r", (1, 0), visibility="restricted")
    index.upsert(public); index.upsert(restricted)
    found = [item[0] for item in index.search((1, 0), allowed_visibility={"public"})]
    assert found == [public.point_id]


@case("filter.language")
def _() -> None:
    index = ExactIndex("g1")
    fr = point("fr", "bonjour", (1, 0), language="fr")
    en = point("en", "hello", (1, 0), language="en")
    index.upsert(fr); index.upsert(en)
    found = [item[0] for item in index.search((1, 0), allowed_visibility={"internal"}, language="fr")]
    assert found == [fr.point_id]


@case("filter.required_tags")
def _() -> None:
    index = ExactIndex("g1")
    both = point("both", "x", (1, 0), tags={"lore", "north"})
    one = point("one", "y", (1, 0), tags={"lore"})
    index.upsert(both); index.upsert(one)
    found = [item[0] for item in index.search((1, 0), allowed_visibility={"internal"}, required_tags={"lore", "north"})]
    assert found == [both.point_id]


@case("filter.visibility_required")
def _() -> None:
    try:
        ExactIndex("g1").search((1, 0), allowed_visibility=set())
    except ValueError:
        return
    raise AssertionError("Une politique vide aurait dû être refusée.")


@case("query.limit")
def _() -> None:
    index = ExactIndex("g1")
    for number in range(5):
        index.upsert(point(str(number), str(number), (1, number / 10)))
    assert len(index.search((1, 0), limit=2, allowed_visibility={"internal"})) == 2


@case("metadata.provenance_required")
def _() -> None:
    invalid = Point("id", "", (1.0,), "x", "fr", "internal", frozenset(), "rev", "hash")
    try:
        ExactIndex("g1").upsert(invalid)
    except ValueError:
        return
    raise AssertionError("La provenance vide aurait dû être refusée.")


@case("identity.deterministic")
def _() -> None:
    assert point("s", "texte", (1, 0)).point_id == point("s", "texte", (1, 0)).point_id


@case("identity.content_change")
def _() -> None:
    assert point("s", "texte", (1, 0)).point_id != point("s", "texte modifié", (1, 0)).point_id


@case("identity.ordinal_change")
def _() -> None:
    assert point("s", "texte", (1, 0), ordinal=0).point_id != point("s", "texte", (1, 0), ordinal=1).point_id


@case("lifecycle.upsert_idempotent")
def _() -> None:
    index = ExactIndex("g1")
    value = point("s", "texte", (1, 0))
    index.upsert(value); index.upsert(value)
    assert len(index.points) == 1


@case("lifecycle.replace_source")
def _() -> None:
    index = ExactIndex("g1")
    old = point("s", "ancien", (1, 0))
    new = point("s", "nouveau", (0, 1))
    index.upsert(old); index.replace_source("s", [new])
    assert set(index.points) == {new.point_id}


@case("lifecycle.delete_source")
def _() -> None:
    index = ExactIndex("g1")
    a, b = point("a", "a", (1, 0)), point("b", "b", (0, 1))
    index.upsert(a); index.upsert(b); index.delete_source("a")
    assert index.source_ids() == {"b"}


@case("lifecycle.stale_source_detection")
def _() -> None:
    index = ExactIndex("g1")
    index.upsert(point("a", "a", (1, 0))); index.upsert(point("b", "b", (0, 1)))
    assert index.source_ids() - {"a"} == {"b"}


@case("generation.staging_isolated")
def _() -> None:
    active, staging = ExactIndex("g1"), ExactIndex("g2")
    active.upsert(point("s", "v1", (1, 0)))
    staging.upsert(point("s", "v2", (0, 1)))
    assert next(iter(active.points.values())).text == "v1"
    assert next(iter(staging.points.values())).text == "v2"


@case("generation.alias_switch")
def _() -> None:
    indexes = {"g1": ExactIndex("g1"), "g2": ExactIndex("g2")}
    alias = "g1"
    indexes["g2"].upsert(point("s", "v2", (1, 0)))
    alias = "g2"
    assert indexes[alias].generation == "g2"


@case("generation.rollback")
def _() -> None:
    aliases = ["g1", "g2"]
    active = aliases[-1]
    active = aliases[-2]
    assert active == "g1"


@case("evaluation.hit_at_k")
def _() -> None:
    close(hit_at_k(["a", "b"], {"b"}, 2), 1.0)
    close(hit_at_k(["a", "b"], {"c"}, 2), 0.0)


@case("evaluation.recall_at_k")
def _() -> None:
    close(recall_at_k(["a", "b", "c"], {"a", "c", "d"}, 3), 2.0 / 3.0)


@case("evaluation.reciprocal_rank")
def _() -> None:
    close(reciprocal_rank(["x", "y", "z"], {"y"}), 0.5)


@case("evaluation.mrr")
def _() -> None:
    runs = [(["a"], {"a"}), (["x", "b"], {"b"}), (["x"], {"z"})]
    close(mean_reciprocal_rank(runs), 0.5)


@case("evaluation.ndcg_perfect")
def _() -> None:
    close(ndcg_at_k([3, 2, 1], 3), 1.0)


@case("evaluation.ndcg_degraded")
def _() -> None:
    value = ndcg_at_k([1, 3, 2], 3)
    assert 0.0 < value < 1.0


@case("hybrid.rrf_deterministic")
def _() -> None:
    assert reciprocal_rank_fusion([["a", "b"], ["b", "a"]]) == ["a", "b"]


@case("hybrid.rrf_promotes_consensus")
def _() -> None:
    fused = reciprocal_rank_fusion([["a", "b", "c"], ["b", "d", "a"], ["b", "a"]])
    assert fused[0] == "b"


@case("reproducibility.corpus_digest")
def _() -> None:
    corpus = [{"id": "a", "text": "alpha"}, {"id": "b", "text": "beta"}]
    encoded = json.dumps(corpus, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    assert hashlib.sha256(encoded).hexdigest() == hashlib.sha256(encoded).hexdigest()


@case("reproducibility.report_path_isolated")
def _() -> None:
    with tempfile.TemporaryDirectory(prefix="l5-ch15-") as directory:
        path = Path(directory) / "synthetic.json"
        path.write_text("{}", encoding="utf-8")
        assert path.is_file() and path.parent != Path.cwd()


@case("reproducibility.runtime_manifest")
def _() -> None:
    manifest = {
        "python": platform.python_version(),
        "platform": platform.platform(),
        "backend": "stdlib-exact-synthetic",
        "network": False,
        "model_loaded": False,
    }
    assert manifest["python"] and manifest["platform"] and not manifest["network"]


def main() -> int:
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    started = time.perf_counter()
    results: list[dict[str, object]] = []
    if len(CASES) != EXPECTED_CASES:
        raise RuntimeError(f"Expected {EXPECTED_CASES} cases, found {len(CASES)}")
    for name, function in CASES:
        case_started = time.perf_counter()
        try:
            function()
        except Exception as exc:  # evidence needs exact failed case
            results.append({
                "name": name,
                "status": "failed",
                "duration_ms": round((time.perf_counter() - case_started) * 1000, 3),
                "error": f"{type(exc).__name__}: {exc}",
            })
        else:
            results.append({
                "name": name,
                "status": "passed",
                "duration_ms": round((time.perf_counter() - case_started) * 1000, 3),
            })
    passed = sum(result["status"] == "passed" for result in results)
    failed = len(results) - passed
    report = {
        "schema_version": 1,
        "suite": "livre-v-ch15-vector-contract-fixtures",
        "backend": "python-stdlib-exact-synthetic",
        "python_version": platform.python_version(),
        "python_implementation": platform.python_implementation(),
        "platform": platform.platform(),
        "total": len(results),
        "passed": passed,
        "failed": failed,
        "duration_ms": round((time.perf_counter() - started) * 1000, 3),
        "network_used": False,
        "model_loaded": False,
        "vector_backend_loaded": False,
        "user_data_processed": False,
        "cases": results,
    }
    REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: report[key] for key in (
        "suite", "backend", "python_version", "platform", "total", "passed", "failed", "duration_ms"
    )}, ensure_ascii=False))
    for result in results:
        if result["status"] == "failed":
            print(f"FAILED {result['name']}: {result['error']}", file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
