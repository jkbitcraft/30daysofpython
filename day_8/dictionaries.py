#Day 8
#Exercies 
#1-8
dog = {}

dog["color"] = "Black"
dog["breed"] = "Labrador"
dog["legs"] = True
dog["age"] = 3
print(dog)

students = {"first_name": "", "last_name": "", "gender": None, "age": None, "marital_status": None, "skills": [], "country": "", "city": "", "address": ""}
print(students)

print(len(students))

print(students["skills"])
print(type(students["skills"]))

students["skills"] = ("Python", "Java")
print(students)

keys = students.keys()
print(keys)

values = students.values()
print(values)

print(students.items())

students.pop("marital_status")
print(students)

del students
#print(students)    to check if dict still there