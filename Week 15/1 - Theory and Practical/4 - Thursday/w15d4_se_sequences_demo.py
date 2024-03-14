# ======= How to transform dictionaries to write to file - Learner Question
my_dictionary = {"01":"Apple", "02":"Banana", "03":"Orange"}

keys_list = list(my_dictionary.keys())   # Result: keys_list = ["01", "02", "03"]

values_list = list(my_dictionary.values()) 
# Result: values_list = ["Apple", "Banana", "Orange"]

for line_count, key in enumerate(keys_list):
    file_write_line = f"{keys_list[line_count]};{values_list[line_count]}"

# ===== If you loose key, how can you find key with value? - Learner Question
# Remember: We can have duplicate values, so only the key for first value will return
def get_key(my_dictionary, value):
    for key, val in my_dictionary.items():
        if val == value:
            return key
    return None

# Main Code
my_dictionary = {"01":"Banana", "02":"Banana", "03":"Orange"}

my_value = "orange"

key_value = get_key(my_dictionary, my_value)
print(key_value)

# ====== 3 lists into dictionary - Learner Question
# product_list, price_list, quantity_list
my_dictionary = {"P1":[23.01, 30], "P2":[23.01, 30], "P3":[23.01, 30]}

# The value can be anything, even more dictionaries, like a tree structure.
my_dictionary = {"P1":{"x1":20,"x2":30}, "P2":{"x1":20,"x2":30}, "P3":{"x1":20,"x2":30}}

"""
1. String Fundamentals
"""
#===>  Creating a string datatype
# Python does the string declaration derived from the value format
my_str = "Let's learn about strings!"
print(my_str)

# Getting the length of a string
print(len(my_str))

# Looping over a string with for-loop
for letter in my_str:
    print(letter)

# Comparing strings
word = "chicken"
if word == "chicken":
    print(f"We will be eating {word} tonight!")

# Index to a character in a string
my_str = "Let's learn some more about strings!"
print(my_str[1])            # Print letter 'e'

# Print the first word in the string
position = my_str.find(" ")
first_word = my_str[0:position]
print(first_word)

# Below concatenation can be done, but not practical to implement: Code too static
print(my_str[6] + my_str[7] + my_str[8] + my_str[9] + my_str[10])

#----------------------
# Can't change string characters because of the immutable attribute
my_sentence = "This is my mostest favouritous sentence of 2024!"
my_sentence[-2] = '3'           # This will give an error

# Depending on the implementation use .replace() if you know the value
my_sentence.replace('s','!')

# ELSE

# We can cast it to a list if we only have the position
my_list = list(my_sentence)
print(my_list)
my_list[-2] = '3'
print(my_list)

# Now join it back to the string to get the change in the string
my_str = "".join(my_list)
print(my_str)
#----------------------

# Change a string to all uppercase
my_str = "This is really, really the last thing I am showing!!!!!!!"
print(my_str.upper())
# For the above remember that my_str is still the original value 
# because of the immutable attribute

# Storing the uppercase string
my_str = my_str.upper()
# **** FYI: For the above, Python creates a new memory space where it constructs 
# the new value and then once the new string is constructed, Python updates 
# the reference held by the variable my_str to point to this newly allocated memory 
# space. This effectively changes the address in memory where my_str was pointing 
# to point to the location of the newly created string.

"""
2. Lists Fundamentals
"""
#===>  Creating a list datatype
new_list = []
word_list = ["word1", "word2", "word3"]

# -- Create lists with casting
# Data types that we can cast to a list
my_string = "Hello"
my_list = list(my_string)
print(my_list)

my_tuple = (1, 2, 3)
my_list = list(my_tuple)
print(my_list)

my_set = {1, 2, 3}
my_list = list(my_set)
print(my_list)

my_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
list_from_keys = list(my_dictionary.keys())
print(list_from_keys)

my_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
list_from_values = list(my_dictionary.values())
print(list_from_values)

my_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
list_from_items = list(my_dictionary.items())
print(list_from_items)

# -- Creating lists with the range function
# Normally we will have
for even_num in range(2, 11, 2): # range(10)
    print(even_num)

# Another option to above
# range(2, 201, 2) is a memory object that is not viewable
my_range = list(range(2, 201, 2))   
print(my_range)

for even_num in my_range:
    print(even_num)

"""
3. List Comprehension
""" 
#===> Basic List Comprehension
# Create a list of squares of numbers from 0 to 9
squares = [x**2 for x in range(10)]
print(squares)              # Result: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#===> List Comprehension with Condition
# Create a list of even numbers from 0 to 9
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)         # Result: [0, 2, 4, 6, 8]

#===> List Comprehension with Transformation
# Create a list of strings representing the lengths of words
words = ["apple", "banana", "orange"]
word_lengths = [len(word) for word in words]
print(word_lengths)         # Result: [5, 6, 6]

#===> Nested List Comprehension
# Create a flattened list from a 2D List
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for row in matrix for item in row]
print(flattened)            # Result: [1, 2, 3, 4, 5, 6, 7, 8, 9]

#===> List Comprehension with Function
# Create a list of squares of even numbers
def square_if_even(x):
    return x**2 if x % 2 == 0 else None

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squares_of_even = [square_if_even(x) for x in numbers]
print(squares_of_even)      # Result: [None, 4, None, 16, None, 36, None, 64, None]

"""
4. 2D Lists
"""
# ========================== List dimensions

#===>  Dealing with mixed lists
mixed_list = ["Hello", 13, 87.89, True, None, (), [1, 2, 3, ['a', 'b', 'c']], {}]
my_item = mixed_list[6][3][1]       # Access the 'b'

# A one-dimensional list
num_list = [1,2,3,4,5]
my_item = num_list[2]               # Access the 3

# Creating a 2d-list
list_1 = [1,2,3]
list_2 = [4,5,6]
list_3 = [7,8,9]

list_2d = [[1,2,3], 
           [4,5,6], 
           [7,8,9]]

my_item = list_2d[1][1]              # Access the 5

# Creating a 3d-list
list_2d_1 = [[1,2,3], [4,5,6], [7,8,9]]
list_2d_2 = [[11,12,13], [14,15,16], [17,18,19]]
list_2d_3 = [[21,22,23], [24,25,26], [27,28,29]]

list_3d = [[[1,2,3], [4,5,6], [7,8,9]],
        [[11,12,13], [14,15,16], [17,18,19]],
        [[21,22,23], [24,25,26], [27,28,29]]]

my_item = list_3d[1][2][1]           # Access the 18

"""
5. Fundamentals of Dictionaries
"""

#===>  Creating a dictionary datatype
cat_dict = {"name": "bartholomeow", "age": 12, "city": "Paris", "breed": "Burmese"}
print(cat_dict)

cat_dict = dict(name = "bartholomeow", age = 12, city = "Paris", breed = "Burmese")
print(cat_dict)

#===>  Working with dictionaries
# Access value
breed_var = cat_dict["breed"]
print(breed_var)

breed_var = cat_dict.get("Breed")
print(breed_var)

# Changing or updating particular values
cat_dict["breed"] = "York Chocolate"
print(cat_dict)

# Looping
cats_dict = {"Bartholomeow": "Bermese", "Garfield": "Orange", "Tom": "Egyptian Mau", "Beans": "Persian" }
print(cats_dict)

# Traditional - Option 1
for key in cats_dict:
    print(key, cats_dict[key])

# Values - Options 2  
for value in cats_dict.values():
    print(value)

# Keys - Option 3
for key in cats_dict.keys():
    print(key)   

for key, value in cats_dict.items():    # ("Bartholomeow", "Bermese")
    print(f"{key}: {value}")

# See top of demo file for more on dictionaries
