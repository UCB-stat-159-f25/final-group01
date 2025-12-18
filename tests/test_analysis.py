import pandas as pd
import numpy as np
from utils.analysis import calculate_rolling_stats

def test_calculate_rolling_stats_values():
    """Test if rolling mean and std are calculated correctly."""
    
    # Create simple data: 0, 1, 2, 3, 4
    data = pd.Series([0, 1, 2, 3, 4])
    window = 3
    
    # Call function
    result = calculate_rolling_stats(data, window=window)
    
    # Expected logic:
    # Index 0, 1 should be NaN (window size not met)
    # Index 2 should be mean(0, 1, 2) = 1.0
    # Index 3 should be mean(1, 2, 3) = 2.0
    
    assert pd.isna(result[f'Rolling_Mean_{window}'].iloc[0])
    assert pd.isna(result[f'Rolling_Mean_{window}'].iloc[1])
    assert result[f'Rolling_Mean_{window}'].iloc[2] == 1.0
    assert result[f'Rolling_Mean_{window}'].iloc[3] == 2.0

def test_calculate_rolling_stats_columns():
    """Test if the output DataFrame has the correct column names."""
    data = pd.Series([1, 2, 3, 4, 5])
    window = 5
    
    result = calculate_rolling_stats(data, window=window)
    
    expected_cols = ["Original", f"Rolling_Mean_{window}", f"Rolling_Std_{window}"]
    assert list(result.columns) == expected_cols
