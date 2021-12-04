#!/usr/bin/env python
# coding: utf-8

# In[24]:


for i in range(1,6):
    for j in range(0,i) :
        print("*",end="")
    print()
for k in range(6,0,-1):
    for l in range(k-1,0,-1):
        print("*",end="")
    print()
    


# In[29]:


a = input("Enter a string to be reversed ")
l = len(a) - 1
for i in a:
    print(a[l],end='')
    l = l-1


# In[ ]:




