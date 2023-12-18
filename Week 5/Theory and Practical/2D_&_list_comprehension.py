# List comprehension
# Basic Structure
# new_list = [expression for item in iterable]

# Squaring numbers from 0 to 9
squares = [x**2 for x in range(10)]
# Result: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
   

# ------------------------------------------------------

# Benefits:
# Using a traditional for-loop
even_numbers = []
for x in range(10):
    if x % 2 == 0:
        even_numbers.append(x)

# Using a list comprehension
even_numbers = [x for x in range(10) if x % 2 == 0]


# ------------------------------------------------------

""" 
Python's ternary operator (AKA 'conditional expression') is a neat way to express basic if/else statements in a 
single line. It assesses a boolean condition and returns a true or false value.
In comparison to basic if/else statements, it is shorter and easier to read.
"""

"x if condition else y"
# Ternary operator example
result = "Even" if 6 % 2 == 0 else "Odd"
print(result)

# ------------------------------------------------------

# # Using a traditional for-loop
squared_numbers = []
for x in range(5):
    squared_numbers.append(x**2)

# # Using a list comprehension
squared_numbers = [x**2 for x in range(5)]

# -------------------------------------------------------

# Considerations
# Overly complex list comprehension
complex_squares = [x**2 if x % 2 == 0 else 0 for x in range(10) if x > 2 and x < 8]

# Readable alternative using a for-loop and an if statement
readable_squares = []
for x in range(10):
    if 2 < x < 8 and x % 2 == 0:
        readable_squares.append(x**2)

# --------------------------------------------------------
        

# Basic Iteration
two_D = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Iterate over each row
for row in two_D:
    # Iterate over each element in the row
    for element in row:
        print(element, end=" ")
    print("\n")


# --------------------------------------------------------



grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Iterate over rows and indices
for i, row in enumerate(grid):
    # Iterate over elements and indices in the row
    for j, element in enumerate(row):
        print(f"matrix[{i}][{j}] = {element}")


# --------------------------------------------------------

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Iterate over each element, considering only even numbers
for row in matrix:
    for element in row:
        if element % 2 == 0:
            print(element, end=" ")
print()
