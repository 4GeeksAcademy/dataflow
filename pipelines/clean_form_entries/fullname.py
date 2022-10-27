import pandas as pd
import numpy as np
from datetime import datetime


expected_input = [{
    'first_name': 'Maria',
    'last_name': 'Smith'
}]

expected_output = [{
    'first_name': 'Maria',
    'last_name': 'Smith',
    'fullname': 'Maria Smith'
}]



def run(df):
    """
    This function creates a fullname column by combining first and last name into one cell.
    Then it inserts it in the right place (4th column).
    """

    #Combine first and last name ignoring nulls
    df['fullname'] = df['first_name'].fillna('') + str(' ') + df['last_name'].fillna('')

    # shift column 'Fullname' to third position
    fourth_column = df.pop('fullname')
    df.insert(2, 'fullname', fourth_column)

    return df
