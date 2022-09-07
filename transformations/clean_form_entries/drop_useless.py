import pandas as pd
import numpy as np
from datetime import datetime

from utils import build_features as features
from utils.constants import TO_DROP

temporal_dict = {}
for x in TO_DROP:
    temporal_dict[x] = 1
expected_input = pd.DataFrame({
    'ac_contact_id' : ["John","Deep","Julia","Kate","Sandy"], 
    'email': ['a@4geeks.co', 'a@gmail.com', 'b@gmail.com','c@gmail.com','d@gmail.com'],
    'ids':[None,None,None,None,None],
    #'utm_source':['fintech','ticjob','ticjob','ticjob','ticjob'],
    **temporal_dict
    })


expected_output = pd.DataFrame({
    'email': ['a@gmail.com', 'b@gmail.com','c@gmail.com','d@gmail.com'],
    #'utm_source':['ticjob','ticjob','ticjob','ticjob']
})



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
    df = features.drop_test_rows(df)
    print(df.head())

    #dropping two other test rows identified
    #df.drop(df[df['utm_source'] == 'test_s'].index, inplace = True)
    #df.drop(df[df['utm_source'] == 'fintech'].index, inplace = True)

    return df
