import tempfile
from pathlib import Path
import unittest

from scripts.validate_registers import (
    check_csv_row_widths,
    check_no_authored_pdfs,
    check_sensitive_paths,
)
from scripts.validate_public_release import check_no_go_register, check_publication_checklist


class ValidateRegistersTest(unittest.TestCase):
    def test_check_csv_row_widths_reports_malformed_rows(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "bad.csv").write_text(
                "a,b,c\n1,2,3\n4,5\n",
                encoding="utf-8",
            )

            errors = check_csv_row_widths(root)

        self.assertEqual(errors, ["bad.csv:3 has 2 fields; expected 3"])

    def test_pdf_scan_is_case_insensitive(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "docs").mkdir()
            (root / "docs" / "OfficerPack.PDF").write_text("placeholder", encoding="utf-8")

            errors = check_no_authored_pdfs(root)

        self.assertEqual(errors, ["authored or misplaced PDF is not allowed: docs/OfficerPack.PDF"])

    def test_pdf_scan_rejects_non_raw_evidence_pdfs_under_raw_tree(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "evidence/raw").mkdir(parents=True)
            (root / "evidence/raw/officer-pack.pdf").write_text("placeholder", encoding="utf-8")

            errors = check_no_authored_pdfs(root)

        self.assertEqual(errors, ["authored PDF-like file is not allowed in raw evidence: evidence/raw/officer-pack.pdf"])

    def test_sensitive_path_scan_flags_public_references(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "docs/public").mkdir(parents=True)
            (root / "docs/public/README.md").write_text(
                "Do not expose consultation/response_data/raw/example.csv\n",
                encoding="utf-8",
            )

            errors = check_sensitive_paths(root)

        self.assertEqual(
            errors,
            ["restricted path reference exposed in public/officer content: docs/public/README.md -> consultation/response_data/raw/"],
        )

    def test_public_release_no_go_register_rejects_unsafe_wording(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            rel = "publication/controls/public-release-no-go-register.csv"
            path = root / rel
            path.parent.mkdir(parents=True)
            path.write_text(
                "claim_id,prohibited_claim,allowed_wording,current_status,gate_effect\n"
                "PUB-NG-001,public repository means council approval,Approval is ready,blocked,P0\n",
                encoding="utf-8",
            )

            errors = check_no_go_register(root)

        self.assertIn(f"{rel} PUB-NG-001 allowed_wording contains unsafe term: approval", errors)

    def test_publication_checklist_rejects_readiness_gate_effect(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            rel = "publication/controls/repository-publication-checklist.csv"
            path = root / rel
            path.parent.mkdir(parents=True)
            path.write_text(
                "control_id,control_area,requirement,evidence,current_status,gate_effect,next_check\n"
                "repo_visibility,github_visibility,Repository is public,evidence,public_verified,approves_wpl,next\n",
                encoding="utf-8",
            )

            errors = check_publication_checklist(root)

        self.assertIn(f"{rel} repo_visibility has unsafe gate_effect approves_wpl", errors)
