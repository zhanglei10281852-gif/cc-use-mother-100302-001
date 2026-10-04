"""碳纤维批次谱系与放行基础契约测试。"""

import unittest

from carbon_batch import MaterialBatch, unique_by_identity


class ContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.values = {'batch_code': 'batch-code-001', 'product_grade': 'product-grade-001', 'process_revision': 'process-revision-001', 'status': 'draft'}

    def test_fingerprint_is_stable(self) -> None:
        left = MaterialBatch(**self.values)
        right = MaterialBatch(**dict(reversed(list(self.values.items()))))
        self.assertEqual(left.fingerprint(), right.fingerprint())

    def test_evolve_keeps_original(self) -> None:
        original = MaterialBatch(**self.values)
        change_key = next(key for key, value in self.values.items() if isinstance(value, str))
        changed = original.evolve(**{change_key: "revised-value"})
        self.assertNotEqual(original.fingerprint(), changed.fingerprint())
        self.assertEqual(getattr(original, change_key), self.values[change_key])

    def test_conflicting_identity_is_rejected(self) -> None:
        first = MaterialBatch(**self.values)
        changed_values = dict(self.values)
        change_key = next(key for key in self.values if key != "batch_code")
        changed_values[change_key] = 2 if isinstance(changed_values[change_key], int) else "conflict"
        second = MaterialBatch(**changed_values)
        with self.assertRaises(ValueError):
            unique_by_identity([first, second])


if __name__ == "__main__":
    unittest.main()
