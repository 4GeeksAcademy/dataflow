import pandas as pd
import numpy as np
from datetime import datetime
from slugify import slugify


expected_input = pd.DataFrame({
    'country': ['Venezuela','United States','nan','Colombia'],
    'phone_country': ['Peru','Congo','Congo','Error from invalid phone'],
    'location': ['caracas-venezuela','downtown-miami','downtown-miami','caracas-venezuela']
})

expected_output = pd.DataFrame({
    'country': ['venezuela','united-states', 'nan','colombia'],
    'phone_country': ['peru','congo','congo','error-from-invalid-phone'],
    'location': ['caracas-venezuela','downtown-miami','downtown-miami','caracas-venezuela'],
    'correct_location': ['lima-peru','downtown-miami','No location assigned','bogota-colombia']
})
    

def run(df):
    """
    This function creates a new column to specify the correct location assigned, according to the country the lead comes from.
    """

    LATAM_COUNTRIES = ['Argentina','Bolivia','Brazil','Chile','Colombia','Ecuador','Paraguay','Peru','Uruguay','Venezuela','Belize',
                    'Costa Rica','Cuba','Dominican Republic','El Salvador','Guatemala','Haiti','Honduras','Jamaica','Mexico','Nicaragua',
                    'Panama','Saint Lucia','Antigua and Barbuda','Guyana','Suriname','Saint Kitts & Nevis','Bahamas','Barbados',
                    'Trinidad and Tobago','Grenada','Saint Vincent and the Grenadines','Dominica']

    LATAM_LOCATIONS = ['caracas-venezuela','santiago-chile','bogota-colombia','online','costa-rica','buenosaires-argentina','mexicocity-mexico',
                    'quito-ecuador','panamacity-panama','montevideo-uruguay','sanjose-uruguay','lapaz-bolivia','lima-peru',
                    'maracaibo-venezuela']

    EUROPE_COUNTRIES = ['Hungary','Belarus','Austria','Serbia','Switzerland','Germany','Holy See','Andorra','Bulgaria','United Kingdom',
                    'France','Montenegro','Luxembourg','Italy','Denmark','Finland','Slovakia','Norway','Ireland','Spain','Malta',
                    'Ukraine','Croatia','Moldova','Monaco','Liechtenstein','Poland','Iceland','San Marino','Bosnia and Herzegovina',
                    'Albania','Lithuania','Macedonia','Slovenia','Romania','Latvia','Netherlands','Russia','Estonia','Belgium',
                    'Czech Republic','Greece','Portugal','Sweeden']

    EUROPE_LOCATIONS = ['madrid-spain','europe','barcelona-spain','malaga-spain','munich-germany','berlin-germany','valencia-spain',
                    'rome-italy','lisbon-portugal','maracaibo-venezuela','hamburg-germany','dublin-ireland','milan-italy','europe']

    print('Shape before creating correct_location ', df.shape)

    #put all country column, and country lists in lower case

    df['country'] = df['country'].str.lower()
    df['phone_country'] = df['phone_country'].str.lower()
    LATAM_COUNTRIES = list(map(str.lower,LATAM_COUNTRIES))
    EUROPE_COUNTRIES = list(map(str.lower,EUROPE_COUNTRIES))

    #put '-' in any blank space in a country name
    df['country'] = df['country'].astype(str).apply(lambda x :slugify(x))
    df['phone_country'] = df['phone_country'].astype(str).apply(lambda x :slugify(x))

    #create a correct_location list according to several conditions

    correct_location = []

    for row in df.itertuples(index=False):
        def compare_with(target_phone):
            if str(target_phone) in str(row.location):    
                return row.location
            elif str(target_phone) in str('united-states'):    
                return 'downtown-miami'
            elif str(target_phone) in LATAM_COUNTRIES and (v for v in LATAM_LOCATIONS if str(target_phone) in v):  
                latam_search = str(target_phone)
                latam_match = list(filter(lambda x: latam_search in x, LATAM_LOCATIONS))
                return latam_match
            elif str(target_phone) in EUROPE_COUNTRIES and str(target_phone) in EUROPE_LOCATIONS:
                europe_search = str(target_phone)
                europe_match = list(filter(lambda x: europe_search in x, EUROPE_LOCATIONS))
                return europe_match
            elif str(target_phone) in LATAM_COUNTRIES: 
                return 'online'
            elif str(target_phone) in EUROPE_COUNTRIES:  
                return 'europe'
            return None

        location = compare_with(row.phone_country) if str(row.phone_country) not in ['Error from invalid phone','No country assigned'] else None
        if  location is not None:
            correct_location.append(location)
            continue

        if location:= compare_with(row.country):
            correct_location.append(location)
            continue
        
        correct_location.append('No location assigned')

    #create new column with the values of correct_location list

    df['correct_location'] = correct_location

    #remove '[ ]' from any list in correct_location column (created because of having more than one item)

    f = lambda x: ','.join(map(str, x)) if isinstance(x, list) else x
    df['correct_location'] = df['correct_location'].apply(f)

    print('Shape after new correct_location column ', df.shape)

    return df







