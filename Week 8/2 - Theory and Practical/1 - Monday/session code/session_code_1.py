# User Defined Functions
def greet(user_name):
    print(f"Hello {user_name}!")


# Getting user input
user_input = input("Enter your name: ")

# greet() function calls
greet(user_input)
greet("Obi-wan")
greet("Pluto")

# Parameters and arguments
def add(x, y):      # these are your parameters
    return x + y


# function call, the user values will be arguments
result_of_add_function = add(50, 3)     # 50 and 3 are our arguments

# Return and Print
# greet("Serge")      # displays result but does not store it
# result_of_add_function = add(50, 3)  # return the results to variable

# print(result_of_add_function)


# Docstrings
def subtract(x, y):
    """
    subtract two numbers

    parameters:
    - x: first number
    - y: second number

    Returns:
    The difference of x and y
    """
    print(f"Result of {x} - {y} = {x - y}")
    return x - y

# subtract function call
subtract(40, 3)
result_of_subtraction = subtract(50, 2)
print(result_of_subtraction * 5)