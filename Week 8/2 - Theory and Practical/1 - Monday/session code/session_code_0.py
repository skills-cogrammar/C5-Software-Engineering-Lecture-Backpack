import math
from my_custom_library import custom_greeting


def hello_world():
    print("hello world")


hello_world()


# parameters vs arguments
def plus_one(value_one):   # parameter  
    pass


plus_one(789)    # argument

# print vs return
# return example
def plus_one_return(value_one): 
    return value_one + 1


# print example
def plus_one_print(value_one): 
    print(value_one + 1)

# print - will simply display the data you are working with and not store it in memory
# return - return the data and store it in memory but not display unless specified


print(plus_one_print(5))
# print(plus_one_return(10))

custom_greeting()