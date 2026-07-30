from __future__ import annotations
import copy, json, shutil, tempfile, unittest
from pathlib import Path
from knowledge_base.core import *

PACK=Path(__file__).resolve().parents[2]
CORPUS=PACK/"corpus"

class KnowledgeBaseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index=build_index(CORPUS)

    def test_01_documents_count(self): self.assertEqual(len(self.index["documents"]),8)
    def test_02_unique_document_ids(self): self.assertEqual(len({d["id"] for d in self.index["documents"]}),8)
    def test_03_all_source_synthetic(self): self.assertTrue(all(d["redistribution"]=="synthetic-original" for d in self.index["documents"]))
    def test_04_truth_statuses(self): self.assertEqual({d["truth_status"] for d in self.index["documents"]},{"canonical","rumor","memory","reference"})
    def test_05_deterministic_index(self): self.assertEqual(canonical_json(build_index(CORPUS)),canonical_json(build_index(CORPUS)))
    def test_06_digest_valid(self):
        data=copy.deepcopy(self.index); digest=data.pop("index_digest")
        self.assertEqual(digest,sha256_bytes(canonical_json(data).encode()))
    def test_07_chunk_ids_unique(self): self.assertEqual(len(self.index["chunks"]),len({c["chunk_id"] for c in self.index["chunks"]}))
    def test_08_chunk_bounds(self): self.assertTrue(all(c["end_word"]>c["start_word"] for c in self.index["chunks"]))
    def test_09_postings_sorted(self): self.assertTrue(all(v==sorted(v) for v in self.index["postings"].values()))
    def test_10_search_heliostat(self): self.assertEqual(search(self.index,"héliostat flux")[0]["document_id"],"AST-CODEX-TECH")
    def test_11_search_rumor(self): self.assertEqual(search(self.index,"reine de braise")[0]["document_id"],"AST-RUMOR-EMBER-QUEEN")
    def test_12_filter_canonical_excludes_rumor(self): self.assertFalse(any(r["truth_status"]=="rumor" for r in search(self.index,"reine de braise",truth_status="canonical")))
    def test_13_filter_rumor(self): self.assertEqual(search(self.index,"reine de braise",truth_status="rumor")[0]["document_id"],"AST-RUMOR-EMBER-QUEEN")
    def test_14_memory_search(self): self.assertEqual(search(self.index,"tempête silhouette rouge")[0]["document_id"],"AST-MEM-SERA-VOSS")
    def test_15_category_filter(self): self.assertTrue(all(r["category"]=="rag" for r in search(self.index,"suppression document",category="rag")))
    def test_16_empty_query(self): self.assertEqual(search(self.index,"---"),[])
    def test_17_lexical_mode(self): self.assertEqual(search(self.index,"régulateur faisceau",mode="lexical")[0]["document_id"],"AST-CODEX-TECH")
    def test_18_vector_mode_returns(self): self.assertTrue(search(self.index,"registre canonique",mode="vector"))
    def test_19_remove_document(self):
        out=remove_document(self.index,"AST-RUMOR-EMBER-QUEEN"); self.assertEqual(len(out["documents"]),7)
    def test_20_verify_deleted(self): self.assertTrue(verify_deleted(remove_document(self.index,"AST-RUMOR-EMBER-QUEEN"),"AST-RUMOR-EMBER-QUEEN"))
    def test_21_removed_search_absent(self):
        out=remove_document(self.index,"AST-RUMOR-EMBER-QUEEN")
        self.assertFalse(any(r["document_id"]=="AST-RUMOR-EMBER-QUEEN" for r in search(out,"reine de braise")))
    def test_22_remove_missing_raises(self):
        with self.assertRaises(KeyError): remove_document(self.index,"MISSING")
    def test_23_source_manifest_removed(self):
        out=remove_document(self.index,"AST-RUMOR-EMBER-QUEEN"); self.assertNotIn("AST-RUMOR-EMBER-QUEEN",out["source_manifest"])
    def test_24_rebuild_matches_pruned(self):
        with tempfile.TemporaryDirectory() as d:
            dst=Path(d)/"corpus"; shutil.copytree(CORPUS,dst); (dst/"lore/rumors/ember-queen.json").unlink()
            self.assertEqual(canonical_json(remove_document(self.index,"AST-RUMOR-EMBER-QUEEN")),canonical_json(build_index(dst)))
    def test_25_source_unchanged(self):
        before={p.relative_to(CORPUS).as_posix():sha256_file(p) for p in CORPUS.rglob("*.json")}
        build_index(CORPUS)
        after={p.relative_to(CORPUS).as_posix():sha256_file(p) for p in CORPUS.rglob("*.json")}
        self.assertEqual(before,after)
    def test_26_accent_normalization(self): self.assertEqual(normalize("HÉLIOSTAT"),["heliostat"])
    def test_27_invalid_chunk_settings(self):
        with self.assertRaises(ValueError): chunk_words(["a"]*10,5,5)
    def test_28_duplicate_ids_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            dst=Path(d)
            shutil.copy(CORPUS/"codex/factions.json",dst/"a.json")
            shutil.copy(CORPUS/"codex/factions.json",dst/"b.json")
            with self.assertRaises(ValueError): build_index(dst)
    def test_29_invalid_status_rejected(self):
        doc=json.loads((CORPUS/"codex/factions.json").read_text())
        doc["truth_status"]="unknown"
        with self.assertRaises(ValueError): validate_document(doc)
    def test_30_index_round_trip(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"index.json"; write_index(self.index,p); self.assertEqual(load_index(p),self.index)
    def test_31_tamper_detected(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"index.json"; write_index(self.index,p)
            data=json.loads(p.read_text()); data["documents"].pop(); p.write_text(json.dumps(data))
            with self.assertRaises(ValueError): load_index(p)
    def test_32_chunks_reference_docs(self):
        ids={d["id"] for d in self.index["documents"]}
        self.assertTrue(all(c["document_id"] in ids for c in self.index["chunks"]))

if __name__=="__main__":
    unittest.main()
