import pandas as pd
import numpy as np
from datetime import datetime

from utils import build_features as features
from constants import TO_DROP

expected_input = [{
    'first_name': 'Maria',
    'email': 'maria@gmail.com',
    'language':'en'
}, {
    'first_name': 'Alejandra',
    'email': 'alejandra@4geeks.co',
    'language':'en'
}]

expected_output = [{
    'email': 'maria@gmail.com',
    'language':'en'
}]



def run(df):
    """
    This function drops 100% null columns, irrelevant columns and original columns used for combination.
    It also drops rows that contain 4geeks emails that were used for testing.
    """

    #drop null columns
    features.drop_null_columns(df)

    #drop irrelevant columns
    df.drop(TO_DROP, axis=1, inplace=True)

    #drop testing rows
    features.drop_test_rows(df)

    #dropping two other test rows identified
    df.drop(df[df['utm_source'] == 'test_s'].index, inplace = True)
    df.drop(df[df['utm_source'] == 'fintech'].index, inplace = True)

    return df
