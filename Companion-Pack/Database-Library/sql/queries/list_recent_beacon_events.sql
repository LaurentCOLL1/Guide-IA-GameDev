SELECT
    event_id,
    beacon_id,
    actor_id,
    occurred_at_utc
FROM beacon_activation_event
WHERE beacon_id = ?
ORDER BY occurred_at_utc DESC, event_id DESC
LIMIT ?;
