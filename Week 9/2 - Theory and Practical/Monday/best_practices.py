"""
Descriptive Function Names:
Instead of foo() or bar(), let's name our functions 
so that anyone reading our code knows exactly what's going on.
"""


"""Single Responsibility Principle: 
One function, one responsibility. Break down your code into smaller, 
focused functions.
"""
# 1 function = 1 Responsibility

# def process_info(info):
#     # Clean Data
#     positives = [x for x in info if x > 0]

#     # Calculate
#     average = sum(positives)/len(positives)

#     # Display results
#     print(average)

# def get_positives(info):
#     positives = [x for x in info if x > 0]
#     return positives

    
# def get_average(info):
#      # Calculate
#     average = sum(info)/len(info)
#     return average

# info = []
# print(get_average(get_positives(info)))

"""Default Argument Values:
Be careful with default values. They're handy but watch out for mutable defaults.
"""
# with open("t.txt", 'w') as text:
#     print("Go to text file", text)
#     print("no error")

# def greeting(name, company="Company Y"):
#     print(f"Hello {name}, welcome to the {company} Log In page")

# greeting("Liano")
# greeting("Liano", company="Liano-Debugs")

# Buggy case:

# def appends(number, destination=[]):
#     destination.append(number)
#     print(destination)
#     return destination

# appends(1)
# appends(4)
# appends(100)




"""
Avoiding Global Variables:
Global variables can be tricky. Stick to local scope and keep your functions pure.
"""

# student_name = "Liano"

# def name_change(new_name):
#     global student_name
#     student_name = new_name
#     print(f"Function Scope: {student_name}" )
#     return student_name

# name_change("Dave")
# print(f"Global Scope: {student_name}")



# Input Validation & Sanity Checks ;)
"""
Input Sanity Checks: 
Input validation is like checking your ingredients before cooking. 
Ensure your functions get what they expect.
"""


"""
Exception Handling:
Expect the unexpected. Wrap your code in try-except blocks
and provide meaningful error messages.
"""


"""
Logging: 
Logging is your friend. Add informative logs to aid debugging.
"""


import logging

logging.basicConfig(filename="my_logs.log")
logger = logging.getLogger()
logger.setLevel(logging.INFO)



def file_opener():
    try:
        with open("not_here.txt", 'r') as text:
            content = text.read()
            return content
    except FileNotFoundError:
        logger.error("The not_here.txt file was not found :( (line 117))")

logger.info("Calling file_opener @ line 118")
file_opener()




# os Module

import os

# print(os.path.exists("my_log.log"))

file_exists = os.path.exists("my_lgggggg.log")
print(file_exists)

if file_exists:
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    print("File exists")
else:
    print("Log file does not exist")
    logger.error("Log file does not exist")
