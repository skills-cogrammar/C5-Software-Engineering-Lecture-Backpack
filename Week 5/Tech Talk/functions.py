# Built-in functions
print("Hello world!")
input("Please enter your name: ")
len("Hello")
max([1,2,3,4,5])
min([3,4,5,6,7])


# Basic function
def print_greeting():
    print("Welcome to the Tech Talk.")

print_greeting()


# Funtions with parameter
def print_greeting(name):
    print(f"Hello {name}, how are you?")

print_greeting("David")


# Function with mulitple parameters
def print_greeting(name, surname, age):
    print(f"Hello {name} {surname}, how does is feel to be {age} years old?")

print_greeting("Mark", "Nickson", 35)


# Function with default parameters
def print_greeting(name, age, surname=""):
    print(f"Hello {name} {surname}, how does is feel to be {age} years old?")

print_greeting("Michelle", 22)

# Functions that return a value
def sum_of_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

result = sum_of_numbers([2,2,4,3,5,4,7])
print(result)


def manipulate_text(text):
    mid = len(text)//2
    first_half = text[:mid]
    second_half = text[mid:]
    second_half = second_half[::-1]
    return second_half + first_half

print(manipulate_text("Armand"))


# Function with an unknown amount of arguments
def sum_of_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_of_numbers(1,2,3,4,4,6,5,4,3))


# Function with an unknown amount of keyword arguments
def print_greeting(**kwargs):
    print(f"Hello {kwargs['name']}, you are {kwargs['age']} years old"
          + f" and have {kwargs['hair_color']} hair.")

print_greeting(name="Jack", age=30, hair_color="Brown")


# Higher Order Functions
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def get_result(num1, num2, operation):
    return operation(num1, num2)

print(get_result(1, 3, add))
print(get_result(10, 3, subtract))
print(get_result(15, 3, multiply))


# Recursion
def add_numbers(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + add_numbers(numbers[1:])

print(add_numbers([1,2,3,4,5]))


# Importing modules
from math import pow

result = pow(5, 3)
print(result)