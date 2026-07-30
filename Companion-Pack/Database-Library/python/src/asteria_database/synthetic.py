from __future__ import annotations

import hashlib
import json
import sqlite3
from pathlib import Path

from .models import BeaconState, ContentDocument
from .repositories import (
    BeaconStateRepository,
    ContentDocumentRepository,
    put_derived_cache_entry,
)
from .util import pack_root


def seed_synthetic_data(
    connection: sqlite3.Connection,
    fixture_path: str | Path | None = None,
) -> dict[str, int]:
    """Load deterministic fictional records through the public repositories."""
    path = (
        Path(fixture_path)
        if fixture_path
        else pack_root() / "data/synthetic/asteria-fixture.json"
    )
    payload = json.loads(path.read_text(encoding="utf-8"))
    if int(payload.get("schema_version", 0)) != 1:
        raise ValueError("unsupported synthetic fixture schema_version")
    if "No personal data" not in str(payload.get("notice", "")):
        raise ValueError("synthetic fixture notice is missing")

    beacon_repository = BeaconStateRepository(connection)
    content_repository = ContentDocumentRepository(connection)

    for item in payload["beacons"]:
        beacon_repository.save(
            BeaconState(
                beacon_id=str(item["beacon_id"]),
                is_enabled=bool(item["is_enabled"]),
                activation_count=int(item["activation_count"]),
                cooldown_remaining=float(item["cooldown_remaining"]),
                last_activated_at_utc=item["last_activated_at_utc"],
                updated_at_utc=str(item["updated_at_utc"]),
            )
        )
    for item in payload["events"]:
        beacon_repository.add_event(
            beacon_id=str(item["beacon_id"]),
            actor_id=str(item["actor_id"]),
            occurred_at_utc=str(item["occurred_at_utc"]),
        )

    for item in payload["documents"]:
        content_repository.save(
            ContentDocument(
                document_id=str(item["document_id"]),
                title=str(item["title"]),
                body=str(item["body"]),
                language_code=str(item["language_code"]),
                content_version=int(item["content_version"]),
                updated_at_utc=str(item["updated_at_utc"]),
            )
        )
    for item in payload["tags"]:
        content_repository.upsert_tag(
            str(item["tag_id"]),
            str(item["label"]),
        )
    for item in payload["document_tags"]:
        content_repository.assign_tag(
            str(item["document_id"]),
            str(item["tag_id"]),
        )
    for item in payload["cache_entries"]:
        put_derived_cache_entry(
            connection,
            cache_key=str(item["cache_key"]),
            source_checksum=hashlib.sha256(
                str(item["source_text"]).encode("utf-8")
            ).hexdigest(),
            payload=item["payload"],
            expires_at_utc=item["expires_at_utc"],
        )

    return {
        "beacons": len(payload["beacons"]),
        "events": len(payload["events"]),
        "documents": len(payload["documents"]),
        "tags": len(payload["tags"]),
        "cache_entries": len(payload["cache_entries"]),
    }
