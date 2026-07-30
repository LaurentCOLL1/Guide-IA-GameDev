import unittest
from pathlib import Path
from benchmark_library.workloads import cpu_workload, memory_workload, load_jsonl, retrieve, corpus_workload

PACK=Path(__file__).resolve().parents[2]
class WorkloadTests(unittest.TestCase):
    def test_cpu_deterministic(self):
        self.assertEqual(cpu_workload(1,3,16),cpu_workload(1,3,16))
    def test_memory_deterministic(self):
        self.assertEqual(memory_workload(2,100)[0],memory_workload(2,100)[0])
    def test_retrieve_oracle(self):
        docs=load_jsonl(PACK/"fixtures/corpus/synthetic-documents.jsonl")
        self.assertEqual(retrieve("minerai charbon outils",docs),"DOC-SYN-002")
    def test_corpus_accuracy(self):
        c,a=corpus_workload(PACK/"fixtures/corpus/synthetic-documents.jsonl",PACK/"fixtures/corpus/synthetic-queries.jsonl",1)
        self.assertEqual(a,1.0); self.assertEqual(len(c),64)
