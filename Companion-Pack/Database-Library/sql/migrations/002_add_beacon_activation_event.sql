CREATE TABLE beacon_activation_event (
    event_id INTEGER PRIMARY KEY,
    beacon_id TEXT NOT NULL,
    actor_id TEXT NOT NULL,
    occurred_at_utc TEXT NOT NULL,
    FOREIGN KEY (beacon_id)
        REFERENCES beacon_state(beacon_id)
        ON DELETE CASCADE
) STRICT;

CREATE INDEX idx_beacon_activation_event_beacon_time
    ON beacon_activation_event(beacon_id, occurred_at_utc);
