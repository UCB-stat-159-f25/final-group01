import unittest
import pandas as pd
import os
import shutil
import tempfile

# --- ASSUMING THE FUNCTION IS IMPORTED ---
# In a real scenario, you would do: from your_script import process_price_index
# For this script to be runnable standalone, I am pasting the function here:

def process_price_index(input_file, output_file, item_col_name, base_dir):
    input_path = os.path.join(base_dir, 'preprocessed', input_file)
    df = pd.read_csv(input_path)
    
    df[item_col_name] = (
        df[item_col_name]
        .str.replace('-', "_", regex=False)
        .str.replace(' ', "_", regex=False)
        .str.replace(',', "", regex=False)
    )
    
    processed_df = df.pivot(
        index='Year', 
        columns=item_col_name, 
        values='Percent change'
    )
    
    output_dir = os.path.join(base_dir, 'processed')
    os.makedirs(output_dir, exist_ok=True)
    
    output_path = os.path.join(output_dir, output_file)
    processed_df.to_csv(output_path)
    return processed_df

# --- THE TEST SUITE ---

class TestPriceIndexProcessor(unittest.TestCase):

    def setUp(self):
        """
        Runs BEFORE every test. 
        Creates a temporary directory and a dummy CSV file.
        """
        # 1. Create a temporary directory structure
        self.test_dir = tempfile.mkdtemp()
        self.preprocessed_dir = os.path.join(self.test_dir, 'preprocessed')
        os.makedirs(self.preprocessed_dir)
        
        # 2. Create Dummy Data
        # We purposely use spaces, commas, and dashes to test the cleaning logic
        data = {
            'Year': [2020, 2020, 2021, 2021],
            'Consumer Price Index item': ['Apples, Red', 'Bananas-Yellow', 'Apples, Red', 'Bananas-Yellow'],
            'Percent change': [1.5, 2.0, 1.8, 2.2]
        }
        self.df = pd.DataFrame(data)
        
        # 3. Save dummy data to csv
        self.input_filename = 'test_cpi.csv'
        self.df.to_csv(os.path.join(self.preprocessed_dir, self.input_filename), index=False)

    def tearDown(self):
        """
        Runs AFTER every test.
        Deletes the temporary directory and all files in it.
        """
        shutil.rmtree(self.test_dir)

    def test_process_price_index_cleaning_and_pivoting(self):
        """
        Tests if the function correctly cleans strings and pivots the table.
        """
        output_filename = 'processed_test_cpi.csv'
        item_col = 'Consumer Price Index item'

        # 1. Run the function
        result_df = process_price_index(
            input_file=self.input_filename,
            output_file=output_filename,
            item_col_name=item_col,
            base_dir=self.test_dir
        )

        # 2. Check if output file was actually created
        expected_output_path = os.path.join(self.test_dir, 'processed', output_filename)
        self.assertTrue(os.path.exists(expected_output_path), "Output file was not created.")

        # 3. Verify Column Cleaning
        # 'Apples, Red' should become 'Apples_Red'
        # 'Bananas-Yellow' should become 'Bananas_Yellow'
        expected_columns = ['Apples_Red', 'Bananas_Yellow']
        for col in expected_columns:
            self.assertIn(col, result_df.columns, f"Column {col} missing. Cleaning logic failed.")

        # 4. Verify Data Values (Pivoting)
        # Check value for Apples_Red in 2020 (should be 1.5)
        self.assertEqual(result_df.loc[2020, 'Apples_Red'], 1.5)
        # Check value for Bananas_Yellow in 2021 (should be 2.2)
        self.assertEqual(result_df.loc[2021, 'Bananas_Yellow'], 2.2)

if __name__ == '__main__':
    unittest.main()