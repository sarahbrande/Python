#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
  #working with dataframes, similar to excel, headers, etc


# In[4]:


# Method #1 specify full path to file
# "C:\Users\sarah\Desktop\Udemy\Pythoncourse\P4-Demographic-Data.csv"


# In[5]:


#Windows  don't forget double slashes to avoid escape character issue
stats = pd.read_csv('C:\\Users\\sarah\\Desktop\\Udemy\\Pythoncourse\\P4-Demographic-Data.csv')


# In[6]:


stats


# In[7]:


# method 2
import os


# In[8]:


print(os.getcwd())


# In[9]:


#If you had put it in the above folder(where it saves notebook), you don't need to give path


# In[10]:


#mess up, change back
os.chdir('C:\\Users\\sarah\\Desktop\\Udemy\\Pythoncourse')


# In[11]:


print(os.getcwd())


# In[12]:


stat2 = pd.read_csv('P4-Demographic-Data.csv')


# In[13]:


# explore dataframe 1.
stats


# In[14]:


#2 Number of rows
len(stats)  #195 rows imported


# In[15]:


#3 See columns
stats.columns


# In[16]:


#4 NUMBER OF colunms
len(stats.columns)


# In[17]:


# top rows
stats.head(6)


# In[18]:


stats.tail(6)   # head and 


# In[19]:


#7 info on the columns
stats.info()


# In[20]:


stats.describe()


# In[21]:


stats.describe().transpose()


# In[22]:


stats.columns


# In[23]:


stats.columns=['a','b','c','d','e']


# In[24]:


stats.columns


# In[25]:


stats.columns=['Country Name', 'Country Code', 'Birth rate', 'Internet users',  
       'Income Group']
# In Jupyter Notebook can continue even with newline , but regular python need a \ 


# In[26]:


stats.columns=['CountryName', 'CountryCode',               'Birthrate', 'Internetusers','IncomeGroup']


# In[27]:


stats.head()


# In[28]:


# 2 parts, Rows, columns, combination
stats[21:26] #every row new entry of data so it new rows


# In[29]:


stats[:5]


# In[30]:


#Reverse
stats[::-20]  #to reverse reassign stats=stats[::-1]


# In[31]:


#my fav columns
stats['CountryName']


# In[32]:


x=stats['CountryName'].transpose


# In[33]:


stats['CountryName'].head()


# In[34]:


stats[['CountryName','Birthrate']].head()


# In[35]:


stats[['Birthrate','CountryName']].head()


# In[36]:


stats.Birthrate     # can't have spaces  ---- only works with 1 column


# In[37]:


# Combining rows/columns
stats[4:8][['CountryName','Birthrate']]


# In[38]:


stats[['CountryName','Birthrate']][4:8]


# In[39]:


stats[['CountryName','Birthrate','Internetusers']][4:8]


# In[40]:


results = stats.Birthrate * stats.Internetusers


# In[41]:


results[4:8]  # results.head() for top 10


# In[42]:


# add col
stats['Mycalc'] = stats.Birthrate * stats.Internetusers


# In[43]:


stats.head()


# In[44]:


stats['xyz'] = range(1,196)


# In[45]:


stats.head()


# In[46]:


# removing column
stats.drop('Mycalc',1)  #vert axis =0, horizontla (columns)=1  shift tab 


# In[47]:


stats=stats.drop('Mycalc',1)


# In[48]:


stats[4:10]


# In[ ]:





# In[ ]:


stats.head()


# In[56]:


Filter=stats.Internetusers<2
Filter.head()


# In[63]:


Filter=stats.Internetusers<90
stats[~Filter]


# In[65]:


Filterx=stats.Internetusers<90
stats[~Filterx]


# In[69]:


Filter2=stats.Birthrate>40
stats[Filter2].head()


# In[70]:


stats[stats.Birthrate>40].head()


# In[77]:


#combining filters
stats[(stats.Birthrate>40) & (stats.Internetusers<2)].head()  #use & for bitwise - a lot of explanation


# In[79]:


#another one
stats[stats.IncomeGroup=="High income"].head()


# In[81]:


#how to get unique catagories
stats.IncomeGroup.unique()


# In[82]:


stats[stats.CountryName=="Malta"]


# In[ ]:




