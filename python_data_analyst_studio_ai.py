import json
import os
import re
import sys
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def _detect_sep(text: str) -> str:
    sample = "\n".join(text.splitlines()[:20])
    return max([";", ",", "\t", "|"], key=sample.count)


def load_any_file(path: str) -> pd.DataFrame:
    ext = os.path.splitext(path)[1].lower()

    if ext in (".xlsx", ".xls"):
        df = pd.read_excel(path)
        if df.shape[1] <= 3 and df.iloc[:, 0].astype(str).str.contains(";").mean() > 0.5:
            rows = [str(r).split(";") for r in df.iloc[:, 0]]
            w = max(len(r) for r in rows)
            rows = [(r + [""] * (w - len(r)))[:w] for r in rows]
            hdr = [re.sub(r"[^\x00-\x7F]", "", h).strip() or f"Col_{i}" for i, h in enumerate(rows[0])]
            df = pd.DataFrame(rows[1:], columns=hdr)
        return _clean_nulls(df)

    if ext == ".json":
        with open(path, "r", encoding="utf-8") as f:
            return _clean_nulls(pd.json_normalize(json.load(f)))

    raw = None
    for enc in ["utf-8", "utf-8-sig", "latin-1", "cp1252"]:
        try:
            with open(path, "r", encoding=enc, errors="replace") as f:
                raw = f.read()
            break
        except Exception:
            continue
    if not raw:
        raise ValueError("Cannot read file.")

    sep = _detect_sep(raw)
    lines = [l.strip() for l in raw.splitlines() if l.strip() and not re.fullmatch(r"[;,|\t\s]+", l.strip())]
    rows = [l.split(sep) for l in lines]
    width = max(set(len(r) for r in rows), key=[len(r) for r in rows].count)
    rows = [(r + [""] * (width - len(r)))[:width] for r in rows]

    hdr = rows[0]
    hdr = [re.sub(r"[^\x00-\x7F]", "", h).strip().replace(" ", "_") or f"Col_{i}" for i, h in enumerate(hdr)]
    seen, clean = {}, []
    for n in hdr:
        if n in seen:
            seen[n] += 1
            clean.append(f"{n}_{seen[n]}")
        else:
            seen[n] = 0
            clean.append(n)

    df = pd.DataFrame(rows[1:], columns=clean)
    return _clean_nulls(df)


def _clean_nulls(df: pd.DataFrame) -> pd.DataFrame:
    nulls = ["NULL", "null", "N/A", "NA", "n/a", "#N/A", "#n/a", "None", "none", "nan", "NaN", "?", "-", "", "INF", "inf"]
    df.replace(nulls, pd.NA, inplace=True)
    for col in df.select_dtypes(include=["object"]).columns:
        s = df[col].dropna().astype(str).str.strip()
        if s.empty:
            continue
        num = pd.to_numeric(s.str.replace(r"[$,\s%]", "", regex=True), errors="coerce")
        if num.notna().mean() > 0.82:
            df[col] = pd.to_numeric(df[col].astype(str).str.replace(r"[$,\s%]", "", regex=True), errors="coerce")
    return df


def build_profile(df: pd.DataFrame) -> str:
    lines = [
        f"SHAPE: {len(df):,} rows x {len(df.columns)} columns",
        f"MISSING CELLS: {int(df.isna().sum().sum()):,}",
        f"DUPLICATE ROWS: {int(df.duplicated().sum()):,}",
        "",
    ]
    for col in df.columns:
        s = df[col]
        missing = int(s.isna().sum())
        pct = f"{missing/len(df)*100:.1f}%" if len(df) else "0%"
        uniq = s.nunique()
        dtype = str(s.dtype)
        lines.append(f"COLUMN {col}  type={dtype}  missing={missing}({pct})  unique_values={uniq}")

        non_null = s.dropna().astype(str).str.strip()
        if non_null.empty:
            lines.append("  -> All values missing")
            continue

        sample = non_null.value_counts().head(10).index.tolist()
        lines.append(f"  Sample values: {sample}")

        if pd.api.types.is_numeric_dtype(s):
            num = pd.to_numeric(s, errors="coerce").dropna()
            if len(num):
                lines.append(f"  Numeric stats: min={num.min():.4g}  max={num.max():.4g}  mean={num.mean():.4g}  std={num.std():.4g}")
                if int(np.isinf(num).sum()):
                    lines.append(f"  Has inf/-inf values: {int(np.isinf(num).sum())}")
        else:
            try:
                dr = pd.to_datetime(non_null, errors="coerce", infer_datetime_format=True).notna().mean()
                if dr > 0.5:
                    lines.append(f"  Date-parse rate: {dr*100:.0f}% (stored as text)")
            except Exception:
                pass

            nr = pd.to_numeric(non_null.str.replace(r"[$,\s%]", "", regex=True), errors="coerce").notna().mean()
            if nr > 0.7:
                lines.append(f"  Numeric-as-text rate: {nr*100:.0f}%")
        lines.append("")
    return "\n".join(lines)


AI_PROMPT = """You are a world-class data analyst and data quality expert.
A user has uploaded a dataset. You are given a statistical profile of it.

Your job: find EVERY data quality problem, exactly like a senior data engineer would.

Look for:
- Missing / null values (which columns, how bad)
- Duplicate rows
- Wrong data types (numbers stored as text, dates stored as text)
- Inconsistent formats (mixed date formats, mixed separators, currency symbols)
- Inconsistent capitalisation (e.g. "usa" vs "USA" vs "Us")
- Typos and misspellings (e.g. "New Zeland", "Pg-13" vs "PG-13")
- Wrong decimal scale (e.g. score=86.0 when it should be 8.6)
- Impossible or suspicious values (inf, negative duration, 0 income)
- Ghost/unnamed columns (Col_0, Col_1, Unnamed...)
- Truncated column names (e.g. GENR, TITL)
- Multi-value cells that should be split (genres, tags)
- ID columns with duplicates
- Columns that are 80%+ empty

Output format - one issue per line with emoji:
⚠️ [issue]
❓ [issue]
🔢 [issue]
📅 [issue]
🔠 [issue]
🔤 [issue]
📊 [issue]
👻 [issue]

Then add:

-- HOW TO FIX IT --
1. [Specific action]
2. [Specific action]
...

Be specific. Use exact column names. Be direct. Do not repeat the profile."""


def run_ai_scan(df: pd.DataFrame, api_key: str, on_chunk=None, on_done=None, on_error=None):
    def _worker():
        try:
            from groq import Groq
        except ImportError:
            if on_error:
                on_error("?  Package missing.\n\nRun this in terminal:\n\n" + f'    "{sys.executable}" -m pip install groq')
            return

        profile = build_profile(df)

        try:
            client = Groq(api_key=api_key)
            stream = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "system", "content": AI_PROMPT}, {"role": "user", "content": f"Dataset profile:\n\n{profile}"}],
                max_tokens=2048,
                stream=True,
            )
            full = []
            for chunk in stream:
                piece = chunk.choices[0].delta.content or ""
                full.append(piece)
                if on_chunk:
                    on_chunk(piece)
            if on_done:
                on_done("".join(full))
        except Exception as e:
            if on_error:
                on_error(f"Groq API error:\n\n{str(e)}")

    threading.Thread(target=_worker, daemon=True).start()


def one_click_clean(df: pd.DataFrame):
    log = []
    df = df.copy()

    nulls = ["NULL", "null", "N/A", "NA", "n/a", "#N/A", "#n/a", "None", "none", "nan", "NaN", "?", "-", "", "INF", "inf", "-inf"]
    hits = int(df.isin(nulls).sum().sum())
    df.replace(nulls, pd.NA, inplace=True)
    if hits:
        log.append(f"Replaced {hits} null-like tokens with proper blanks.")

    for c in df.select_dtypes(include=["object", "string"]).columns:
        df[c] = df[c].astype("string").str.strip()
    log.append("Trimmed whitespace from all text columns.")

    before = len(df)
    df = df[df.isna().mean(axis=1) <= 0.8].copy()
    if before - len(df):
        log.append(f"Removed {before - len(df)} rows that were >80% empty.")

    before = len(df)
    df = df.dropna(how="all").drop_duplicates().copy()
    if before - len(df):
        log.append(f"Removed {before - len(df)} fully blank / duplicate rows.")

    for c in df.select_dtypes(include=["object", "string"]).columns:
        s = df[c].astype(str).str.replace(r"[$,\s%]", "", regex=True)
        num = pd.to_numeric(s, errors="coerce")
        if num.notna().mean() > 0.80:
            df[c] = pd.to_numeric(s, errors="coerce")
            log.append(f"Converted {c} from text to numeric.")

    for c in df.select_dtypes(include=["object", "string"]).columns:
        try:
            p = pd.to_datetime(df[c].astype(str), errors="coerce", infer_datetime_format=True)
            if p.notna().mean() > 0.70:
                df[c] = p
                log.append(f"Converted {c} from text to datetime.")
        except Exception:
            pass

    df.columns = [re.sub(r"\s+", "_", re.sub(r"[^\w\s]", "", str(c)).strip()).upper() for c in df.columns]
    log.append("Column names standardised to UPPER_SNAKE_CASE.")

    if not log:
        log.append("Data already looks clean - no changes made.")
    return df, log


class ExcelAICleaner:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Excel AI Cleaner - Powered by Groq (Free)")
        self.root.geometry("1400x820")

        self.df_original = pd.DataFrame()
        self.df = pd.DataFrame()
        self.file_path = ""
        self._api_key = tk.StringVar(value=self._load_key())
        self._in_fix = False

        self._build_ui()

    def _key_file(self):
        here = os.path.dirname(os.path.abspath(__file__))
        if os.path.basename(here).lower() == "__pycache__":
            here = os.path.dirname(here)
        return os.path.join(here, ".groq_key")

    def _load_key(self):
        try:
            with open(self._key_file(), encoding="utf-8") as f:
                return f.read().strip()
        except Exception:
            return os.environ.get("GROQ_API_KEY", "")

    def _save_key(self):
        try:
            with open(self._key_file(), "w", encoding="utf-8") as f:
                f.write(self._api_key.get().strip())
            messagebox.showinfo("Saved", "Groq API key saved.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _build_ui(self):
        bar = ttk.Frame(self.root, padding=8)
        bar.pack(fill="x")

        buttons = [
            ("Open File", self.open_file),
            ("AI Scan", self.ai_scan),
            ("One Click Clean", self.auto_clean),
            ("Reset", self.reset),
            ("Export CSV", self.export_csv),
            ("Export Excel", self.export_excel),
        ]
        for label, cmd in buttons:
            ttk.Button(bar, text=label, command=cmd).pack(side="left", padx=3)

        self.lbl_file = ttk.Label(bar, text="No file opened", foreground="gray")
        self.lbl_file.pack(side="left", padx=12)

        self.var_status = tk.StringVar(value="Ready")
        ttk.Label(bar, textvariable=self.var_status, foreground="#0055cc", font=("Segoe UI", 9, "bold")).pack(side="right", padx=8)

        self.pbar = ttk.Progressbar(self.root, mode="indeterminate")
        self.pbar.pack(fill="x", padx=10, pady=2)

        nb = ttk.Notebook(self.root)
        nb.pack(fill="both", expand=True, padx=10, pady=4)
        self.nb = nb

        frames = {}
        for key, title in [
            ("preview", "Data Preview"),
            ("ai", "AI Issues & Fixes"),
            ("clean", "Clean / Replace"),
            ("pivot", "Pivot Table"),
            ("chart", "Chart"),
            ("settings", "Settings"),
        ]:
            f = ttk.Frame(nb)
            nb.add(f, text=title)
            frames[key] = f

        self.frames = frames
        self._tab_preview(frames["preview"])
        self._tab_ai(frames["ai"])
        self._tab_clean(frames["clean"])
        self._tab_pivot(frames["pivot"])
        self._tab_chart(frames["chart"])
        self._tab_settings(frames["settings"])

    def _tab_preview(self, p):
        top = ttk.Frame(p, padding=8)
        top.pack(fill="x")
        self.lbl_summary = ttk.Label(top, text="Rows: 0 | Columns: 0 | Missing: 0 | Duplicates: 0", font=("Segoe UI", 10, "bold"))
        self.lbl_summary.pack(anchor="w")

        tf = ttk.Frame(p)
        tf.pack(fill="both", expand=True, padx=8, pady=4)
        self.tree_preview = ttk.Treeview(tf, show="headings")
        self.tree_preview.pack(side="left", fill="both", expand=True)
        ttk.Scrollbar(tf, orient="vertical", command=self.tree_preview.yview).pack(side="right", fill="y")
        xs = ttk.Scrollbar(p, orient="horizontal", command=self.tree_preview.xview)
        xs.pack(fill="x")
        self.tree_preview.configure(xscrollcommand=xs.set)

    def _tab_ai(self, p):
        hdr = ttk.Frame(p, padding=8)
        hdr.pack(fill="x")
        ttk.Label(hdr, text="AI Problem Finder - powered by Groq (Llama 3)", font=("Segoe UI", 11, "bold")).pack(side="left")
        ttk.Button(hdr, text="Run AI Scan", command=self.ai_scan).pack(side="right", padx=4)
        ttk.Button(hdr, text="Clear", command=lambda: self.ai_box.delete("1.0", "end")).pack(side="right", padx=4)

        self.ai_box = tk.Text(p, wrap="word", font=("Consolas", 10), bg="#0d1117", fg="#c9d1d9", insertbackground="white", selectbackground="#264f78")
        self.ai_box.pack(fill="both", expand=True, padx=8, pady=4)

        self.ai_box.tag_config("head", foreground="#58a6ff", font=("Consolas", 11, "bold"))
        self.ai_box.tag_config("issue", foreground="#f0883e")
        self.ai_box.tag_config("fix", foreground="#3fb950")
        self.ai_box.tag_config("dim", foreground="#8b949e")

    def _tab_clean(self, p):
        f = ttk.Frame(p, padding=10)
        f.pack(fill="both", expand=True)

        r1 = ttk.Frame(f)
        r1.pack(fill="x", pady=3)
        ttk.Label(r1, text="Column").pack(side="left", padx=3)
        self.cb_col = ttk.Combobox(r1, state="readonly", width=20)
        self.cb_col.pack(side="left", padx=3)
        ttk.Label(r1, text="Find").pack(side="left", padx=3)
        self.ent_find = ttk.Entry(r1, width=16)
        self.ent_find.pack(side="left", padx=3)
        ttk.Label(r1, text="Replace With").pack(side="left", padx=3)
        self.ent_repl = ttk.Entry(r1, width=16)
        self.ent_repl.pack(side="left", padx=3)
        ttk.Button(r1, text="Replace All", command=self.replace_values).pack(side="left", padx=3)

        r2 = ttk.Frame(f)
        r2.pack(fill="x", pady=3)
        for txt, cmd in [
            ("Drop Blank Rows", self.drop_blanks),
            ("Drop Duplicates", self.drop_dupes),
            ("Trim Spaces", self.trim_spaces),
            ("Fix Dates", self.fix_dates),
            ("Fix Numbers", self.fix_nums),
            ("Title Case", self.title_case),
            ("Remove Junk Rows", self.remove_junk),
        ]:
            ttk.Button(r2, text=txt, command=cmd).pack(side="left", padx=3)

        self.clean_log = tk.Text(f, wrap="word", font=("Consolas", 10))
        self.clean_log.pack(fill="both", expand=True, pady=6)

    def _tab_pivot(self, p):
        f = ttk.Frame(p, padding=10)
        f.pack(fill="both", expand=True)
        ctrl = ttk.Frame(f)
        ctrl.pack(fill="x", pady=4)
        ttk.Label(ctrl, text="Group By").pack(side="left", padx=4)
        self.cb_piv_idx = ttk.Combobox(ctrl, state="readonly", width=20)
        self.cb_piv_idx.pack(side="left", padx=4)
        ttk.Label(ctrl, text="Value").pack(side="left", padx=4)
        self.cb_piv_val = ttk.Combobox(ctrl, state="readonly", width=20)
        self.cb_piv_val.pack(side="left", padx=4)
        ttk.Label(ctrl, text="Agg").pack(side="left", padx=4)
        self.cb_piv_agg = ttk.Combobox(ctrl, state="readonly", width=10, values=["sum", "mean", "count", "min", "max"])
        self.cb_piv_agg.set("sum")
        self.cb_piv_agg.pack(side="left", padx=4)
        ttk.Button(ctrl, text="Create Pivot", command=self.make_pivot).pack(side="left", padx=4)

        tf = ttk.Frame(f)
        tf.pack(fill="both", expand=True, pady=6)
        self.tree_pivot = ttk.Treeview(tf, show="headings")
        self.tree_pivot.pack(side="left", fill="both", expand=True)
        ttk.Scrollbar(tf, orient="vertical", command=self.tree_pivot.yview).pack(side="right", fill="y")

    def _tab_chart(self, p):
        f = ttk.Frame(p, padding=10)
        f.pack(fill="both", expand=True)
        ctrl = ttk.Frame(f)
        ctrl.pack(fill="x", pady=4)
        ttk.Label(ctrl, text="Type").pack(side="left", padx=4)
        self.cb_cht_type = ttk.Combobox(ctrl, state="readonly", width=12, values=["bar", "line", "pie", "histogram", "scatter"])
        self.cb_cht_type.set("bar")
        self.cb_cht_type.pack(side="left", padx=4)
        ttk.Label(ctrl, text="X / Category").pack(side="left", padx=4)
        self.cb_cht_x = ttk.Combobox(ctrl, state="readonly", width=20)
        self.cb_cht_x.pack(side="left", padx=4)
        ttk.Label(ctrl, text="Y / Value").pack(side="left", padx=4)
        self.cb_cht_y = ttk.Combobox(ctrl, state="readonly", width=20)
        self.cb_cht_y.pack(side="left", padx=4)
        ttk.Button(ctrl, text="Show Chart", command=self.show_chart).pack(side="left", padx=4)
        ttk.Label(f, text="Tip: pick a text column as X and a number column as Y.", foreground="gray").pack(anchor="w", pady=6)

    def _tab_settings(self, p):
        f = ttk.Frame(p, padding=24)
        f.pack(fill="both", expand=True)

        ttk.Label(f, text="Groq API Key (Free)", font=("Segoe UI", 12, "bold")).pack(anchor="w")
        ttk.Label(f, text="Get your free key -> https://console.groq.com  (sign up, click API Keys, create key)", foreground="#0055cc").pack(anchor="w", pady=4)

        row = ttk.Frame(f)
        row.pack(fill="x", pady=8)
        self.ent_key = ttk.Entry(row, textvariable=self._api_key, width=55, show="*")
        self.ent_key.pack(side="left", padx=4)
        ttk.Button(row, text="Show/Hide", command=lambda: self.ent_key.config(show="" if self.ent_key.cget("show") == "*" else "*")).pack(side="left", padx=4)
        ttk.Button(row, text="Save Key", command=self._save_key).pack(side="left", padx=4)
        ttk.Button(row, text="Test Key", command=self._test_key).pack(side="left", padx=4)

        ttk.Separator(f).pack(fill="x", pady=16)
        ttk.Label(f, text="How it works", font=("Segoe UI", 10, "bold")).pack(anchor="w")
        ttk.Label(
            f,
            justify="left",
            foreground="gray",
            text=(
                "1.  Open any CSV / Excel / JSON file - even huge or messy ones.\n"
                "2.  Click AI Scan - the app builds a statistical profile of your data\n"
                "    and sends ONLY that summary to the AI (not your raw data).\n"
                "3.  The AI (Llama 3 via Groq) reads the profile and thinks like a real\n"
                "    data analyst.\n"
                "4.  Click One Click Clean to auto-fix the common issues instantly.\n\n"
                "Works on any file size."
            ),
        ).pack(anchor="w")

    def open_file(self):
        path = filedialog.askopenfilename(filetypes=[("Data Files", "*.csv *.xlsx *.xls *.json"), ("All", "*.*")])
        if not path:
            return
        self._busy(True, "Loading...")
        threading.Thread(target=self._load_thread, args=(path,), daemon=True).start()

    def _load_thread(self, path):
        try:
            df = load_any_file(path)
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Load Error", str(e)))
            self._busy(False, "Load failed")
            return
        self.root.after(0, lambda: self._finish_load(path, df))

    def _finish_load(self, path, df):
        self.file_path = path
        self.df_original = df.copy()
        self.df = df.copy()
        self.lbl_file.config(text=os.path.basename(path), foreground="black")
        self._refresh()
        self._busy(False, f"Loaded  {len(df):,} rows x {len(df.columns)} cols")

    def _refresh(self):
        self._upd_summary()
        self._fill_tree(self.tree_preview, self.df.head(500))
        self._upd_combos()

    def _upd_summary(self):
        if self.df.empty:
            self.lbl_summary.config(text="Rows: 0 | Columns: 0 | Missing: 0 | Duplicates: 0")
            return
        self.lbl_summary.config(
            text=f"Rows: {len(self.df):,} | Columns: {len(self.df.columns)} | Missing: {int(self.df.isna().sum().sum()):,} | Duplicates: {int(self.df.duplicated().sum()):,}"
        )

    def _upd_combos(self):
        cols = self.df.columns.tolist()
        nums = self.df.select_dtypes(include="number").columns.tolist()
        for cb in [self.cb_col, self.cb_piv_idx, self.cb_cht_x]:
            cb["values"] = cols
            if cols:
                cb.set(cols[0])
        for cb in [self.cb_piv_val, self.cb_cht_y]:
            cb["values"] = nums or cols
            if (nums or cols):
                cb.set((nums or cols)[0])

    def _fill_tree(self, tree, df):
        tree.delete(*tree.get_children())
        tree["columns"] = list(df.columns)
        for c in df.columns:
            tree.heading(c, text=c)
            tree.column(c, width=130, anchor="center", minwidth=50)
        for _, row in df.iterrows():
            tree.insert("", "end", values=["" if pd.isna(v) else str(v) for v in row])

    def ai_scan(self):
        if self.df.empty:
            messagebox.showwarning("No Data", "Please open a file first.")
            return
        key = self._api_key.get().strip()
        if not key:
            messagebox.showwarning("No API Key", "Please add your Groq API key in the Settings tab.\n\nFree key at: https://console.groq.com")
            self.nb.select(self.frames["settings"])
            return

        self._in_fix = False
        self.ai_box.delete("1.0", "end")
        self._ai_write("AI Problem Finder - Groq / Llama-3\n", "head")
        self._ai_write(f"File : {os.path.basename(self.file_path)}\n", "dim")
        self._ai_write(f"Size : {len(self.df):,} rows x {len(self.df.columns)} columns\n\n", "dim")
        self.nb.select(self.frames["ai"])
        self._busy(True, "AI is thinking...")

        run_ai_scan(
            df=self.df,
            api_key=key,
            on_chunk=lambda piece: self.root.after(0, lambda p=piece: self._stream_chunk(p)),
            on_done=lambda _: self.root.after(0, lambda: self._busy(False, "AI scan complete")),
            on_error=lambda e: self.root.after(0, lambda err=e: self._on_ai_error(err)),
        )

    def _stream_chunk(self, piece: str):
        tag = "fix" if hasattr(self, "_in_fix") and self._in_fix else None
        if "HOW TO FIX" in piece.upper():
            self._in_fix = True
        self.ai_box.insert(
            "end",
            piece,
            tag or "issue" if any(piece.startswith(e) for e in ["⚠", "❓", "🔢", "📅", "🔠", "🔤", "📊", "👻", "✂", "💰", "🔍"]) else "",
        )
        self.ai_box.see("end")

    def _on_ai_error(self, err):
        self._busy(False, "AI error")
        self._ai_write("\n" + err + "\n", "issue")

    def _ai_write(self, text, tag=None):
        self.ai_box.insert("end", text, tag or "")
        self.ai_box.see("end")

    def auto_clean(self):
        if self.df.empty:
            messagebox.showwarning("No Data", "Open a file first.")
            return
        self._busy(True, "Cleaning...")
        threading.Thread(target=self._clean_thread, daemon=True).start()

    def _clean_thread(self):
        cleaned, log = one_click_clean(self.df)
        self.root.after(0, lambda: self._finish_clean(cleaned, log))

    def _finish_clean(self, df, log):
        self.df = df
        self._refresh()
        self.clean_log.insert("end", "One Click Clean - Done\n" + "-" * 50 + "\n")
        for line in log:
            self.clean_log.insert("end", line + "\n")
        self.clean_log.insert("end", "\n")
        self.nb.select(self.frames["clean"])
        self._busy(False, "Clean complete")

    def replace_values(self):
        if self.df.empty:
            return
        col = self.cb_col.get()
        find = self.ent_find.get()
        repl = self.ent_repl.get()
        if not col:
            return
        self.df[col] = self.df[col].replace(find, repl)
        self._refresh()
        self.clean_log.insert("end", f"Replaced '{find}' -> '{repl}' in {col}\n")

    def drop_blanks(self):
        if self.df.empty:
            return
        b = len(self.df)
        self.df = self.df.dropna(how="all").copy()
        self._refresh()
        self.clean_log.insert("end", f"Dropped {b-len(self.df)} blank rows.\n")

    def drop_dupes(self):
        if self.df.empty:
            return
        b = len(self.df)
        self.df = self.df.drop_duplicates().copy()
        self._refresh()
        self.clean_log.insert("end", f"Dropped {b-len(self.df)} duplicate rows.\n")

    def trim_spaces(self):
        if self.df.empty:
            return
        for c in self.df.select_dtypes(include=["object", "string"]).columns:
            self.df[c] = self.df[c].astype("string").str.strip()
        self._refresh()
        self.clean_log.insert("end", "Trimmed whitespace.\n")

    def fix_dates(self):
        if self.df.empty:
            return
        fixed = []
        for c in self.df.select_dtypes(include=["object", "string"]).columns:
            try:
                p = pd.to_datetime(self.df[c].astype(str), errors="coerce", infer_datetime_format=True)
                if p.notna().mean() > 0.5:
                    self.df[c] = p
                    fixed.append(c)
            except Exception:
                pass
        self._refresh()
        self.clean_log.insert("end", f"Fixed date columns: {', '.join(fixed)}\n" if fixed else "No date columns found.\n")

    def fix_nums(self):
        if self.df.empty:
            return
        fixed = []
        for c in self.df.select_dtypes(include=["object", "string"]).columns:
            n = pd.to_numeric(self.df[c].astype(str).str.replace(r"[$,\s%]", "", regex=True), errors="coerce")
            if n.notna().mean() > 0.6:
                self.df[c] = n
                fixed.append(c)
        self._refresh()
        self.clean_log.insert("end", f"Fixed numeric: {', '.join(fixed)}\n" if fixed else "None found.\n")

    def title_case(self):
        if self.df.empty:
            return
        for c in self.df.select_dtypes(include=["object", "string"]).columns:
            self.df[c] = self.df[c].astype("string").str.title()
        self._refresh()
        self.clean_log.insert("end", "Applied Title Case.\n")

    def remove_junk(self):
        if self.df.empty:
            return
        b = len(self.df)
        self.df = self.df[self.df.isna().mean(axis=1) <= 0.8].copy()
        self._refresh()
        self.clean_log.insert("end", f"Removed {b-len(self.df)} junk rows.\n")

    def make_pivot(self):
        if self.df.empty:
            return
        try:
            piv = pd.pivot_table(
                self.df,
                index=self.cb_piv_idx.get(),
                values=self.cb_piv_val.get(),
                aggfunc=self.cb_piv_agg.get(),
            ).reset_index()
            self._fill_tree(self.tree_pivot, piv)
        except Exception as e:
            messagebox.showerror("Pivot Error", str(e))

    def show_chart(self):
        if self.df.empty:
            return
        ct, xc, yc = self.cb_cht_type.get(), self.cb_cht_x.get(), self.cb_cht_y.get()
        try:
            plt.figure(figsize=(10, 6))
            if ct == "bar":
                self.df.groupby(xc, dropna=False)[yc].sum().plot(kind="bar")
            elif ct == "line":
                self.df.groupby(xc, dropna=False)[yc].sum().plot(kind="line", marker="o")
            elif ct == "pie":
                self.df.groupby(xc, dropna=False)[yc].sum().plot(kind="pie", autopct="%1.1f%%")
                plt.ylabel("")
            elif ct == "histogram":
                pd.to_numeric(self.df[yc], errors="coerce").dropna().plot(kind="hist", bins=20)
            elif ct == "scatter":
                plt.scatter(pd.to_numeric(self.df[xc], errors="coerce"), pd.to_numeric(self.df[yc], errors="coerce"), alpha=0.5)
            plt.title(f"{ct.title()}  -  {yc}  by  {xc}")
            plt.tight_layout()
            plt.show()
        except Exception as e:
            messagebox.showerror("Chart Error", str(e))

    def export_csv(self):
        if self.df.empty:
            return
        p = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV", "*.csv")])
        if p:
            self.df.to_csv(p, index=False)
            messagebox.showinfo("Saved", p)

    def export_excel(self):
        if self.df.empty:
            return
        p = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel", "*.xlsx")])
        if p:
            self.df.to_excel(p, index=False)
            messagebox.showinfo("Saved", p)

    def reset(self):
        if self.df_original.empty:
            return
        self.df = self.df_original.copy()
        self._refresh()
        self.clean_log.delete("1.0", "end")
        self.ai_box.delete("1.0", "end")
        self._busy(False, "Reset to original")

    def _test_key(self):
        key = self._api_key.get().strip()
        if not key:
            messagebox.showwarning("No Key", "Enter your Groq key first.")
            return
        self._busy(True, "Testing...")

        def _t():
            try:
                from groq import Groq

                Groq(api_key=key).chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "user", "content": "Say OK"}],
                    max_tokens=5,
                )
                self.root.after(0, lambda: (messagebox.showinfo("Success", "Groq key works. AI is connected."), self._busy(False, "Key OK")))
            except ImportError:
                self.root.after(
                    0,
                    lambda: (
                        messagebox.showerror("Missing package", "Run in terminal:\n\n" + f'    "{sys.executable}" -m pip install groq'),
                        self._busy(False, ""),
                    ),
                )
            except Exception as e:
                self.root.after(0, lambda err=e: (messagebox.showerror("API Error", str(err)), self._busy(False, "Key failed")))

        threading.Thread(target=_t, daemon=True).start()

    def _busy(self, on: bool, status: str = ""):
        def _do():
            self.var_status.set(status)
            if on:
                self.pbar.start(10)
            else:
                self.pbar.stop()

        self.root.after(0, _do)


if __name__ == "__main__":
    root = tk.Tk()
    ExcelAICleaner(root)
    root.mainloop()
