# microeda/viz.py
import pandas as pd  # type: ignore
from typing import Dict
import os

def interactive_report(df: pd.DataFrame, report: Dict, output_html: str = "viz_report.html"):
    """
    Generate interactive HTML dashboard for numeric, categorical, datetime, and text columns.
    Requires: plotly
    """
    try:
        import plotly.express as px  # type: ignore
        import plotly.graph_objects as go  # type: ignore
        from plotly.subplots import make_subplots  # type: ignore
    except ImportError:
        raise ImportError("plotly is required for interactive_report. Install via `pip install plotly`")

    # Ensure output folder exists
    folder = os.path.dirname(output_html)
    if folder:
        os.makedirs(folder, exist_ok=True)

    # Create a list to hold all figure HTMLs
    figs_html = []

    for col, ctype in report['column_types'].items():
        col_data = df[col].dropna()
        if col_data.empty:
            continue

        if ctype == "numeric":
            fig = px.histogram(df, x=col, nbins=20, title=f"{col} Distribution")
        elif ctype in ("categorical", "boolean"):
            counts = col_data.astype(str).value_counts().reset_index()
            counts.columns = [col, "count"]
            fig = px.bar(counts, x=col, y="count", title=f"{col} Counts")
        elif ctype == "datetime":
            fig = px.histogram(df, x=col, nbins=20, title=f"{col} Over Time")
        elif ctype in ("text", "semi-structured", "json-string"):
            lengths = col_data.astype(str).map(len)
            fig = px.histogram(lengths, nbins=20, title=f"{col} Text Length Distribution")
        else:
            continue

        figs_html.append(fig.to_html(full_html=False, include_plotlyjs='cdn'))

    # Combine all figures into a single HTML
    html_content = "<html><head><title>Interactive EDA Dashboard</title></head><body>"
    html_content += f"<h1>Interactive EDA Dashboard — {report.get('name','dataset')}</h1>"
    for f_html in figs_html:
        html_content += f"<div style='margin-bottom:50px;'>{f_html}</div>"
    html_content += "</body></html>"

    # Write the combined dashboard
    with open(output_html, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Interactive HTML dashboard saved as '{output_html}'")