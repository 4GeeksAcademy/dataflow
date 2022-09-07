import pandas as pd
import numpy as np
from datetime import datetime

from utils import build_features as features

expected_input = [{
    'course': 'full-stack-ft',
    'location': 'los-cortijos-caracas',
    'language': 'us',
    'utm_source':'4geeks',
    'utm_medium':'rrss'
}]

expected_output = [{
    'course': 'full-stack',
    'location': 'caracas-venezuela',
    'language': 'en',
    'utm_source': 'ticjob',
    'utm_medium':'referral'
}]



def run(df):
    """
    This function cleans the categories in course, language, location, utm_source and utm_medium columns.
    """

    #Clean course column
    df = features.clean_course(df,'course')

    #Clean location column
    df = features.clean_location(df,'location')

    #clean language column
    df = features.clean_language(df,'language')

    #clean utm_source

    df = features.assign_with_conditions(df)

    df = features.clean_utm_source(df,'utm_source')

    #clean utm_medium
    df = features.clean_utm_medium(df,'utm_medium')

    return df
