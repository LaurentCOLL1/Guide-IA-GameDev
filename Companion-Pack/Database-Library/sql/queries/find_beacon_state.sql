SELECT
    beacon_id,
    is_enabled,
    activation_count,
    cooldown_remaining,
    last_activated_at_utc,
    updated_at_utc
FROM beacon_state
WHERE beacon_id = ?;
