#!/usr/bin/env python
# coding: utf-8

# ## Loops in Python
# > #### For and While
# 
# 

# ### For- Loop
# 
# This is used to iterate over a sequence which may be **a List, a tuple, a dictionary, a set, or a string**
# 
# _With for loop , you can perform a block of statement over a given sequence_
# > `for each_element in sequence:`
#         >> `block of statements`
#        
# **Always take note of the indentation**

# #### Examples
# ##### **ACTIVITIES**
# - Print each score
# - Reduce each score using 0.8
# - store reduced values into a new variable(list) called new_scores
# - Find the average of the score
# - Store average value into variable called avg_score
# - Any score less than 50 should be removed from the new list 

# In[20]:


scores_of_students = [34,56,88,90,34,67]
new_scores = []
total = 0

score_length = len(scores_of_students)
for each_score in scores_of_students:
    print(each_score)
    new_scores.append(each_score*0.8)
    total = total + each_score
#print(scores_of_students)
print("Created Scores")
print(new_scores)

avg_score = total / length
#print(total)
#print(avg_score)

for new_each_score in new_scores:
    if float(new_each_score) < 50.0:
        new_scores.remove(new_each_score)

print("refined Scores")
print(new_scores)


# #### Introduction to range
# 
# ###### ACTIVITIES
# - What is range
# > `range(start, end, increment)`
# - Print out an example using range
# - Apply range to a for loop

# In[25]:



for each_value in range(1,20,2):
    print(each_value, end=",")


# #### Deeper in **for** loop
# ##### ACTIVITIES
# - Iterate over other sequential data types (string, tuple and dictionary)
# - For the dictionary print the following
#     > - The Keys
#     > - The Values
#     > - The Sum of all the values
# - Introduce us to **break** and **continue**

# In[32]:


fav_fruit = "pineapple"
fav_fruits = ("Banana", "Apple", "Orange", "Guava")
fav_fruits_dict = {"Banana": 5, "Apple": 2, "Orange": 7, "Guava": 6}
for each_fruit in fav_fruits_dict:
    sumo += fav_fruits_dict[each_fruit]
print(sumo)
    


# #### Break and Continue
# > Use the List of scores above
# 
# ##### ACTIVITIES
#  - Explain the concept of break and continue
#  - Excecute example

# In[34]:


scores_of_students = [34,56,88,190,34,67]
for each_score in scores_of_students:
    if each_score > 100:
        print("error in the list")
        break;
    elif each_score > 50:
        print("Score %d is excellent" %each_score)
        continue
    print(each_score)


# #### Nexted Loop
# ##### ACTIVITIES
# - Explain and examples

# In[36]:


fav_fruits = ("Banana", "Apple", "Orange", "Guava")
colors= ('red', 'green','yellow')
for each_fruit in fav_fruits:
    print(each_fruit)
    for color in colors:
        print(color)
    print("Done with inner loop")   
print("Done with outer loop")


# #### Pass
# > Take Note: for loop cannot be empty, hence we use pass

# In[37]:


for each_fruit in fav_fruits:
    pass


# ## While - Loops

# In[40]:


a = 1
while a <= 20:
    print(a, end=',')
    a+=1
print("end of loop")


# ### Take Note
# **You can also apply break and continue functionilty to while loop**

# In[43]:


a = 5
while a < 20:   
    a+=1
    print(a, end=',')
    if a == 10:
        print("we have gotten to 10 ooo")
        break


# In[ ]:




