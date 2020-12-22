#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from unicodedata import normalize
import matplotlib.pyplot as plt


get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


dfTRT = pd.read_html('https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M')
len(dfTRT)


# In[3]:


dfTRT = dfTRT[0]
dfTRT


# In[4]:


dfTRT.groupby(by = 'Borough').agg('count')


# In[5]:


rows = len(dfTRT.index)
dropped = 0
for i in range (0, rows):
    if dfTRT.at[i, 'Borough'] == 'Not assigned':
        dfTRT.drop(i, inplace = True)
        rows = rows - 1
        dropped = dropped +1
print('Rows Remaining: ', len(dfTRT.index), 'Rows Dropped: ', dropped)
dfTRT.reset_index(inplace = True)


# In[6]:



for i in range (0, rows):
    if dfTRT.at[i, 'Neighbourhood'] == 'Not assigned':
       
        dfTRT.at[i, 'Neighbourhood'] = dfTRT.at[i, 'Borough'] 
   
    


# In[8]:





# In[ ]:




