import unittest
from asteria_code import InMemoryRepository, ServiceRegistry

class ServicesRepositoriesTests(unittest.TestCase):
    def test_registry_is_explicit(self):
        registry = ServiceRegistry()
        registry.register("answer", 42)
        self.assertEqual(registry.resolve("answer", int), 42)
        with self.assertRaises(KeyError):
            registry.register("answer", 43)

    def test_repository_defensive_copy(self):
        repository = InMemoryRepository()
        source = {"items": [1]}
        repository.save("x", source)
        source["items"].append(2)
        fetched = repository.get_by_id("x")
        self.assertEqual(fetched, {"items": [1]})
        fetched["items"].append(9)
        self.assertEqual(repository.get_by_id("x"), {"items": [1]})

    def test_repository_order(self):
        repository = InMemoryRepository()
        repository.save("b", 2)
        repository.save("a", 1)
        self.assertEqual(repository.list_ids(), ["a", "b"])
