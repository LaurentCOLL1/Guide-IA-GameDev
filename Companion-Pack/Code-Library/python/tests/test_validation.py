import unittest
from asteria_code import ValidationIssue, Validator

class ValidationTests(unittest.TestCase):
    def test_composes_issues(self):
        validator = Validator().add_rule(lambda value: ValidationIssue("empty", "required") if not value else None)
        result = validator.validate("")
        self.assertFalse(result.is_valid)
        self.assertEqual(result.issues[0].code, "empty")

    def test_warning_is_not_error(self):
        validator = Validator().add_rule(lambda value: ValidationIssue("short", "short", severity="warning"))
        self.assertTrue(validator.validate("x").is_valid)
