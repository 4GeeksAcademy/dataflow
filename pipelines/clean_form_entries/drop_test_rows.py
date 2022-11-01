import pandas as pd
import numpy as np
from datetime import datetime

mediums= ['ab', 'xxxxx','bc','cd'] 
sources= ['ab','bc','fintech','cd'] 
emails= ['a@4geeksacademy.com', 'd@gmail.com', 'bc', 'c@gmail.com']


dict = {'utm_medium':mediums,'utm_source':sources, 'email':emails}

#expected input as dataframe
expected_input = pd.DataFrame(dict)

#values for Output
output_mediums = ['cd']
output_sources = ['cd']
output_emails = ['c@gmail.com']

#expected output
expected_output = pd.DataFrame({'utm_medium':output_mediums, 'utm_source':output_sources,'email':output_emails})

def run(df):
    """
    This function drops additional rows used for testing, as they show invalid utm_medium categories, and were created
    by 4geeks employees using personal emails
    """

    print('Shape before drop_test_rows', df.shape)

    # Drop testing rows
    df = df[df["email"].str.contains("@4geeks") == False]

    #Do not keep rows that were only for test (identify them even if they do not have @4geeks email)
    df = df[df['utm_source'] != 'test_s']
    df = df[df['utm_source'] != 'fintech']
    df = df[df['utm_medium'] != 'xxxxx']
    df = df[df['utm_medium'] != 'marico']

    print('Shape after drop_test_rows', df.shape)

    return df
