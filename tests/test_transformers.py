import pandas as pd
from utils.transformers import reshape_to_long_format

def test_reshape_to_long_format():
    """Test if wide data is correctly melted to long format."""
    
    # Create a 'wide' dataframe
    df_wide = pd.DataFrame({
        'Year': [2020],
        'Apples': [1.5],
        'Bananas': [2.0]
    })
    
    # Call function
    df_long = reshape_to_long_format(
        df_wide,
        id_vars=['Year'],
        var_name='Food_Type',
        value_name='Price Change')
    
    # Check dimensions: Should be 2 rows (Apples, Bananas) and 3 columns
    assert df_long.shape == (2, 3)
    
    # Check columns
    assert 'Food_Type' in df_long.columns
    assert 'Price Change' in df_long.columns
    
    # Check content
    apple_row = df_long[df_long['Food_Type'] == 'Apples']
    assert apple_row['Price Change'].values[0] == 1.5
