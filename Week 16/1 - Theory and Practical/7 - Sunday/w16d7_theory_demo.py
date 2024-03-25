# ========= Built-in functions
my_num = input("Provide a number: ")

num_abs = abs(my_num)
print(num_abs)

# ----------------
print(max([8,7,4,7,5,2,20,1,-1]))

print(sum([8,7,4,7,5,2,20,1,-1]))

# ========= Importing Functions
from math import sqrt, gcd

print(sqrt(25))

print(gcd(5,8,8,9,17))

# ========= User defined imports
from my_library import *

print_name()

# ========== User define functions
def print_menu() -> None:
    print("Please select an option below:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Option 4")
    print("5. Option 5")

def print_menu(options) -> None:
    
    menu = "Please select an option below: \n"

    for num, option in enumerate(options):
        menu += ". ".join((str(num), option)) + "\n"
        menu += ":"
        print(menu)

options = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]
print_menu(options)

# ========== User define functions with further parameters
def greet_user(name: str, surname: str) -> None:
    print(f"Hi {name} {surname}. Welcome to the tea party!")

greet_user("John", "Almost-Done")
#------------
def add_number(num1, num2):
    print(f"{num1} + {num2} = {num1 + num2}")

add_number(1, 2,)
# ========== User define functions with further parameters using return
def add_number(num1, num2):
    result = num1 + num2
    return result

num1 = 3
num2 = 4
print(f"{num1} + {num2} = {add_number(num1, num2)}")

# ========== User define functions with further parameters and further functions/methods
def process_data(user_data):
    new_user = {}
    split_data = user_data.split(", ")
    new_user.update(
        username = split_data[0],
        email = split_data[1],
        password = split_data[2]
    )

    return new_user

users = []
user_data = "username, email, password"
users.append(process_data(user_data))

# my_user = process_data(user_data)
# users.append(my_user)

# ========== User define functions with default parameters
def print_line() -> None:
    print("=" * 80)

def print_line(length: int = 80) -> None:
    print("=" * length)

def print_line(symbol: str = "=", length: int = 80) -> None:
    print(symbol * length)

print_line("*", 80)

# ========== Higher Order Functions
# -----------Reduce        
from functools import reduce

def add(x, y):
    return x + y

# Example iterable
numbers = [1, 2, 3, 4, 5]

# Using reduce to sum the elements
result = reduce(add, numbers, 0)
# eg. [1,2,3,4,5,6] = 21

# ----------- Filter
# Example function (filter even numbers)
def is_even(num):
    return num % 2 == 0

# Example iterable
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using filter to get even numbers
result = filter(is_even, numbers)

# eg. [1,2,3,4,5,6] = [2,4,6]

# ----------- Map
# Example function (square each number)
def square(num):
    return num ** 2

# Example iterable
numbers = [1, 2, 3, 4, 5]

# Using map to square each number
result = map(square, numbers)
print(f"result: {result}")      # Iterable object

# To re-use an iterable object, use itertools.tee   ---------
from itertools import tee
# Read original result and make copies
# Remember that result used for tee can't be read again, since read pointer
# is at the end, but we created a copy by overwriting the same variable 
# with read pointer at the start
result_active, result = tee(result) 

squared_numbers = list(result_active)
# eg. [1,2,3,4,5,6] = [1,4,9,16,25,36]

