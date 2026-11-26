import json
from pathlib import Path
import unittest

class InputLayout(unittest.TestCase):
    def test_synthetic_input(self):
        value = json.loads(Path("fixture.json").read_text(encoding="utf-8"))
        self.assertIs(value["synthetic"], True)
        events = value["events"]
        self.assertEqual(len(events), 3)
        self.assertEqual(len({row["id"] for row in events}), 3)
        self.assertTrue(all(row["kind"] and row["organization"] == "training" for row in events))
