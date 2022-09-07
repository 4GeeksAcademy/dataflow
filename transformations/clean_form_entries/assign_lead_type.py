import pandas as pd
import numpy as np
from datetime import datetime

from utils import build_features as features

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
    df = features.assign_lead_type(df, 'tags','lead_type')

    return df
