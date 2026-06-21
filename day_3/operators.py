import math

#Exercises Day 3

#1-3
age = 300 
height = 202.32
complex = 4+4j

#4
user_base = int(input("Base of triangle: "))
user_height = int(input("Height of triangle: "))
triangle_area = 0.5*user_base*user_height
print(triangle_area)

#5
user_side_a = int(input("Triangle side A: "))
user_side_b = int(input("Triangle side B: "))
user_side_c = int(input("Triangle side C: "))
triangle_perimeter = user_side_a + user_side_b + user_side_c
print(triangle_perimeter)

#6
rec_length = int(input("Rectangle length: "))
rec_width = int(input("Rectangle width: "))
rec_area = rec_length*rec_width
rec_perimeter = rec_length+rec_width
print(rec_area)
print(rec_perimeter)

#7
circle_radius = int(input("Circle radius: "))
circle_area = math.pi*circle_radius*circle_radius
circle_circum = 2*math.pi*circle_radius
print(circle_area)
print(circle_circum)

#8 y=2x-2
m_8 = 2
b_8 = -2
slope_8 = m_8
y_int = (0, b_8)
x_int = (-b_8/m_8, 0)
print("Slope = ", slope_8)
print("X-int = ", x_int)
print("Y-int = ", y_int)

#9 (2,2)(6,10)
slope_9 = (10-2)/(6-2)
euclidean_9 = math.sqrt((6-2)**2+(10-2)**2)
print(slope_9)
print(euclidean_9)

#10 
slope_diff = slope_9 - slope_8
print(slope_diff)

#11
x = -5
y = x**2 + 6*x + 9
print(y)

x = -4
y = x**2 + 6*x + 9
print(y)

x = -3
y = x**2 + 6*x + 9
print(y)

#12
python_len = len("python")
dragon_len = len("dragon")
string_comp = python_len > dragon_len
print(string_comp)

#13
print('on in python' and 'on in dragon')

#14
print('jargon in I hope this course is not full of jargon')

#15
print('on not in dragon' and 'on not in python')

#16
python_len = len("python")
print(type(python_len))
python_len = float(python_len)
print(type(python_len))
python_len = str(python_len)
print(type(python_len))

#17
print(4%2==0) #Check if even by x%2==0

#18
print((7//3)==(int(2.7))) #true

#19
print('10'==10) #false

#20
print(int(9.8)==10) #if 9.8 then False if '9.8' then error

#21
hours = int(input("Enter hours: "))
rate = int(input("Enter rate per hour: "))
weekly = hours*rate
print(f"Your weekly earning is", weekly)

#22 Altered to a countdown as question didn't make sense
years_alive = int(input("Enter number of years you have lived: "))
total_sec = 100*365*24*60*60
seconds_left = total_sec - (years_alive*365*24*60*60)
print(f"You have", seconds_left, "seconds left.")

#23
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")