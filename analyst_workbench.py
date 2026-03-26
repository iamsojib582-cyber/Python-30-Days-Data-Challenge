from io import BytesIO

import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(page_title="Analyst Workbench", layout="wide")

MISSING_TOKENS = {"", "na", "n/a", "null", "none", "nan", "?", "-", "--"}


def load_file(uploaded_file) -> pd.DataFrame:
    if uploaded_file.name.lower().endswith(".csv"):
        try:
            return pd.read_csv(uploaded_file)
        except UnicodeDecodeError:
            uploaded_file.seek(0)
            return pd.read_csv(uploaded_file, encoding="latin-1")
    return pd.read_excel(uploaded_file)


def normalize_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = df.copy()
    text_columns = cleaned.select_dtypes(include=["object", "string"]).columns
    for column in text_columns:
        cleaned[column] = cleaned[column].astype("string").str.strip()
        cleaned[column] = cleaned[column].replace(list(MISSING_TOKENS), pd.NA)
    return cleaned


def detect_column_issues(df: pd.DataFrame) -> pd.DataFrame:
    normalized = normalize_missing_values(df)
    issue_rows = []

    for column in normalized.columns:
        series = normalized[column]
        non_null = series.dropna()
        issue_list = []

        missing_count = int(series.isna().sum())
        duplicate_count = int(non_null.duplicated().sum())

        if missing_count:
            issue_list.append(f"{missing_count} missing")
        if duplicate_count:
            issue_list.append(f"{duplicate_count} duplicated values")

        if pd.api.types.is_object_dtype(series) or pd.api.types.is_string_dtype(series):
            lowered = non_null.astype(str).str.lower()
            numeric_ratio = pd.to_numeric(lowered, errors="coerce").notna().mean() if len(lowered) else 0
            parsed_dates = pd.to_datetime(non_null, errors="coerce")
            date_ratio = parsed_dates.notna().mean() if len(non_null) else 0
            unique_count = int(non_null.nunique())

            if numeric_ratio > 0.8 and unique_count > 0:
                issue_list.append("looks numeric but stored as text")
            elif date_ratio > 0.8 and unique_count > 0:
                issue_list.append("looks like a date but stored as text")

            if unique_count > 0 and unique_count <= 20:
                stripped_unique = pd.Series(non_null.astype(str).str.strip().unique())
                lowered_unique = pd.Series(stripped_unique.str.lower().unique())
                if len(stripped_unique) != len(lowered_unique):
                    issue_list.append("possible inconsistent capitalization")

        if pd.api.types.is_numeric_dtype(series):
            numeric = pd.to_numeric(series, errors="coerce").dropna()
            if len(numeric) >= 4:
                q1 = numeric.quantile(0.25)
                q3 = numeric.quantile(0.75)
                iqr = q3 - q1
                if iqr > 0:
                    lower = q1 - 1.5 * iqr
                    upper = q3 + 1.5 * iqr
                    outlier_count = int(((numeric < lower) | (numeric > upper)).sum())
                    if outlier_count:
                        issue_list.append(f"{outlier_count} possible outliers")

        issue_rows.append(
            {
                "column": column,
                "dtype": str(series.dtype),
                "missing": missing_count,
                "unique_values": int(non_null.nunique()),
                "issues_found": ", ".join(issue_list) if issue_list else "No obvious issues",
            }
        )

    return pd.DataFrame(issue_rows)


def auto_clean_dataframe(df: pd.DataFrame) -> tuple[pd.DataFrame, list[str]]:
    cleaned = normalize_missing_values(df)
    actions = []

    before_rows = len(cleaned)
    cleaned = cleaned.dropna(how="all").drop_duplicates().copy()
    removed_rows = before_rows - len(cleaned)
    if removed_rows:
        actions.append(f"Removed {removed_rows} empty/duplicate rows.")

    for column in cleaned.columns:
        series = cleaned[column]
        non_null = series.dropna()

        if pd.api.types.is_object_dtype(series) or pd.api.types.is_string_dtype(series):
            as_text = non_null.astype(str)
            numeric_ratio = pd.to_numeric(as_text, errors="coerce").notna().mean() if len(as_text) else 0
            date_ratio = pd.to_datetime(as_text, errors="coerce").notna().mean() if len(as_text) else 0

            if numeric_ratio > 0.8:
                cleaned[column] = pd.to_numeric(cleaned[column], errors="coerce")
                actions.append(f"Converted `{column}` to numeric.")
                continue

            if date_ratio > 0.8:
                cleaned[column] = pd.to_datetime(cleaned[column], errors="coerce")
                actions.append(f"Converted `{column}` to datetime.")
                continue

            unique_count = int(as_text.nunique())
            if 0 < unique_count <= 20:
                lowered = {value.lower() for value in as_text.unique()}
                if len(lowered) != unique_count:
                    mapping = {}
                    for value in as_text.unique():
                        words = str(value).lower().split()
                        mapping[value] = " ".join(word.capitalize() for word in words)
                    cleaned[column] = cleaned[column].replace(mapping)
                    actions.append(f"Standardized text formatting in `{column}`.")

    return cleaned, actions


def to_excel_bytes(df: pd.DataFrame) -> BytesIO:
    output = BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="CleanedData")
    output.seek(0)
    return output


st.title("Analyst Workbench")
st.caption("Preview files, detect messy data, auto-clean them, build pivot tables, and create charts.")

uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx", "xls"])

if uploaded_file:
    raw_df = load_file(uploaded_file)

    if "working_df" not in st.session_state or st.session_state.get("source_name") != uploaded_file.name:
        st.session_state.source_name = uploaded_file.name
        st.session_state.raw_df = raw_df.copy()
        st.session_state.working_df = raw_df.copy()

    working_df = st.session_state.working_df

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Rows", len(working_df))
    col2.metric("Columns", len(working_df.columns))
    col3.metric("Blank Cells", int(working_df.isna().sum().sum()))
    col4.metric("Duplicate Rows", int(working_df.duplicated().sum()))

    preview_tab, issues_tab, clean_tab, pivot_tab, charts_tab, export_tab = st.tabs(
        ["Preview", "Issues", "Clean", "Pivot", "Charts", "Export"]
    )

    with preview_tab:
        st.subheader("Data Preview")
        edited_df = st.data_editor(working_df, use_container_width=True, num_rows="dynamic")
        st.session_state.working_df = edited_df
        working_df = edited_df

    with issues_tab:
        st.subheader("Detected Issues")
        issues_df = detect_column_issues(working_df)
        st.dataframe(issues_df, use_container_width=True, hide_index=True)

        normalized_df = normalize_missing_values(working_df)
        empty_rows = normalized_df[normalized_df.isna().all(axis=1)]
        if not empty_rows.empty:
            st.write("Fully blank rows")
            st.dataframe(empty_rows, use_container_width=True)

        duplicate_rows = working_df[working_df.duplicated(keep=False)]
        if not duplicate_rows.empty:
            st.write("Duplicate rows")
            st.dataframe(duplicate_rows, use_container_width=True)

    with clean_tab:
        st.subheader("One-Click Cleaning")
        st.write(
            "This applies practical cleaning rules: trims text, converts common missing markers, drops empty/duplicate rows, "
            "and tries to convert text columns into numeric or date columns when they clearly look that way."
        )

        left, right = st.columns([1, 1])
        if left.button("Auto Clean Data", use_container_width=True):
            cleaned_df, actions = auto_clean_dataframe(working_df)
            st.session_state.working_df = cleaned_df
            working_df = cleaned_df
            st.success("Cleaning applied.")
            if actions:
                for action in actions:
                    st.write(f"- {action}")
            else:
                st.write("No major issues were changed.")

        if right.button("Reset to Original File", use_container_width=True):
            st.session_state.working_df = st.session_state.raw_df.copy()
            st.info("Reset back to the original uploaded file.")

        st.write("Current working data")
        st.dataframe(working_df.head(20), use_container_width=True)

    with pivot_tab:
        st.subheader("Pivot Table Builder")
        columns = working_df.columns.tolist()
        numeric_columns = working_df.select_dtypes(include="number").columns.tolist()

        index_col = st.selectbox("Group rows by", columns, key="pivot_index")
        agg_options = ["count", "nunique"] if not numeric_columns else ["sum", "mean", "count", "min", "max", "nunique"]
        value_options = numeric_columns if numeric_columns else columns
        value_col = st.selectbox("Values column", value_options, key="pivot_value")
        agg_func = st.selectbox("Aggregation", agg_options, key="pivot_agg")

        if index_col and value_col:
            pivot_df = pd.pivot_table(
                working_df,
                index=index_col,
                values=value_col,
                aggfunc=agg_func,
            ).reset_index()
            st.dataframe(pivot_df, use_container_width=True, hide_index=True)

    with charts_tab:
        st.subheader("Visualization")
        columns = working_df.columns.tolist()
        numeric_columns = working_df.select_dtypes(include="number").columns.tolist()
        chart_type = st.selectbox("Chart type", ["bar", "line", "histogram", "box", "scatter", "pie"])

        if chart_type in {"bar", "line", "scatter", "pie"}:
            x_col = st.selectbox("X / Category", columns, key="chart_x")
            y_choices = numeric_columns if numeric_columns else columns
            y_col = st.selectbox("Y / Value", y_choices, key="chart_y")

            chart_df = working_df.copy()
            if chart_type == "bar":
                if y_col in numeric_columns:
                    bar_df = chart_df.groupby(x_col, dropna=False)[y_col].sum().reset_index()
                    fig = px.bar(bar_df, x=x_col, y=y_col)
                else:
                    bar_df = chart_df[x_col].value_counts(dropna=False).reset_index()
                    bar_df.columns = [x_col, "count"]
                    fig = px.bar(bar_df, x=x_col, y="count")
            elif chart_type == "line":
                if y_col in numeric_columns:
                    line_df = chart_df.groupby(x_col, dropna=False)[y_col].sum().reset_index()
                    fig = px.line(line_df, x=x_col, y=y_col)
                else:
                    line_df = chart_df[x_col].value_counts(dropna=False).reset_index()
                    line_df.columns = [x_col, "count"]
                    fig = px.line(line_df, x=x_col, y="count")
            elif chart_type == "scatter":
                if y_col in numeric_columns:
                    fig = px.scatter(chart_df, x=x_col, y=y_col)
                else:
                    scatter_df = chart_df[x_col].value_counts(dropna=False).reset_index()
                    scatter_df.columns = [x_col, "count"]
                    fig = px.scatter(scatter_df, x=x_col, y="count")
            else:
                if y_col in numeric_columns:
                    pie_df = chart_df.groupby(x_col, dropna=False)[y_col].sum().reset_index()
                    fig = px.pie(pie_df, names=x_col, values=y_col)
                else:
                    pie_df = chart_df[x_col].value_counts(dropna=False).reset_index()
                    pie_df.columns = [x_col, "count"]
                    fig = px.pie(pie_df, names=x_col, values="count")
            st.plotly_chart(fig, use_container_width=True)
        else:
            target_col = st.selectbox("Target column", numeric_columns if numeric_columns else columns, key="chart_target")
            if chart_type == "histogram":
                fig = px.histogram(working_df, x=target_col)
            else:
                fig = px.box(working_df, y=target_col)
            st.plotly_chart(fig, use_container_width=True)

    with export_tab:
        st.subheader("Export")
        csv_bytes = working_df.to_csv(index=False).encode("utf-8")
        excel_bytes = to_excel_bytes(working_df)

        st.download_button(
            "Download as CSV",
            data=csv_bytes,
            file_name="cleaned_data.csv",
            mime="text/csv",
            use_container_width=True,
        )
        st.download_button(
            "Download as Excel",
            data=excel_bytes,
            file_name="cleaned_data.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True,
        )
else:
    st.info("Upload a CSV or Excel file to start exploring and cleaning your data.")
