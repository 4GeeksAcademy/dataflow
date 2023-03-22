import pandas as pd
import numpy as np
from datetime import datetime

TO_DROP = ['client_comments','street_address','city','latitude','longitude','state',
                  'zip_code','referral_key','browser_lang','ac_expected_cohort','current_download','utm_content',
                  'user_id','ac_contact_id','first_name','last_name','storage_status_text']

expected_input = [{
    'client_comments':'ab',
    'street_address':'ab',
    'city':'ab',
    'latitude':'ab',
    'longitude':'ab',
    'state':'ab',
    'zip_code':'ab',
    'referral_key':'ab',
    'browser_lang':'ab',
    'ac_expected_cohort':'ab',
    'current_download':'ab',
    'utm_content':'ab',
    'storage_status':'ab',
    'user_id':'ab',
    'ac_contact_id':'ab',
    'first_name':'ab',
    'last_name':'ab',
    'storage_status_text':'ab',
    'email':'d@gmail.com'
}]

expected_output = [{
    'storage_status':'ab',
    'email':'d@gmail.com'
}]


def run(df):
    """
    This function drops 100% null columns, irrelevant columns and original columns used for combination.
    It also drops rows that contain 4geeks emails that were used for testing.
    """

    print('Shape before drop_useless ', df.shape)

    # Drop irrelevant columns
    df.drop(TO_DROP, axis=1, inplace=True)

    # Drop null columns
    df.dropna(axis=1, how='all', inplace=True)

    print('Shape after drop_useless ', df.shape)

    return df
