import pandas as pd

def calculate_rolling_stats(series, window=5):
    """
    Calculates rolling mean and standard deviation.
    
    Args:
        series (pd.Series): The time series data.
        window (int): The rolling window size (default 5 years).
        
    Returns:
        pd.DataFrame: DataFrame containing original values, rolling mean, and rolling std.
    """
    rolling_mean = series.rolling(window=window).mean()
    rolling_std = series.rolling(window=window).std()
    
    return pd.DataFrame({
        "Original": series,
        f"Rolling_Mean_{window}": rolling_mean,
        f"Rolling_Std_{window}": rolling_std
        })
