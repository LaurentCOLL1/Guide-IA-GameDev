from __future__ import annotations

import hashlib
import json
import re
import tracemalloc
from pathlib import Path
from typing import Any

TOKEN_RE = re.compile(r"[\wÀ-ÿ]+", re.UNICODE)


def cpu_workload(seed: int, iterations: int, payload_bytes: int) -> str:
    state = hashlib.sha256(str(seed).encode("ascii")).digest()
    payload = bytes((i + seed) % 251 for i in range(payload_bytes))
    for index in range(iterations):
        state = hashlib.sha256(state + payload + index.to_bytes(8, "little")).digest()
    return state.hex()


def memory_workload(seed: int, items: int) -> tuple[int, int]:
    tracemalloc.start()
    values = [((index * 48271) + seed) % 2147483647 for index in range(items)]
    checksum = sum(values[:: max(1, items // 1024)]) % 2147483647
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return checksum, peak


def tokenize(text: str) -> set[str]:
    return {token.casefold() for token in TOKEN_RE.findall(text)}


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def retrieve(query: str, documents: list[dict[str, Any]]) -> str:
    query_tokens = tokenize(query)
    scored: list[tuple[int, str]] = []
    for document in documents:
        document_tokens = tokenize(document["title"] + " " + document["text"] + " " + " ".join(document.get("tags", [])))
        scored.append((len(query_tokens & document_tokens), document["id"]))
    scored.sort(key=lambda item: (-item[0], item[1]))
    return scored[0][1]


def corpus_workload(documents_path: Path, queries_path: Path, repeats: int) -> tuple[str, float]:
    documents = load_jsonl(documents_path)
    queries = load_jsonl(queries_path)
    hits = 0
    digest = hashlib.sha256()
    for repeat in range(repeats):
        for query in queries:
            result = retrieve(query["query"], documents)
            hits += int(result == query["expected_id"])
            digest.update(f"{repeat}:{result}".encode("utf-8"))
    accuracy = hits / (len(queries) * repeats)
    return digest.hexdigest(), accuracy
