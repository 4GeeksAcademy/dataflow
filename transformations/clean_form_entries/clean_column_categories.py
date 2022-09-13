import pandas as pd
import numpy as np
from datetime import datetime


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
    df['course'] = df['course'].replace(['full-stack-ft', 'full_stack', 'full-stack,software-engineering',
                                    'coding-introduction', 'outcomes'], 'full-stack')
    df['course'] = df['course'].replace(['machine-learning', 'machine-learning-enginnering'],
                                    'machine-learning-engineering')


    #Clean location column
    df['location'] = df['location'].replace(['maracaibo'], 'maracaibo-venezuela')
    df['location'] = df['location'].replace(['los-cortijos-caracas'], 'caracas-venezuela')


    #clean language column
    df['language'] = df['language'].replace('us', 'en')

    #clean utm_source

    #1.assign with conditions
    df['utm_medium'] = np.where((df['utm_source'] == 'Facebook ads') |
                                (df['utm_source'] == 'Facebook_Marketplace') |
                                (df['utm_source'] == 'Facebook_Mobile_Feed') |
                                (df['utm_source'] == 'facebook_awareness') |
                                (df['utm_source'] == 'Facebook_Stories') |
                                (df['utm_source'] == 'Facebook_Desktop_Feed') |
                                (df['utm_source'] == 'Business Manager IG') |
                                (df['utm_source'] == 'Instagram_Feed') |
                                (df['utm_source'] == 'Instagram_Stories'),
                                'cpc', df['utm_medium'])

    df['utm_source'] = np.where((df['utm_medium'] == 'Instagram_Stories') |
                                (df['utm_medium'] == 'Instagram_Feed'),
                                'instagram', df['utm_source'])

    df['utm_source'] = np.where((df['utm_medium'] == 'Facebook_Mobile_Feed'),
                                'facebook', df['utm_source'])

    #2 clean utm source column
    df['utm_source'] = df['utm_source'].replace('LInkedin', 'linkedin')
    df['utm_source'] = df['utm_source'].replace('CourseReport', 'coursereport')
    df['utm_source'] = df['utm_source'].replace(['landingjobs?utm_medium=machine-learning-engineering',
                                    'landingjobs?utm_medium=full-stack', 'landingjobs?utm_medium=RRSS'],
                                    'landingjobs')
    df['utm_source'] = df['utm_source'].replace('google_ads', 'google')
    df['utm_source'] = df['utm_source'].replace(
        ['Business Manager IG', 'Instagram_Feed', 'ig', 'Instagram_Stories'], 'instagram')
    df['utm_source'] = df['utm_source'].replace(['Facebook', 'Facebook ads', 'Facebook_Marketplace', 'Facebook_Mobile_Feed',
                                    'facebook_instagram', 'fb', 'an', 'facebook_awareness', 'Facebook_Stories',
                                     'Facebook_Desktop_Feed'], 'facebook')
    df['utm_source'] = df['utm_source'].replace('4geeks', 'ticjob')



    #clean utm_medium
    df['utm_medium'] = df['utm_medium'].replace(['schoolpage', 'coursereportschoolpage', 'schoolpage?utm_source=careerkarma',
                                    'Blog', 'affiliate_email', 'rrss', 'inscripcion', 'event'], 'referral')
    df['utm_medium'] = df['utm_medium'].replace(['ppc', 'FB paid', 'Facebook_Mobile_Feed', 'Instagram_Stories', 'Instagram_Feed'],
                                    'cpc')
    df['utm_medium'] = np.where((df['utm_source'] == 'linkedin') & (df['utm_medium'] == 'social'),
                          'cpc', df['utm_medium'])

    df['utm_medium'] = np.where((df['utm_source'] == 'linkedin') & (df['utm_medium'] == 'Inmail'),
                          'cpc', df['utm_medium'])

    return df
