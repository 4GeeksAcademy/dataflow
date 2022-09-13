import pandas as pd
import numpy as np
from datetime import datetime


# list of values in columns
created_dates= ['2021-11-21','2020-10-20','2018-11-11','2019-12-11']
emails= ['daniela@gmail.com', 'daniela@gmail.com', 'maria@gmail.com', 'daniela@gmail.com']
has_gclid= [0,0,1,1] 
# dictionary of lists 
dict = {'email':emails, 'created_at':created_dates,'has_gclid':has_gclid} 

#expected input as dataframe
expected_input = pd.DataFrame(dict)

#values for Output
output_dates = ['2019-12-11', '2018-11-11']
output_emails = ['daniela@gmail.com','maria@gmail.com']
output_gclids= [1,1]

#expected output
expected_output = pd.DataFrame({'email':output_emails,'created_at':output_dates, 'has_gclid':output_gclids})

def run(df):
    """
    This function sorts data according to the created_at date, and combines duplicate rows by grouping by email
    and using only the first row value. If it is null, it uses the next one.
    """

    # remove duplicated rows by combining them considering the first creation date
    print('Shape before combining duplicates: ', df.shape)
    df = df.replace("Nan", np.nan)
    df = df.sort_values("created_at")
    df = df.groupby("email").first().reset_index()
    print('Shape after combining duplicates: ', df.shape)

    return df
