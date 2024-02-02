"""
Function Decorators:
"""
# -- Example 1 - Decorate a cake
def decorate_it(func):
    # Define the inner function 
    def decoration():
        # Add some functionality to decorate the other function with
        print("I've been decorated!!!")

        # call original function(Remember this will be provided as an argument)
        func()
    # return the inner function
    return decoration

# Define normal function - Decorate the cake with a cherry on top
@decorate_it
def carrot_cake():
    print("I am a carrot cake!")
    
# Decorate the normal function 
print(carrot_cake())

"""
like num = num + 1, now carrot_cake = decorate_it(carrot_cake)
We use the original carrot_cake function and decorate_it and now
we update the carrot_cake function with the updated version.

This will be the same as decorated_carrot_cake = decorate_it(carrot_cake)
and now we print or call the decorated_carrot_cake function with
decorated_carrot_cake()
"""

# -- Example 2
def my_decorator(func):     # func is paramater that receives the function name
    def wrapper():          # wrapper can be any name
        print("It is time to celebrate.")
        func()
        print("Here comes the sparkles.")
    return wrapper

@my_decorator       # Same as say_hello_with_sparkles = my_decorator(say_hello)
def say_hello():
    print("Hello!")

@my_decorator       # Same as say_cheers_while_smiling = my_decorator(say_cheers)
def say_cheers():
    print("Cheers!")

# Using the decorated function
say_hello()
"""
You can also remove @my_decorator above function and the say_hello() and
replace with below by placing it after the function
"""
# say_hello_with_sparkles = my_decorator(say_hello)
# say_hello_with_sparkles()
print()

say_cheers()
"""
You can also remove @my_decorator above function and the say_cheers() and
replace with below by placing it after the function
"""
# say_cheers_while_smiling = my_decorator(say_cheers)
# say_cheers_while_smiling()


# ----- See also time_decorator example lower down

"""
Type Annotations :
"""
def add_numbers(a: int, b:int) -> int:  # return value must be int
    return a + b

# If you want to indicate types like List and Dict
from typing import List, Dict

def process_data(data: List[str]) -> None:
    # Code to process the data
    data.sort()

# Annotations will not give compile or runtime errors, but helps with documentation	
# and some error checking tool extention might point out errors


"""
Docstrings
"""

def calculate_area(radius):
    """
    Calculate the area of a circle.

    :param radius: The radius of the circle.
    :type radius: float
    :return: The area of the circle.
    :rtype: float
    """
    # Code for calculating area

# Doctrings are valuable and can create file documentation by using Sphinx
# Use pip install sphinx to add this 


"""
Block Comments
"""
def complex_algorithm(data):
    # Step 1: Preprocess the data
    processed_data = preprocess(data)

    # Step 2: Apply the main algorithm
    result = apply_algorithm(processed_data)

    return result


"""
Inline Comments
"""
# This is a user-defined function named 'multiply'
def multiply(a, b):
    """
    This function takes two parameters, 'a' and 'b',
    and returns their product.
    """
    result = a * b  # Multiply the values of 'a' and 'b'
    return result   # Return the result
	
# It is important to add comments that adds value and does not just repeat what the code is already saying.

"""
How do we use '*args' and '**kwargs'	- Not reserved words. Can use any name, but this is a convention
"""
# Args allow us to provide a function a variable amount of
# NON-KEYWORD arguments. We use * before the parameter name('args' is conventional).
# *args = variable arguments, ie. name, company, etc
# **kwargs = variable keyword arguments, ie. name="John", company="Company Y"
def triple(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)

triple(1, 2, 3) 
triple(9, 21, 40, 46)


"""
Return types
"""
# -- Example 1
def find_item(item, item_list):
    if item in item_list:
        return True
    else:
        return "Item not in list"
    
# Above example can return a boolean or a string
    
# --- The better option
def find_item(item, item_list):
    return item in item_list

# Above example will always return the type of item


# -- Example 2
def calculate_area(shape, *args):
    if shape == "circle":
        radius = args[0]
        return 3.14 * (radius ** 2)
    elif shape == "rectangle":
        length, width = args
        return length * width 
    else:
        return "Unsupported shape" # Here the return type is inconsistent

# For Example - Duplicate code:
circle_area = calculate_area("circle", 5)
print(f"The area of the circle is: {circle_area}")

rectangle_area = calculate_area("rectangle", 5, 4)
print(f"The area of the rectangle is: {rectangle_area}")

# ---- The better way to do this would be as follows:
def calculate_area(shape, *args):
    if shape == "circle":
        radius = args[0]
        return 3.14 * (radius ** 2)
    elif shape == "rectangle":
        length, width = args
        return length * width
    else:
        raise ValueError("Unsupported shape")

# Now we'll raise an error if the types are unsupported instead:
try:
    triangle_area = calculate_area("triangle", 2, 4 ,6)
except ValueError as e:
    print(f"Error: {e}")


"""
Building Custom decorators: 
"""
import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        # *args = variable arguments, ie. name, company, etc
        # **kwargs = variable keyword arguments, ie. name="John", company="Company Y"
        start_time = time.time()
        result = func(*args, **kwargs)
        """ 
        result above is a new variable and will take on the type of whatever
        the function returns.
        Wrapper then calls the original function (function name in variable func) 
		with any provided arguments and keyword arguments.
        """
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds to run.")
        return result
    return wrapper

# -- decorator implimentation
@time_decorator
def slow_function():
    # some time-consuming task
    time.sleep(6)	# waits 6 seconds

# Using the decorated function
slow_function()

# --- Alternative to above decorator implimentation
def slow_function():
    # some time-consuming task
    time.sleep(6)	# waits 6 seconds

# declare new decorated function
function_duration = time_decorator(slow_function)
# Using the decorated function
function_duration()

# ---- The end: Enjoy the carrot_cake
