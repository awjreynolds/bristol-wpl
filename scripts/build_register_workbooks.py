#!/usr/bin/env python3
"""Build officer-editable workbook views from controlled CSV registers."""

from __future__ import annotations

import csv
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
ZIP_DATE = (2026, 1, 1, 0, 0, 0)

WORKBOOKS = [
    ("evidence/source_register.csv", "evidence/source_register.xlsx", "source_register"),
    ("governance/risk_register.csv", "governance/risk_register.xlsx", "risk_register"),
]

PARKING_WORKBOOK = (
    "spatial/parking_inventory/parking-base-register.xlsx",
    [
        ("spatial/parking_inventory/canonical/sites.csv", "sites"),
        ("spatial/parking_inventory/canonical/premises.csv", "premises"),
        ("spatial/parking_inventory/canonical/occupiers.csv", "occupiers"),
        ("spatial/parking_inventory/canonical/parking_areas.csv", "parking_areas"),
        ("spatial/parking_inventory/canonical/parking_observations.csv", "observations"),
        ("spatial/parking_inventory/canonical/licence_declarations.csv", "declarations"),
        ("spatial/parking_inventory/canonical/inspections.csv", "inspections"),
        ("spatial/parking_inventory/canonical/exemptions_discounts.csv", "exemptions"),
        ("spatial/parking_inventory/canonical/appeals_enforcement_links.csv", "appeal_links"),
        ("spatial/parking_inventory/canonical/audit_events.csv", "audit_events"),
    ],
)

APPRAISAL_WORKBOOKS = [
    (
        "analysis/economic/options-framework-filter.csv",
        "analysis/economic/options-framework-filter.xlsx",
        "options_filter",
    ),
    (
        "analysis/economic/appraisal-specification-summary-tables.csv",
        "analysis/economic/appraisal-specification-summary-tables.xlsx",
        "asst",
    ),
    (
        "models/uncertainty/uncertainty-register.csv",
        "models/uncertainty/uncertainty-log.xlsx",
        "uncertainty",
    ),
]


def cell_ref(col_index: int, row_index: int) -> str:
    letters = ""
    col = col_index
    while col:
        col, rem = divmod(col - 1, 26)
        letters = chr(65 + rem) + letters
    return f"{letters}{row_index}"


def read_csv(rel: str) -> tuple[list[str], list[list[str]]]:
    with (ROOT / rel).open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        columns = reader.fieldnames or []
        return columns, [[row.get(column, "") for column in columns] for row in reader]


def write_xlsx(rel: str, sheet_name: str, columns: list[str], rows: list[list[str]]) -> None:
    write_multi_xlsx(rel, [(sheet_name, columns, rows)])


def write_multi_xlsx(rel: str, sheets: list[tuple[str, list[str], list[list[str]]]]) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    worksheet_parts = {}
    workbook_sheets = []
    relationships = []
    overrides = []
    for sheet_index, (sheet_name, columns, rows) in enumerate(sheets, start=1):
        all_rows = [columns] + rows
        sheet_rows = []
        for row_index, row in enumerate(all_rows, start=1):
            cells = []
            for col_index, value in enumerate(row, start=1):
                ref = cell_ref(col_index, row_index)
                cells.append(f'<c r="{ref}" t="inlineStr"><is><t>{escape(str(value))}</t></is></c>')
            sheet_rows.append(f'<row r="{row_index}">{"".join(cells)}</row>')
        worksheet_parts[f"xl/worksheets/sheet{sheet_index}.xml"] = f"""<?xml version="1.0" encoding="UTF-8"?>
<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
<sheetData>{''.join(sheet_rows)}</sheetData>
</worksheet>"""
        safe_sheet_name = escape(sheet_name[:31])
        workbook_sheets.append(f'<sheet name="{safe_sheet_name}" sheetId="{sheet_index}" r:id="rId{sheet_index}"/>')
        relationships.append(
            f'<Relationship Id="rId{sheet_index}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet{sheet_index}.xml"/>'
        )
        overrides.append(
            f'<Override PartName="/xl/worksheets/sheet{sheet_index}.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>'
        )

    files = {
        "[Content_Types].xml": """<?xml version="1.0" encoding="UTF-8"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>
__WORKSHEET_OVERRIDES__
</Types>""".replace("__WORKSHEET_OVERRIDES__", "\n".join(overrides)),
        "_rels/.rels": """<?xml version="1.0" encoding="UTF-8"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>
</Relationships>""",
        "xl/workbook.xml": """<?xml version="1.0" encoding="UTF-8"?>
<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
<sheets>__SHEETS__</sheets>
</workbook>""".replace("__SHEETS__", "".join(workbook_sheets)),
        "xl/_rels/workbook.xml.rels": """<?xml version="1.0" encoding="UTF-8"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
__RELATIONSHIPS__
</Relationships>""".replace("__RELATIONSHIPS__", "\n".join(relationships)),
    }
    files.update(worksheet_parts)
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as workbook:
        for name, data in files.items():
            info = zipfile.ZipInfo(name, ZIP_DATE)
            info.compress_type = zipfile.ZIP_DEFLATED
            workbook.writestr(info, data)


def main() -> int:
    for csv_rel, xlsx_rel, sheet_name in WORKBOOKS:
        columns, rows = read_csv(csv_rel)
        write_xlsx(xlsx_rel, sheet_name, columns, rows)
        print(f"Wrote {xlsx_rel} with {len(rows)} rows")
    parking_xlsx, parking_sheets = PARKING_WORKBOOK
    sheets = []
    total_rows = 0
    for csv_rel, sheet_name in parking_sheets:
        columns, rows = read_csv(csv_rel)
        sheets.append((sheet_name, columns, rows))
        total_rows += len(rows)
    write_multi_xlsx(parking_xlsx, sheets)
    print(f"Wrote {parking_xlsx} with {total_rows} rows across {len(sheets)} sheets")
    for csv_rel, xlsx_rel, sheet_name in APPRAISAL_WORKBOOKS:
        columns, rows = read_csv(csv_rel)
        write_xlsx(xlsx_rel, sheet_name, columns, rows)
        print(f"Wrote {xlsx_rel} with {len(rows)} rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
