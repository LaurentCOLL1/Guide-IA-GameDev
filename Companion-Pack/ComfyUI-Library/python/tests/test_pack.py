from __future__ import annotations
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

PACK = Path(__file__).resolve().parents[2]
TOOLS = PACK / "tools"
sys.path.insert(0, str(TOOLS))

from png_utils import PNG_SIGNATURE, text_chunks, write_checkerboard

class PackTests(unittest.TestCase):
    def load(self, rel: str):
        return json.loads((PACK/rel).read_text(encoding="utf-8"))

    def test_manifest_version(self):
        self.assertEqual(self.load("manifest.json")["version"], (PACK/"VERSION").read_text().strip())

    def test_catalog_workflows(self):
        self.assertEqual(self.load("catalog.json")["workflows"], ["WF-COMFY-0001","WF-COMFY-0100"])

    def test_validation_workflow_has_only_builtin_copy_nodes(self):
        api=self.load("workflows/api/WF-COMFY-0001-validation-copy.json")
        self.assertEqual({node["class_type"] for node in api.values()}, {"LoadImage","SaveImage"})

    def test_validation_manifest_has_no_model_or_custom_node(self):
        manifest=self.load("manifests/workflows/WF-COMFY-0001.yaml")
        self.assertEqual(manifest["models"], [])
        self.assertEqual(manifest["custom_nodes"], [])

    def test_template_stays_unexecuted(self):
        manifest=self.load("manifests/workflows/WF-COMFY-0100.yaml")
        self.assertEqual(manifest["status"], "review")
        self.assertFalse(manifest["backend"]["executed"])

    def test_model_is_excluded(self):
        model=self.load("manifests/models/MODELS.yaml")["models"][0]
        self.assertEqual(model["redistribution"], "excluded")
        self.assertIsNone(model["sha256"])

    def test_custom_node_auto_install_is_disabled(self):
        policy=self.load("manifests/custom-nodes/CUSTOM-NODES.yaml")["installation_policy"]
        self.assertFalse(policy["automatic"])

    def test_profiles_are_distinct(self):
        ids={self.load(f"presets/{name}.yaml")["id"] for name in ("cpu","amd","quality")}
        self.assertEqual(len(ids),3)

    def test_png_generator_is_deterministic(self):
        with tempfile.TemporaryDirectory() as tmp:
            a=Path(tmp)/"a.png"; b=Path(tmp)/"b.png"
            write_checkerboard(a); write_checkerboard(b)
            self.assertEqual(hashlib.sha256(a.read_bytes()).hexdigest(), hashlib.sha256(b.read_bytes()).hexdigest())

    def test_png_signature(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/"test.png"; write_checkerboard(path)
            self.assertTrue(path.read_bytes().startswith(PNG_SIGNATURE))

    def test_plain_png_has_no_metadata(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/"test.png"; write_checkerboard(path)
            self.assertEqual(text_chunks(path), {})

    def test_no_model_binaries(self):
        forbidden={".safetensors",".ckpt",".pt",".pth",".bin",".onnx",".gguf"}
        self.assertFalse([p for p in PACK.rglob("*") if p.is_file() and p.suffix.lower() in forbidden])

if __name__=="__main__":
    unittest.main()
