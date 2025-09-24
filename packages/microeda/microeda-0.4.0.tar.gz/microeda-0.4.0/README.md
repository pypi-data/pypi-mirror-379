# 🚀 microeda

[![PyPI version](https://img.shields.io/pypi/v/microeda?color=blue&label=PyPI)](https://pypi.org/project/microeda/) 
[![Python Versions](https://img.shields.io/pypi/pyversions/microeda)](https://pypi.org/project/microeda/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![GitHub Issues](https://img.shields.io/github/issues/SaptarshiMondal123/microeda)](https://github.com/SaptarshiMondal123/microeda/issues)

**microeda** is an ultra-lightweight Python library for **Exploratory Data Analysis (EDA)** on small datasets (<10k rows). Get deep insights into your data **instantly**—detect column types, summarize statistics, spot missing values & outliers, and explore relationships.

---

## ✨ Features

- **Automatic Column Typing**: `numeric`, `categorical`, `boolean`, `datetime`, `text`, `ID`.
- **Smart Summaries**:
  - **Numeric:** mean, median, quartiles, missing values, outliers
  - **Categorical:** unique counts, top values
  - **Datetime:** min, max, range, missing
  - **Text:** token counts, top words
- **Missing Data Analysis**:
  - Column-level missing percentages
  - Pairwise missing correlations
- **Outlier Detection**:
  - IQR method
  - Z-score method
- **Pairwise Relationships**:
  - Pearson for numeric
  - Mutual Information & Cramer's V for categorical
- **CLI Support**: Generate **Markdown** or **HTML** reports
- **Dependency-light**: Only `pandas` & `numpy` required, optional `rich` for pretty CLI
- **Semi-structured Data Support**: Detect columns with JSON-like or list-like structures


---

## 📦 Installation

**From PyPI:**

```bash
pip install microeda
```

Or install from source:

```bash
git clone https://github.com/SaptarshiMondal123/microeda.git
cd microeda
pip install .
```

## Usage

### Python API

```python
import pandas as pd
from microeda import analyze

df = pd.read_csv("your_data.csv")
report = analyze(df, name="My Dataset")

# Inspect your data
print(report["column_types"])
print(report["summaries"])
print(report["missingness"])
print(report["pairwise_hints"])
```

…will only give you raw dicts, no table.

If you want a readable table like the demo output, you should do:

```
from microeda import analyze_table

analyze_table(df, name="My Dataset")
```

### CLI

Generate a Markdown report directly from the terminal:

```bash
microeda path/to/data.csv --style md --out report.md
microeda path/to/data.csv --style html --out report.html
```

Options:

```bash
--style: md (Markdown) or html (HTML)

--out: output file path
```
### 🌟 Example Output
Dataset: 100 rows x 5 cols

Column Summary:
| Column | Type        | Unique | Missing | Sample Stats          |
|--------|------------|--------|---------|----------------------|
| Age    | numeric     | 30     | 0       | mean=29.8            |
| Gender | categorical | 2      | 5       | Male:55, Female:40   |
| Name   | text        | 95     | 0       | avg_tokens=2         |
| Salary | numeric     | 50     | 2       | mean=55000           |
| City   | text        | 10     | 0       | avg_tokens=1         |


## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

- Fork the repo

- Create a new branch (git checkout -b feature-name)

- Make your changes

- Run tests (pytest)

- Submit a pull request

## License

MIT License © 2025 Saptarshi Mondal

### Links

GitHub: https://github.com/SaptarshiMondal123/microeda

PyPI: https://pypi.org/project/microeda/