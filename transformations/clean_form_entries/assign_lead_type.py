import pandas as pd
import numpy as np
from datetime import datetime


expected_input = [{
    'tags': 'website-lead',
    'lead_type': 'NaN'
}]

expected_output = [{
    'tags': 'website-lead',
    'lead_type': 'STRONG'
}]



def run(df):
    """
    This function assigns the correct lead_type values according to the tags column.
    """

    #Assign values

    df.loc[df['tags'] == 'request_more_info', 'lead_type'] = 'SOFT'
    df.loc[df['tags'] == 'website-lead', 'lead_type'] = 'STRONG'
    df.loc[df['tags'] == 'newsletter', 'lead_type'] = 'DISCOVERY'
    df.loc[df['tags'] == 'contact-us', 'lead_type'] = 'SOFT'
    df.loc[df['tags'] == 'utec-uruguay', 'lead_type'] = 'STRONG'
    df.loc[df['tags'] == 'jobboard-lead', 'lead_type'] = 'STRONG'
    df.loc[df['tags'] == 'hiring-partner', 'lead_type'] = 'OTHER'
    df.loc[df['tags'] == 'download_outcome', 'lead_type'] = 'DISCOVERY'
    df.loc[df['tags'] == 'website-lead,blacks-in-technology', 'lead_type'] = 'STRONG'
    df.loc[df['tags'] == 'request_downloadable', 'lead_type'] = 'DISCOVERY'

    return df
