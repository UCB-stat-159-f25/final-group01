import pytest
import pandas as pd
from unittest.mock import patch, MagicMock
from utils.data_loader import load_inflation_data

# Create dummy data for testing
mock_cpi_data = pd.DataFrame({'Year': [2020, 2021], 'CPI': [100, 105]})
mock_ppi_data = pd.DataFrame({'Year': [2020, 2021], 'PPI': [100, 108]})

@patch('pandas.read_csv')
@patch('os.path.exists')
def test_load_inflation_data_success(mock_exists, mock_read_csv):
    """Test that data loads correctly when files exist."""
    
    # Setup mocks
    mock_exists.return_value = True
    mock_read_csv.side_effect = [mock_cpi_data, mock_ppi_data]

    # Call function
    cpi, ppi = load_inflation_data("dummy/path")

    # Assertions
    assert cpi.equals(mock_cpi_data)
    assert ppi.equals(mock_ppi_data)
    assert mock_exists.call_count == 2 # Should check for both files

@patch('os.path.exists')
def test_load_inflation_data_file_not_found(mock_exists):
    """Test that the function raises an error if files are missing."""
    
    # Simulate file not found
    mock_exists.return_value = False

    # Assert that FileNotFoundError is raised
    with pytest.raises(FileNotFoundError):
        load_inflation_data("dummy/path")
