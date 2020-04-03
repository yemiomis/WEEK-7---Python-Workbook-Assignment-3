#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,-2,77,78,101]
GradeList = zip(names,grades)
df = pd.DataFrame(data = list(GradeList), columns=['Names', 'Grades'])


# In[4]:


df.loc[df['Grades'] <= 100]


# In[8]:


df.loc[(df['Grades'] >= 100,'Grades')] = 100
df


# In[9]:


df.loc[(df['Grades'] <= 0,'Grades')] = 0
df


# In[ ]:




