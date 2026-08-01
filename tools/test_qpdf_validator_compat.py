#!/usr/bin/env python3
"""Lightweight tests for the qpdf validator compatibility adapter."""
from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "tools" / "qpdf_validator_compat.py"
SPEC = importlib.util.spec_from_file_location("qpdf_validator_compat", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("impossible de charger qpdf_validator_compat.py")
COMPAT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(COMPAT)


class MarkInfoCompatibilityTests(unittest.TestCase):
    def test_indirect_markinfo_reference_is_detected(self) -> None:
        catalog = "<< /Type /Catalog /MarkInfo 42 0 R /StructTreeRoot 8 0 R >>"
        self.assertEqual(COMPAT.markinfo_object_id(catalog), "42,0")

    def test_inline_markinfo_needs_no_dereference(self) -> None:
        catalog = "<< /MarkInfo << /Marked true >> >>"
        self.assertIsNone(COMPAT.markinfo_object_id(catalog))

    def test_dereferenced_dictionary_is_appended_for_legacy_regex(self) -> None:
        catalog = "<< /MarkInfo 42 0 R >>"
        augmented = COMPAT.append_markinfo_dictionary(
            catalog,
            "<< /Marked true /Suspects false >>\n",
        )
        self.assertIn("/MarkInfo << /Marked true /Suspects false >>", augmented)

    def test_empty_dictionary_is_not_appended(self) -> None:
        catalog = "<< /MarkInfo 42 0 R >>"
        self.assertEqual(
            COMPAT.append_markinfo_dictionary(catalog, "\n"),
            catalog,
        )


if __name__ == "__main__":
    unittest.main()
