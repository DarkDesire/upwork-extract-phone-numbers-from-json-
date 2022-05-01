#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json


# In[ ]:


INPUT_FILE = 'Reonomy_Retail.json'
OUTPUT_FILE = './extract-phone-numbers-from-json.xlsx'


# In[ ]:


with open(INPUT_FILE, 'r') as file:
    data = json.load(file)


# In[ ]:


results = []
for obj in data:
    
    persons = []
    for person in obj['persons']:
        output_obj = {}
        output_obj['company_name'] = obj['name']
        output_obj['person_name'] = person['name']
        
        if person.get('emails', None) is not None and len(person['emails'])>0 :
            output_obj['email'] = ",".join([obj['email'] for obj in person['emails']])
            
        if person.get('phones', None) is not None and len(person['phones'])>0 :
            output_obj['phone'] = ",".join([obj['number'] for obj in person['phones']])
        
    results.append(output_obj)


# In[ ]:


import pandas as pd # for saving from dataclass into excel format
df = pd.DataFrame(results) #converting from results to DataFrame
df.to_excel(OUTPUT_FILE, index=False, header=True) #saving dataframe to file

