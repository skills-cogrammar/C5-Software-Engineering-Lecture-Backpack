from typing import List


# Built-in functions

print("Print is an example of a built-in function.")
input("Please enter a value and press enter: ")

print(abs(-123))
print(max([8,7,4,7,6,5,3,5,7,9]))
print(sum([1,2,3,4,5]))

# User defined functions
# No return or parameters
def print_menu() -> None:
    print("Please select an option below:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Option 4")


def print_menu() -> None:
    options = ["Option1", "Option2", "Option3", "Option4"]
    menu = "Please select an option below: \n"
    for i, option in enumerate(options):
        menu += ". ".join((str(i), option)) + "\n"
    menu += ": "
    print(menu)

print_menu()

# Functions with parameters
def greet_user(name: str, surname: str) -> None:
    print(f"Hi {name} {surname}. Welcome to my application.")


def add_number(num1: int, num2: int) -> None:
    print(f"{num1 + num2 =}")

add_number(1, 2)

# Functions using return

def add_number(num1: int, num2: int) -> int:
    result = num1 + num2
    return result

print(add_number(3, 4))

def calculate_average(numbers: List[int]) -> float:
    return sum(numbers)/len(numbers)



def process_data(user_data: str) -> str:
    new_user = {}
    split_data = user_data.split(",")
    new_user.update(
        username = split_data[0],
        email = split_data[1],
        password= split_data[2]
    )
    return new_user

users = []

user_data = "username,email,password"
users.append(process_data(user_data))


# Funtions using default values
def print_line() -> None:
    print("-"*80)

def print_line(length: int = 80) -> None:
    print("-"*length)

def print_line(symbol: str = "-", length: int = 80) -> None:
    print(symbol*length)


def greet_user(user: str) -> None:
    print(f"Hello {user}, welcome to my app!")

def greet_user(user: str ="Guest") -> None:
    print(f"Hello {user}, welcome to my app!")

def greet_user(user: str =None) -> None:
    if user:
       print(f"Hello {user}, welcome to my app!") 
    else:
        print("There is nobody to greet :(")


# Higher Order Functions

# We can store functions in variables
x = print
x("Hello")

# Parameters function like variables thus we can use functions as argument
def print_something(func) -> None:
    func("Something")

print_something(print)

# Now let use our own functions
def print_user_data(user_data: str, key=None):
    data = f"Name: {user_data[0]}\n"
    data += f"Surname: {user_data[1]}\n"
    data += f"Age: {user_data[2]}"
    if key:
        data = key(data)
    print(data)


user = ["John", "Johnson", 35]
print_user_data(user)
print_user_data(user, str.upper)

def bold(x):
    return f"\033[1m" + x + "\033[0m"

print_user_data(user, bold)