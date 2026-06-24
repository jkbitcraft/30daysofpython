#Day 6

#Exercises: Level 1
#1-5
empty_tup = ()

brothers = ("Eric", "Andrew", "Michael")
sisters = ("Eve", "Angie", "Margaret")

siblings = brothers + sisters 
print(siblings)

print(len(siblings))

parents = ("Father", "Mother")
family_members = parents + siblings 
print(family_members)

#Exercises: Level 2
#1
a, b, c, d, e, f, g, h = family_members 

#2-3
fruits = ("Apples", "Oranges", "Kiwi")
vegetables = ("Carrot", "Kale", "Lettuce")
animal_products = ("Eggs", "Milk", "Cheese")
food_stuff_tp = fruits + vegetables + animal_products

food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

#4 - cannot delete from tuple 
n = len(food_stuff_lt)
print(food_stuff_lt[n//2])

#5
first_three = food_stuff_lt[0:3]
last_three = food_stuff_lt[-4:-1]
print(first_three)
print(last_three)

#6
del food_stuff_tp
# print(food_stuff_tp) muted. check to see if food_stuff_tp was still there

#7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)