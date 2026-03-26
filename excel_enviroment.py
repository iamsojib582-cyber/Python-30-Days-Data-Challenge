import json
import tkinter as tk
import zipfile
from tkinter import filedialog, messagebox, ttk

import pandas as pd
import plotly.express as px
from tksheet import Sheet


class DataAnalystStudio:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Data Analyst Studio")
        self.root.geometry("1400x820")

        self.original_df = pd.DataFrame()
        self.df = pd.DataFrame()
        self.current_file = ""

        self._build_ui()

    def _build_ui(self) -> None:
        top_bar = ttk.Frame(self.root, padding=10)
        top_bar.pack(fill="x")

        ttk.Button(top_bar, text="Open File", command=self.open_file).pack(side="left", padx=5)
        ttk.Button(top_bar, text="Apply Grid Changes", command=self.apply_grid_changes).pack(side="left", padx=5)
        ttk.Button(top_bar, text="AI Scan Problems", command=self.scan_problems).pack(side="left", padx=5)
        ttk.Button(top_bar, text="One Click Clean", command=self.auto_clean).pack(side="left", padx=5)
        ttk.Button(top_bar, text="Reset Data", command=self.reset_data).pack(side="left", padx=5)
        ttk.Button(top_bar, text="Export CSV", command=self.export_csv).pack(side="left", padx=5)
        ttk.Button(top_bar, text="Export Excel", command=self.export_excel).pack(side="left", padx=5)

        self.file_label = ttk.Label(top_bar, text="No file opened")
        self.file_label.pack(side="left", padx=15)

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        self.preview_tab = ttk.Frame(self.notebook)
        self.issues_tab = ttk.Frame(self.notebook)
        self.clean_tab = ttk.Frame(self.notebook)
        self.pivot_tab = ttk.Frame(self.notebook)
        self.chart_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.preview_tab, text="Data Preview")
        self.notebook.add(self.issues_tab, text="AI Issues")
        self.notebook.add(self.clean_tab, text="Clean / Replace")
        self.notebook.add(self.pivot_tab, text="Pivot Table")
        self.notebook.add(self.chart_tab, text="Visualization")

        self._build_preview_tab()
        self._build_issues_tab()
        self._build_clean_tab()
        self._build_pivot_tab()
        self._build_chart_tab()

    def _build_preview_tab(self) -> None:
        info_frame = ttk.Frame(self.preview_tab, padding=10)
        info_frame.pack(fill="x")

        self.summary_label = ttk.Label(info_frame, text="Rows: 0 | Columns: 0 | Missing: 0 | Duplicates: 0")
        self.summary_label.pack(anchor="w")

        table_frame = ttk.Frame(self.preview_tab, padding=10)
        table_frame.pack(fill="both", expand=True)

        self.preview_sheet = Sheet(table_frame)
        self.preview_sheet.enable_bindings(
            "single_select",
            "row_select",
            "column_select",
            "arrowkeys",
            "right_click_popup_menu",
            "rc_select",
            "copy",
            "cut",
            "paste",
            "delete",
            "edit_cell",
        )
        self.preview_sheet.pack(fill="both", expand=True)

    def _build_issues_tab(self) -> None:
        frame = ttk.Frame(self.issues_tab, padding=10)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="AI-style problem finder").pack(anchor="w")

        self.issues_box = tk.Text(frame, wrap="word", height=30)
        self.issues_box.pack(fill="both", expand=True, pady=10)

    def _build_clean_tab(self) -> None:
        frame = ttk.Frame(self.clean_tab, padding=10)
        frame.pack(fill="both", expand=True)

        controls = ttk.Frame(frame)
        controls.pack(fill="x", pady=5)

        ttk.Label(controls, text="Column").pack(side="left", padx=5)
        self.column_combo = ttk.Combobox(controls, state="readonly", width=25)
        self.column_combo.pack(side="left", padx=5)

        ttk.Label(controls, text="Find").pack(side="left", padx=5)
        self.find_entry = ttk.Entry(controls, width=20)
        self.find_entry.pack(side="left", padx=5)

        ttk.Label(controls, text="Replace With").pack(side="left", padx=5)
        self.replace_entry = ttk.Entry(controls, width=20)
        self.replace_entry.pack(side="left", padx=5)

        ttk.Button(controls, text="Replace All", command=self.replace_values).pack(side="left", padx=5)
        ttk.Button(controls, text="Drop Blank Rows", command=self.drop_blank_rows).pack(side="left", padx=5)
        ttk.Button(controls, text="Drop Duplicate Rows", command=self.drop_duplicates).pack(side="left", padx=5)
        ttk.Button(controls, text="Trim Spaces", command=self.trim_spaces).pack(side="left", padx=5)

        self.clean_log = tk.Text(frame, wrap="word", height=25)
        self.clean_log.pack(fill="both", expand=True, pady=10)

    def _build_pivot_tab(self) -> None:
        frame = ttk.Frame(self.pivot_tab, padding=10)
        frame.pack(fill="both", expand=True)

        controls = ttk.Frame(frame)
        controls.pack(fill="x", pady=5)

        ttk.Label(controls, text="Group By").pack(side="left", padx=5)
        self.pivot_index_combo = ttk.Combobox(controls, state="readonly", width=25)
        self.pivot_index_combo.pack(side="left", padx=5)

        ttk.Label(controls, text="Value").pack(side="left", padx=5)
        self.pivot_value_combo = ttk.Combobox(controls, state="readonly", width=25)
        self.pivot_value_combo.pack(side="left", padx=5)

        ttk.Label(controls, text="Agg").pack(side="left", padx=5)
        self.pivot_agg_combo = ttk.Combobox(
            controls, state="readonly", width=12, values=["sum", "mean", "count", "min", "max"]
        )
        self.pivot_agg_combo.set("sum")
        self.pivot_agg_combo.pack(side="left", padx=5)

        ttk.Button(controls, text="Create Pivot", command=self.create_pivot).pack(side="left", padx=5)

        pivot_frame = ttk.Frame(frame)
        pivot_frame.pack(fill="both", expand=True, pady=10)

        self.pivot_tree = ttk.Treeview(pivot_frame, show="headings")
        self.pivot_tree.pack(side="left", fill="both", expand=True)

        pivot_scroll = ttk.Scrollbar(pivot_frame, orient="vertical", command=self.pivot_tree.yview)
        pivot_scroll.pack(side="right", fill="y")
        self.pivot_tree.configure(yscrollcommand=pivot_scroll.set)

    def _build_chart_tab(self) -> None:
        frame = ttk.Frame(self.chart_tab, padding=10)
        frame.pack(fill="both", expand=True)

        controls = ttk.Frame(frame)
        controls.pack(fill="x", pady=5)

        ttk.Label(controls, text="Chart Type").pack(side="left", padx=5)
        self.chart_type_combo = ttk.Combobox(controls, state="readonly", width=15, values=["bar", "line", "pie", "histogram"])
        self.chart_type_combo.set("bar")
        self.chart_type_combo.pack(side="left", padx=5)

        ttk.Label(controls, text="Category / X").pack(side="left", padx=5)
        self.chart_x_combo = ttk.Combobox(controls, state="readonly", width=25)
        self.chart_x_combo.pack(side="left", padx=5)

        ttk.Label(controls, text="Value / Y").pack(side="left", padx=5)
        self.chart_y_combo = ttk.Combobox(controls, state="readonly", width=25)
        self.chart_y_combo.pack(side="left", padx=5)

        ttk.Button(controls, text="Show Chart", command=self.show_chart).pack(side="left", padx=5)

        self.chart_help = ttk.Label(
            frame,
            text="Example: choose City as category and Sales as value to see total sales by city.",
        )
        self.chart_help.pack(anchor="w", pady=10)

    def open_file(self) -> None:
        file_path = filedialog.askopenfilename(
            title="Open Data File",
            filetypes=[
                ("Data Files", "*.csv *.xlsx *.xls *.json *.zip"),
                ("CSV Files", "*.csv"),
                ("Excel Files", "*.xlsx *.xls"),
                ("JSON Files", "*.json"),
                ("ZIP Files", "*.zip"),
                ("All Files", "*.*"),
            ],
        )

        if not file_path:
            return

        try:
            if file_path.lower().endswith(".csv"):
                df = self.load_csv_flexibly(file_path)
            elif file_path.lower().endswith((".xlsx", ".xls")):
                df = pd.read_excel(file_path)
            elif file_path.lower().endswith(".json"):
                with open(file_path, "r", encoding="utf-8") as file:
                    raw_data = json.load(file)
                df = pd.json_normalize(raw_data)
            elif file_path.lower().endswith(".zip"):
                df = self.load_from_zip(file_path)
            else:
                messagebox.showerror("Unsupported File", "Please open CSV, Excel, JSON, or ZIP files.")
                return
        except Exception as error:
            messagebox.showerror("Open Error", f"Could not open file.\n\n{error}")
            return

        self.current_file = file_path
        self.original_df = df.copy()
        self.df = df.copy()
        self.file_label.config(text=file_path)

        self.refresh_everything()
        self.log_issue("File loaded successfully.")

    def load_csv_flexibly(self, file_path: str) -> pd.DataFrame:
        attempts = [
            {"sep": None, "engine": "python", "encoding": "utf-8"},
            {"sep": ",", "engine": "python", "encoding": "utf-8"},
            {"sep": ";", "engine": "python", "encoding": "utf-8"},
            {"sep": "\t", "engine": "python", "encoding": "utf-8"},
            {"sep": "|", "engine": "python", "encoding": "utf-8"},
            {"sep": None, "engine": "python", "encoding": "latin-1"},
            {"sep": ",", "engine": "python", "encoding": "latin-1"},
            {"sep": ";", "engine": "python", "encoding": "latin-1"},
        ]

        last_error = None
        for options in attempts:
            try:
                df = pd.read_csv(file_path, on_bad_lines="skip", **options)
                if not df.empty and len(df.columns) > 0:
                    return df
            except Exception as error:
                last_error = error

        raise ValueError(
            "The file is too messy to read automatically. "
            "Please check whether it is really CSV and whether rows use mixed separators."
        ) from last_error

    def load_from_zip(self, file_path: str) -> pd.DataFrame:
        with zipfile.ZipFile(file_path, "r") as zip_file:
            file_names = zip_file.namelist()
            supported_files = [
                name
                for name in file_names
                if name.lower().endswith((".csv", ".xlsx", ".xls", ".json"))
            ]

            if not supported_files:
                raise ValueError("ZIP file does not contain any CSV, Excel, or JSON file.")

            target_file = supported_files[0]
            with zip_file.open(target_file) as inner_file:
                if target_file.lower().endswith(".csv"):
                    temp_path = None
                    try:
                        import os
                        import tempfile

                        with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as temp_file:
                            temp_file.write(inner_file.read())
                            temp_path = temp_file.name
                        return self.load_csv_flexibly(temp_path)
                    finally:
                        if temp_path:
                            try:
                                os.remove(temp_path)
                            except OSError:
                                pass

                if target_file.lower().endswith((".xlsx", ".xls")):
                    return pd.read_excel(inner_file)

                raw_data = json.load(inner_file)
                return pd.json_normalize(raw_data)

    def refresh_everything(self) -> None:
        self.update_summary()
        self.show_dataframe_in_sheet(self.df.head(500))
        self.update_column_options()

    def update_summary(self) -> None:
        if self.df.empty:
            self.summary_label.config(text="Rows: 0 | Columns: 0 | Missing: 0 | Duplicates: 0")
            return

        missing = int(self.df.isna().sum().sum())
        duplicates = int(self.df.duplicated().sum())
        self.summary_label.config(
            text=f"Rows: {len(self.df)} | Columns: {len(self.df.columns)} | Missing: {missing} | Duplicates: {duplicates}"
        )

    def update_column_options(self) -> None:
        columns = self.df.columns.tolist()
        numeric_columns = self.df.select_dtypes(include="number").columns.tolist()

        for combo in [self.column_combo, self.pivot_index_combo, self.chart_x_combo]:
            combo["values"] = columns
            if columns:
                combo.set(columns[0])

        value_options = numeric_columns if numeric_columns else columns
        for combo in [self.pivot_value_combo, self.chart_y_combo]:
            combo["values"] = value_options
            if value_options:
                combo.set(value_options[0])

    def show_dataframe_in_tree(self, tree: ttk.Treeview, df: pd.DataFrame) -> None:
        tree.delete(*tree.get_children())
        tree["columns"] = list(df.columns)

        for column in df.columns:
            tree.heading(column, text=column)
            tree.column(column, width=140, anchor="center")

        for _, row in df.iterrows():
            values = ["" if pd.isna(value) else str(value) for value in row.tolist()]
            tree.insert("", "end", values=values)

    def show_dataframe_in_sheet(self, df: pd.DataFrame) -> None:
        display_df = df.fillna("")
        self.preview_sheet.headers(display_df.columns.tolist())
        self.preview_sheet.set_sheet_data(display_df.astype(str).values.tolist())

    def apply_grid_changes(self) -> None:
        if self.df.empty:
            messagebox.showwarning("No Data", "Please open a file first.")
            return

        try:
            grid_data = self.preview_sheet.get_sheet_data()
            updated_df = pd.DataFrame(grid_data, columns=self.df.columns.tolist()).replace("", pd.NA)
            self.df = updated_df
            self.update_summary()
            self.update_column_options()
            self.clean_log.insert("end", "Applied manual changes from spreadsheet grid.\n")
        except Exception as error:
            messagebox.showerror("Grid Error", f"Could not apply changes from grid.\n\n{error}")

    def scan_problems(self) -> None:
        if self.df.empty:
            messagebox.showwarning("No Data", "Please open a file first.")
            return

        self.issues_box.delete("1.0", "end")
        messages = []

        blank_rows = int(self.df.isna().all(axis=1).sum())
        duplicate_rows = int(self.df.duplicated().sum())

        if blank_rows:
            messages.append(f"- Found {blank_rows} fully blank rows.")
        if duplicate_rows:
            messages.append(f"- Found {duplicate_rows} duplicate rows.")

        for column in self.df.columns:
            series = self.df[column]
            missing = int(series.isna().sum())
            if missing:
                messages.append(f"- Column `{column}` has {missing} missing values.")

            if pd.api.types.is_object_dtype(series) or pd.api.types.is_string_dtype(series):
                text = series.dropna().astype(str).str.strip()
                if not text.empty:
                    lowered_unique = {value.lower() for value in text.unique()}
                    if len(lowered_unique) != text.nunique() and text.nunique() <= 30:
                        messages.append(f"- Column `{column}` may have inconsistent capitalization or spelling.")

                    numeric_ratio = pd.to_numeric(text, errors="coerce").notna().mean()
                    if numeric_ratio > 0.8:
                        messages.append(f"- Column `{column}` looks numeric but is stored as text.")

                    date_ratio = pd.to_datetime(text, errors="coerce").notna().mean()
                    if date_ratio > 0.8:
                        messages.append(f"- Column `{column}` looks like dates but is stored as text.")

            if pd.api.types.is_numeric_dtype(series):
                numeric = pd.to_numeric(series, errors="coerce").dropna()
                if len(numeric) >= 4:
                    q1 = numeric.quantile(0.25)
                    q3 = numeric.quantile(0.75)
                    iqr = q3 - q1
                    if iqr > 0:
                        lower = q1 - 1.5 * iqr
                        upper = q3 + 1.5 * iqr
                        outliers = int(((numeric < lower) | (numeric > upper)).sum())
                        if outliers:
                            messages.append(f"- Column `{column}` has {outliers} possible outliers.")

        if not messages:
            messages.append("- No obvious data problems found.")

        self.issues_box.insert("end", "AI Problem Scan Result\n\n")
        self.issues_box.insert("end", "\n".join(messages))
        self.log_issue("AI scan finished.")

    def auto_clean(self) -> None:
        if self.df.empty:
            messagebox.showwarning("No Data", "Please open a file first.")
            return

        actions = []

        text_columns = self.df.select_dtypes(include=["object", "string"]).columns
        for column in text_columns:
            self.df[column] = self.df[column].astype("string").str.strip()
            self.df[column] = self.df[column].replace(["", "NA", "N/A", "null", "None", "?"], pd.NA)

        before_rows = len(self.df)
        self.df = self.df.dropna(how="all").drop_duplicates().copy()
        removed = before_rows - len(self.df)
        if removed:
            actions.append(f"Removed {removed} blank/duplicate rows.")

        for column in self.df.columns:
            series = self.df[column]
            if pd.api.types.is_object_dtype(series) or pd.api.types.is_string_dtype(series):
                text = series.dropna().astype(str)
                if not text.empty:
                    numeric_ratio = pd.to_numeric(text, errors="coerce").notna().mean()
                    date_ratio = pd.to_datetime(text, errors="coerce").notna().mean()

                    if numeric_ratio > 0.8:
                        self.df[column] = pd.to_numeric(self.df[column], errors="coerce")
                        actions.append(f"Converted `{column}` to numeric.")
                        continue

                    if date_ratio > 0.8:
                        self.df[column] = pd.to_datetime(self.df[column], errors="coerce")
                        actions.append(f"Converted `{column}` to datetime.")
                        continue

                    if text.nunique() <= 30:
                        mapping = {value: str(value).strip().title() for value in text.unique()}
                        self.df[column] = self.df[column].replace(mapping)

        self.refresh_everything()
        self.clean_log.insert("end", "Auto clean completed.\n")
        for action in actions:
            self.clean_log.insert("end", f"- {action}\n")
        if not actions:
            self.clean_log.insert("end", "- No major changes were needed.\n")

    def replace_values(self) -> None:
        if self.df.empty:
            messagebox.showwarning("No Data", "Please open a file first.")
            return

        column = self.column_combo.get()
        find_value = self.find_entry.get()
        replace_value = self.replace_entry.get()

        if not column:
            messagebox.showwarning("No Column", "Please choose a column.")
            return

        self.df[column] = self.df[column].replace(find_value, replace_value)
        self.refresh_everything()
        self.clean_log.insert("end", f"Replaced `{find_value}` with `{replace_value}` in `{column}`.\n")

    def drop_blank_rows(self) -> None:
        if self.df.empty:
            return
        before = len(self.df)
        self.df = self.df.dropna(how="all").copy()
        self.refresh_everything()
        self.clean_log.insert("end", f"Dropped {before - len(self.df)} fully blank rows.\n")

    def drop_duplicates(self) -> None:
        if self.df.empty:
            return
        before = len(self.df)
        self.df = self.df.drop_duplicates().copy()
        self.refresh_everything()
        self.clean_log.insert("end", f"Dropped {before - len(self.df)} duplicate rows.\n")

    def trim_spaces(self) -> None:
        if self.df.empty:
            return
        text_columns = self.df.select_dtypes(include=["object", "string"]).columns
        for column in text_columns:
            self.df[column] = self.df[column].astype("string").str.strip()
        self.refresh_everything()
        self.clean_log.insert("end", "Trimmed spaces from text columns.\n")

    def create_pivot(self) -> None:
        if self.df.empty:
            messagebox.showwarning("No Data", "Please open a file first.")
            return

        index_col = self.pivot_index_combo.get()
        value_col = self.pivot_value_combo.get()
        agg_func = self.pivot_agg_combo.get()

        if not index_col or not value_col:
            messagebox.showwarning("Missing Selection", "Please choose group and value columns.")
            return

        try:
            pivot_df = pd.pivot_table(
                self.df,
                index=index_col,
                values=value_col,
                aggfunc=agg_func,
            ).reset_index()
        except Exception as error:
            messagebox.showerror("Pivot Error", f"Could not create pivot table.\n\n{error}")
            return

        self.show_dataframe_in_tree(self.pivot_tree, pivot_df)

    def show_chart(self) -> None:
        if self.df.empty:
            messagebox.showwarning("No Data", "Please open a file first.")
            return

        chart_type = self.chart_type_combo.get()
        x_col = self.chart_x_combo.get()
        y_col = self.chart_y_combo.get()

        if not x_col:
            messagebox.showwarning("Missing Selection", "Please choose a category column.")
            return

        try:
            if chart_type == "bar":
                grouped = self.df.groupby(x_col, dropna=False)[y_col].sum()
                fig = px.bar(grouped.reset_index(), x=x_col, y=y_col, title=f"{y_col} by {x_col}")
            elif chart_type == "line":
                grouped = self.df.groupby(x_col, dropna=False)[y_col].sum()
                fig = px.line(grouped.reset_index(), x=x_col, y=y_col, markers=True, title=f"{y_col} by {x_col}")
            elif chart_type == "pie":
                grouped = self.df.groupby(x_col, dropna=False)[y_col].sum()
                fig = px.pie(grouped.reset_index(), names=x_col, values=y_col, title=f"{y_col} share by {x_col}")
            elif chart_type == "histogram":
                numeric_series = pd.to_numeric(self.df[y_col], errors="coerce").dropna()
                fig = px.histogram(numeric_series, x=y_col, nbins=20, title=f"{y_col} distribution")

            fig.show()
        except Exception as error:
            messagebox.showerror("Chart Error", f"Could not create chart.\n\n{error}")

    def export_csv(self) -> None:
        if self.df.empty:
            messagebox.showwarning("No Data", "Please open a file first.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if not file_path:
            return

        self.df.to_csv(file_path, index=False)
        messagebox.showinfo("Saved", "CSV file saved successfully.")

    def export_excel(self) -> None:
        if self.df.empty:
            messagebox.showwarning("No Data", "Please open a file first.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])
        if not file_path:
            return

        self.df.to_excel(file_path, index=False)
        messagebox.showinfo("Saved", "Excel file saved successfully.")

    def reset_data(self) -> None:
        if self.original_df.empty:
            return
        self.df = self.original_df.copy()
        self.refresh_everything()
        self.clean_log.delete("1.0", "end")
        self.issues_box.delete("1.0", "end")
        self.log_issue("Data reset to original file.")

    def log_issue(self, message: str) -> None:
        self.issues_box.insert("end", f"{message}\n")


if __name__ == "__main__":
    app_root = tk.Tk()
    app = DataAnalystStudio(app_root)
    app_root.mainloop()
