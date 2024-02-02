# -- Decorator
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

# -- Example with variable positional inputs ---------------------------------
def calculate_area(shape, *args):
    if shape == "circle":
        radius = args[0]
        return 3.14 * (radius ** 2)
    elif shape == "rectangle":
        length, width = args
        return length, width 		# Inconsistent return type
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

shape = "triangle"			
# Global and local variable name can be the same here, 
#ie. shape since the value is never changed.

# Now we'll raise an error if the types are unsupported instead:
try:
    shape_area = calculate_area(shape, 2, 4 ,6)
except ValueError as e:
    print(f"Error: {e}")

print(f"The area of the {shape} is: {shape_area}")

"""
Building Custom decorators: 
"""
# ---- Example - How long does a function run  ---------------------------------
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

# ---- Example - Implement authorization to run a function ** Nested decorator ----------------------
def authorization_decorator(required_role):
    def decorator(func):
        def wrapper(user_role):
            try:
                if user_role == required_role:
                    return func(user_role)
                else:
                    raise PermissionError(f"User does not have the required role: {required_role}")
            except PermissionError as e:
                print(f"PermissionError: {e}")
        return wrapper
    return decorator

@authorization_decorator(required_role="admin")
def admin_only_function(user_role):				# This is the no auth admin_only_function
    return f"Admin function executed by user with role: {user_role}"

# Using the decorated function 
result = admin_only_function("admin")			# This is the with auth admin_only_function (After decorating)
result = admin_only_function("user")			# If no permission the result will have the value None

if result != None:
	print(result)
	
# ---- Example - Input validation decorator  ---------------------------------
def validate_int_args(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError(f"Invalid argument type: {type(arg)} is not an integer.")
        return func(*args, **kwargs)
    return wrapper

@validate_int_args
def add_numbers(x, y):
    return x + y

# Example usage
result = add_numbers(3, 5)
print(result)

# This will raise a TypeError due to invalid argument types
# result = add_numbers("3", 5)
