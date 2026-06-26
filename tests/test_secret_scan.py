import subprocess
import sys
import tempfile
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class SecretScanTest(unittest.TestCase):
    def test_secret_scan_passes_current_repo(self):
        result = subprocess.run(
            [sys.executable, "scripts/scan_secrets.py"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_secret_scan_redacts_findings(self):
        sample = "eyJrIjoi" + ("A" * 48)
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "sample.txt"
            path.write_text(f"token={sample}\n", encoding="utf-8")
            result = subprocess.run(
                [sys.executable, "scripts/scan_secrets.py", str(path)],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
        self.assertEqual(result.returncode, 1)
        self.assertIn("grafana_legacy_or_powerbi_collision", result.stdout)
        self.assertIn("sha256=", result.stdout)
        self.assertNotIn(sample, result.stdout + result.stderr)
