import pandas as pd
import numpy as np
from datetime import datetime


expected_input = [{
    'course': 'full-stack-ft',
    'location': 'maracaibo',
    'language': 'us',
    'utm_source':'4geeks',
    'utm_medium':'rrss',
    'academy_id': 1.0,
    'gclid': 'Cj0KCQiAubmPBhCyARIsAJWNpiOwBq3xtBtRHks7SF0NvV'
}]

expected_output = [{
    'course': 'full-stack',
    'location': 'maracaibo-venezuela',
    'language': 'en',
    'utm_source': 'ticjob',
    'utm_medium':'referral',
    'academy_id': 2.0,
    'gclid': 'Cj0KCQiAubmPBhCyARIsAJWNpiOwBq3xtBtRHks7SF0NvV'
}]



def run(df):
    """
    This function cleans the categories in course, language, location, utm_source and utm_medium columns.
    """
    print('Shape before cleaning categories ', df.shape)


    #Clean course column
    df['course'] = df['course'].replace(['full-stack-ft', 'full_stack', 'full-stack,software-engineering',
                                    'coding-introduction', 'outcomes'], 'full-stack')
    df['course'] = df['course'].replace(['machine-learning', 'machine-learning-enginnering'],
                                    'machine-learning-engineering')


    #Clean location column
    df['location'] = df['location'].replace(['maracaibo'], 'maracaibo-venezuela')
    df['location'] = df['location'].replace(['los-cortijos-caracas'], 'caracas-venezuela')
    df['location'] = df['location'].replace(['lisboa-portugal'], 'lisbon-portugal')


    #clean language column
    df['language'] = df['language'].replace('us', 'en')

    #clean academy_id

    df['academy_id'] = np.where((df['location'] == 'maracaibo-venezuela'),
                                2.0, df['academy_id'])
    df['academy_id'] = np.where((df['location'] == 'toronto-canada'),
                                4.0, df['academy_id'])
    df['academy_id'] = np.where((df['location'] == 'costa-rica') |
                                (df['location'] == 'sanjose-uruguay'),
                                7.0, df['academy_id'])

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

    df['utm_medium'] = np.where((df['utm_source'] == 'landingjobs'),
                                'referral', df['utm_medium'])

    df['utm_medium'] = np.where((df['utm_source'] == 'careerkarma') & (df['utm_medium'].isnull() == True), 
                          'referral', df['utm_medium'])

    df['utm_medium'] = np.where((df['utm_source'] == 'facebook') & (df['utm_medium'].isnull() == True),
                          'cpc', df['utm_medium'])

    df['utm_medium'] = np.where((df['utm_source'] == 'zoho_recruite') & (df['utm_medium'] == 'cpc'),
                          'referral', df['utm_medium'])

    #Convert null medium in cpc or referral if gclid is not null

    df['utm_medium'] = np.where((df['utm_medium'].isnull()) & (df['gclid'].str.startswith('Cj')), 
                        'cpc', df['utm_medium'])

    df['utm_medium'] = np.where((df['utm_medium'].isnull()) & (df['gclid'].str.startswith('cl')), 
                        'referral', df['utm_medium'])

    #convert null source in google according to gclid

    df['utm_source'] = np.where((df['utm_source'].isnull() == True) &
                        ((df['gclid'].str.startswith('Cj')) | 
                        (df['gclid'].str.startswith('EA'))),
                        'google', df['utm_source'])


    #convert null source in facebook according to gclid

    df['utm_source'] = np.where((df['utm_source'].isnull() == True) &
                        (df['gclid'].str.startswith('PAA')),
                        'facebook', df['utm_source'])


    #convert null source in careerkarma according to gclid

    df['utm_source'] = np.where((df['utm_source'].isnull() == True) &
                        (df['gclid'].str.startswith('cl')),
                        'careerkarma', df['utm_source'])

    # change name of null medium

    df['utm_medium'] = np.where((df['utm_source'].isnull() == True) & (df['utm_medium'].isnull() == True),
                                'undefined & organic', df['utm_medium'])

    # change name of null source

    df['utm_source'] = np.where((df['utm_medium'] == 'undefined & organic'),
                                'undefined', df['utm_source'])


    return df
