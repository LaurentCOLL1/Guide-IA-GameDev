class_name AiClientConfig
extends RefCounted

var base_url: String = "http://127.0.0.1:8765"
var websocket_url: String = "ws://127.0.0.1:8766/events"
var request_timeout_seconds: float = 5.0
var max_response_bytes: int = 4 * 1024 * 1024

func validate() -> PackedStringArray:
	var errors := PackedStringArray()
	if not _is_loopback_url(base_url, "http"):
		errors.append("base_url doit viser la boucle locale avec http")
	if not _is_loopback_url(websocket_url, "ws"):
		errors.append("websocket_url doit viser la boucle locale avec ws")
	if request_timeout_seconds < 0.1 or request_timeout_seconds > 120.0:
		errors.append("request_timeout_seconds hors limites")
	if max_response_bytes < 1024 or max_response_bytes > 32 * 1024 * 1024:
		errors.append("max_response_bytes hors limites")
	return errors

func _is_loopback_url(value: String, scheme: String) -> bool:
	var prefix := scheme + "://127.0.0.1:"
	if not value.begins_with(prefix):
		return false
	var remainder := value.trim_prefix(prefix)
	var slash_index := remainder.find("/")
	var port_text := remainder if slash_index < 0 else remainder.left(slash_index)
	return port_text.is_valid_int() and port_text.to_int() >= 1 and port_text.to_int() <= 65535
