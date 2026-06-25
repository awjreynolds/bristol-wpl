import csv
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class Stage1ControlsTest(unittest.TestCase):
    def read_csv(self, rel):
        with (ROOT / rel).open(newline="", encoding="utf-8") as handle:
            return list(csv.DictReader(handle))

    def test_json_schemas_parse(self):
        for path in sorted((ROOT / "schemas").glob("*.schema.json")):
            with self.subTest(path=path.name):
                json.loads(path.read_text(encoding="utf-8"))

    def test_source_register_unique_ids_and_current_counts(self):
        rows = self.read_csv("evidence/source_register.csv")
        ids = [row["source_id"] for row in rows]
        self.assertEqual(len(ids), len(set(ids)))
        statuses = {status: sum(1 for row in rows if row["status"] == status) for status in {row["status"] for row in rows}}
        self.assertGreaterEqual(statuses.get("downloaded", 0), 49)
        self.assertEqual(statuses.get("download_failed", 0), 1)

    def test_extraction_manifest_is_current_state(self):
        sources = self.read_csv("evidence/source_register.csv")
        manifest = self.read_csv("evidence/extraction_manifest.csv")
        self.assertEqual(len(manifest), len(sources))
        source_status = {row["source_id"]: row["status"] for row in sources}
        manifest_status = {row["source_id"]: row["status"] for row in manifest}
        for source_id, status in source_status.items():
            if status == "downloaded":
                self.assertEqual(manifest_status[source_id], "extracted")
            elif status == "download_failed":
                self.assertEqual(manifest_status[source_id], "skipped_download_failed")

    def test_stage1_review_artifacts_exist(self):
        required = [
            "review/stage_gate_reports/stage-1-source-acquisition-and-simulated-assurance-report.md",
            "review/legal_review/stage-1-legal-and-statutory-powers-review.md",
            "review/peer_review/stage-1-bristol-governance-review.md",
            "review/peer_review/stage-1-weca-mca-governance-review.md",
            "review/peer_review/stage-1-comparator-evidence-review.md",
            "review/analytical_assurance/stage-1-appraisal-tag-assurance-review.md",
            "review/analytical_assurance/stage-1-spatial-data-operations-review.md",
        ]
        for rel in required:
            with self.subTest(rel=rel):
                self.assertTrue((ROOT / rel).exists())

    def test_editable_markdown_templates_exist(self):
        required = [
            "business_case/obc/03-economic-case/economic-case.md",
            "business_case/fbc/05-financial-case/financial-case.md",
            "statutory_dossier/draft_scheme_order/scheme_order_working_draft.md",
            "statutory_dossier/licensing_enforcement_and_appeals/licensing_enforcement_appeals.md",
        ]
        for rel in required:
            with self.subTest(rel=rel):
                text = (ROOT / rel).read_text(encoding="utf-8")
                self.assertIn("#", text)
                self.assertGreater(len(text), 200)
