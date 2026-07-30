from __future__ import annotations
from collections.abc import Callable, Iterable
from dataclasses import dataclass, field
from typing import Any, Literal

Severity = Literal["warning", "error"]

@dataclass(frozen=True, slots=True)
class ValidationIssue:
    code: str
    message: str
    path: str = ""
    severity: Severity = "error"

@dataclass(slots=True)
class ValidationResult:
    issues: list[ValidationIssue] = field(default_factory=list)

    @property
    def is_valid(self) -> bool:
        return not any(issue.severity == "error" for issue in self.issues)

    def add(self, issue: ValidationIssue) -> None:
        self.issues.append(issue)

    def extend(self, issues: Iterable[ValidationIssue]) -> None:
        self.issues.extend(issues)

    def by_severity(self, severity: Severity) -> list[ValidationIssue]:
        return [issue for issue in self.issues if issue.severity == severity]

Rule = Callable[[Any], ValidationIssue | Iterable[ValidationIssue] | None]

class Validator:
    def __init__(self) -> None:
        self._rules: list[Rule] = []

    def add_rule(self, rule: Rule) -> "Validator":
        self._rules.append(rule)
        return self

    def validate(self, value: Any) -> ValidationResult:
        result = ValidationResult()
        for rule in self._rules:
            produced = rule(value)
            if produced is None:
                continue
            if isinstance(produced, ValidationIssue):
                result.add(produced)
            else:
                result.extend(produced)
        return result
