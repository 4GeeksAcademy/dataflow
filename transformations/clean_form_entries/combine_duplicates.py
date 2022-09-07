import pandas as pd
import numpy as np
from datetime import datetime

from utils import build_features as features

expected_input = [{
    'email': '',
    'created_at':''
}]

expected_output = [{
    'email': '',
    'created_at':''
}]



def run(df):
    """
    This function sorts data according to the created_at date, and combines duplicate rows by grouping by email
    and using only the first row value. If it is null, it uses the next one.
    """

    #remove duplicated rows by combining them considering the first creation date
    df = features.remove_duplicates(df)

    return df
