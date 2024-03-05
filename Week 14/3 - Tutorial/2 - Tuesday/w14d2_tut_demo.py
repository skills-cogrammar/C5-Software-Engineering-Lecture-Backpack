"""
Using del to remove values from a list
"""

my_list = [1, 2, 3, 4, 5]

# Remove the value from the list at index 2
del my_list[2]              # Note the square brackets
print(my_list)

"""
Using remove() to remove values from a list
"""
my_list = [1, 2, 3, 4, 5]

# Remove the value 3 from the list regardless of the index position
my_list.remove(3)           # Note the round brackets
print(my_list)
