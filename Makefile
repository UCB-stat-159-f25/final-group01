# =========================
# Configuration
# =========================

PYTHON := python
NOTEBOOKS := notebooks
DATA_PRE := data/preprocessed
DATA_PROC := data/processed
FIGURES := figures
OUTPUTS := outputs
PDF_BUILDS := pdf_builds

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
	python -m ipykernel install --user --name=food_inflation --display-name "Python (food_inflation)"
	jupyter nbconvert --to notebook --execute $(NB_EDA) --output EDA.ipynb --ExecutePreprocessor.kernel_name=food_inflation
	jupyter nbconvert --to notebook --execute $(NB_TRENDS) --output food_price_trends_analysis.ipynb --ExecutePreprocessor.kernel_name=food_inflation
	jupyter nbconvert --to notebook --execute $(NB_HEALTH) --output healthy_vs_unhealthy_inflation.ipynb --ExecutePreprocessor.kernel_name=food_inflation
	jupyter nbconvert --to notebook --execute $(NB_ECON) --output food_inflation_across_major_economic_periods.ipynb --ExecutePreprocessor.kernel_name=food_inflation

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
	@echo "Setting up conda environment..."
	conda env update -f environment.yml --prune || conda env create -f environment.yml

# =========================
# Build MyST HTML site
# =========================

.PHONY: html
html:
	@echo "Caveat: this build can only be viewed locally."
	myst build --html

.PHONY: pdf
pdf:
	myst build --pdf

# =========================
# Cleanup
# =========================

.PHONY: clean
clean:
	rm -f $(DATA_PROC)/*.csv
	rm -rf $(OUTPUTS)/eda_summary
	rm -rf $(OUTPUTS)/food_price_trend_summary
	rm -f $(FIGURES)/*.png
	rm -rf _build
