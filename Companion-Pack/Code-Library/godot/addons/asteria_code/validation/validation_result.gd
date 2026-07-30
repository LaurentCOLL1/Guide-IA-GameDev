extends RefCounted
class_name ValidationResult

var issues: Array[ValidationIssue] = []

func add(issue: ValidationIssue) -> void:
    issues.append(issue)

func extend(new_issues: Array) -> void:
    for issue in new_issues:
        if issue is ValidationIssue:
            issues.append(issue)

func is_valid() -> bool:
    for issue in issues:
        if issue.severity == "error":
            return false
    return true

func by_severity(severity: String) -> Array[ValidationIssue]:
    var result: Array[ValidationIssue] = []
    for issue in issues:
        if issue.severity == severity:
            result.append(issue)
    return result
