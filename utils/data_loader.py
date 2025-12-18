import pandas as pd
import os

def load_inflation_data(base_path="../data/processed/"):
    """
    Loads the processed CPI and PPI datasets.
    
    Args:
        base_path (str): The directory containing the processed CSV files.
        
    Returns:
        tuple: (cpi_df, ppi_df)
    """
    cpi_path = os.path.join(base_path, "processed_cpi.csv")
    ppi_path = os.path.join(base_path, "processed_ppi.csv")
    
    if not os.path.exists(cpi_path) or not os.path.exists(ppi_path):
        raise FileNotFoundError(f"Data files not found in {base_path}")

    cpi = pd.read_csv(cpi_path)
    ppi = pd.read_csv(ppi_path)
    
    return cpi, ppi
