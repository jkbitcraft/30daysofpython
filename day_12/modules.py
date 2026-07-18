#Day 12
#Exercises: Level 1
import random
import string

def random_user_id():
    characters = string.ascii_letters + string.digits
    result = ''.join(random.choice(characters) for _ in range(6))
    return result
print(random_user_id())

def user_id_gen_by_user():
    length = int(input("Length: "))
    amount = int(input("Amount: "))
    characters = string.ascii_letters + string.digits
    for _ in range(amount):
        result = ''.join(random.choice(characters) for _ in range(length))
        print(result)
user_id_gen_by_user()

def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0,255)
    return (f'rgb({r},{g},{b})')
print(rgb_color_gen())

#Exercises: Level 2
def list_of_hexa_colors(n):
    hexchars = "".join(sorted(set(string.hexdigits.lower())))
    colors = []
    for _ in range(n):
        color = "#" + "".join(random.choice(hexchars) for _ in range(6))
        colors.append(color)
    return colors
print(list_of_hexa_colors(3))

def list_of_rgb_colors(n):
    colors = []
    for _ in range(n):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0,255)
        colors.append(f"rgb({r},{g},{b})")
    return colors
print(list_of_rgb_colors(4))

def generate_colors(color_type, n):
    if color_type == "hexa":
        return list_of_hexa_colors(n)
    elif color_type == "rgb":
        return list_of_rgb_colors(n)
print(generate_colors("hexa", 5))

#Exercises: Level 3
def shuffle_list(lst):
    random.shuffle(lst)
    return lst
print(shuffle_list([1,2,3,4,5]))

def unique_rand_numbers():
    num_arr = []
    n = 7
    while n > 0: 
        x = random.randint(0,9)
        if x not in num_arr:
            num_arr.append(x)
            n -= 1
    return num_arr
print(unique_rand_numbers())