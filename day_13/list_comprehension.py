#Day 13
#Exercises 1-13
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
neg_zero = [n for n in numbers if n <=0]
print(neg_zero)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
comp_list = [n for row in list_of_lists for n in row]
print(comp_list)

list_of_tups = [(i, i**0, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
print(list_of_tups)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
country_abb = [[country.upper(), country[:3].upper(), city.upper()] for [[country, city]] in countries]
print(country_abb)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
country_city = [{'country': country.upper(), 'city': city.upper()} for [[country, city]] in countries]
print(country_city)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_names = [first_name + ' ' + last_name for [[first_name, last_name]] in names]
print(full_names)

slope = lambda x1, x2, y1, y2: (y2-y1)/(x2-x1)
print(slope(2,3,4,5))
y_intercept = lambda m, x, y: y - m * x
print(y_intercept(2,3,6))