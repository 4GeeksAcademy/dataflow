import pandas as pd
import numpy as np
from datetime import datetime

from utils import build_features as features

expected_input = [{
    'first_name': 'Maria',
    'last_name': 'Smith'
}]

expected_output = [{
    'fullname': 'Maria Smith'
}]



def run(df):
    """
    This function creates a fullname column by combining first and last name into one cell.
    Then it inserts it in the right place (4th column).
    """

    #Combine first and last name ignoring nulls
    features.combine_columns(df, 'first_name', 'last_name', 'fullname')

    # shift column 'Fullname' to third position
    fourth_column = df.pop('fullname')
    df.insert(3, 'fullname', fourth_column)

    return df
