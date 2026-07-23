#Day 14

#Exercises: Level 1

#Map - transform every item
#Filter - keep only items that pass a condition
#Reduce - compile all items to one value

#higher order functions - function that takes another function as an argument and/or returns a function (Q1)
# closure - inner function that remembers variables from outer function even after outer func has finished
#decorator - special HOF that wraps another function to add behaviour 

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

from functools import reduce

def square(x): 
    return x ** 2
def is_even(x):
    return x % 2 == 0 
def add(a, b):
    return a + b
print(list(map(square, numbers)))
print(list(filter(is_even, numbers)))
print(reduce(add, numbers))  

for country in countries:
    print(country)

for name in names:
    print(name)

for number in numbers:
    print(number)

#Exercises: Level 2
def upper_convert(str):
    return str.upper()
countries_upper = map(upper_convert, countries)
print(list(countries_upper))

def squared(number):
    return number**2
numbers_squared = map(squared, numbers)
print(list(numbers_squared))

names_upper = map(upper_convert, names)
print(list(names_upper))

def in_word(word): 
    return ('land' in word)
countries_cont = filter(in_word, countries)
print(list(countries_cont))

def max_len(word): 
    return (len(word) == 6)
countries_len = filter(max_len, countries)
print(list(countries_len))

def more_than_six(word): 
    return (len(word) >= 6)
countries_six_plus = filter(more_than_six, countries)
print(list(countries_six_plus))

def contains_e(word):
    return (word.startswith("E"))
countries_e = filter(contains_e, countries)
print(list(countries_e))

result = reduce(
    add,
    filter(
        is_even,
        map(square, numbers)
    )
)
print(result)

lst = ['hello', 42, 'world', 3.14, True, 'python']
def get_string_lists(some_list):
    return list(filter(lambda item: type(item) == str, some_list))
print(get_string_lists(lst))

print(reduce(add,numbers))

def join_countries(lst, country): 
    if country == countries[-1]:
        return lst + ', and ' + country
    return lst + ', ' + country
sentence = reduce(join_countries, countries) + ' are north European countries'
print(sentence)

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent / 'resources'))
from countries_data import countries_data # type: ignore

def categorize_countries(pattern):
    def has_pattern(country):
        return pattern in country['name']
    matches = filter(has_pattern, countries_data)
    return list(map(lambda country:country['name'], matches))
print(categorize_countries('land'))

def countries_by_start_letter(): 
    letter_count = {}
    for country in countries_data:
        first_letter = country['name'][0]
        letter_count[first_letter] = letter_count.get(first_letter, 0) + 1
    return letter_count
print(countries_by_start_letter())

def get_first_ten_countries():
    first_ten = []
    for country in countries_data:
        if len(first_ten) < 10: 
            first_ten.append(country['name'])
    return (first_ten)
print(get_first_ten_countries())

def get_last_ten_countries():
    last_ten = []
    for country in countries_data[-10:]:
        if len(last_ten) < 10: 
            last_ten.append(country['name'])
    return (last_ten)
print(get_last_ten_countries())

#Exercises: Level 3
by_name = sorted(countries_data, key=lambda country: country['name'])
by_capital = sorted(countries_data, key=lambda country: country['capital'])
by_population = sorted(countries_data, key=lambda country: country['population'])
print([c['name'] for c in by_name[:5]])
print([c['name'] for c in by_capital[:5]])
print([c['name'] for c in by_population[:5]])

def most_spoken_languages(countries, n=10):
    language_count = {}
    for country in countries:
        for language in country['languages']:
            language_count[language] = language_count.get(language, 0) + 1
    sorted_languages = sorted(
        language_count.items(),
        key=lambda item: item[1],
        reverse=True
    )
    return sorted_languages[:n]
print(most_spoken_languages(countries_data, 10))

def most_populated_countries(countries, n=10):
    sorted_countries = sorted(
        countries,
        key=lambda country: country['population'],
        reverse=True
    )
    top = sorted_countries[:n]
    return [(country['name'], country['population']) for country in top]
print(most_populated_countries(countries_data, 10))