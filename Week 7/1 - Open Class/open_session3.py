"""
Could you show please, how to slice string from file.
Thank you
"""

# could have been opened in w+ and saved some lines!!!
with open("test.txt", "w+") as text:
    text.write("This is line 1\nThis is line 2")
    file_string = text.read()
    sliced = file_string[0:4]
print("Does this run my python program?\n Yes, clearly it does. :| ")

"""
you could have used w+ instead of r+ previously
r+ reads and writes but doesn't create a file if inexistent
w+ reads and writes and can create a file if inexistent
"""

# with open("test.txt", "r") as text:
#     file_string = text.read()
#     sliced = file_string[0:4]

# print(sliced)

"""
Please can you cover
LIST slicing and does it create new strings?

sorry Liano
I meant does it create a new list such that changes are separate
"""


"""
whats the code for calculating the average number input by user
"""

# amount = amount of numbers the user has entered.
# sum = sum of all the amounts that the user has entered.

"""Can we have two files open and transfer from one to another directly?"""

# file_string =""
# with open("test.txt", "r") as text:
#     file_string = text.read()
#     sliced = file_string[0:4]

# with open("test_copy.txt", "w") as copy_to:
#     copy_to.write(file_string)


"""
can we use slicing on readlines()
"""

# What the method will return
# with open("test.txt", "r") as text:
#     file_string = text.readlines()
#     print(file_string)
#     # print(type(file_string))
#     print(file_string[1:3])

# Where slicing can be applied.
    # Iterables = Slicing can be achieved

# Absolute Path:
"./T17 - Capstone Project - Lists, Functions, and String Handling/10-025-1 Capstone Project - Lists, Functions and String Handling/user.txt"

# Relative Path:
"user.txt"

# Settings to change execution dir:
"File -> Preferences -> Settings [Search for 'execute in file dir'] -> Tick the box"