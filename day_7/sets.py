#Day 7
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Exercises: Level 1
#1-5
print(len(it_companies))

it_companies.add("Twitter")
print(it_companies)

it_companies.update(["Company1", "Company2", "Company3"])
print(it_companies)

it_companies.pop()
print(it_companies)

#.remove() = will raise errors. .discard() will not. Use .remove() when you also want a check for the item

#Exercises: Level 2
#1-7
C = A.union(B)
print(C)

print(A.intersection(B))

print(A.issubset(B))

print(B.isdisjoint(A))

print(A.symmetric_difference(B))

del A
del B
#print(A)
#print(B)

#Exercies: Level 3
#1-3
st_age = set(age)
print(st_age)
print(len(age))
print(len(st_age))  #list is longer as there are duplicates

#String - sequence of characters
#List - ordered collection + changable 
#Tuple - ordered collection - changable 
#Set - unordered + unique collection

sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()
unq_words = set(words)
print(unq_words)
print(len(unq_words))