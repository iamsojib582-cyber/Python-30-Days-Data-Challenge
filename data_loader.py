import json
import os
import tempfile
import zipfile

import pandas as pd

from utils import detect_separator, read_text_file, standardize_dataframe_columns


def load_csv_flexibly(path: str) -> pd.DataFrame:
    raw = read_text_file(path)
    sep = detect_separator(raw)
    lines = [line.strip() for line in raw.splitlines() if line.strip()]
    rows = [line.split(sep) for line in lines]
    if not rows:
        raise ValueError("CSV file is empty.")

    width = max(len(row) for row in rows)
    rows = [(row + [""] * (width - len(row)))[:width] for row in rows]
    header = rows[0]
    data = rows[1:] if len(rows) > 1 else []
    df = pd.DataFrame(data, columns=header)
    return standardize_dataframe_columns(df)


def load_from_zip(path: str) -> pd.DataFrame:
    with zipfile.ZipFile(path, "r") as zf:
        candidates = [
            name
            for name in zf.namelist()
            if name.lower().endswith((".csv", ".xlsx", ".xls", ".json"))
        ]
        if not candidates:
            raise ValueError("ZIP does not contain a supported file.")

        target = candidates[0]
        with zf.open(target) as inner:
            suffix = os.path.splitext(target)[1].lower()
            if suffix == ".csv":
                with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as temp:
                    temp.write(inner.read())
                    temp_path = temp.name
                try:
                    return load_csv_flexibly(temp_path)
                finally:
                    try:
                        os.remove(temp_path)
                    except OSError:
                        pass
            if suffix in (".xlsx", ".xls"):
                return standardize_dataframe_columns(pd.read_excel(inner))
            return standardize_dataframe_columns(pd.json_normalize(json.load(inner)))


def load_any_file(path: str) -> pd.DataFrame:
    ext = os.path.splitext(path)[1].lower()
    if ext == ".csv":
        return load_csv_flexibly(path)
    if ext in (".xlsx", ".xls"):
        return standardize_dataframe_columns(pd.read_excel(path))
    if ext == ".json":
        with open(path, "r", encoding="utf-8") as f:
            return standardize_dataframe_columns(pd.json_normalize(json.load(f)))
    if ext == ".zip":
        return load_from_zip(path)
    raise ValueError("Unsupported file type. Use CSV, Excel, JSON, or ZIP.")
