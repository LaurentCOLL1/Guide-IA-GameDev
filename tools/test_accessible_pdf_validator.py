#!/usr/bin/env python3
"""Lightweight tests for the accessible PDF validator."""
from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "tools" / "validate_accessible_pdf.py"
SPEC = importlib.util.spec_from_file_location("validate_accessible_pdf", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("impossible de charger validate_accessible_pdf.py")
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class SourceMaskingTests(unittest.TestCase):
    def test_code_examples_are_not_audited_as_images(self) -> None:
        source = """\
![Visible](visible.png)
`![](inline-example.png)`
```markdown
![](fenced-example.png)
<img src="fenced.png">
```
<img src="visible-html.png" alt="Visible HTML">
"""
        cleaned = VALIDATOR.strip_code_and_comments(source)
        markdown = [
            match.group(1)
            for match in VALIDATOR.MARKDOWN_INLINE_IMAGE.finditer(cleaned)
        ]
        html_images = list(VALIDATOR.HTML_IMAGE.finditer(cleaned))
        self.assertEqual(markdown, ["Visible"])
        self.assertEqual(len(html_images), 1)
        alt_match = VALIDATOR.HTML_ALT.search(html_images[0].group(1))
        self.assertIsNotNone(alt_match)
        self.assertEqual(alt_match.group(2), "Visible HTML")

    def test_empty_alternatives_remain_detectable(self) -> None:
        source = "![](empty.png)\n<img src=\"empty-html.png\" alt=\"\">\n"
        cleaned = VALIDATOR.strip_code_and_comments(source)
        markdown = next(
            VALIDATOR.MARKDOWN_INLINE_IMAGE.finditer(cleaned)
        )
        html_image = next(VALIDATOR.HTML_IMAGE.finditer(cleaned))
        html_alt = VALIDATOR.HTML_ALT.search(html_image.group(1))
        self.assertEqual(VALIDATOR.normalize_alt(markdown.group(1)), "")
        self.assertIsNotNone(html_alt)
        self.assertEqual(VALIDATOR.normalize_alt(html_alt.group(2)), "")


class VeraPdfParserTests(unittest.TestCase):
    def parse(self, xml: str):
        with tempfile.TemporaryDirectory() as directory:
            report = Path(directory) / "verapdf.xml"
            report.write_text(xml, encoding="utf-8")
            return VALIDATOR.parse_verapdf(report)

    def test_compliant_report_is_not_confused_by_noncompliant_summary(self) -> None:
        result, errors, warnings = self.parse(
            '<validationReport isCompliant="true" failedChecks="0"/>'
            '<batchSummary nonCompliant="0" compliant="1"/>'
        )
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])
        self.assertTrue(result["report_parsed"])
        self.assertTrue(result["machine_compliant"])
        self.assertEqual(result["failed_checks"], 0)

    def test_noncompliant_report_is_a_reservation(self) -> None:
        result, errors, warnings = self.parse(
            '<validationReport isCompliant="false" failedChecks="3"/>'
            '<batchSummary nonCompliant="1" compliant="0"/>'
        )
        self.assertEqual(errors, [])
        self.assertEqual(
            warnings,
            [
                "verapdf_ua1_noncompliance_requires_correction_or_reservation"
            ],
        )
        self.assertTrue(result["report_parsed"])
        self.assertFalse(result["machine_compliant"])
        self.assertEqual(result["failed_checks"], 3)

    def test_unparseable_report_is_blocking(self) -> None:
        result, errors, warnings = self.parse("<report/>")
        self.assertEqual(errors, ["verapdf_result_unparseable"])
        self.assertEqual(warnings, [])
        self.assertFalse(result["report_parsed"])


if __name__ == "__main__":
    unittest.main()
