#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import os
import json
from pandas.io.json import json_normalize
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib
import sys
import datetime;
import requests


# Run below Cell to find  state code

# In[4]:


url="https://cdn-api.co-vin.in/api/v2/admin/location/states"
payload={}
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}
pd.set_option('display.max_rows', 1000)
response = requests.request("GET", url, headers=headers, data=payload)
format_data = response.json()
slots_df=pd.json_normalize(format_data['states'])
# newdf=pd.Series(flatten_json(format_data)).to_frame()
# slots_df
# newdf
header_df=pd.json_normalize(format_data)
slots_df


# In[6]:


#enter state id in below variable
state_id='34'
url="https://cdn-api.co-vin.in/api/v2/admin/location/districts/"+state_id
payload={}
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}
pd.set_option('display.max_rows', 1000)
response = requests.request("GET", url, headers=headers, data=payload)
format_data = response.json()
slots_df=pd.json_normalize(format_data['districts'])
# newdf=pd.Series(flatten_json(format_data)).to_frame()
# slots_df
# newdf
header_df=pd.json_normalize(format_data)
slots_df


# In[7]:


#enter district id in below variable


district_id='670'
url="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id="+district_id+"&date=15-06-2021"
payload={}
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}
pd.set_option('display.max_rows', 1000)
response = requests.request("GET", url, headers=headers, data=payload)
print(response)
format_data = response.json()
slots_df=pd.json_normalize(format_data['sessions'])
# slots_df=pd.json_normalize(format_data['centers']['sessions'])

# newdf=pd.Series(flatten_json(format_data)).to_frame()
# slots_df
# newdf
header_df=pd.json_normalize(format_data['sessions'])

slots_df
# index = queryList_df.index
# print(response.text)


# In[227]:


#Make an account on sinch to get sms alerts on your phone 
#Make necessary changes in if conditions
res=''
ct = datetime.datetime.now()
for i in slots_df.index:
    if(slots_df['available_capacity_dose2'][i]!= 0  and slots_df['fee_type'][i]=='Free' and slots_df['min_age_limit'][i]==18 and slots_df['vaccine'][i]=='COVAXIN' and slots_df['center_id'][i]==692549 ):
        res=str(slots_df['available_capacity_dose2'][i])+' slots for '+slots_df['vaccine'][i]+' are available on '+slots_df['date'][i]+' in '+slots_df['name'][i]+', '+slots_df['address'][i]+' at '+str(ct)
        print(res)
        res2=str(res)
        headers = {
        'Authorization': 'Bearer *******************',
        'Content-Type': 'application/json',
        }

        data = {"from": "COWIN", "to": [ "<your phone number>" ], "body": res2 }
        data_json=json.dumps(data)
        print(data_json)
        response = requests.post('https://sms.api.sinch.com/xms/v1/*************/batches', headers=headers, data=data_json)
#         print(response)



# In[158]:





# In[224]:





# In[151]:





# In[140]:





# In[ ]:





# In[140]:





# In[ ]:





# In[ ]:





# In[ ]:




