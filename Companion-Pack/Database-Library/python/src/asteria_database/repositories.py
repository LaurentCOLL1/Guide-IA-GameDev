from __future__ import annotations

import json
import sqlite3
from dataclasses import asdict
from typing import Any

from .models import BeaconState, ContentDocument
from .util import utc_now_text


class BeaconStateRepository:
    """Persistent collection of beacon state records."""

    def __init__(self, connection: sqlite3.Connection) -> None:
        self.connection = connection

    def save(self, record: BeaconState) -> None:
        if not record.beacon_id.strip():
            raise ValueError("beacon_id must not be empty")
        if record.activation_count < 0:
            raise ValueError("activation_count must be non-negative")
        if record.cooldown_remaining < 0:
            raise ValueError("cooldown_remaining must be non-negative")
        self.connection.execute(
            """
            INSERT INTO beacon_state(
                beacon_id,
                is_enabled,
                activation_count,
                cooldown_remaining,
                last_activated_at_utc,
                updated_at_utc
            ) VALUES (?, ?, ?, ?, ?, ?)
            ON CONFLICT(beacon_id) DO UPDATE SET
                is_enabled = excluded.is_enabled,
                activation_count = excluded.activation_count,
                cooldown_remaining = excluded.cooldown_remaining,
                last_activated_at_utc = excluded.last_activated_at_utc,
                updated_at_utc = excluded.updated_at_utc
            """,
            (
                record.beacon_id,
                int(record.is_enabled),
                record.activation_count,
                record.cooldown_remaining,
                record.last_activated_at_utc,
                record.updated_at_utc,
            ),
        )

    def find(self, beacon_id: str) -> BeaconState | None:
        row = self.connection.execute(
            """
            SELECT
                beacon_id,
                is_enabled,
                activation_count,
                cooldown_remaining,
                last_activated_at_utc,
                updated_at_utc
            FROM beacon_state
            WHERE beacon_id = ?
            """,
            (beacon_id,),
        ).fetchone()
        return _beacon_from_row(row) if row else None

    def list_all(self) -> tuple[BeaconState, ...]:
        rows = self.connection.execute(
            """
            SELECT
                beacon_id,
                is_enabled,
                activation_count,
                cooldown_remaining,
                last_activated_at_utc,
                updated_at_utc
            FROM beacon_state
            ORDER BY beacon_id
            """
        ).fetchall()
        return tuple(_beacon_from_row(row) for row in rows)

    def delete(self, beacon_id: str) -> bool:
        cursor = self.connection.execute(
            "DELETE FROM beacon_state WHERE beacon_id = ?",
            (beacon_id,),
        )
        return cursor.rowcount > 0

    def add_event(
        self,
        *,
        beacon_id: str,
        actor_id: str,
        occurred_at_utc: str,
    ) -> int:
        cursor = self.connection.execute(
            """
            INSERT INTO beacon_activation_event(
                beacon_id, actor_id, occurred_at_utc
            ) VALUES (?, ?, ?)
            """,
            (beacon_id, actor_id, occurred_at_utc),
        )
        return int(cursor.lastrowid)

    def list_recent_events(
        self,
        beacon_id: str,
        *,
        limit: int = 50,
    ) -> tuple[dict[str, Any], ...]:
        if limit < 1 or limit > 500:
            raise ValueError("limit must be between 1 and 500")
        rows = self.connection.execute(
            """
            SELECT event_id, beacon_id, actor_id, occurred_at_utc
            FROM beacon_activation_event
            WHERE beacon_id = ?
            ORDER BY occurred_at_utc DESC, event_id DESC
            LIMIT ?
            """,
            (beacon_id, limit),
        ).fetchall()
        return tuple(dict(row) for row in rows)


class ContentDocumentRepository:
    """Repository for canonical synthetic content and its normalized tags."""

    def __init__(self, connection: sqlite3.Connection) -> None:
        self.connection = connection

    def save(self, document: ContentDocument) -> None:
        if not document.document_id.strip():
            raise ValueError("document_id must not be empty")
        if not 1 <= len(document.title) <= 200:
            raise ValueError("title length must be between 1 and 200")
        if document.content_version < 1:
            raise ValueError("content_version must be positive")
        self.connection.execute(
            """
            INSERT INTO content_document(
                document_id,
                title,
                body,
                language_code,
                content_version,
                updated_at_utc
            ) VALUES (?, ?, ?, ?, ?, ?)
            ON CONFLICT(document_id) DO UPDATE SET
                title = excluded.title,
                body = excluded.body,
                language_code = excluded.language_code,
                content_version = excluded.content_version,
                updated_at_utc = excluded.updated_at_utc
            """,
            (
                document.document_id,
                document.title,
                document.body,
                document.language_code,
                document.content_version,
                document.updated_at_utc,
            ),
        )

    def upsert_tag(self, tag_id: str, label: str) -> None:
        self.connection.execute(
            """
            INSERT INTO content_tag(tag_id, label)
            VALUES (?, ?)
            ON CONFLICT(tag_id) DO UPDATE SET label = excluded.label
            """,
            (tag_id, label),
        )

    def assign_tag(self, document_id: str, tag_id: str) -> None:
        self.connection.execute(
            """
            INSERT OR IGNORE INTO content_document_tag(document_id, tag_id)
            VALUES (?, ?)
            """,
            (document_id, tag_id),
        )

    def search_by_tag(self, tag_id: str) -> tuple[ContentDocument, ...]:
        rows = self.connection.execute(
            """
            SELECT
                d.document_id,
                d.title,
                d.body,
                d.language_code,
                d.content_version,
                d.updated_at_utc
            FROM content_document AS d
            JOIN content_document_tag AS dt
                ON dt.document_id = d.document_id
            WHERE dt.tag_id = ?
            ORDER BY d.updated_at_utc DESC, d.document_id ASC
            """,
            (tag_id,),
        ).fetchall()
        return tuple(
            ContentDocument(
                document_id=str(row["document_id"]),
                title=str(row["title"]),
                body=str(row["body"]),
                language_code=str(row["language_code"]),
                content_version=int(row["content_version"]),
                updated_at_utc=str(row["updated_at_utc"]),
            )
            for row in rows
        )


def put_derived_cache_entry(
    connection: sqlite3.Connection,
    *,
    cache_key: str,
    source_checksum: str,
    payload: Any,
    expires_at_utc: str | None = None,
) -> None:
    """Store a non-authoritative derived value.

    This helper deliberately does not implement queues, retry policy, LRU, or a
    provider cache. Those concerns remain owned by the AI Library.
    """
    if len(source_checksum) != 64:
        raise ValueError("source_checksum must be a 64-character SHA-256 hex string")
    payload_json = json.dumps(
        payload,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    )
    connection.execute(
        """
        INSERT INTO derived_cache_entry(
            cache_key,
            source_checksum,
            payload_json,
            created_at_utc,
            expires_at_utc
        ) VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(cache_key) DO UPDATE SET
            source_checksum = excluded.source_checksum,
            payload_json = excluded.payload_json,
            created_at_utc = excluded.created_at_utc,
            expires_at_utc = excluded.expires_at_utc
        """,
        (
            cache_key,
            source_checksum,
            payload_json,
            utc_now_text(),
            expires_at_utc,
        ),
    )


def _beacon_from_row(row: sqlite3.Row) -> BeaconState:
    return BeaconState(
        beacon_id=str(row["beacon_id"]),
        is_enabled=bool(row["is_enabled"]),
        activation_count=int(row["activation_count"]),
        cooldown_remaining=float(row["cooldown_remaining"]),
        last_activated_at_utc=(
            str(row["last_activated_at_utc"])
            if row["last_activated_at_utc"] is not None
            else None
        ),
        updated_at_utc=str(row["updated_at_utc"]),
    )
