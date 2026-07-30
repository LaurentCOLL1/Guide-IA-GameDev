class_name OpenAiCompatibleMapper
extends RefCounted

func encode_chat(request_id: String, model: String, message: String) -> Dictionary:
	if request_id.is_empty() or model.is_empty() or message.is_empty():
		return {}
	return {
		"model": model,
		"messages": [
			{"role": "user", "content": message},
		],
		"max_tokens": 64,
		"stream": false,
		"metadata": {
			"request_id": request_id,
			"client": "asteria-ai-library-godot",
		},
	}

func decode_chat(request_id: String, payload: Dictionary) -> Dictionary:
	var choices: Array = payload.get("choices", [])
	if choices.is_empty():
		return {"ok": false, "error": "missing_choices"}
	var choice: Dictionary = choices[0]
	var message: Dictionary = choice.get("message", {})
	var content: Variant = message.get("content")
	if content is not String:
		return {"ok": false, "error": "invalid_content"}
	return {
		"ok": true,
		"request_id": request_id,
		"text": content,
		"finish_reason": choice.get("finish_reason", "unknown"),
	}
