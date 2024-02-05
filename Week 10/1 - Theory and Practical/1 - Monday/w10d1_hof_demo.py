""" Build-in HOF reduce()
The use of reduce() can lead to more concise and expressive code 
when dealing with operations that involve accumulating values over an iterable.

Parameters:

*A binary function: This function takes two arguments and 
defines the operation to be performed on the elements.
*An iterable: The collection of elements that the function will be applied to.
*An optional initial value: This value serves as the starting point for 
the reduction process. If provided, the first call to the binary function 
will use this initial value and the first element of the iterable.
"""

# --------------  Original required code
# Example binary function (addition)
def add(x, y):
    return x + y

# Example iterable
numbers = [1, 2, 3, 4, 5]
start_with = 0
result = start_with

# Main Code
for number in numbers:
    x = result
    y = number
    result = add(x, y)

print(f"result: {result}") 

# --------------  Using HOF Reduce()
from functools import reduce

# Example binary function (addition)
def add(x, y):
    return x + y

# Example iterable
numbers = [1, 2, 3, 4, 5]

# Using reduce to sum the elements
result = reduce(add, numbers, 0)
print(f"result: {result}")  # Output: 15 -> 0 + (1 + 2 + 3 + 4 + 5)

""" Build-in HOF filter()
It filters elements from an iterable (e.g., a list) 
based on a specified condition. 
It returns a new iterable containing only the elements for which 
the given condition is true.

Parameters:

*A function: This function should return a Boolean value (True or False). 
Each element of the iterable is passed to this function, 
and only the elements for which the function returns True 
are included in the result.
*An iterable: The collection of elements that you want to filter.
"""

# --------------  Using HOF filter()
# Example function (filter even numbers)
def is_even(num):
    return num % 2 == 0

# Example iterable
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using filter to get even numbers
result = filter(is_even, numbers)
print(f"result: {result}")      # Iterable object
"""
result variable above is an 'iterator object' and not readable as a whole, but
designed to be efficient and memory-friendly especially for large data sets. 
They provide elements one at a time, and 
they don't store the entire sequence of elements in memory. 
Instead, they generate each element on-the-fly as needed.
"""
filtered_numbers = list(result) # Cast to list to make readable as a whole
print(f"filtered numbers: {filtered_numbers}")  # Output: [2, 4, 6, 8, 10]

# FOR FUN: how do we print this without the [] brackets?
print("filtered numbers:", end=" ")
print(*filtered_numbers, sep=", ")

# ----- OR use the iterable object with a for-loop
"""
This will only work if you have not already 
iterated through the result object.
In this case we iterated through the object with list(result) and the 
below will produce and empty result. To show result, we need to recreate
the result.
"""
result = filter(is_even, numbers)   # recreate the result

print("filtered numbers:", end=" ")
for iter_num in result:
    print(iter_num, end=" ")

""" Build-in HOF map()
It applies a given function to all items in an iterable (e.g., a list) 
and return a new iterable containing the results.

Parameters:

*A function: This function defines the operation to be applied to 
each element of the iterable.
*An iterable: The collection of elements that you want to process.
"""

# --------------  Using HOF map()
# Example function (square each number)
def square(num):
    return num ** 2

# Example iterable
numbers = [1, 2, 3, 4, 5]

# Using map to square each number
result = map(square, numbers)
print(f"result: {result}")      # Iterable object
squared_numbers = list(result)
print(f"squared numbers: {squared_numbers}")  # Output: [1, 4, 9, 16, 25]

#### Using an iterable objects multiple times -------------------
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
print(f"squared numbers: {squared_numbers}")  # Output: [1, 4, 9, 16, 25]

#Read result copy and make copies again. Now we can use result_active again.
result_active, result = tee(result) 

#### Lambda functions -------------------
# --------------  Using HOF map() with Lambda
# Example iterable
numbers = [1, 2, 3, 4, 5]

# Using map with a lambda function to square each number
result_iterator = map(lambda x: x ** 2, numbers)

# Converting the iterator to a list for printing
result_list = list(result_iterator)

# Printing the result
print(result_list)  # Output: [1, 4, 9, 16, 25]
