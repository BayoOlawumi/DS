#!/usr/bin/env python
# coding: utf-8

# ## Operators

# - Arithmetic operators
# - Assignment operators
# - Comparison operators
# - Logical operators
# - Identity operators
# - Membership operators
# - Bitwise operators

# ### Arithmetic Operators

# In[ ]:


#These are normal mathematical opeartions
#Examples
a = 34
b = 56
c =a + b
#Other operations like -, / , and *.
#%  Modulus--- Remainder Concept
#** Exponentiation--- Raise to Power Concept
#// Floor division can be performed on them--- Whole Number division concept


# ### Assignment operators

# In[9]:


b = 6/2

#other smart operations include
print(b)
#var var + operator +operator + var

b += 3
#Same as b = b + 3
print(b)

b /=3
#Same as b = b/3
print(b)


# ### Comparison Operators

# In[13]:


# There are times when we will need to compare different values , we use this type of operators then
# ==(Equal to), !=(Not equal to), >(Greater than),
#<(Lessthan), >=(Greater than or equal to, <=(Less than or equal to) 
a = 4
b = 7


# ###  Logical Operators

# In[20]:


# This is to check conditions
#They are 'and', 'or', 'not'

age = 23
if age >= 23 and type(age)==int:
    print("Yeah Yeah")
    
    


# ### Identity Operators

# In[23]:


#They are is and is not

a = 5
b = 6

a is not b


# ### Membership Operators

# In[24]:


#This include in and not in
std_score = [45, 67, 89]
new_score = 34
new_score in std_score_score


# ### Bitwise Operators
# ***Bitwise operators are used to compare (binary) numbers:***

# In[34]:


a = 60            # 60 = 0011 1100 
b = 13            # 13 = 0000 1101 
c = 0

c = a & b;        # 12 = 0000 1100
print ("Line 1 - Value of c is ", c)

d = a | b;        # 61 = 0011 1101 
print("Line 2 - Value of c is ", d)

e = a ^ b;        # 49 = 0011 0001
print ("Line 3 - Value of c is ", e)


# In[ ]:




