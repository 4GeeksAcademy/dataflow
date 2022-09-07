import pandas as pd
import numpy as np
from datetime import datetime

from utils import build_features as features

expected_input = [{
    'email': 'daniela@gmail.com',
    'created_at': '2021-11-21 16:10:04.837967+00:00'
}, {
    'email': 'daniela@gmail.com',
    'created_at': '2020-10-20 21:45:03.837967+00:00'
}, {
    'email': 'daniela@gmail.com',
    'created_at': '2021-11-11 13:32:04.837967+00:00'
}, {
    'email': 'alejandro@gmail.com',
    'created_at': '2019-12-11 13:29:23.837967+00:00'
}]

expected_output = [{
    'email': 'daniela@gmail.com',
    'created_at': '2020-10-20 21:45:03.837967+00:00'
}, {
    'email': 'alejandro@gmail.com',
    'created_at': '2019-12-11 13:29:23.837967+00:00'
}]


def run(df):
    """
    This function sorts data according to the created_at date, and combines duplicate rows by grouping by email
    and using only the first row value. If it is null, it uses the next one.
    """

    # remove duplicated rows by combining them considering the first creation date
    df = features.remove_duplicates(df)

    return df
