import tempfile
from pathlib import Path
import unittest

from scripts.validate_registers import check_csv_row_widths


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
