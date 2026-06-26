import csv
import subprocess
import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ClaimSummaryControlTest(unittest.TestCase):
    def test_claim_summary_validator_passes(self):
        result = subprocess.run(
            [sys.executable, "scripts/validate_claim_summaries.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Claim summaries QA passed", result.stdout)
        self.assertIn("claim-use control layer only", result.stdout)

    def test_stage_16a_covers_existing_claim_matrix_exactly(self):
        with (ROOT / "evidence/claim_evidence_matrix.csv").open(
            newline="",
            encoding="utf-8",
        ) as handle:
            claims = {row["claim_id"] for row in csv.DictReader(handle)}
        with (ROOT / "evidence/claim_summaries/claim-summary-register.csv").open(
            newline="",
            encoding="utf-8",
        ) as handle:
            summaries = {row["claim_id"] for row in csv.DictReader(handle)}

        expected = {f"CLM-{number:04d}" for number in range(1, 39)}
        self.assertEqual(claims, expected)
        self.assertEqual(summaries, expected)

    def test_blank_source_claims_are_labelled_as_control_claims(self):
        with (ROOT / "evidence/claim_evidence_matrix.csv").open(
            newline="",
            encoding="utf-8",
        ) as handle:
            blank_claims = [
                row["claim_id"] for row in csv.DictReader(handle) if not row["source_ids"]
            ]

        for claim_id in blank_claims:
            text = (
                ROOT / "evidence/claim_summaries/summaries" / f"{claim_id.lower()}.md"
            ).read_text(encoding="utf-8")
            self.assertIn("No direct source IDs in the claim matrix", text)
            self.assertIn("absence/control claim", text)

    def test_future_claim_gap_remains_open(self):
        with (ROOT / "evidence/evidence_gap_register.csv").open(
            newline="",
            encoding="utf-8",
        ) as handle:
            gaps = {row["gap_id"]: row for row in csv.DictReader(handle)}

        self.assertEqual(gaps["EG-0044"]["status"], "partially_closed_stage_16a")
        self.assertEqual(gaps["EG-0045"]["status"], "open")


if __name__ == "__main__":
    unittest.main()
