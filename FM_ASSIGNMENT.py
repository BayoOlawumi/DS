#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a Program to add egg to a user input for his favorite food if it is egg.
fav_food = []
new_fav_food = input('enter your favorite food: ')
if new_fav_food =='egg':
    fav_food.append('egg')
print(fav_food)


# In[3]:


#Write a program to collect the name of a student, print “you have a nice name” if the name of the student starts with “A”
name_of_students = input("Enter your name: ")
if name_of_students.startswith("A"):
        print("you have a nice name")


# In[4]:


#Write a program that accepts the score of a student, tell the student his grade following the grade system below:
#•“A” - 70-100
#•“B” – 60-69
#•“C” – 50-59
#•“D” – 45-49
#•“F” – 0 -44
score_of_student = float(input('enter your score: '))
if score_of_student in range(0,45):
    print("your score is F")
elif score_of_student in range(45,50):
    print("your score is D")
elif score_of_student in range(50,60):
    print("your score is C")
elif score_of_student in range(60,70):
    print("your score is B")
elif score_of_student in range(70,101):
    print("your score is A")


# In[5]:


#Write a program to extract and print the acronym from a sentence supplied by a user
user_sentence = input("enter your sentence here: ").title()
word = user_sentence.split(' ')
for letter in word:
    print(letter[0], end='')


# In[6]:


#Write a program to calculate the area or the perimeter of a square.
#Ask the user for the length and also what he wants to calculate
length = float(input('enter your length: '))
what_to_calculate = input('what would you like to calculate? : ')
a = length ** 2
p = length * 4
if what_to_calculate == "area":
    print(a)
elif what_to_calculate == "perimeter":
    print(p)


# In[7]:


#Write and execute a python function that replaces every “a” in a word supplied by the user
user_word = input("enter your word here: ")
new_word = user_word.replace("a","e")
print(new_word)


# In[25]:


#Write a program that asks the user how many Fibonacci numbers to print and then prints that many
no_of_terms = int(input("How many terms? "))
n1 = 0
n2 = 1
count = 0
if no_of_terms <= 0:
   print("Please enter a positive integer")
elif no_of_terms == 1:
   print("Fibonacci sequence: ",no_of_terms,":")
   print(n1)
else:
   print("Fibonacci sequence: ")
   while count < no_of_terms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1


# In[15]:


#Use a for loop to print a triangle like the one below. Allow the user to specify how high the triangle should be.
#*
#*     *
#*      *      *
#*      *      *      *
#*      *      *      *      *
height_of_triangle = int(input('enter a number for the height of triangle: '))
for height in range(1, height_of_triangle+1):
    print("* " * height)


# In[28]:


#Write a program that asks the user for a number and then prints out the factorial of that number

user_number = int(input('enter your number: '))
factorial = 1
if user_number < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif user_number == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,user_number + 1):
       factorial = factorial*i
   print("The factorial of",user_number,"is",factorial)


# In[10]:


#Write a program that asks the user for a number and then prints out the sine, cosine, and tangent 
angle = float(input('enter a number: '))
import math
print(math.sin(angle)) 
print(math.tan(angle))
print(math.cos(angle))


# In[11]:


#Ask the user for a temperature. Then ask them what units, Celsius or Fahrenheit, the temperature is in.
#Your program should convert the temperature to the other unit. The conversions are (F = 9/5C + 32, C = 5/9(F-32))
user_temp = float(input('input the temperature: '))
temp_unit = input("enter fahrenheit or celsius: ")
f = 9/5*user_temp + 32
c = 5/9*(user_temp - 32)
if temp_unit == "fahrenheit":
    print(c)
elif temp_unit == "celsius":
    print(f)
    


# In[12]:


#Ask the user of your program to enter a temperature in Celsius. The program should print a message based on the temperature:
#•If the temperature is less than -273.15, print that the temperature is invalid because it is absolute zero.
#•If it is exactly -273.15, print that the temperature is absolute 0.
#•If the temperature is between -273.15 and 0, print that the temperature is below freezing
#•If it is 0, print that the temperature is at the freezing point.
#•If it is between 0 and 100, print that the temperature is in the normal range.
#•If it is100, print that the temperature is at the boiling point.
#•If it is above 100, print that the temperature is above the boiling point.
celsius_temp = float(input('enter a temperature in celsius: '))
if celsius_temp <-273.15:
    print('temperature is invalid because it is absolute zero.')
if celsius_temp ==-273.15:
    print('temperature is absolute 0')
if celsius_temp ==-273.15 or celsius_temp <=0:
    print('temperature is below freezing')
if celsius_temp ==0:    
    print('temperature is below freezing')
if celsius_temp in range(0,101): 
    print('temperature is in the normal range')
if celsius_temp ==100:    
    print('temperature is at the boiling point')
if celsius_temp >100:    
    print('temperature is above the boiling point.')


# In[13]:


#A store charges $16 per item if you buy less than 11 items.
#If you buy between 11 and 99 items, the cost is $12 per item. If you buy 100 or more items, the cost is $7 per item. 
#Write a program that asks the user how many items they are buying and prints the total cost.
number_of_items_bought = float(input("enter the number of goods bought: "))
price_1 = 16 * number_of_items_bought
if number_of_items_bought <11:
     print(price_1)
price_2 = 12 * number_of_items_bought
if number_of_items_bought in range(12,99):
     print(price_2)
price_3 = 7 * number_of_items_bought
if number_of_items_bought >=100:
     print(price_3)


# In[16]:


#Write a program that extract every alphabetical element in a string.
#E.g if a user enter this: ‘bolu will be 34 by 2030 ’your program should output boluwillbeby.
#(every element except string has been eliminated.)
sentence = input("enter your statement here: ")
for value in sentence:
    if value.isalpha():
        print(value, end="")


# In[18]:


#Write a program that collects the name and age of 30 students. 
#Store the names and ages inside a dictionary.
#Evaluate and print the average of the students’ age.
student_data = {'dwayne':21,'peju':30,'rolu':27,'ayinde':21,'brad':23,'anita':17,
                'lopez':23,'segun':24,'jolu':29,'solu':32,'brown':19,'steve':19,
                'drake':30,'dami':26,'kolu':28,'molu':32,'prestige':32,'taye':25,
               'taylor':29,'youn':30,'polu':27,'zolu':21,'excel':34,'ade':15,
               'swift':24,'bolasie':31,'volu':26,'dolu':30,'klint':32,'sade':15,}
import statistics
average = statistics.mean(student_data.values())
print(average)


# In[ ]:




