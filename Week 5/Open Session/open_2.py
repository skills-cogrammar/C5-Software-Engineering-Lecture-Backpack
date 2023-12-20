"""
quick question before we start, when we highlight a new_variable_2 it 
automatically highlights all the new_variable_2s with the same name in the program, 
is there a way to change or edit the name of all of them at the same time?
"""


# # 1. 
# new_name = 'Foo'

# print(new_name)

# # 2. 
# new_variable_2 = "123"

# print(new_variable_2)



"""
Could you give an example of nested list iteration?
"""

# nested_list = [
#             ["Liano", 56, "Ghost_White"],
#             [10, 12, 18]
#             ]

# for i in range(len(nested_list)): # Iterate over the elements in the outer list.
#     for j in range(len(nested_list[i])): # Iterating over the elements in the inner list.
#         current_nested_element = nested_list[i][j]
#         print(current_nested_element)





# nested_list = [[i for i in range(3)] for _ in range(3)]
# print(nested_list)
        

"""
so does the len function always start counting from 0? or does it start from 0 
because it is pointing to a list so automatically count indices starting at 0?
"""

# listy = ["A", "B", "C"] 
# string = "Liano"
# print(len(string)) # + 3

# for i in range(1, 11):
#     print(i)


"""How To Loop over Dictionary?"""

info = {"\033[3m Liano \033[0m":"\033[37m Ghost_White \033[0m",
        "Armand": "\033[32m Green \033[0m",
        "Sulaiman" : "\033[35m Purple \033[0m"
        }

print(info["Sulaiman"])

# .items() method

for item in info.items():
    print(item)

# .keys() method
print("-" * 30)
for key in info.keys():
    print(key)


print("-" * 30)
# .values() method
for value in info.values():
    print(value)


print("-" * 30)
# Both Keys & Values
for key, value in info.items():
    print(f"Key: {key}\nValue: {value}\n")

"""
so the key and value variables you used in the last for loop could 
have been any name? 
just the first points to the key and the 2nd points to the valuw?
"""

print("-" * 30)
# Both Keys & Values
for i, j in info.items():
    print(f"Key: {i}\nValue: {j}\n")