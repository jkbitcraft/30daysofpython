#1
string = ("Thirty" + " " + "Days" + " " + "Of" + " " + "Python"), 
print(string)

#2 
string = ("Coding" + " " + "For" + " " + "All")
print(string)

#3-11
company = "Coding For All"
print(company)
print(len(company))
print(str.upper(company))
print(str.lower(company))
print(str.capitalize(company))
print(str.title(company))
print(str.swapcase(company))
print(company[:6])
print(company.find("Coding"))
print(company.replace("Coding", "Python"))

#12
pcompany = "Python For Everyone"
print(pcompany.replace("Everyone", "All"))

#13
print(company.split(" "))

#14
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(","))

#15-21
print(company[0])
print(company[-1])
print(company[10])
print(pcompany[0:7:11])
print(pcompany[0] + pcompany[7] + pcompany[11])
print(company[0] + company[7] + company[11])
print(company.index("C"))
print(company.index("F"))

#22
xcompany = "Coding For All People"
print(xcompany.rfind("l"))

#23
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index("because"))

#24
rsentence = 'You cannot end a sentence with because because because is a conjunction'
print(rsentence.rfind("because"))

#25-29
ssentence = 'You cannot end a sentence with because because because is a conjunction'
start = ssentence.find("because")
ss_length = ssentence[start:start + len("because because because")]
print(ss_length)
print(ssentence.find("because"))
print(ss_length)
print(xcompany.startswith("Coding"))
print(xcompany.endswith("coding"))

#30
empty_string = '   Coding For All      ' 
print(empty_string.strip(" "))

#31
string_one = "30DaysOfPython"
string_two = "thirty_days_of_python"
print(string_one.isidentifier())
print(string_two.isidentifier()) #This one is True

#32
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(" # ".join(libraries))

#33-34
print("I am enjoying this challenge. \nI just wonder what is next.")
print("Name\t\tAge\tCountry\t\tCity\nAsabeneh\t250\tFinland\t\tHelsinki")

#35
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {int(area)} meters square.")

#36
a = 8
b = 6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")