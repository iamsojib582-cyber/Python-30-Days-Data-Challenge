from pathlib import Path
import re
import pandas as pd

CSV_FOLDER = Path(r"D:\CSV_Files")
OUTPUT_FILE = Path(r"D:\Excel Workbook\combined_csv_files.xlsx")

def make_sheet_name(file_stem: str, used_names: set[str]) -> str:
    # Excel sheet name rules: max 31 chars, disallow: : \ / ? * [ ]
    cleaned = re.sub(r'[:\\/?*\[\]]', "_", file_stem).strip()
    if not cleaned:
        cleaned = "Sheet"
    cleaned = cleaned[:31]

    base = cleaned
    counter = 1
    while cleaned in used_names:
        suffix = f"_{counter}"
        cleaned = f"{base[:31 - len(suffix)]}{suffix}"
        counter += 1

    used_names.add(cleaned)
    return cleaned

def main() -> None:
    if not CSV_FOLDER.exists():
        raise FileNotFoundError(f"Folder not found: {CSV_FOLDER}")

    csv_files = sorted(CSV_FOLDER.glob("*.csv"))
    if not csv_files:
        raise FileNotFoundError(f"No CSV files found in: {CSV_FOLDER}")

    used_sheet_names: set[str] = set()

    with pd.ExcelWriter(OUTPUT_FILE, engine="openpyxl") as writer:
        for csv_file in csv_files:
            df = pd.read_csv(csv_file)
            sheet_name = make_sheet_name(csv_file.stem, used_sheet_names)
            df.to_excel(writer, sheet_name=sheet_name, index=False)

    print(f"Done. {len(csv_files)} CSV files were merged into:")
    print(OUTPUT_FILE)


if __name__ == "__main__":
    main()
