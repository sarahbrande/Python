#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
from pandas import DataFrame
from bitstring import BitArray
import os
import re


# In[4]:


Data=pd.read_csv('C:\\Users\\sarah\\Desktop\\Udemy\\Pythoncourse\\FakeData.csv')


# In[5]:


Data


# In[6]:


#the goal is to build The values into a word.  The LSB (lease significant bit) is to the right
# in this case it would be 0b0111110  (hex F = binary 1111)
# E is really 16, not 15/ also wanted to lead with zero to make sure leading zeros aren't dropped


# In[7]:


x="4hF"
regex=r"(\d+)h"
re.sub(regex,'0x',x)


# In[8]:


# Trying to figure out how to 
x=Data.Value[1]
regex=r"(\d+)'h"
BitArray(re.sub(regex,'0x',x))


# In[9]:


def Bitnum(x):  # this changes the values into a string bitstring function can recognize
                # BitArray recognizes 0b as binary and 0x as hex
    regex=r"(\d+)'b"           # search for any decimals, followed by a tick and then b
    x=re.sub(regex,'0b',x)     # replace what is found int the regex search with 0b
    regex=r"(\d+)'h"
    x=re.sub(regex,'0x',x)
    return x


# In[29]:





# In[ ]:





# In[11]:


Data['BitVals']=Data.Value.apply(Bitnum)


# In[12]:


Data


# In[13]:


BitWord=BitArray(Data.BitVals[3]+Data.BitVals[2])


# In[14]:


BitWord


# In[20]:


def BitBin(x):           #This turns anything in hex to binary
    x=BitArray(x).bin
    return x


# In[22]:


Data['Bits']=Data.BitVals.apply(BitBin)


# In[23]:


Data


# In[28]:


Bitword=Data.Bits[3]+Data.Bits[2]+Data.Bits[1]+Data.Bits[0]
Bitword                                                      #This is the answer


# In[43]:


#-----------------Now for checks

#number of dogs  10binary = 2decimal
Bitword[6:8]


# In[45]:


len(Bitword)  #checking to make sure leading zeros weren't dropped


# In[46]:


Data.Bits


# In[ ]:




