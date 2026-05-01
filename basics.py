"""
This is a multi line comment
"""

name = "HK"
age = 28
is_student = False
first_name = "Hari"
# This is a test comment

from typing import Final

PI: Final = 3.14
PI = "121"
cir_val = PI + 4**2
print(cir_val)
8 + 9

# Strings
greetings = "Hello Good eve"

# Long strings
my_long_string = """
This is a long string that spans multiple lines.
It can contain line breaks and special characters.
"""
print(my_long_string)

first_name = "Hari"
last_name = "Kumar"
full_name = first_name + " " + last_name
print(full_name)

long_dash = "-" * 50
print(long_dash)
print(full_name)
print(long_dash)

len(full_name)
len(long_dash)

is_logged_in = True

age = 16
can_vote = age >= 18
print(can_vote)

15**5

## Logical Operator

age = 25
has_license = True
drunk = True

# And - both must be true

can_drive = age >= 16 and has_license and not drunk

print(can_drive)

child_age = 8

is_teenager = not (child_age <= 16)
print(is_teenager)

score = 94
score %= 6
score

name = " Hari Krishnan GTV "
str = f".   Hello, {name} Good Morning! How can i help.     "
removed_whitespace = name.strip()
print(removed_whitespace)

"GTV" in name

name.count("h")

temperature = 50
if temperature > 100:
    print("Its Hot....")
elif temperature >= 50:
    print("Its moderate")
else:
    print("Its nice!!")

temp = 35
if temp > 25:
    print("Its Hot")
if temp > 30:
    print("Its too hot")
else:
    print("Cool...")


score = 85

if score > 95:
    print("O Grade")
elif score > 85:
    print("A+ Grade")
elif score > 75:
    print("A Grade")
elif score > 65:
    print("B Grade")
else:
    print("C grade")

age = 20
day = "Sunday"
has_license = True
if age >= 16 and has_license:
    print("Eligible to Drive")

if "Sunday" in day or "Saturday" in day:
    print("Weekend....!")
if not age <= 18:
    print("MON")

has_ticket = False
age = 25

if has_ticket:
    if age >= 18:
        print("Enjoy the movie")
    else:
        print("Not allowed")
else:
    print("Get a ticket")

for i in range(5):
    print(i)

for i in range(24, 1, -2):
    print(i)

i = 1
while i <= 5:
    print("*")
    i += 1

while True:
    print("Execute Once")
    break

f_name = "Krish"
has_license = True
my_list = [1, "HK", f_name, f_name, has_license, False]

name = my_list[1]
fname = my_list[2]
backward = my_list[-1]
hasLic = my_list[-2]

for item in my_list:
    print(item)

name_slice = my_list[1:3]
rev_slice = my_list[-1:-3:-1]

my_list[1] = "HariKrish"
my_list.append(25)

my_list.remove("Krish")  # Removes first occurrence of value.
my_list.insert(6, "This is 6")  # Insert object before index
my_list.insert(26, "This is 26")
# If we give a index that is not in the list, it will simply append to the end

my_list.pop()
del my_list[5]  # delete an element from index

my_list.count(1)
len(my_list)
cp_list = my_list.copy()
cp_list.reverse()

cp_list.index("Krish")  # Return first index of value.

empty_dict = {}
my_dict = {"name": "HK", "age": 25, "dob": 1998, "nation": "IND"}

cre_dict = dict(math=95, eng=90, sci=98)

my_dict["dob"]
my_dict["name"]

my_dict["name"] = "hari"
my_dict["has_license"] = True

del my_dict["nation"]

my_dict.get("age")
my_dict.get(
    "mstatus", "UnMarried"
)  # Return the value for key if key is in the dictionary, else default.
dict_items = my_dict.items()


# Update multiple values
my_dict.update({"age": "27", "job": "SWE"})

# Nested Dict

students = {
    "hari": {"name": "HK", "age": "27", "dob": "1999"},
    "ak": {"name": "Ak", "age": "26", "dob": "1999"},
    "section": "B-Tech",
    "rollNo": 160213,
    "projInfo": {
        "name": "ML Weather Forecasting",
        "types": {"miniProject": "yes", "grade": "O", "paperPublished": True},
    },
}
print(students["hari"]["dob"])
students["projInfo"]["types"]["paperPublished"]
proj_type = "miniProject"
students["projInfo"]["types"][proj_type]

students["projInfo"]["types"].pop(proj_type)

dict_key = students.keys()
dict_values = students.values()
dict_items = students.items()

for key in dict_key:
    print(f"Keys: {key}")

for val in dict_values:
    print(f"Values: {val}")

for key, val in dict_items:
    print(f"Key: {key} and this is value {val}")

tup_ex = (1, 2, 3)

color_tuple = ("Red", "Green", "Blue", "Orange", "Yellow", "Purple")

nes_tuple = (((0, 1), (0, 2)), ((1, 1), (1, 2)))

color_tuple[0] = "Orange"

color_tuple[0:4:2]
color_tuple[::1]
color_tuple[-1:-4:-1]
color_tuple[::-2]

nes_tuple[0][0]


# Unpacking Tuple

r, g, b, o, y, p = color_tuple

x1, x2 = nes_tuple

dict_tup = {
    (0, 0): "11224.21",
    (0, 1): "13532.22",
    (1, 0): "24141.21",
    (1, 1): "09828.21",
}
dict_tup[(0, 0)]
dict_tup.get((1, 1))
dict_tup.keys()
dict_tup.values()

dict_sam = dict({"name": "JK", "age": 35})

# Sets

empty_set = set()

# We can also create sets with just { }

numbers = {1, 2, 3, 4, 5}

fruits = set(["apple", "banana", "orange"])

color_set = set({"red", "blue", "green", "purple"})

# It will remove duplicate automatically
scores = [85, 90, 85, 100, 90]

remove_dup = set(scores)

color_set.add("yellow")
fruits.add("mango")
fruits.discard("banana")

# This will throw error if element not found
fruits.remove("pine")


### Functions:

# Defining Functions:


def greet():
    add = 56 + 4
    print("Welcome to AI Eng Roadmap")
    print(f"Result {add}")


greet()

temperature = 62


def check_weather():
    if temperature > 56:
        print("Too Hot")
    elif temperature > 60:
        print("Very Hot")
    else:
        print("Good Chil!!")


check_weather()

## Scope of Variables:

# Local:


def calculat_price():
    price = 100
    tax = price * 0.1
    print(f"Total {price + tax}")


# Global Variable

gst = 0.05  # 5%


def calculate_gst():
    tot_price = 250
    tax = 250 * gst
    print(f"Total {tot_price + tax}")


# Modifying global variable inside function
def calc_gst():
    tot_price = 500
    global gst
    gst = 0.09
    tax = tot_price * gst
    print(f"Total: {tot_price + tax}")


calculat_price()
calculate_gst()
calc_gst()

## Functions with Parameters:


def introduce(f_name, l_name):
    print(f"Hello {f_name}_{l_name} Welcome")


introduce("Hari Krishnan", "GTV")

# We can also pass fn params like below
introduce(f_name="Krish", l_name="GTV")

# Order doens't matter if you use this approach
introduce(l_name="GTV", f_name="Krish")

# Default parameter


def full_name(f_name="John", last_name="Wick"):
    print(f"Full name is {f_name} {last_name}")


full_name()

# Multiple params:


def calc_total(price, tax_rat, discount):
    tax = price * tax_rat
    total = (price + tax) - discount
    print(f"Total price of purchase is: {total}")


# Order matters in params
calc_total(500, 0.05, 10)

# Returning values from function


def add_numbers(num1, num2):
    return num1 + num2


result = add_numbers(34, 43)
print(result)


def calculate_area(width, height):
    area = width * height
    return area


room_area = calculate_area(101, 25)
print(f"Room size is {room_area}")


def double_num(number):
    return number * 2


# Store in Variables
double_number = double_num(99)

# Used as experssion
total = double_num(87) + double_num(34)

# Use in condition
if total > 100:
    print("This number is big")
else:
    print("The number is small")

if double_num(7) > 10:
    print("DoubleNum of 7 is Bigger")

# Returning Multiple Values


def mul_list(numbers):
    double_num = []
    for num in numbers:
        double_num.append(num * 100)
    return double_num


mul_list([1, 2, 3, 4, 5, 6])


# Returning multiple values as tuples
def get_min_max(numbers):
    return min(numbers), max(numbers)


min_num, max_num = get_min_max([12, 44, 12, 90, 10])

user_info = {"name": "HK", "age": "27", "job": "SWE"}


def add_company(comp):
    user_info["Company"] = comp
    return user_info


updated_info = add_company("Comcast")

## Packages:

import math

from math import sqrt, pi

math.pow(2, 19)
pi
sqrt(16)

import random

random_num = random.randint(1, 100)  # Gives a random num of 1 to 100

fruit_ran = ["apple", "mango", "pineapple", "pumpkin", "grapes"]
random.choice(fruit_ran)

tup_ran = ("red", "green", "blue", "yellow")

random.choice(tup_ran)

dict_rand = [
    {"name": "HK", "age": "27", "job": "SWE", "dob": "1998"},
    {"name": "AK", "age": "26", "job": "No", "dob": "1999"},
    {"name": "JK", "age": "28", "job": "SP", "dob": "1997"},
]

random.choice(dict_rand)

from math import sqrt as square, pi as pie

square(16)
pie

from datetime import datetime, timedelta

now = datetime.now()

cus_date = datetime(2025, 11, 14, 10, 30)

now.year
now.month
now.day
now.hour
now.minute

formatted = now.strftime("%Y-%m-%d %H:%M:%S")

str_date = "Tue Mar 24 2026 11:44:01 GMT+0530"

cleaned_dt = str_date.replace("GMT", "")

conv_date = now.strptime(cleaned_dt, "%a %b %d %Y %H:%M:%S %z")

# We can use Parser to parse

from dateutil import parser

dt = parser.parse("Tue Mar 24 2026 11:44:01 GMT+0530")
dt

from datetime import datetime, timedelta

now = datetime.now()

now

future = now + timedelta(5)

past = now - timedelta(4)

d1 = datetime(2026, 3, 20) - datetime(2026, 3, 14)
d1.days

import time

ts = time.time()
time.sleep(5)

import calendar

tz = calendar.month(2026, 4)

import os

current_dir = os.getcwd()

# JSON package

import json

j_data = {"name": "Hk", "age": "27", "job": "SWE"}

json_str = json.dumps(j_data)

data_load = json.loads(json_str)

with open("data.json", "w") as f:
    json.dump(j_data, f)

with open("data.json", "r") as fr:
    data_r = json.load(fr)

print(json.dump())


# List comprehension:
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# I want 'n' for each 'n' in nums
my_list = []
for n in nums:
    my_list.append(n)
print(my_list)

# List comprehension
my_list = [n for n in nums]

# I want 'n*n' for each 'n' in nums

my_list = [n1 * n1 for n1 in nums]

num1 = "100"
num2 = "200"

resNum = int(num1)

# Lambda Function

# With one params
add_1 = lambda x: x + 1

add_1(10)


# With multiple params

mul_1 = lambda x, y: x * y

mul_1(10, 10)


# Map function
my_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def square(x):
    return x * x


square_res = list(map(lambda x: x * 2, my_nums))

evns_num = list(filter(lambda x: x % 2 == 0, my_nums))

# SORT Function:

values = [(1, "a", "world"), (2, "a", "hello"), (3, "c", "ok")]

sorted_val = sorted(values, key=lambda x: x[1] + x[2])

len(values)

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Using reduce to sum the list without initializer

sum_numbers = reduce(lambda acc, x: acc + x, numbers)
# Initially -> acc = 1 and x = 2

# Using reduce to find max num

max_num = reduce(lambda acc, x: acc if acc > x else x, numbers)


# Ternary

hk_info = {"name": "HK", "age": "31", "dob": "1998", "hobby": "code"}

eligible_for_uk_visa = (
    "Eligible"
    if int(hk_info["age"]) < 30
    else "Eligible"
    if hk_info["hobby"] == "code"
    else "He is Not Eligible"
)

# Dict comprehension
fancy_comp = {x: (lambda x: x * x)(x) for x in range(5)}


fancY_redue = {"x": reduce(lambda acc, x: acc * x, numbers)}

resul_odd_eve = ["Even" if num % 2 == 0 else "Odd" for num in numbers]

# Zipped
a = (1, 2, 3)
b = ("a", "b", "c")

zipped = tuple(zip(a, b))


# Comprehension Continued

user_list = [1, 2, 3, 4, 5]
final_u_list = list(map(lambda x: x * x, user_list))

odd_even_list1 = list(map(lambda x: "Even" if x % 2 == 0 else "Odd", user_list))

even_list = [n for n in numbers if n % 2 == 0]

# we want an item 'n' but for each item in numbers do the mod % 2 == 0 and append the result and return once iteration done

fil_even_11 = [filter(lambda num: num % 2 == 0, numbers)]


alph_1 = "abcd"

abc_o1 = [(a, n) for a in alph_1 for n in range(4)]

num_129 = 1234

for n in alph_1:
    print(n)
sample_129 = [n for n in num_129]

# Dictionary comprehension

names_mcu = ["Bruce", "Tony", "Peter", "Logan", "Clark"]
heroes_mcu = ["Batman", "Iron Man", "Spider Man", "X-men", "SuperMan"]

zip_heroes = tuple(zip(names_mcu, heroes_mcu))

zip_heroes_dict = {name: hero for name, hero in zip_heroes}

# Add some restrction (modify) by removing Clark

zip_heroes_dict = {name: hero for name, hero in zip_heroes if name != "Clark"}

dup_num24 = [1, 2, 2, 3, 4, 5, 5, 6, 6, 6, 7, 8, 8, 9, 10, 11, 11]

# Before Comprehension
dump_set = set()
for s in dup_num24:
    dump_set.add(s)

# After Set Comprehension
dump_set = {s for s in dup_num24}

pairs = [(1, 3), (2, 1), (4, 2)]

sorted(pairs, key=lambda x: x[1])

pairs[0][1]

# Generators


def square_number(nums):
    sqrted = []
    for i in nums:
        sqrted.append(i * i)
    return sqrted


square_number(range(1, 5))


# Converted that fn to Generator


def gen_square_number(nums):
    for i in nums:
        yield (i * i)


my_gen_resp = gen_square_number(range(1, 5))

next(my_gen_resp)
next(my_gen_resp)
next(my_gen_resp)
next(my_gen_resp)


for num in my_gen_resp:
    print(num)

# Convert the Generator fn to List Comprehension

my_gen_resp_2 = [x1 * x1 for x1 in range(1, 6)]

# Convert the above into Generator List Comprehension

my_gen_resp_2 = (x1 * x1 for x1 in range(1, 6))

# Then we can convert that generator to List for further use

list(my_gen_resp_2)

# Performance calculation for Generator
import memory_profiler
import time
import random

names = ["John", "Corey", "Hari", "Adam", "Steve", "Rick", "Thomas"]
majors = ["Math", "Engineering", "Math&Eng", "CompSci", "Arts", "Business"]

print(f"Memory (Before): Mb {memory_profiler.memory_usage()}")


def people_list(nums):
    result = []
    for n in range(nums):
        ppl_list = {
            "id": n,
            "name": random.choice(names),
            "job_major": random.choice(majors),
        }
    return result.append(ppl_list)


def people_list_generator(nums):
    for n in range(nums):
        ppl_list = {
            "id": n,
            "name": random.choice(names),
            "job_major": random.choice(majors),
        }
    yield (ppl_list)


# Normal function
t1 = time.perf_counter()
my_ppl_list = people_list(10000000)
t2 = time.perf_counter()

# Generator
t1 = time.perf_counter()
my_ppl_list = people_list_generator(100000000)
t2 = time.perf_counter()

print(f"Memory (After): Mb {memory_profiler.memory_usage()}")
print(f"Took seconds {round(t2 - t1)}")


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

gen_z_list = (n * n for n in nums)

for i in gen_z_list:
    print(i)


# F String format

f"{'Hi':<5}"
f"{'Hi':*<10}"
f"{'Hi':*>10}"
f"{'Hi':*^10}"

f"{1000000:,}"
f"{12344.567:,.2f}"

f"{0.28:.1%}"
f"{0.256:.2%}"

f"{1234:.2e}"
f"{5:03}"

x = 10
print(f"{x=}")


print(list(zip(range(3))))

print(10 / 0)

## Try Except

try:
    print(10 / 100)
except Exception as e:
    print(f"Hi There this is an error {e}")
else:
    print("The number divided")
finally:
    print("This is finally")
