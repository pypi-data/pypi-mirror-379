# microeda/cli.py
import sys
import argparse
import pandas as pd  # type: ignore
import webbrowser
from .core import analyze
from .report import render_report

def main():
    p = argparse.ArgumentParser(description='MicroEDA — lightweight EDA')
    p.add_argument('input', help='CSV file or - for stdin')
    p.add_argument('--name', default=None, help='Dataset name')
    p.add_argument('--out', help='Export report to file (md|html)')
    p.add_argument('--style', default='terminal', choices=['terminal','md','html'])
    p.add_argument('--max-rows', type=int, default=10000,
                   help='If dataset large, sample first N rows')
    p.add_argument('--interactive', action='store_true', help='Generate interactive plots (requires plotly)')
    p.add_argument('--viz-out', default='viz_report', help='Output prefix for interactive HTML plots')
    args = p.parse_args()

    df = pd.read_csv(sys.stdin if args.input == '-' else args.input)
    if args.max_rows and len(df) > args.max_rows:
        df = df.head(args.max_rows)

    res = analyze(df, name=args.name)

    # Render main report
    if args.style == 'terminal':
        render_report(res, style='terminal')
    else:
        content = render_report(res, style=args.style)
        if args.out:
            with open(args.out, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Saved report to {args.out}")
        else:
            print(content)

    # Optional interactive visualizations
    if args.interactive:
        try:
            from .viz import interactive_report
            interactive_report(df, res, output_html=args.viz_out)

            # Automatically open generated HTMLs if possible
            import glob
            html_files = glob.glob(f"{args.viz_out}_*.html")
            if html_files:
                print("\nInteractive plots generated:")
                for f in html_files:
                    print(f"- {f}")
                    # Attempt to open in default browser
                    try:
                        webbrowser.open(f)
                    except Exception:
                        pass
        except ImportError:
            print("plotly not installed. Run `pip install plotly` to enable interactive plots.")

if __name__ == "__main__":
    main()