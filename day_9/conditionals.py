#Day 9
#Exercises: Level 1
age = int(input("Enter your age: "))
if age >= 18: 
    print("You are old enough to drive")
else:
    print(f"You need {18-age} more years to learn to drive.")

my_age = 20
your_age = int(input("Enter your age: "))
if my_age > your_age:
    print(f"I am {my_age-your_age} years older than you.")
elif my_age == your_age:
    print("We are the same age.")
else: 
    print(f"You are {your_age-my_age} years older than me.")

num_1 = int(input("Enter number one: "))
num_2 = int(input("Enter number two: "))
if num_1 > num_2:
    print(f"{num_1} is less than {num_2}")
elif num_1 < num_2:
    print(f"{num_1} is greater than {num_2}")
else: 
    print(f"{num_1} is equal to {num_2}")

#Exercises: Level 2
grade = int(input("Mark: "))
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")

autumn = ("September", "October", "November")
winter = ("December", "January", "February")
spring = ("March", "April", "May")
summer = ("June", "July", "August")
month = input("What month is it: ")
if month in autumn:
    print(f"{month} is in Autumn")
elif month in winter:
    print(f"{month} is in Winter")
elif month in spring:
    print(f"{month} is in Spring")
elif month in summer:
    print(f"{month} is in Summer")
else:
    print("You need a valid month")

fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input("Give me a fruit: ")
if new_fruit in fruits:
    print("That fruit already exists in the list")
else:
    fruits.append(new_fruit)
    print(fruits)

#Exercises: Level 3
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
    'street': 'Space street',
    'zipcode': '02210'
}
}

#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if "skills" in person:
    skills = person["skills"]
    middle = len(skills)//2
    print(skills[middle])

#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if "skills" in person: 
    skills = person["skills"]
    if "Python" in skills:
        print("Python")
else:
    print("not found")

#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
skills = input("List your skills: ").split(", ")
skills = set(skills)

if {"React", "Node", "MongoDB"} <= skills:
    print("He is a fullstack developer")
elif {"Node", "Python", "MongoDB"} <= skills:
    print("He is a backend developer")
elif {"React", "JavaScript"} <= skills:
    print("He is a front end developer")
else: 
    print("Unknown title")

#  * If the person is married and if he lives in Finland, print the information in the following format:
name = input("Name: ")
location = input("Location: ")
married_input = (input("Are you married? True or False: "))
married = married_input == "True"

if married == True:
    print(f"{name} lives in {location}. He is married.")
else:
    print(f"{name} lives in {location}. He is not married.")
