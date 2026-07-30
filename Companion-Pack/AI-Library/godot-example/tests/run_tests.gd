extends SceneTree

var _failures: Array[String] = []

func _initialize() -> void:
	call_deferred("_run")

func _expect(condition: bool, message: String) -> void:
	if not condition:
		_failures.append(message)
		push_error(message)

func _run() -> void:
	var config := AiClientConfig.new()
	_expect(config.validate().is_empty(), "La configuration locale doit être valide.")

	var invalid := AiClientConfig.new()
	invalid.base_url = "http://example.org:8765"
	_expect(not invalid.validate().is_empty(), "Une URL distante doit être refusée.")

	var mapper := OpenAiCompatibleMapper.new()
	var encoded := mapper.encode_chat("gd-1", "mock-model", "Bonjour Godot")
	_expect(encoded.get("stream", true) == false, "Le streaming HTTP doit rester désactivé.")
	_expect(encoded.get("messages", []).size() == 1, "Un message doit être encodé.")

	var http_client := HttpAiClient.new()
	root.add_child(http_client)
	var http_result: Dictionary = await http_client.chat(
		config,
		"gd-http-1",
		"mock-model",
		"Bonjour Godot"
	)
	_expect(http_result.get("ok", false), "L’appel HTTP mock doit réussir.")
	_expect(http_result.get("text", "") == "mock:Bonjour Godot", "La réponse HTTP doit venir du mock.")
	http_client.queue_free()

	var websocket := WebSocketEventClient.new()
	var ws_result: Dictionary = await websocket.receive_progress(
		config.websocket_url,
		"gd-ws-1"
	)
	_expect(ws_result.get("ok", false), "L’événement WebSocket mock doit être reçu.")
	var event: Dictionary = ws_result.get("event", {})
	_expect(event.get("request_id", "") == "gd-ws-1", "La corrélation WebSocket doit être conservée.")

	if _failures.is_empty():
		print("AI_LIBRARY_GODOT_TESTS: PASS")
		quit(0)
	else:
		print("AI_LIBRARY_GODOT_TESTS: FAIL")
		quit(1)
