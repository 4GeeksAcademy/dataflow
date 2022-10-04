import pandas as pd
import numpy as np
from datetime import datetime

TO_DROP = ['phone','client_comments','street_address','city','latitude','longitude','state',
                  'zip_code','referral_key','browser_lang','ac_expected_cohort','current_download','utm_content',
                  'storage_status','user_id','ac_contact_id','first_name','last_name','storage_status_text']

# list of values in columns
ph= ['ab','ba','cb','bc'] 
cmts= ['ab','ba','cb','bc'] 
adrs= ['ab','ba','cb','bc'] 
cty= ['ab','ba','cb','bc'] 
ltde= ['ab','ba','cb','bc'] 
lgde= ['ab','ba','cb','bc']  
state= ['ab','ba','cb','bc'] 
zip= ['ab','ba','cb','bc']  
key= ['ab','ba','cb','bc']  
lang= ['ab','ba','cb','bc']  
ac_cohort= ['ab','ba','cb','bc']  
download= ['ab','ba','cb','bc'] 
utm_content= ['ab','ba','cb','bc'] 
status= ['ab','ba','cb','bc'] 
user_id= ['ab','ba','cb','bc'] 
ac_contact_id= ['ab','ba','cb','bc']
first_name= ['ab','ba','cb','bc']
last_name= ['ab','ba','cb','bc'] 
ids= [None, None, None, None] 
emails= ['a@4geeks.co', 'd@gmail.com', 'b@4geeksacademy.com', 'c@gmail.com']
 
# dictionary of lists 
dict = {'phone': ph,'client_comments':cmts,'street_address':adrs,'city':cty,'latitude':ltde,'longitude':lgde,'state':state,
                  'zip_code':zip,'referral_key':key,'browser_lang':lang,'ac_expected_cohort':ac_cohort,'current_download':download,
                  'utm_content':utm_content,'storage_status':status,'user_id':user_id,'ac_contact_id':ac_contact_id,
                  'first_name':first_name,'last_name':last_name, 'ids':ids, 'email':emails} 

#expected input as dataframe
expected_input = pd.DataFrame(dict)

#values for Output
output_emails = ['d@gmail.com', 'c@gmail.com']

#expected output
expected_output = pd.DataFrame({'email':output_emails})
    

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

    # Drop testing rows
    df = df[df["email"].str.contains("@4geeks") == False]
    
    print('Shape after drop_useless ', df.shape)

    return df
