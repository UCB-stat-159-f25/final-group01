import pandas as pd
from typing import List

def reshape_to_long_format(
    df: pd.DataFrame,
    id_vars: List[str]|str = ['Year'],
    var_name: str = 'category',
    value_name: str = 'pct_change'
) -> pd.DataFrame:
    """
    Converts a wide-format dataframe (years as rows, categories as columns)
    into a long-format dataframe suitable for seaborn/plotting.
    """
    return df.melt(id_vars=id_vars, var_name=var_name, value_name=value_name)
