#!/usr/bin/env python
# coding: utf-8

# Question:1 
# 
# The following is a list of 10 students ages: 
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24] 
# 
# • Sort the list and find the min and max age
# 
# • Add the min age and the max age again to the list 
# 
# • Find the median age (one middle item or two middle items divided by two)
# 
# • Find the average age (sum of all items divided by their number) 
# 
# • Find the range of the ages (max minus min) 

# In[28]:


import statistics

#1 

#Sort the list and find the min and max age 
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24] 
print(sorted(ages))

# maximum number use max() command
print("maximum number is:", end="")
print(max(ages))

# minimum number use min() command 
print("minimum numebr is:", end="")
print(min(ages)) 

#2

#ages.append(max(ages))
#print(sorted(ages))

ages.insert(-1, max(ages))
print(sorted(ages))

ages.insert(0, min(ages))
print(sorted(ages))

#3  

#find median of this ages so that's why we add (import statistics) in starting 
print(statistics.median(ages))

#4

def Average(ages):
    return sum(ages) / len(ages) # use sum of all ages and divide by that len of ages like 273/12 = 22.75
                                 #print(sum(ages))
                                 #print(len(ages))
average = Average(ages)
print("Average list =", round(average, 2))

#5 • Find the range of the ages (max minus min) 
print(ages)
range_of_data = min(ages),max(ages)
print(range_of_data)
print(max(ages)-min(ages))


# Question 2
# 
# 
# • Create an empty dictionary called dog
# 
# • Add name, color, breed, legs, age to the dog dictionary
# 
# • Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address   as keys for the dictionary
# 
# • Get the length of the student dictionary
# 
# • Get the value of skills and check the data type, it should be a list
# 
# • Modify the skills values by adding one or two skills
# 
# • Get the dictionary keys as a list
# 
# • Get the dictionary values as a list

# In[32]:


#1
dog = {}
print(dog)
print(type(dog))

#2
dog = {"name" :"abc", "color":"black", "breeds" : "wsx", "legs":4, "age": 5 ,
      }
print(dog)


# In[6]:


#3 Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name':'Dee',
    'last_name':'Patel',
    'age':23,
    'gender': 'M',
    'city': 'kansas city',
    'country':'USA',
    'is_marred':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'troost street',
        'zipcode':'64108'
    }
}
print(student)


# In[7]:


#4 Get the length of the student dictionary
student = {
    'first_name':'Dee',
    'last_name':'Patel',
    'age':23,
    'gender': 'M',
    'city': 'kansas city',
    'country':'USA',
    'is_marred':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'troost street',
        'zipcode':'64108'
    }
}
print(student)
print(len(student)) # use len for find lenght of dictionary


# In[8]:


#8 Get the value of skills and check the data type,
print(type(student["skills"]))

#5 Modify the skills values by adding one or two skills

student['skills'].append('HTML')
print(student)


# In[9]:


#6 Get the dictionary keys as a list
#dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
#keys = dct.keys()
#print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])
 
student = {
    'first_name':'Dee',
    'last_name':'Patel',
    'age':23,
    'gender': 'M',
    'city': 'kansas city',
    'country':'USA',
    'is_marred':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'troost street',
        'zipcode':'64108'
    }
}
keys = student.keys()
print(keys)


# In[35]:


#7 Get the dictionary values as a list
#dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
#values = dct.values()
#print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])
student = {
    'first_name':'Dee',
    'last_name':'Patel',
    'age':23,
    'gender': 'M',
    'city': 'kansas city',
    'country':'USA',
    'is_marred':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'troost street',
        'zipcode':'64108'
    }
}
values = student.values()
print(values)


# Question 3
# 
# 
# • Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
# 
# • Join brothers and sisters tuples and assign it to siblings
# 
# • How many siblings do you have?
# 
# • Modify the siblings tuple and add the name of your father and mother and assign it to family_members

# In[56]:


#1
brothers = ('Deep','Dev' , 'Nik', 'Nirav')
sisters = ('sivu','ashmi') 
print(brothers)
print(sisters)

#2
siblings = brothers + sisters
print(siblings)

#3 
print(brothers)
print(sisters)
print(siblings)
len(siblings)

#4
siblings = ('Deep','Dev', 'Nik', 'Nirav', 'sivu', 'ashmi')
family = ("KHP","IKP",)
family += siblings
print(family)


# Question 4
# 
# 
# it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# 
# A = {19, 22, 24, 20, 25, 26}
# 
# B = {19, 22, 20, 25, 26, 24, 28, 27}
# 
# age = [22, 19, 24, 25, 26, 24, 25, 24]
# 
# 
# • Find the length of the set it_companies
# 
# • Add 'Twitter' to it_companies
# 
# • Insert multiple IT companies at once to the set it_companies
# 
# • Remove one of the companies from the set it_companies
# 
# • What is the difference between remove and discard
# 
# • Join A and B
# 
# • Find A intersection B
# 
# • Is A subset of B
# 
# • Are A and B disjoint sets
# 
# • Join A with B and B with A
# 
# • What is the symmetric difference between A and B
# 
# • Delete the sets completely
# 
# • Convert the ages to a set and compare the length of the list and the set.

# In[71]:



it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

A = {19, 22, 24, 20, 25, 26}

B = {19, 22, 20, 25, 26, 24, 28, 27}

age = [22, 19, 24, 25, 26, 24, 25, 24]

#1
#Find the length of the set it_companies
#st = {'item1', 'item2', 'item3', 'item4'}
#len(set)
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
len(it_companies)


# In[72]:


#2
#Add 'Twitter' to it_companies
#st = {'item1', 'item2', 'item3', 'item4'}
#st.add('item5')
it_companies.add('Twitter')
print(it_companies)


# In[74]:


#3 
#Insert multiple IT companies at once to the set it_companies
#st = {'item1', 'item2', 'item3', 'item4'}
#st.update(['item5','item6','item7'])
it_companies.update(['SAAS','SnapChat','DELL'])
print(it_companies)


# In[103]:


#4
# Remove one of the companies from the set it_companies
#st = {'item1', 'item2', 'item3', 'item4'}
#st.remove('item2')

#fruits = {'banana', 'orange', 'mango', 'lemon'}
#fruits.pop()
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(it_companies)
it_companies.remove('IBM')
print(it_companies)

#discard use: set.discard(value)
it_companies.discard('Amazon')
print(it_companies)


# In[1]:


#5
#What is the difference between remove and discard?
#The main difference is that this discard function leaves a set unchange if element is not in set ,whereas in remove() function will give an error in such condition.


# In[3]:


#6
#Join A and B
#st1 = {'item1', 'item2', 'item3', 'item4'}
#st2 = {'item5', 'item6', 'item7', 'item8'}
#st3 = st1.union(st2)

A = {19, 22, 24, 20, 25, 26}

B = {19, 22, 20, 25, 26, 24, 28, 27}

print(A.union(B))


# In[4]:


#7
#Find A intersection B
# syntax
#st1 = {'item1', 'item2', 'item3', 'item4'}
#st2 = {'item3', 'item2'}
#st1.intersection(st2)    # {'item3', 'item2'}

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A.intersection(B)) 


# In[5]:


#8
#Is A subset of B
#st1 = {'item1', 'item2', 'item3', 'item4'}
#st2 = {'item2', 'item3'}
#st2.issubset(st1) # True
#st1.issuperset(st2) # True

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
A.issubset(B)


# In[6]:


#9
#Are A and B disjoint sets
#set_a.isdisjoint(set_b)
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
A.isdisjoint(B)


# In[11]:


#10
#Join A with B and B with A
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A.union(B))
print(B.union(A))


# In[12]:


#11
#What is the symmetric difference between A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
A.symmetric_difference(B)


# In[14]:


#12
#delete set
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
del A
print(A) # GOT error means now we dont have any A set.


# In[26]:


#13
#Convert the ages to a set and compare the length of the list and the set.
age = [22, 19, 24, 25, 26, 24, 25, 24]
set_convert = set(age)
print(set_convert)

len(set_convert)


# In[27]:


age = [22, 19, 24, 25, 26, 24, 25, 24]
len(age) 


# Question 5
# 
# The radius of a circle is 30 meters.
# 
# • Calculate the area of a circle and assign the value to a variable name of _area_of_circle_
# 
# • Calculate the circumference of a circle and assign the value to a variable name of _circum_of_circle_
# 
# • Take radius as user input and calculate the area.

# In[28]:


#1
R = 30 
area_of_circle = 3.14 * R * R 
print(area_of_circle)


# In[29]:


#2
R = 30
circum_of_circle = 2 * 3.14 * R 
print(circum_of_circle)


# In[34]:


#3
from math import pi
r = float(input ("Enter the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))


# Question 6
# 
# “I am a teacher and I love to inspire and teach people”
# 
# • How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

# In[2]:


challenge = 'I am a teacher and I love to inspire and teach people'
print(challenge.split())


# In[3]:


challenge = 'I am a teacher and I love to inspire and teach people'
print(len(set(challenge.split())))


# In[7]:


unique_numbers = list(set(challenge))
print(unique_numbers)


# In[10]:


bb=dict(zip(list(challenge),[list(challenge).count(i) for i in list(challenge)]))
print(bb)


# Question 7
# 
# Use a tab escape sequence to get the following lines.
# 
# Name Age Country City
# 
# Asabeneh 250 Finland Helsinki

# In[15]:


print('Name\t\tAge\tCountry\t\tCity') 
print('Asabeneh\t250\tFinland\t\tHelsinki')


# Question 8
# 
# Use the string formatting method to display the following:
# 
# radius = 10
# 
# area = 3.14 * radius ** 2
# 
# “The area of a circle with radius 10 is 314 meters square.”

# In[22]:


radius = 10                                 
area_of_circle = 3.14 * radius ** 2         
print ("The area of the circle with radius " + str(radius) + " is " + str(3.14 * radius**2) + " meters square. ")


# Question 9
# 
# Write a program, which reads weights (lbs.) of N students into a list and convert these weights to kilograms in a separate list using Loop.
# 
# N: No of students (Read input from user)
# 
# Ex: L1: [150, 155, 145, 148]
# 
# Output: [68.03, 70.3, 65.77, 67.13]

# In[3]:


stat = 0.45
x = int(input('Enter the number of students :'))
list=[]
for i in range(x):
    list.append(int(input('Enter the weight in lbs:')))
    
output = [stat*i for i in list]
print("The list in kg is:",output)


# In[ ]:




