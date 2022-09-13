import pandas as pd
import numpy as np
from datetime import datetime


expected_input = [{
    'gclid': 'PAAab8L77tPGqrIXMaKHBN_wUSzd7JLK9jYhkgNhNx3TvULnny_5X7gsQZpi8',
}]

expected_output = [{
    'gclid': 'PAAab8L77tPGqrIXMaKHBN_wUSzd7JLK9jYhkgNhNx3TvULnny_5X7gsQZpi8',
    'has_gclid': 1
}]



def run(df):
    """
    This function takes care of processing any datetime string incoming in the dfset
    It also creates a year-month column and a time column
    """

    df['has_gclid'] = np.where(df['gclid'].isnull(), 0, 1)
    
    return df
