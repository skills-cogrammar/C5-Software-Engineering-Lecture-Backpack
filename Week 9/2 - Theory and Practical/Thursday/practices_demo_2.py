"""
Note that Python has no default functions where the name has an underscore
between words. This will then be a good naming convension to use to indicate
default or newly defined functions.
"""

# ----------  Using the global keyword
global_variable = 10

def my_function():
    global global_variable  # Change the global variable as well
    global_variable = 20
    print("Inside the function:", global_variable)


my_function()
print("Outside the function:", global_variable)

# ----- Better -----
def my_function(global_variable):
    global_variable = 20
    print("Inside the function:", global_variable)
    return global_variable


# Main Code
global_variable = 10

global_variable = my_function(global_variable)

print("Outside the function:", global_variable)

# ----- Bestest -----
def my_function(local_variable):
    local_variable = 20
    print("Inside the function:", local_variable)
    return local_variable


# Main Code
global_variable = 10

global_variable = my_function(global_variable)

print("Outside the function:", global_variable)

# ----------------------------------------------
"""Default Argument Values:
Be careful with default values. They're handy but watch out for 
mutable defaults.
"""
# Remember this?
def appends(number, destination=[]):
    destination.append(number)
    print(destination)
    return destination

appends(1)
appends(4)
appends(100)

# Above: destination is a list and updating lists does not create a new 
# object since it is mutable. Therefor we rather want to use the None default
# and then test if we should initialise the variable with and empty list

def appends(number, destination = None):
    if destination is None:
        destination = []

    destination.append(number)
    print(destination)
    return destination

appends(1)
appends(4)
appends(100)

# Better option for above 3 lines
global_dest = appends(1)
global_dest = appends(4, global_dest)
global_dest = appends(100, global_dest)

# Best solution to replace above 3 lines with below
"""
global_dest = []

## -- loop
user_num = input("Provide a number (-1 when done):")
global_dest = appends(user_num, global_dest)
## -- end loop
"""


# ---- Use print statement to write to file
with open("t.txt", 'w') as text:
    values = ["This will print", "This will also print"]
    print(*values, sep=' ', end="\n", file=None, flush=False)
    print("Go to text file", text)		# This will not work since file is not the second parameter
	# print("Go to text file", file=text)	# This is the correct syntax
    print("no error")

# ---- Greeting Function
def quest_greeting(name, company="Company Y", contact="whiskers@gmail.com"):
    print(f"Hello {name}, welcome to the {company} Log In page")

quest_greeting("John")  # Must provide values for parameters with no default
quest_greeting("John", "Paws n Cart")
quest_greeting("John", contact="whoofff@gmail.com")

# ---- The same principle goes for the .format method
name = "John"
age = 30
city = "London"
occupation = "Engineer"

# Using .format() to create a formatted string
formatted_string = "Hello, my name is {}. I am {} years old and live in {}. " \
                    "I work as an {}.".format(name, age, city, occupation)

formatted_string = "Hello, his name is {0}. {0} is {1} years old and lives in {2}. " \
                    "{0} works as an {3}.".format(name, age, city, occupation)

# Printing the formatted string
print(formatted_string)

# --------- Note the error when leaving out a number
formatted_string = "Hello, his name is {0}. {0} is {1} years old and lives in {2}. " \
                    "{0} works as an {}.".format(name, age, city, occupation)

# Printing the formatted string
print(formatted_string)
# ----------------------------------------------