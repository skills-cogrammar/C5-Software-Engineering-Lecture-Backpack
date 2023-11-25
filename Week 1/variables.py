"""
Define a greeting variable 

Get name from user through input

Concatenate the user entered name to greeting

print our greeting
"""

greeting = "Hello"

name = input("Please enter your name: ")

full_greeting = f"{greeting} {name}"

print(full_greeting)


"""
Get a number from user through input

multiply user number with 15

print the result
"""

user_number = input("Please enter a number of your choice: ")

user_number = int(user_number)
added_number = user_number + 15

print(added_number)

print("-"*80)