class_name HttpAiClient
extends Node

func chat(
	config: AiClientConfig,
	request_id: String,
	model: String,
	message: String
) -> Dictionary:
	var errors := config.validate()
	if not errors.is_empty():
		return {"ok": false, "error": "invalid_config", "details": errors}
	var mapper := OpenAiCompatibleMapper.new()
	var payload := mapper.encode_chat(request_id, model, message)
	if payload.is_empty():
		return {"ok": false, "error": "invalid_request"}

	var http := HTTPRequest.new()
	http.timeout = config.request_timeout_seconds
	http.download_chunk_size = 65_536
	add_child(http)

	var headers := PackedStringArray([
		"Content-Type: application/json",
		"Accept: application/json",
		"X-Asteria-Request-Id: " + request_id,
	])
	var error := http.request(
		config.base_url + "/v1/chat/completions",
		headers,
		HTTPClient.METHOD_POST,
		JSON.stringify(payload)
	)
	if error != OK:
		http.queue_free()
		return {"ok": false, "error": "request_start_failed", "code": error}

	var completed: Array = await http.request_completed
	http.queue_free()
	var result_code: int = completed[0]
	var response_code: int = completed[1]
	var body: PackedByteArray = completed[3]
	if result_code != HTTPRequest.RESULT_SUCCESS:
		return {"ok": false, "error": "transport_failed", "code": result_code}
	if response_code < 200 or response_code >= 300:
		return {"ok": false, "error": "http_error", "status": response_code}
	if body.size() > config.max_response_bytes:
		return {"ok": false, "error": "response_too_large"}

	var parsed: Variant = JSON.parse_string(body.get_string_from_utf8())
	if parsed is not Dictionary:
		return {"ok": false, "error": "invalid_json"}
	return mapper.decode_chat(request_id, parsed)
