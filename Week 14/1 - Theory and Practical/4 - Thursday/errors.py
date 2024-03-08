# try:
#     print("Hello world!")
#     add_nums = "1" + 3
# except TypeError:
#     print("Error has occured!")
# else:
#     print("Numbers added successfully!")
# finally:
#     print("All actions have been completed.")

# Non-specific Error
# try:
#     my_list = [1,2,3,4]
#     my_list[5]
# except Exception:
#     print("An error occured!")
#     raise


# Storing a reference to the exception
# try:
#     my_list = [1,2,3,4]
#     my_list[5]
# except Exception as e:
#     e.add_note("Check index range of num_list")
#     raise

def divide(num1, num2):
    return num1/num2


def divide(num1, num2):
    result = 0
    try:
        result = num1/num2
    except ZeroDivisionError:
        print("You cannot divide by Zero!")
    return result


def divide(num1, num2):
    if num2 == 0:
        print("You cannot divide by Zero!")
        return 0
    else:
        return num1/num2

# num1 = int(input("Please enter a number: "))
# num2 = int(input("Please enter a number: "))
# result = divide(num1, num2)

# print(result)

def validate_num_input(user_input):
    try:
        user_input = int(user_input)
    except ValueError:
        return None
    else:
        return user_input

# names = ["Mike", "Peter", "Michelle", "Tina"]

# print("Please choose a name below: ")
# for i, name in enumerate(names):
#     print(i, name, sep=". ")
# user_choice = input(": ")
# user_choice = validate_num_input(user_choice)

# if isinstance(user_choice, int) and 0 <= user_choice < len(names):
#     print(f"Selected Name: {names[user_choice]}")
# else:
#     print("Invalid choice!")




# file = open("RandomFile.txt", "r")

# file.close()

# with open("RandomFile.txt", "r") as file:

# try:
#     with open("RandomFile.txt", "r") as file: 
#         data = file.readlines()
# except FileNotFoundError:
#     print("Data file missing")


import os

if os.path.exists("RandomFile.txt"):
    with open("RandomFile.txt", "r") as file: 
        data = file.readlines()
else:
    print("Data file missing")


# number = int(input("Please enter a positive number: "))

# def count_down(num):
#     if num < 0:
#         raise ValueError("Only positive number will work")
#     while num != 0:
#         print(num)
#         num -= 1


try:
    num = "1"/0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except TypeError:
    print("Incorrect types for division")



