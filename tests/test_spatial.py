import subprocess
import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class PlaceholderControlTest(unittest.TestCase):
    def test_stage4a_spatial_qa_passes(self):
        result = subprocess.run(
            [sys.executable, "scripts/validate_spatial.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Stage 4 gate remains blocked", result.stdout)

    def test_stage4a_canonical_inventory_headers_exist(self):
        expected = [
            ROOT / "spatial/parking_inventory/canonical/sites.csv",
            ROOT / "spatial/parking_inventory/canonical/premises.csv",
            ROOT / "spatial/parking_inventory/canonical/parking_observations.csv",
            ROOT / "spatial/parking_inventory/canonical/audit_events.csv",
        ]
        for path in expected:
            self.assertTrue(path.exists(), path)
