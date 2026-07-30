from __future__ import annotations

import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


generator = load_module("generator", ROOT / "scripts/generate_document.py")
validator = load_module("validator", ROOT / "scripts/validate_documentation_library.py")


class DocumentationLibraryTests(unittest.TestCase):
    def test_version(self):
        self.assertEqual((ROOT / "VERSION").read_text().strip(), "1.0.0")

    def test_manifest_candidate(self):
        data = json.loads((ROOT / "manifest.json").read_text())
        self.assertEqual(data["id"], "CP-PACK-07-DOCUMENTATION-LIBRARY")
        self.assertEqual(data["version"], "1.0.0")

    def test_catalog_ids_unique(self):
        entries = json.loads((ROOT / "catalog.json").read_text())["entries"]
        self.assertEqual(len(entries), len({entry["id"] for entry in entries}))

    def test_catalog_paths_exist(self):
        entries = json.loads((ROOT / "catalog.json").read_text())["entries"]
        self.assertTrue(all((ROOT / entry["path"]).is_file() for entry in entries))

    def test_template_count(self):
        self.assertEqual(len([p for p in (ROOT / "templates").rglob("*") if p.is_file()]), 13)

    def test_filled_example_count(self):
        self.assertEqual(len([p for p in (ROOT / "examples/filled").rglob("*") if p.is_file()]), 10)

    def test_generator_rejects_missing_token(self):
        with self.assertRaises(ValueError):
            generator.render("{{A}} {{B}}", {"A": "x"})

    def test_generator_rejects_unused_value(self):
        with self.assertRaises(ValueError):
            generator.render("{{A}}", {"A": "x", "B": "y"})

    def test_generator_normalizes_final_newline(self):
        self.assertEqual(generator.render("{{A}}", {"A": "x"}), "x\n")

    def test_generation_plan_is_deterministic(self):
        plan = json.loads((ROOT / "examples/generation-plan.json").read_text())
        for job in plan["jobs"]:
            template = (ROOT / job["template"]).read_text()
            data = json.loads((ROOT / job["data"]).read_text())
            expected = (ROOT / job["output"]).read_text()
            self.assertEqual(generator.render(template, data), expected)

    def test_examples_have_no_placeholders(self):
        for path in (ROOT / "examples/filled").rglob("*"):
            if path.is_file():
                self.assertNotRegex(path.read_text(), r"\{\{[A-Z0-9_]+\}\}")

    def test_markdown_examples_have_usage_markers(self):
        for path in (ROOT / "examples/filled").glob("*.md"):
            self.assertIn("Repères d’utilisation", path.read_text())

    def test_markdown_examples_have_one_h1(self):
        for path in (ROOT / "examples/filled").glob("*.md"):
            text = path.read_text()
            count = sum(1 for line in text.splitlines() if line.startswith("# "))
            self.assertEqual(count, 1, path)

    def test_front_matter_ids_are_ascii(self):
        for path in (ROOT / "examples/filled").glob("*.md"):
            meta = validator.front_matter(path)
            self.assertRegex(meta["id"], r"^[A-Z0-9]+(?:-[A-Z0-9]+)+$")

    def test_validation_yaml_parses(self):
        data = yaml.safe_load((ROOT / "examples/filled/VALIDATION-EXEMPLE.yaml").read_text())
        self.assertEqual(data["status"], "complete")
        self.assertEqual(data["schema-version"], 1)

    def test_no_forbidden_binaries(self):
        forbidden = {".pdf", ".docx", ".epub", ".zip", ".exe", ".dll"}
        self.assertFalse([p for p in ROOT.rglob("*") if p.is_file() and p.suffix.lower() in forbidden])

    def test_checksums_match(self):
        data = json.loads((ROOT / "checksums.json").read_text())
        for rel, expected in data["files"].items():
            self.assertEqual(hashlib.sha256((ROOT / rel).read_bytes()).hexdigest(), expected)

    def test_static_validator_passes(self):
        result = validator.validate(ROOT)
        self.assertEqual(result["errors"], [])
        self.assertEqual(result["status"], "success")


if __name__ == "__main__":
    unittest.main()
