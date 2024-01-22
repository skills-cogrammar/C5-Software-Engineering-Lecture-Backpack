# Libraries
import math

result = math.sqrt(25)

print(result)

# different import ways

# importing the entire library
import math

# import the specific function from library
from math import sqrt


# Example of datetime library
from datetime import datetime

current_time = datetime.now()

print(current_time)


# using custom library
from my_custom_library import custom_greeting
# custom_greeting()

import my_custom_library

user_statement = input("What did dumbledore say ? ")

my_custom_library.dumbledore_said(user_statement)

# Benefits of User-defined functions
"""
1. Modularity - breaking down into smaller pieces
2. Abstraction - Function hide the implementation details.
3. Extension - libraries extend the capabilities of our programs
"""
