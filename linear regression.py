#!/usr/bin/env python
# coding: utf-8

# In[7]:


print("hello world")


# In[10]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data =pd.read_csv("F:\om\Train.csv")
data


# In[11]:


data.head()


# In[12]:


data_= data.loc[:,['humidity','temperature']]
data_.head(5)


# In[13]:


data.describe()


# In[14]:


data.tail()


# In[29]:


import matplotlib.pyplot as plt
from matplotlib import style
data_.plot(x='humidity',y='temperature',style='o')
plt.xlabel=('huminity')
plt.ylabel=('temperature')
plt.show


# In[30]:


x = pd.DataFrame(data_['humidity'])
y= pd.DataFrame(data_['temperature'])
print(x.size,y.size)


# In[ ]:




