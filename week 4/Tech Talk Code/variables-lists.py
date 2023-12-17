# Data Types

# string = type("This is a string")
# boolean = True
# boolean = False
# integers = -8
# floats = 8.3
# none = type(None)

# print(string, integers, floats, none)


# user_input = input("Enter your name: ")


# if integers > floats:
#     print("The integer is greater")
# else:
#     print("Float is greater")



# Simple For Loop

# for i in range(1, 11):
#     print(i)

# Simple While
# while True:
#     user_input = int(input("Enter a number: "))

#     if user_input % 2 == 0:
#         print("This is an even number.")
#         break



# Exception Handling

# try:
#     while True:
#         user_input = int(input("Enter a number: "))

#         if user_input % 2 == 0:
#             print("This is an even number.")
#             break
# except ValueError as value_error:
#     print(f"Error: This normally happens when you enter a numerical value. \n ({value_error})")

# # Lists.
# string = "This is a string"
# boolean = True
# boolean = False
# integers = -8
# floats = 8.3
# none = type(None)

# lists = [string, boolean, floats]
# print(lists)
# print(lists[-1])

# 3 items -> iterate 3 times -> For Loop
#len()

# for i in range(len(lists)):
#     print(lists[i])

# lists.append(21)
# print(lists)
# lists.pop()
# lists.remove(string)
# lists.insert(1, "test")
# print(lists)



# Dictionaries.
name = "Liano"
age = 90
fav_food = "Pasta"

user_details = {"name": name, 
              "age": age, 
              "favFood": fav_food
              }

user_details["name"] = "Marcus"
user_details["email"] = "test@gmail.com"
user_details(2, "test")

# dictionary.items()
# dictionary.get()
# dictinary.pop()

print(user_details["email"])
