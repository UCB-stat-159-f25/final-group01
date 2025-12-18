[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/sSkqmNLf)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCB-stat-159-f25/final-group01/HEAD)


# Food Inflation Analysis Project

This project analyzes **food price inflation across major economic periods**, comparing trends in **healthy vs. unhealthy food categories**. The project uses statistical analysis, visualization, and reproducible workflows to provide insights into food price dynamics over time.

All work is performed in **fully reproducible Jupyter Notebook environments**, as specified in `environment.yml`.

You can launch the notebooks directly in your browser using **Binder** by clicking the badge above. Binder will automatically set up JupyterLab and install all required dependencies.

---

## Getting Started

### Prerequisites

Ensure you have [Conda](https://docs.conda.io/en/latest/) installed.

### Environment Setup

Create and activate the conda environment:

```bash
conda env create -f environment.yml
conda activate food_inflation
```

### Running notebooks

All notebooks are in the notebooks/ directory. Open and run them using Jupyter Notebook or Jupyter Lab:

```bash
jupyter notebook
# or
jupyter lab
```

When running locally, ensure the `food_inflation` kernel is selected by running the following:

```bash
python -m ipykernel install --user --name=food_inflation --display-name="Python (food_inflation)"
```

### Building the Documentation

This project uses MyST and a Makefile to generate a static site in _build/. To build:

```bash
make html
```
The documentation site will be available in _build/html/.

#### MyST Webpage:

https://ucb-stat-159-f25.github.io/final-group01/

## Repository Structure

```bash
ai-documentation.txt              # Documentation related to AI/automated analysis
contribution_statement.md         # Contribution statement
environment.yml                   # Conda environment configuration
LICENSE                            # BSD 3-Clause License
Makefile                           # Build automation
myst.yml                           # MyST configuration
notebooks/                         # Jupyter notebooks for analysis
    EDA.ipynb
    food_price_trends_analysis.ipynb
    food_inflation_across_major_economic_periods.ipynb
    healthy_vs_unhealthy_inflation.ipynb
data/                               # Raw and processed data
    preprocessed/
        CPIForecast.csv
        CPIHistoricalForecast.csv
        historicalcpi.csv
        historicalppi.csv
        PPIForecast.csv
        PPIHistoricalForecast.csv
    processed/
        processed_cpi.csv
        processed_ppi.csv
figures/                            # Generated plots and figures
outputs/                            # Generated outputs (tables, reports)
    eda_summary/
    food_price_trend_summary/
utils/                              # Utility scripts for data processing or visualization
    clean_data.py
    tests/
_build/                             # Built documentation/site
README.md                           # This file
project-description.md              # Project overview and objectives
```

## Notebooks Overview

| Notebook                                             | Description                                                   |
| ---------------------------------------------------- | ------------------------------------------------------------- |
| `EDA.ipynb`                                          | Exploratory data analysis of CPI and PPI by food category     |
| `food_price_trends_analysis.ipynb`                   | Analysis of food price trends across time and categories      |
| `food_inflation_across_major_economic_periods.ipynb` | Comparing inflation patterns across major economic periods    |
| `healthy_vs_unhealthy_inflation.ipynb`               | Analysis comparing healthy vs unhealthy food inflation trends |

All notebooks automatically save key outputs (tables, plots) in the `outputs/` and `figures/` directories for reproducibility.

## Key Outputs & Figures

- Rolling volatility of food inflation by category (`5y_rolling_volatility_food_inflation_by_category.png`)

- Healthy vs unhealthy inflation comparison (`healthy_vs_unhealthy_inflation_boxplot.png`)

- Annual CPI and PPI changes by category (`cpi_annual_change_by_category.png`, `ppi_annual_change_by_category.png`)

- Change point detection and broken-stick regression analyses

- Additional summary figures and tables saved in `figures/` and `outputs/`

## Notes

All notebooks are fully reproducible.

The environment is specified in `environment.yml`; running `conda env create -f environment.yml` ensures reproducibility.

Data files in `data/` include both raw/preprocessed and processed summaries.

Utility functions in `utils/` assist with data cleaning and processing.

## License

This project is licensed under the [BSD 3-Clause License](LICENSE).