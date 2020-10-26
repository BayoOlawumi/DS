#!/usr/bin/env python
# coding: utf-8

# In[1]:


import bs4
import requests
import numpy as np
import pandas as pd


# In[8]:


web_server = requests.get("https://toldnetwork.com")


# In[13]:


web_content = bs4.BeautifulSoup(web_server.text, 'html.parser')


# In[14]:


web_content.prettify()


# In[27]:


list_of_p = [tag.text for tag in web_content.find_all('p')]
list_of_links = [(tag.text.translate({ord(i): None for i in '\n\t'}), tag.get('href')) for tag in web_content.find_all('a')]


# In[66]:


df = pd.DataFrame()
df['text'] = [tag.text for tag in web_content.find_all('a') ]
df['link'] = [tag.get('href') for tag in web_content.find_all('a')]
df


# In[5]:


onez = np.ones((2,4))
head = ['id', 'time', 'energy']


# In[20]:


meter = pd.read_csv('meter.csv', header=None, names = head, sep=",")
df2 = pd.DataFrame(meter)


# In[103]:


meter_by_energy = meter.groupby('time').energy.sum()


# In[98]:


meter_energy= meter_by_energy.index[meter_by_energy >= 100]


# In[99]:


meter_energy


# In[39]:


onez


# In[ ]:





# In[40]:


four = onez*4


# In[46]:


np.set_printoptions(precision=2, suppress=True)


# In[47]:


ten_element = np.linspace(1,20,9)


# In[48]:


ten_element


# In[50]:


two_by_four = np.array((ten_element.reshape(3,3)))


# In[51]:


two_by_four


# In[57]:


two_by_four*3.7


# In[58]:


two_by_four.dtype


# In[59]:


plot(arange(10))


# In[3]:


get_ipython().run_line_magic('pinfo2', 'meter')


# In[2]:


get_ipython().run_line_magic('psearch', 'np.*lin*')


# In[21]:


a = np.random.randn(100, 100)
get_ipython().run_line_magic('timeit', 'np.dot(a, a)')
a


# In[122]:


get_ipython().run_line_magic('reset', '-f')


# In[126]:


get_ipython().run_line_magic('logstart', '')


# In[127]:


get_ipython().run_line_magic('pwd', '')


# In[128]:


get_ipython().run_line_magic('env', '')


# In[129]:


get_ipython().run_line_magic('dirs', '')


# In[130]:


get_ipython().run_line_magic('ls', '')


# In[132]:


get_ipython().run_line_magic('alias', 'll ls -l')


# In[133]:


ll /usr


# ### Indexing and Slicing

# In[142]:


a=np.empty((2,3))


# In[153]:


arr =np.array([(3,4,5),(6,7,8)], dtype=np.int16)
# Alter datatype while making variables


# In[56]:


arr.dtype
arr[1][2]


# In[152]:


# If all element in a particalr row, I call the row number
arr[1]
# A specific row number and a column number
arr[1][2] # or arr[1,2]

# Altering values
arr[0,1] = 7
arr
# Starting from a row or column till the end
arr[1:,1:]


# In[154]:


#Altering set of values together
arr[1:,1:] = 20
arr


# **An important first distinction from lists is that array slices are views on the original array. This means that
# the data is not copied, and any modifications to the view will be reflected in the source
# array:**

# In[155]:


# Capture all staring from Row 0 to Row 1

arr_obtained = arr[0:2]
arr_old = arr[0:2].copy()
arr_obtained[:] = 700
arr[0:2] = arr_old
arr

#arr altered badly, but you can copy before doing the alteration, using "*.copy()"


# In[149]:


arr * arr


# In[38]:


arr.dtype


# In[59]:


arred = arr[0:,1:]


# In[60]:


arred[1,0]


# In[154]:


arr[1][0]


# In[33]:


import time

start_time = time.time()
my_list = []
for var in range(1,5000):
     my_list.append(var)
print(time.time()-start_time)

start_time = time.time()
list_2 = [x for x in range(1,5000)]
print(time.time() - start_time)


# ### Boolean Indexing

# In[70]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
bob_name= names == 'Bob'
joe_name = names == 'Joe'
print(bob_name)
print(joe_name)

fine_data = np.arange(1,40). 


# In[71]:


bob_name | joe_name


# In[72]:


bob_name & joe_name


# In[73]:


meter


# ## Fancy Handling

# In[77]:


my_data = np.arange(20).reshape(4,5)
my_data


# In[84]:


my_data[[1, 3],[3,3]]
# Gets all data for row 1, column 1, and row 3, column 3


# ## Transpose

# In[85]:


data_transpose = my_data.T
data_transpose


# ## Dot Product

# In[101]:


data_one = np.arange(20).reshape(4,5)
data_three = np.arange(20).reshape(4,5)
data_two = np.linspace(5,20,20).reshape(5,4)
dot_data = np.dot(data_one, data_three)
# or data_one.dot(data_two)
print(dot_data)


# In[114]:


print(np.sqrt(data_one))


# In[98]:


print(data_two)


# In[100]:


arr = np.random.randn(6, 3)
arr


# In[113]:


arred = arr.swapaxes(1,0)
#Swaps the axes, just liuke Transpose
arred


# ### A universal function, or ** ufunc **, is a function that performs elementwise operations on
# ### data in ndarrays

# In[116]:


np.sqrt(data_two)
#Gives the squareroot of every data in the array data_two


# In[119]:


np.minimum(data_one, data_two.T)
# Vectorized value returned, having comparing the 2 arrays element-wise


# ### Other ufuncs include ``` np.sqare(), np.exp(), np.floor(), np.isnan(), np.sign() ``` and so on

# ## Data Processing using np Array

# In[164]:


points = np.arange(1,20,0.2)

np.shape(points)


# In[161]:


#Turning a 1 Dimensional array to 2 Dimensional Matrices
new_points = np.meshgrid(points, points)
#Or even 2 2 dimentional matrcis
x_points, y_points =  np.meshgrid(points, points)
np.shape(x_points)


# In[159]:


y_points


# In[165]:


z_points = np.sqrt(x_points**2 + y_points**2)
z_points


# ### Suppose you had a matrix of randomly generated data and you wanted to replace all positive values with 2 and all negative values with -2. This is very easy to do with np.where:

# In[177]:


arr = np.linspace(2,5, 20)-3
arr


# In[179]:


np.where(arr < 0, -2, 2)

# (Condition, Action for Validity,InAction for Invalidity)


# In[180]:


np.where(arr > 0, 2, arr) # set only positive values to 2


# In[ ]:


# Can convert to nexted loop or have more than a condition
np.where(cond1 & cond2, 0,
np.where(cond1, 1,
np.where(cond2, 2, 3)))


# ## Mathematical and Statistical Methods
# 
# - Mean
# > np.mean(arr)
# or
# > arr.mean()
#   - Mean of each row or column based
#   **arr.mean(axis=1)

# In[183]:


arr = np.random.randn(3,4)
arr


# In[184]:


arr.mean(axis=1)
# gives me mean of each row, I should have 3 mean values


# In[185]:


arr.mean(axis=0)
# Based on Column


# In[186]:


arr.sum()
# Sum of all elements


# In[187]:


arr.sum(1) 
# Summ all element, based on row


# In[189]:


bool_arr = np.array([False, True, False])


# In[190]:


bool_arr.any()
# Asking if any element is True


# In[191]:


bool_arr.all()
#Asking if all is True


# ### Sorting

# In[194]:


#Based on row
arr = np.random.randn(3,4)
arr


# In[197]:


arr.sort(axis = 1)
arr
#Arring the elements in the row in increasing order


# In[198]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
np.unique(names)


# **unique(x)** - Compute the sorted, unique elements in x
# 
# **intersect1d(x, y)** -  Compute the sorted, common elements in x and y
# 
# **union1d(x, y)** - Compute the sorted union of elements
# 
# **in1d(x, y)** - Compute a boolean array indicating whether each element of x is contained in y
# 
# **setdiff1d(x, y)** - Set difference, elements in x that are not in y
# 
# **setxor1d(x, y)** - Set symmetric differences; elements that are in either of the arrays, but not both

# In[204]:


# lOAD AND SAVE FILES USIING NUMPY, loadtxt and savetxt
meter_data = np.savetxt('dummy.csv',arr, delimiter =',')


# In[202]:


meter_data = np.loadtxt('dummy.txt', delimiter = ',')


# In[203]:


meter_data


# In[212]:


# Inverse of a matrics
from numpy.linalg import inv
arr = np.random.randn(5,5)
inv(arr.T)


# In[215]:


np.printoptions(precision=2, suppress =True)


# In[216]:


arr.dot(inv(arr.T))


# ## Exercises

# In[219]:


arr = np.zeros(10)
arr[:] =5


# In[220]:


arr


# In[221]:


np.arange(10,51)


# In[222]:


np.arange(10,51,2)


# In[223]:


np.arange(0,9).reshape(3,3)


# In[225]:


np.identity(3, dtype=np.int16)


# In[243]:


np.linspace(0,1,20,)


# In[249]:


arr = np.arange(1,26).reshape(5,5)
arr


# In[250]:


arr[2:,1:]


# In[252]:


arr[3,4]


# In[262]:


arr[:, :1].T


# In[256]:


arr[4]


# In[257]:


arr[3:]


# In[259]:


arr.sum()


# In[260]:


arr.std()


# In[261]:


arr.sum(axis=0)


# In[ ]:




