#!/usr/bin/env python
# coding: utf-8

# In[3]:


firstname = "olawumi"
lastname ="joseph"
middlename = "pelumi"
fullname = firstname + " " + lastname + " " + middlename
print(fullname)


# In[5]:


fruits = ['cashew', 'mango', 'banana']
fruits[1]


# In[30]:


first_initial=firstname[0].upper()
second_initial=middlename[0].upper()
refined_lastname = lastname.title()

fullname_initials = first_initial + "." + second_initial + "." + " " + refined_lastname
print(fullname_initials)


# In[19]:


sliced_firstname = firstname[:3]
print(sliced_firstname)


# In[22]:


name_repeated = 3 * fullname_initials
name_repeated


# In[23]:


print(len(fullname_initials))


# In[26]:


'J' in fullname_initials


# In[31]:


new_fullname=fullname_initials.replace('Joseph','Kolapo')
new_fullname


# In[ ]:




