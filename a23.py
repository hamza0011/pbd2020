#!/usr/bin/env python
# coding: utf-8

# In[20]:


#data normalization is essentially a type of process wherein data within a database is
#reorganized in such a way so that users can properly utilize that database for further queries and analysis.

import matplotlib as plt
from matplotlib import pyplot
import numpy as np
import pandas as pd
path="TSLA.csv"
fd=pd.read_csv(path)


# In[12]:


H=["date","open","high","low","close","adjclose","volume"]
fd.drop(0)


# In[13]:


fd.columns=H


# In[14]:


fd.head()


# In[15]:


fd["high"]=fd["high"]/fd["high"].max()


# In[16]:


fd["low"]=fd["low"]/fd["low"].max()


# In[18]:


fd["volume"]=fd["volume"]/fd["volume"].max()


# In[19]:


fd.head(10)


# In[29]:


fd.mean(axis = 1, skipna = True)


# In[30]:


fd.head(10)


# In[ ]:




