from typing import Any, Dict
try:
    from rich.console import Console  # type: ignore
    from rich.table import Table  # type: ignore
    from rich.panel import Panel  # type: ignore
    RICH_AVAILABLE = True
    console = Console()
except Exception:
    RICH_AVAILABLE = False
    console = None


def _format_sample_stats(desc: Dict[str, Any]) -> str:
    t = desc.get("type", "")
    if t == "numeric":
        return f"mean={desc.get('mean', None):.3g}, median={desc.get('50%', None):.3g}"
    elif t == "categorical":
        tops = desc.get("top_values", {})
        return ", ".join([f"{k}:{v}" for k, v in list(tops.items())[:3]])
    elif t == "text":
        return f"avg_tokens={desc.get('avg_tokens',0):.2f}"
    elif t in ("boolean", "datetime", "semi-structured", "json-string"):
        return str(desc.get("n_unique", 0)) + " unique"
    else:
        return ""


def _print_table_from_summaries(summaries: Dict[str, Any]):
    if RICH_AVAILABLE:
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Column")
        table.add_column("Type")
        table.add_column("Missing %", justify="right")
        table.add_column("Unique", justify="right")
        table.add_column("Sample stats", justify="left")
        for col, desc in summaries.items():
            t = desc.get("type", "")
            miss = f"{desc.get('pct_missing', 0):.2f}"
            uniq = str(desc.get("n_unique", 0))
            sample = _format_sample_stats(desc)
            table.add_row(col, t, miss, uniq, sample)
        console.print(table)
    else:
        print(f"{'Column':30} {'Type':10} {'Missing%':8} {'Unique':8} {'Sample'}")
        for col, desc in summaries.items():
            t = desc.get("type", "")
            miss = f"{desc.get('pct_missing', 0):.2f}"
            uniq = str(desc.get("n_unique", 0))
            sample = _format_sample_stats(desc)
            print(f"{col:30.30} {t:10} {miss:8} {uniq:8} {sample}")


def render_report(res: Dict[str, Any], style: str = 'terminal') -> str:
    """
    Render report.
    style: 'terminal' -> prints, 'md' -> markdown string, 'html' -> HTML string
    """
    if style == 'terminal':
        header = f"MicroEDA Report: {res.get('name','dataset')} — {res.get('n_rows')} rows x {res.get('n_cols')} cols"
        if RICH_AVAILABLE:
            console.print(Panel(header, style="bold green"))
        else:
            print(header)
        _print_table_from_summaries(res['summaries'])

        # missingness
        if RICH_AVAILABLE:
            console.print(Panel("Top missingness correlations (phi)", style="yellow"))
            for a, b, s in res['missingness']['top_missing_correlations'][:10]:
                console.print(f"{a} <-> {b} : {s}")
            console.print(Panel("Top pairwise hints", style="yellow"))
            for (a, b, m, s) in res['pairwise_hints']['pairs'][:20]:
                console.print(f"{a} <-> {b} ({m}) = {s}")
        else:
            print("Top missingness correlations (phi):")
            for a, b, s in res['missingness']['top_missing_correlations'][:10]:
                print(f"{a} <-> {b} : {s}")
            print("\nTop pairwise hints:")
            for (a, b, m, s) in res['pairwise_hints']['pairs'][:20]:
                print(f"{a} <-> {b} ({m}) = {s}")
        return ""

    elif style == 'md':
        lines = []
        lines.append(f"# MicroEDA Report — {res.get('name','dataset')}")
        lines.append(f"**Rows:** {res.get('n_rows')}  **Cols:** {res.get('n_cols')}\n")
        lines.append("## Column summaries\n")
        lines.append("|Column|Type|Missing%|Unique|Sample stats|")
        lines.append("|---|---|---:|---:|---|")
        for col, desc in res['summaries'].items():
            t = desc.get("type", "")
            miss = f"{desc.get('pct_missing', 0):.2f}"
            uniq = str(desc.get("n_unique", 0))
            sample = _format_sample_stats(desc)
            lines.append(f"|{col}|{t}|{miss}|{uniq}|{sample}|")
        lines.append("\n## Top missingness correlations (phi)")
        for a, b, s in res['missingness']['top_missing_correlations'][:20]:
            lines.append(f"- {a} <-> {b} : {s}")
        lines.append("\n## Top pairwise hints")
        for (a, b, m, s) in res['pairwise_hints']['pairs'][:50]:
            lines.append(f"- {a} <-> {b} ({m}) = {s}")
        return "\n".join(lines)

    elif style == 'html':
        md = render_report(res, style='md')
        try:
            import markdown  # type: ignore
            return markdown.markdown(md)
        except Exception:
            return '<html><body>' + md.replace('\n', '<br/>') + '</body></html>'

    else:
        raise ValueError('style must be terminal, md, or html')