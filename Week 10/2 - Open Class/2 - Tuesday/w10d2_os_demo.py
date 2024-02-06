# Using HOF map()
# Example function (square each number)
def square(num):
    return num ** 2

# Example iterable
numbers = [1,2,3,4,5]

# How do we use HOF
result = map(square, numbers)
# OR -> result = map(lambda x: x * 2, numbers)
""" 
print(f"result: {result}")    # This display a memory address - not viewable

squared_numbers = list(result)
print(f"result: {squared_numbers}")

squared_again = list(result)
# nothing will print below since result pointer is at end from list(result)
print(f"result2: {squared_again}")

for number in result:
# nothing will print below since result pointer is at end from list(result)
    print(number)    

# How to solve above:
# We can recreate the iterable object
result = map(square, numbers) # Not make sense for large data

# Better solution below:
"""

from itertools import tee # copy/cloning function
result_copy, result = tee(result)

squared_numbers = list(result_copy) # [1, 4, 9, 16, 25] 
print(f"result: {squared_numbers}")

result_copy, result = tee(result)
squared_numbers = list(result_copy) # [1, 4, 9, 16, 25] 
print(f"result: {squared_numbers}")

#### Lambda functions -------------------
# --------------  Using HOF Reduce() with Lambda
from functools import reduce

# Example iterable
numbers = [1, 2, 3, 4, 5]

# Using reduce with a lambda function to sum the elements
result = reduce(lambda x, y: x + y, numbers)
print(result)  # Output: 15 (1 + 2 + 3 + 4 + 5)

# --------------  Using HOF filter() with Lambda
# Example iterable
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using filter with a lambda function to get even numbers
result = filter(lambda x: x % 2 == 0, numbers)
filtered_numbers = list(result)
print(filtered_numbers)  # Output: [2, 4, 6, 8, 10]

# --------------  Using HOF map() with Lambda
# Example iterable
numbers = [1, 2, 3, 4, 5]

# Using map with a lambda function to square each number
result_iterator = map(lambda x: x ** 2, numbers)

# Converting the iterator to a list for printing
result_list = list(result_iterator)

# Printing the result
print(result_list)  # Output: [1, 4, 9, 16, 25]

# Additional use of lambda - Sorted function
words = ["apple", "banana", "cherry", "date"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

##### User-defined HOF function --------------
# As requested by class to implement 2 functions consecutively and this
# also incorporates the request at the end of the lesson for x * y
def apply_operation_to_list(numbers, binary_operation, unary_operation):
    """
    Apply a binary operation element-wise to pairs of numbers from the list,
    and then apply a unary operation to each result.

    Parameters:
    - numbers: List of numbers.
    - binary_operation: Binary operation function taking two arguments.
    - unary_operation: Unary operation function taking one argument.

    Returns:
    - List of transformed values.
    """
    # Apply binary operation element-wise to pairs of numbers
    binary_results = [binary_operation(x, y) for x, y in zip(numbers[:-1], numbers[1:])]
    # numbers[:-1]: Takes all elements in the numbers list except the last one.
    # [1, 2, 3, 4]
    # numbers[1:]: Takes all elements in the numbers list except the first one.
    # [2, 3, 4, 5]
    # zip(): create pairs from these two slices [(1,2), (2,3), (3,4), (4,5)]

    # Apply unary operation to each result
    final_results = [unary_operation(result) for result in binary_results]

    return binary_results, final_results

# Binary operation: Multiply
def multiply(x, y):
    return x * y

# Unary operation: Square
def square(x):
    return x ** 2

# Example usage:
numbers = [1, 2, 3, 4, 5]

# Applying the HOF with addition and square operations
multiply_result, plus_sqr_result = \
    apply_operation_to_list(numbers, multiply, square)

print(multiply_result)  # Output: [2, 6, 12, 20]
print(plus_sqr_result)  # Output: [4, 36, 144, 400]

