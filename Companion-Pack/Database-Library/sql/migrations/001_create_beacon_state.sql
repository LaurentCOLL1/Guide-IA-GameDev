CREATE TABLE beacon_state (
    beacon_id TEXT PRIMARY KEY,
    is_enabled INTEGER NOT NULL DEFAULT 1
        CHECK (is_enabled IN (0, 1)),
    activation_count INTEGER NOT NULL DEFAULT 0
        CHECK (activation_count >= 0),
    cooldown_remaining REAL NOT NULL DEFAULT 0.0
        CHECK (cooldown_remaining >= 0.0),
    last_activated_at_utc TEXT,
    updated_at_utc TEXT NOT NULL
) STRICT;

CREATE INDEX idx_beacon_state_updated_at
    ON beacon_state(updated_at_utc);
