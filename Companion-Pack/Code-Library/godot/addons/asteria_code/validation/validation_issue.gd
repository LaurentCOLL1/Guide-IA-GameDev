extends RefCounted
class_name ValidationIssue

var code: String
var message: String
var path: String
var severity: String

func _init(p_code: String, p_message: String, p_path: String = "", p_severity: String = "error") -> void:
    code = p_code
    message = p_message
    path = p_path
    severity = p_severity
