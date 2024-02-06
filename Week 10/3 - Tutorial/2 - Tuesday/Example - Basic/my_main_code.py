# Example: my_main_code.py
"""
Here is a summary of the directory structure:

Main Project: my_main_code.py
|
|-> my_library.py
    : my_function
    : another_function
"""

# Import libraries ----
# from my_library import *
import my_library

# Declare functions
def my_favourite_function():
    print("Yippee")


# Main code
result = my_library.my_function()
print(result)

# How is "import library" different to "import library*" ?

# import my_library
# from my_library import *