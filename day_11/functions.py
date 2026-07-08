#Day 11
import math
import keyword

#Exercises: Level 1
#1-15

def add_two_numbers(x,y): 
    return x+y
print(add_two_numbers(5,6))

def area_of_circle(radius):
    return math.pi*radius*radius
print(area_of_circle(6))

def add_all_nums(*args):
    all_nums = 0
    for num in args: 
        if isinstance(num, (int)):
            all_nums+=num
        else: 
            return("Only integers allowed")
    return all_nums
print(add_all_nums(8,9,3,4))

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * (9/5)) + 32
print(convert_celsius_to_fahrenheit(32))

def check_season(month):
    if month.lower() in ["december", "january", "february"]:
        return "Summer"
    elif month.lower() in ["march", "april", "may"]:
        return "Autumn"
    elif month.lower() in ["june", "july", "august"]:
        return "Winter"
    elif month.lower() in ["september", "october", "november"]:
        return "Spring"
    else:
        return "Enter a valid month"
print(check_season("may"))

def calculate_slope(x1,x2,y1,y2):
    return(y2-y1)/(x2-x1)
print(calculate_slope(1,2,3,4))

def solve_quadratic_eqn(a,b,c):
    discriminant = (b**2)-(4*a*c)
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (f"x1 = {x1}, x2 = {x2}")
    elif discriminant == 0: 
        x0 = (-b) / (2*a)
        return (f"x = {x0}")
    elif discriminant < 0: 
        return "No real solutions"
print(solve_quadratic_eqn(1, 2, 1))

def print_list(lst):
    for item in lst:
        print(item)
print_list([1,2,3])

def reverse_list(ary):
    reverse = []
    for item in ary:
        reverse.insert(0, item)
    return reverse
print(reverse_list([1,2,3,4,5,20]))

def capitalize_list_items(lst):
    capped_list = []
    for items in lst:
        capped_list.append(items.capitalize())
    return capped_list
print(capitalize_list_items(['apple', 'banana', 'cherry']))

def add_item(lst, item):
    lst.append(item)
    return lst
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_stuff, 'Meat')) 

def remove_item(lst, item):
    lst.remove(item)
    return lst
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango')) 

def sum_of_numbers(num):
    total = 0
    count = num
    while count > 0:
        total += count
        count -= 1
    return total
print(sum_of_numbers(5))

def sum_of_odds(num):
    total = 0
    count = num
    while count > 0:
        if count % 2 == 1:
            total += count
            
        count -= 1
    return total
print(sum_of_odds(10))

def sum_of_even(num):
    total = 0
    count = num
    while count > 0:
        if count % 2 == 0:
            total += count
            
        count -= 1
    return total
print(sum_of_even(10))   

#Exercises: Level 2
#1
def evens_and_odds(num):
    evens = 0
    odd = 0
    count = num
    while count >= 0:
        if count % 2 == 0:
            evens += 1
        elif count % 2 == 1:
            odd += 1
        count -= 1
    print(f"The number of odds are {odd}.")
    print(f"The number of even are {evens}.")
print(evens_and_odds(100))

def factorial(num):
    total = 1
    count = num
    if count == 0:
        return 1
    while count > 0:
        total *= count
        count -= 1
    return total
print(factorial(5))
    
def is_empty(item):
    return len(item) == 0
print(is_empty([2,2]))

def calculate_mean(lst):
    return sum(lst)/len(lst)
print(calculate_mean([2,3,4,5]))

def calculate_median(lst):
    srt_lst = sorted(lst)
    if len(lst) % 2 == 0:
        mid_left = srt_lst[(len(lst)//2)-1]
        mid_right = srt_lst[len(lst)//2]
        mid = (mid_left+mid_right)/2
        return mid
    elif len(lst) % 2 == 1:
        mid = srt_lst[len(lst)//2]
        return mid
print(calculate_median([2,3,4,5]))

def calculate_mode(lst):
    counts = {}
    for num in lst:
        if num in counts:
            counts[num] = counts[num]+1
        else: 
            counts[num] = 1
    
    mode = lst[0]
    highest_count = 0
    for num in counts:
        if counts[num] > highest_count:
            highest_count = counts[num]
            mode=num
    return mode
print(calculate_mode([1,2,2,3,4,5,5,5]))

def calculate_range(lst): 
    srt_lst = sorted(lst)
    return srt_lst[-1] - srt_lst[0]
print(calculate_range([4,3,2,5,3,9]))

def calculate_variance(lst):
    mean = sum(lst)/len(lst)
    variance = 0
    for num in lst:
        variance += (num-mean)**2
    return variance/len(lst)
print(calculate_variance([2,3,4,5,1,3,5,1]))

def calculate_std(lst):
    mean = sum(lst)/len(lst)
    variance = 0
    for num in lst:
        variance += (num-mean)**2
    return math.sqrt(variance/len(lst))
print(calculate_std([2, 4, 4, 4, 5, 5, 7, 9]))

def greet(name = "Guest"):
    print(f"Hello, {name}!")
greet("H")

def show_args(**kwargs):
    parts = []
    for k, v in kwargs.items():
        parts.append(f"{k}: {v}")
    print("Received: " + ", ".join(parts))
show_args(name="Alice", age=30, city="New York")

#Exercises: Level 3
def is_prime(num):
    if num <= 1: 
        return False
    for i in range(2, num):
        if num% i == 0: 
            return False
    return True
print(is_prime(4))

def unique(lst):
    seen = []
    for item in lst:
        if item in seen:
            return False
        else:
            seen.append(item)
    return True
print(unique([1,2,3,4,5]))

def same_data_type(lst):
    first_type = type(lst[0])
    n = len(lst) -1
    while n >= 0:
        if type(lst[n]) != first_type:
            return False
        n -= 1
    return True
print(same_data_type([1, 2, 3, '4']))

def valid_python_variable(vari):
    if vari.isidentifier() and not keyword.iskeyword(vari):
        return True
    else:
        return False
print(valid_python_variable("1rint"))

from countries_data import countries_data

def most_spoken_languages(countries, n):
    language_count = {}

    for country in countries: 
        for language in country["languages"]: 
            if language in language_count:
                language_count[language] += 1
            else:
                language_count[language] = 1

    sorted_languages = sorted(
        language_count.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return sorted_languages[:n]

print(most_spoken_languages(countries_data, 10))
print(most_spoken_languages(countries_data, 20))

def most_populated_countries(countries, n):
    population_list = []

    for country in countries:
        population_list.append((country["name"], country["population"]))

    sorted_countries = sorted(
        population_list,
        key=lambda item: item[1],
        reverse=True
    )

    return sorted_countries[:n]

print(most_populated_countries(countries_data, 10))
print(most_populated_countries(countries_data, 20))

