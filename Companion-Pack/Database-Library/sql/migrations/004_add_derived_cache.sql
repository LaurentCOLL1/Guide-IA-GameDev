CREATE TABLE derived_cache_entry (
    cache_key TEXT PRIMARY KEY,
    source_checksum TEXT NOT NULL CHECK (length(source_checksum) = 64),
    payload_json TEXT NOT NULL CHECK (json_valid(payload_json)),
    created_at_utc TEXT NOT NULL,
    expires_at_utc TEXT
) STRICT;

CREATE INDEX idx_derived_cache_expires
    ON derived_cache_entry(expires_at_utc);
