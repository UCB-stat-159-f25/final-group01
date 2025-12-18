import pandas as pd
import os

def process_price_index(input_file, output_file, item_col_name, base_dir):
    """
    Generic function to process a price index CSV (CPI or PPI).
    
    Parameters:
    - input_file: Name of the raw CSV file (e.g., 'historicalcpi.csv')
    - output_file: Name for the saved CSV file (e.g., 'processed_cpi.csv')
    - item_col_name: The specific column to clean and pivot on 
                     (e.g., 'Consumer Price Index item')
    - base_dir: The root directory containing 'preprocessed' and 'processed' folders
    """
    
    # Construct input path
    input_path = os.path.join(base_dir, 'preprocessed', input_file)
    
    # 1. Read Data
    df = pd.read_csv(input_path)
    
    # 2. Clean the specific item column passed in the arguments
    # We use regex=False for performance and to avoid warnings
    df[item_col_name] = (
        df[item_col_name]
        .str.replace('-', "_", regex=False)
        .str.replace(' ', "_", regex=False)
        .str.replace(',', "", regex=False)
    )
    
    # 3. Pivot
    processed_df = df.pivot(
        index='Year', 
        columns=item_col_name, 
        values='Percent change'
    )
    
    # 4. Save Data
    # Ensure output directory exists
    output_dir = os.path.join(base_dir, 'processed')
    os.makedirs(output_dir, exist_ok=True)
    
    output_path = os.path.join(output_dir, output_file)
    processed_df.to_csv(output_path)
    
    print(f"Successfully processed {input_file} -> {output_path}")
    
    return processed_df

if __name__ == "__main__":
    base_path = '/home/jovyan/final-group01/data'
    
    cpi_df = process_price_index(
        input_file='historicalcpi.csv',
        output_file='processed_cpi.csv',
        item_col_name='Consumer Price Index item',
        base_dir=base_path
    )
    ppi_df = process_price_index(
        input_file='historicalppi.csv',
        output_file='processed_ppi.csv',
        item_col_name='Producer Price Index item',
        base_dir=base_path
    )