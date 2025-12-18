# =========================
# Configuration
# =========================

PYTHON := python
NOTEBOOKS := notebooks
DATA_PRE := data/preprocessed
DATA_PROC := data/processed
FIGURES := figures
OUTPUTS := outputs

# Processed data targets
CPI_PROC := $(DATA_PROC)/processed_cpi.csv
PPI_PROC := $(DATA_PROC)/processed_ppi.csv

# Notebooks
NB_EDA := $(NOTEBOOKS)/EDA.ipynb
NB_TRENDS := $(NOTEBOOKS)/food_price_trends_analysis.ipynb
NB_HEALTH := $(NOTEBOOKS)/healthy_vs_unhealthy_inflation.ipynb
NB_ECON := $(NOTEBOOKS)/food_inflation_across_major_economic_periods.ipynb

# =========================
# Default target
# =========================

.PHONY: all
all: data figures site

# =========================
# Data processing
# =========================

$(CPI_PROC) $(PPI_PROC): utils/clean_data.py $(DATA_PRE)/historicalcpi.csv $(DATA_PRE)/historicalppi.csv
	$(PYTHON) utils/clean_data.py

.PHONY: data
data: $(CPI_PROC) $(PPI_PROC)

# =========================
# Notebook execution
# =========================

.PHONY: figures
figures: data
	jupyter nbconvert --to notebook --execute $(NB_EDA) --output EDA.ipynb
	jupyter nbconvert --to notebook --execute $(NB_TRENDS) --output food_price_trends_analysis.ipynb
	jupyter nbconvert --to notebook --execute $(NB_HEALTH) --output healthy_vs_unhealthy_inflation.ipynb
	jupyter nbconvert --to notebook --execute $(NB_ECON) --output food_inflation_across_major_economic_periods.ipynb

# =========================
# Testing
# =========================

.PHONY: test
test:
	pytest utils/tests

# =========================
# MyST site
# =========================

.PHONY: site
site:
	myst build

# =========================
# Reproducibility helpers
# =========================

.PHONY: env
env:
	conda env create -f environment.yml

# =========================
# Cleanup
# =========================

.PHONY: clean
clean:
	rm -f $(DATA_PROC)/*.csv
	rm -rf $(DATA_PROC)/eda_summary
	rm -rf $(DATA_PROC)/food_price_trend_summary
	rm -f $(FIGURES)/*.png
	rm -rf _build
