#!/usr/bin/env python
# coding: utf-8

# In[1]:


import string
import random


# In[2]:


n = string.ascii_lowercase
N = string.ascii_uppercase
num = string.digits


# In[3]:


xyz = n + N + num 
password = "".join(random.sample(xyz,8))
print("Your Randomly generated password is: " + password)


# In[4]:


OTP = "".join(random.sample(num,6))
print("Your OTP is: " + OTP)


# In[ ]:





# In[ ]:




