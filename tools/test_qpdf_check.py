#!/usr/bin/env python3
"""Lightweight tests for qpdf preflight classification."""
from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "tools" / "run_qpdf_check.py"
SPEC = importlib.util.spec_from_file_location("run_qpdf_check", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("impossible de charger run_qpdf_check.py")
QPDF_CHECK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(QPDF_CHECK)


class QpdfClassificationTests(unittest.TestCase):
    def test_clean_result_is_success(self) -> None:
        report = QPDF_CHECK.classify_qpdf_result(
            0,
            "checking file\nNo syntax or stream encoding errors found\n",
        )
        self.assertEqual(report["status"], "success")
        self.assertEqual(report["errors"], [])
        self.assertEqual(report["warnings"], [])
        self.assertTrue(report["completion_marker_present"])

    def test_warning_exit_code_is_reserved_not_blocking(self) -> None:
        report = QPDF_CHECK.classify_qpdf_result(
            3,
            "WARNING: object has a duplicated /Group key\n"
            "qpdf: operation succeeded with warnings\n",
        )
        self.assertEqual(report["status"], "success-with-reservations")
        self.assertEqual(report["errors"], [])
        self.assertIn("qpdf_completed_with_warnings", report["warnings"])
        self.assertIn("qpdf_reported_warnings", report["warnings"])
        self.assertEqual(len(report["warning_lines"]), 2)
        self.assertTrue(report["completion_marker_present"])
        self.assertTrue(report["warning_success_message_present"])
        self.assertFalse(report["clean_integrity_message_present"])

    def test_real_failure_is_blocking(self) -> None:
        report = QPDF_CHECK.classify_qpdf_result(2, "damaged file\n")
        self.assertEqual(report["status"], "failure")
        self.assertIn("qpdf_exit_code:2", report["errors"])
        self.assertIn("qpdf_completion_marker_absent", report["errors"])

    def test_missing_completion_marker_is_blocking(self) -> None:
        report = QPDF_CHECK.classify_qpdf_result(3, "WARNING: incomplete\n")
        self.assertEqual(report["status"], "failure")
        self.assertIn("qpdf_completion_marker_absent", report["errors"])

    def test_clean_marker_does_not_hide_warning_exit_mismatch(self) -> None:
        report = QPDF_CHECK.classify_qpdf_result(
            3,
            "No syntax or stream encoding errors found\n",
        )
        self.assertEqual(report["status"], "failure")
        self.assertIn("qpdf_completion_marker_absent", report["errors"])


if __name__ == "__main__":
    unittest.main()
