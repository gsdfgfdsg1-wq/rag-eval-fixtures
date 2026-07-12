import unittest
from evaluate import evaluate


class EvalTests(unittest.TestCase):
    def test_calculates_recall(self):
        report = evaluate([{ "id": "q1", "evidence": ["a", "b"]}], [{ "id": "q1", "retrieved": ["a"]}])
        self.assertEqual(report["fixtures"][0]["recall"], 0.5)

    def test_calculates_citation_precision(self):
        report = evaluate([{ "id": "q1", "evidence": ["a"]}], [{ "id": "q1", "retrieved": ["a", "noise"]}])
        self.assertEqual(report["fixtures"][0]["citation_precision"], 0.5)

    def test_detects_expired_fixture(self):
        report = evaluate([{ "id": "q1", "evidence": [], "expires_at": "2020-01-01"}], [], "2024-01-01")
        self.assertTrue(report["fixtures"][0]["expired"])


if __name__ == "__main__":
    unittest.main()
