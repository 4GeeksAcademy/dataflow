import pandas as pd
import numpy as np
from datetime import datetime


expected_input = [{
    'created_at': '2021-11-21 21:32:04.837967+00:00',
    'updated_at': '2022-05-26 20:03:15.027964+00:00',
    'won_at': '2022-05-26 20:03:09.005816+00:00'
}]

expected_output = [{
    'created_at': pd.to_datetime('2021-11-21 21:32:04'),
    'updated_at': pd.to_datetime('2022-05-26 20:03:15'),
    'won_at': pd.to_datetime('2022-05-26 20:03:09'),
    'year-month': pd.to_datetime('2021-11-21 21:32:04').strftime('%Y-%m'),
    'created_time': pd.to_datetime('2021-11-21 21:32:04').strftime('%H:%M:%S'),
    'days_to_convert': 185
}]



def run(df):
    """
    This function takes care of processing any datetime string incoming in the df set
    It also creates a year-month column and a time column
    """

    df['created_at'] = df['created_at'].apply(pd.to_datetime)
    df['updated_at'] = df['updated_at'].apply(pd.to_datetime)
    df['won_at'] = df['won_at'].apply(pd.to_datetime)

    #Changing format
    df['created_at'] = df['created_at'].dt.strftime("%Y-%m-%d %H:%M:%S")
    df['updated_at'] = df['updated_at'].dt.strftime("%Y-%m-%d %H:%M:%S")
    df['won_at'] = df['won_at'].dt.strftime("%Y-%m-%d %H:%M:%S")

    #Format change also changed the column type to object, so we need to convert it to datetime again 
    df['created_at'] = df['created_at'].apply(pd.to_datetime)
    df['updated_at'] = df['updated_at'].apply(pd.to_datetime)
    df['won_at'] = df['won_at'].apply(pd.to_datetime)

    #creating new columns
    df['year-month'] = df['created_at'].dt.strftime('%Y-%m')
    df['created_time'] = df['created_at'].dt.strftime('%H:%M:%S')
    df['days_to_convert'] = (df['won_at'] - df['created_at']).dt.days.abs()
    
    return df
