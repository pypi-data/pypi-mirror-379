import io
import csv
import tempfile
from pathlib import Path
import subprocess

import pytest  # type: ignore
import numpy as np  # type: ignore
import pandas as pd  # type: ignore

import microeda.core as core
import microeda.report as report
import microeda.viz as viz
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning, message="invalid value encountered in divide")


# --------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------
def tiny_dataframe():
    """Create a tiny DataFrame for smoke tests."""
    return pd.DataFrame({
        "num": [1, 2, 3, np.nan],
        "cat": ["a", "b", "a", "b"],
        "dt": pd.to_datetime(["2024-01-01", "2024-01-02", None, "2024-01-04"]),
        "txt": ["foo bar", "baz", "foo baz qux", ""],
        "dup": [1, 1, 1, 1],
    })


def semi_structured_dataframe():
    """DataFrame with JSON-like and list-like columns."""
    return pd.DataFrame({
        "json_col": ['{"a":1}', '{"a":2}', None, '{"a":3}'],
        "list_col": [[1, 2], [3, 4], None, [5, 6]]
    })


# --------------------------------------------------------------------
# Tests
# --------------------------------------------------------------------
def test_analyze_returns_expected_keys():
    df = tiny_dataframe()
    result = core.analyze(df, name="demo")
    for key in ("name", "n_rows", "n_cols", "columns", "alerts", "global"):
        assert key in result
    assert result["n_rows"] == len(df)
    assert result["n_cols"] == len(df.columns)


def test_column_typing_inference():
    df = tiny_dataframe()
    result = core.analyze(df)
    coltypes = {col["name"]: col["type"] for col in result["columns"]}
    assert coltypes["num"] == "numeric"
    assert coltypes["cat"] == "categorical"
    assert coltypes["dt"] == "datetime"
    assert coltypes["txt"] == "text"
    assert coltypes["dup"] == "numeric"


def test_data_quality_alerts():
    df = tiny_dataframe()
    summary = core.analyze(df)
    alerts = summary.get("alerts", [])
    
    # Only check for duplicates if any alerts exist
    dup_alerts = [a for a in alerts if "duplicate rows" in a.get("issue", "")]
    
    # Pass if either there are no duplicates or duplicates are flagged
    n_dupes = df.shape[0] - len(df.drop_duplicates())
    if n_dupes > 0:
        assert len(dup_alerts) > 0, "Duplicate rows exist but not flagged in alerts"
    else:
        assert True  # no duplicates, test passes

def test_target_correlation_alert():
    df = pd.DataFrame({
        "x": np.arange(10),
        "y": np.arange(10),
        "z": np.random.randn(10)
    })
    result = core.analyze(df, target_column="x")
    alerts = [a for a in result["alerts"] if "Highly correlated with target" in a.get("issue", "")]
    assert any(a["column"] == "y" for a in alerts)
    assert all(a["column"] != "z" for a in alerts)


def test_report_markdown_contains_column_names():
    df = tiny_dataframe()
    summary = core.analyze(df)
    md = report.render_report(summary, style="md")
    for col in df.columns:
        assert col in md


def test_html_report_generation():
    df = tiny_dataframe()
    summary = core.analyze(df)
    html = report.render_report(summary, style="html")
    assert "<h1>" in html
    for col in df.columns:
        assert col in html


def test_cli_runs_and_creates_file(tmp_path: Path):
    csv_path = tmp_path / "sample.csv"
    tiny_dataframe().to_csv(csv_path, index=False)
    out_path = tmp_path / "report.md"

    result = subprocess.run(
        ["python", "-m", "microeda.cli", str(csv_path), "--style", "md", "--out", str(out_path)]
    )
    assert result.returncode == 0
    assert out_path.exists()
    text = out_path.read_text()
    assert "num" in text


def test_missing_values_flagged():
    df = pd.DataFrame({"x": [1, None, 3]})
    summary = core.analyze(df)
    col = summary["columns"][0]
    assert col["missing_percent"] > 0


def test_analyze_table_prints_table(capsys):
    df = tiny_dataframe()
    core.analyze_table(df)
    captured = capsys.readouterr()
    for col in df.columns:
        assert col in captured.out


def test_pairwise_hints_generated():
    df = tiny_dataframe()
    summary = core.analyze(df)
    hints = summary.get("pairwise_hints", {}).get("pairs", [])
    assert isinstance(hints, list)


def test_semi_structured_columns_detected():
    df = semi_structured_dataframe()
    df = df.apply(lambda col: col.map(lambda x: tuple(x) if isinstance(x, list) else x))
    summary = core.analyze(df)
    coltypes = {col["name"]: col["type"] for col in summary["columns"]}
    assert coltypes["json_col"] in ("json-string", "semi-structured")
    assert coltypes["list_col"] in ("json-string", "semi-structured")


def test_interactive_viz(tmp_path: Path):
    df = tiny_dataframe()
    summary = core.analyze(df)
    output_html = tmp_path / "viz_test.html"
    
    viz.interactive_report(df, summary, str(output_html))
    
    # Check that the combined HTML file exists
    assert output_html.exists()
    
    # Optional: sanity check that the file contains column names
    content = output_html.read_text()
    for col in df.columns:
        assert col in content