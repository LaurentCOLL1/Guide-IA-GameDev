class_name WebSocketEventClient
extends RefCounted

func receive_progress(
	url: String,
	request_id: String,
	timeout_ms: int = 3000
) -> Dictionary:
	if not url.begins_with("ws://127.0.0.1:"):
		return {"ok": false, "error": "non_loopback_url"}
	var socket := WebSocketPeer.new()
	var error := socket.connect_to_url(url)
	if error != OK:
		return {"ok": false, "error": "connect_failed", "code": error}

	var deadline := Time.get_ticks_msec() + timeout_ms
	var subscription_sent := false
	while Time.get_ticks_msec() < deadline:
		socket.poll()
		var state := socket.get_ready_state()
		if state == WebSocketPeer.STATE_OPEN and not subscription_sent:
			socket.send_text(JSON.stringify({
				"request_id": request_id,
				"subscribe": "task.progress",
			}))
			subscription_sent = true
		if state == WebSocketPeer.STATE_OPEN and socket.get_available_packet_count() > 0:
			var text := socket.get_packet().get_string_from_utf8()
			var parsed: Variant = JSON.parse_string(text)
			socket.close()
			if parsed is not Dictionary:
				return {"ok": false, "error": "invalid_json"}
			if parsed.get("request_id", "") != request_id:
				return {"ok": false, "error": "correlation_failed"}
			return {"ok": true, "event": parsed}
		if state == WebSocketPeer.STATE_CLOSED:
			return {"ok": false, "error": "closed_before_event"}
		await Engine.get_main_loop().process_frame

	socket.close()
	return {"ok": false, "error": "timeout"}
