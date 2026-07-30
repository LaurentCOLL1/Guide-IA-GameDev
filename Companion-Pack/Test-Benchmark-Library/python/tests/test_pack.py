import hashlib, json, unittest
from pathlib import Path
PACK=Path(__file__).resolve().parents[2]
class PackTests(unittest.TestCase):
    def test_version(self): self.assertEqual((PACK/"VERSION").read_text().strip(),"1.0.0")
    def test_contract_count(self): self.assertEqual(len(list((PACK/"contracts").glob("*.json"))),6)
    def test_scenes_exist(self):
        for name in ("cpu_benchmark.tscn","memory_benchmark.tscn","render_proxy_benchmark.tscn"):
            self.assertTrue((PACK/"godot/scenes"/name).is_file())
    def test_catalog_unique(self):
        ids=[x["id"] for x in json.loads((PACK/"catalog.json").read_text())["entries"]]
        self.assertEqual(len(ids),len(set(ids)))
    def test_checksums(self):
        for rel,digest in json.loads((PACK/"checksums.json").read_text())["files"].items():
            self.assertEqual(hashlib.sha256((PACK/rel).read_bytes()).hexdigest(),digest)
    def test_no_binary_results(self):
        self.assertFalse(any(p.suffix.lower() in {".pdf",".docx",".epub",".bin"} for p in PACK.rglob("*") if p.is_file()))
