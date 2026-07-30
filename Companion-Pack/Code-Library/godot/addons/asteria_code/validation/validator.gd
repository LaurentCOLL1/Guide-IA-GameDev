extends RefCounted
class_name Validator

var _rules: Array[Callable] = []

func add_rule(rule: Callable) -> Validator:
    _rules.append(rule)
    return self

func validate(value: Variant) -> ValidationResult:
    var result := ValidationResult.new()
    for rule in _rules:
        var produced: Variant = rule.call(value)
        if produced == null:
            continue
        if produced is ValidationIssue:
            result.add(produced)
        elif produced is Array:
            result.extend(produced)
        else:
            result.add(ValidationIssue.new("invalid_rule_result", "Rule returned an unsupported value"))
    return result
