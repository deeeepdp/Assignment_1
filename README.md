                # Assignment_1
                Assignment 1 – ML  

                Github link: 

                https://github.com/deeeepdp/Assignment_1

                DEEP PATEL       -     DXP44450@UCMO.EDU

 https://drive.google.com/file/d/1FPReT0Y3dAHuodPnhZZrATkpbalmZwFL/view?usp=sharing

        Question:1

The following is a list of 10 students ages: ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

• Sort the list and find the min and max age

• Add the min age and the max age again to the list

• Find the median age (one middle item or two middle items divided by two)

• Find the average age (sum of all items divided by their number)

• Find the range of the ages (max minus min)



Answer: 

import statistics

#1  : use min() and use max() command.

#Sort the list and find the min and max age 

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24] 

print(sorted(ages))

#max command use

print("maximum number is:", end="")

print(max(ages))

#minimum number use min() command 

print("minimum numebr is:", end="")

print(min(ages)) 

#2 : use insert command

#ages.append(max(ages))

#print(sorted(ages))

ages.insert(-1, max(ages))

print(sorted(ages))

ages.insert(0, min(ages))

print(sorted(ages))

#3  

#find median of this ages so that's why we add (import statistics) in starting : use statistics.median() command .

print(statistics.median(ages))

#4

def Average(ages):

 return sum(ages) / len(ages)
 
#use sum of all ages and divide by that len of ages like 273/12 = 22.75
 
 #print(sum(ages))       #print(len(ages))
 
average = Average(ages)

print("Average list =", round(average, 2))

#5 
• Find the range of the ages (max minus min)  : here find range of ages and which is between 19 and 26.

range_of_data = min(ages),max(ages)

print(range_of_data) 

print(max(ages)-min(ages))

output: 

[19, 19, 20, 22, 24, 24, 24, 25, 25, 26]

maximum number is:26

minimum numebr is:19

[19, 19, 20, 22, 24, 24, 24, 25, 25, 26, 26]

[19, 19, 19, 20, 22, 24, 24, 24, 25, 25, 26, 26]

24.0

Average list = 22.75

(19, 26)

7
 
 

        Question 2

• Create an empty dictionary called dog

#1 here we use {} dictionary and check that type.

dog = {}

print(dog)

print(type(dog))

• Add name, color, breed, legs, age to the dog dictionary

dog = {"name" :"abc", "color":"black", "breeds" : "wsx", "legs":4, "age": 5  }

print(dog)

#2 add name, color ,legs and etc. in that dictionary.

• Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary

#3 Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {

    'first_name':'Dee',
    
    'last_name':'Patel',
    
    'age':22,
    
    'gender': 'M',
    
    'city': 'kansas city',
    
    'country':'USA',
    
    'is_marred':False,
    
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':
    
    {
        'street':'troost street',
        
        'zipcode':'64108'
        
    }
}

print(student)


• Get the length of the student dictionary

#4 use len()

print(len(student))

• Get the value of skills and check the data type, it should be a list

#5 Use type(students [skills])

print(type(student["skills"]))

• Modify the skills values by adding one or two skills # use append 

student['skills'].append('HTML')

print(student)

• Get the dictionary keys as a list  # keys = students.keys() 

keys = student.keys()

print(keys)

• Get the dictionary values as a list    #values = students.values()

values = student.values()
 
print(values)

 
      Question 3

• Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)

• Join brothers and sisters tuples and assign it to siblings

• How many siblings do you have? 

• Modify the siblings tuple and add the name of your father and mother and assign it to family_members

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

 
      Question 4

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

A = {19, 22, 24, 20, 25, 26}

B = {19, 22, 20, 25, 26, 24, 28, 27}

age = [22, 19, 24, 25, 26, 24, 25, 24]

• Find the length of the set it_companies

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

len(it_companies)

• Add 'Twitter' to it_companies

it_companies.add('Twitter')

print(it_companies)

• Insert multiple IT companies at once to the set it_companies

it_companies.update(['SAAS','SnapChat','DELL'])

print(it_companies)

• Remove one of the companies from the set it_companies

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

print(it_companies)

it_companies.remove('IBM')

print(it_companies)

#discard use: set.discard(value)

it_companies.discard('Amazon')

print(it_companies)

• What is the difference between remove and discard

#The main difference is that this discard function leaves a set unchange if element is not in set ,whereas in remove() function will give an error in such condition.

• Join A and B

print(A.union(B))

• Find A intersection B

print(A.intersection(B)) 

• Is A subset of B

A.issubset(B)

• Are A and B disjoint sets

A.isdisjoint(B)

• Join A with B and B with A

print(A.union(B))

print(B.union(A))

• What is the symmetric difference between A and B

A.symmetric_difference(B)

• Delete the sets completely

del A

• Convert the ages to a set and compare the length of the list and the set.

age = [22, 19, 24, 25, 26, 24, 25, 24]

set_convert = set(age)

print(set_convert)

len(set_convert)

 
        Question 5

The radius of a circle is 30 meters.

• Calculate the area of a circle and assign the value to a variable name of area_of_circle

R = 30 

area_of_circle = 3.14 * R * R 

print(area_of_circle)

• Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle

R = 30

circum_of_circle = 2 * 3.14 * R 

print(circum_of_circle)

• Take radius as user input and calculate the area.

from math import pi

r = float(input ("Enter the radius of the circle : "))

print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))


          Question 6

“I am a teacher and I love to inspire and teach people”

• How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

#Use len(set(challenge.split()))

challenge = 'I am a teacher and I love to inspire and teach people'

print(len(set(challenge.split())))


          Question 7

Use a tab escape sequence to get the following lines.

Name Age Country City

Asabeneh 250 Finland Helsinki

#use tab \t 

print('Name\t\tAge\tCountry\t\tCity') 

print('Asabeneh\t250\tFinland\t\tHelsinki')
 


          Question 8

Use the string formatting method to display the following:

radius = 10

area = 3.14 * radius ** 2

“The area of a circle with radius 10 is 314 meters square.”

#radius = 10  

area_of_circle = 3.14 * radius ** 2 

print ("The area of the circle with radius " + str(radius) + " is " + str(3.14 * radius**2) + " meters square. ")


          Question 9

Write a program, which reads weights (lbs.) of N students into a list and convert these weights to kilograms in a separate list using Loop.

N: No of students (Read input from user)

Ex: L1: [150, 155, 145, 148]

Output: [68.03, 70.3, 65.77, 67.13]

#Use for loop and append value 
 
 
 stat = 0.45
 
x = int(input('Enter the number of students :'))

list=[]

for i in range(x):

    list.append(int(input('Enter the weight in lbs:')))
    
output = [stat*i for i in list]

print("The list in kg is:",output)

    Thank You

