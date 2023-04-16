from datetime import datetime
import numpy as np
import pandas as pd
from pandas.tseries.offsets import MonthEnd

def format_number(num):
    # Define the suffixes and their values
    suffixes = {
        1000: 'k',
        1000000: 'M',
        1000000000: 'B',
        1000000000000: 'T'
    }
    
    # Loop through the suffixes and find the largest one that's smaller than the number
    for suffix, label in reversed(sorted(suffixes.items())):
        if num >= suffix:
            # Divide the number by the suffix and round to one decimal place
            value = round(num / suffix, 1)
            # Return the value with the suffix
            return f"{value}{label}"
    
    # If the number is smaller than 1000, return it as a string with no suffix
    return str(num)

def last_day(x: datetime):
    """
    input: datetime or series datetime
    return: same as input data type with last day of the month
    """
    return x + MonthEnd(0)


def convert_float(x :str, verbose=True):
    if type(x) is pd.Series:
        return x.str.strip().replace({',': '', "": np.nan}, regex=True).astype(float)
    else:
        try:
            x = float(str(x).strip().replace(","))
            return x
        except:
            if verbose:
                print(f"Please check: {x}")
            return np.nan
        
def explore_df(df: pd.DataFrame, top_n=5):
    cols = df.columns
    for c in cols:
        print("*" * 80)
        print(df[c].value_counts().head(top_n))