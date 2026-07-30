import unittest, json
from pathlib import Path
from benchmark_library.runner import run_benchmark

PACK=Path(__file__).resolve().parents[2]
class RunnerTests(unittest.TestCase):
    def contract(self,name):
        value=json.loads((PACK/"contracts"/name).read_text(encoding="utf-8")); value["warmups"]=0; value["repetitions"]=2; return value
    def test_cpu_result(self):
        c=self.contract("CPU-REFERENCE.json"); c["parameters"]["iterations"]=2; c["parameters"]["payload_bytes"]=8
        result=run_benchmark("cpu",c,PACK)
        self.assertEqual(result["oracle_status"],"pass"); self.assertEqual(len(result["samples"]),2)
    def test_memory_result(self):
        c=self.contract("MEMORY-REFERENCE.json"); c["parameters"]["items"]=100
        self.assertEqual(run_benchmark("memory",c,PACK)["oracle_status"],"pass")
    def test_corpus_result(self):
        c=self.contract("CORPUS-REFERENCE.json"); c["parameters"]["queries"]=1
        result=run_benchmark("corpus",c,PACK)
        self.assertEqual(result["secondary_statistics"]["accuracy"]["mean"],1.0)
