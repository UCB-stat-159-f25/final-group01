[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/sSkqmNLf)

.
├── Makefile             # Updated to point to new paths
├── README.md            # Top-level overview
├── environment.yml      # Conda environment file
├── myst.yml             # Jupyter Book/Sphinx config
├── data/                # (Keep as is)
│   ├── preprocessed/    # Raw/Immutable data
│   └── processed/       # Cleaned data
├── docs/                # Move text-heavy documentation here
│   ├── ai-documentation.txt
│   ├── contribution_statement.md
│   └── project-description.md
├── notebooks/           # Move Jupyter notebooks here
│   └── Q2.ipynb
├── src/                 # Source code for use in this project
│   ├── __init__.py      # Makes this a Python package
│   ├── clean_data.py    # (Renamed from cleanData.py)
│   └── utils/           # Helper functions
│       ├── __init__.py
│       └── file_utils.py
└── tests/               # Unit tests
    └── test_data.py     # (Renamed from utils/testdata.py)
