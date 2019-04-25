#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np
from numpy.random import randn
randn()


# In[77]:


#---- -2---- -1 ---- 0 ---- 1 ----2
answer=None
x=randn()
if x > 1:
    answer = "Greater than 1"
else:
    answer = "less"
print(x)
print(answer)


# In[88]:


#Nested
#---- -2---- -1 ---- 0 ---- 1 ----2
answer=None
x=randn()
if x > 1:
    answer = "Greater than 1"
else:
    if x >= -1:
        answer = "between -1 and 1"
    else:
        answer = "less than -1"
print(x)
print(answer)


# In[92]:


#Chained
#---- -2---- -1 ---- 0 ---- 1 ----2
answer=None
x=randn()
if x > 1:
    answer = "Greater than 1"
elif x >= -1:
        answer = "between -1 and 1"
else:
    answer = "less than -1"
print(x)
print(answer)

