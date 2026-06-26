import subprocess
import sys
from pathlib import Path
import unittest

from scripts.validate_strategic import check_package_funding_controls

ROOT = Path(__file__).resolve().parents[1]


class StrategicControlTest(unittest.TestCase):
    def test_stage3a_strategic_qa_passes(self):
        result = subprocess.run(
            [sys.executable, "scripts/validate_strategic.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Stage 3 gate remains blocked", result.stdout)

    def test_benefits_register_keeps_gross_receipts_as_transfer(self):
        import csv

        with (ROOT / "governance/benefits_register.csv").open(newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))

        self.assertTrue(
            any(
                row["attribution_route"] == "transfer_public_cash_flow_not_economic_benefit"
                and row["status"] == "control_placeholder"
                for row in rows
            )
        )

    def test_mca_trigger_without_route_must_be_p0(self):
        errors = check_package_funding_controls(
            [{"package_id": "PKG-1"}],
            [
                {
                    "package_or_cost_line_id": "PKG-1",
                    "description": "package",
                    "weca_mca_trigger_class": "MCA assurance",
                    "formal_decision_source": "not_evidenced",
                    "assurance_route": "not_assessed",
                    "gate_effect": "P1",
                }
            ],
        )

        self.assertEqual(
            errors,
            [
                "investment_programme/funding/package-funding-assurance-classification.csv "
                "PKG-1 has unresolved MCA/funding assurance trigger and must have gate_effect P0"
            ],
        )

    def test_placeholder_funding_row_joins_package_register(self):
        errors = check_package_funding_controls(
            [{"package_id": "PKG-CTRL-001"}],
            [
                {
                    "package_or_cost_line_id": "PFAC-001",
                    "description": "package_placeholder",
                    "weca_mca_trigger_class": "not_classified",
                    "formal_decision_source": "not_evidenced",
                    "assurance_route": "not_assessed",
                    "gate_effect": "P1",
                }
            ],
        )

        self.assertEqual(
            errors,
            [
                "investment_programme/funding/package-funding-assurance-classification.csv "
                "placeholder row PFAC-001 must join to package-control-register package_id"
            ],
        )
