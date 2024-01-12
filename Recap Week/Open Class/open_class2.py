str_num = "14.5558"

# if str_num.replace(".", "", 1).isnumeric():
#     print(str_num)

# for char in str_num.replace(".", "", 1):
#     if char not in "1234567890.":
#         print("Invalid")
#         break
# else:
#     print("Is numeric")


# my_dict = {"name" : "Jack",
#            "age" : 25,
#            "grades": [76, 68, 78, 84]}

# looking_for = [76, 68, 78, 84]
# index = -1
# print(my_dict.values())
# for i, value in enumerate(my_dict.values()):
#     if value == looking_for:
#         index = i
#         break

# if index >= 0:
#     keys = list(my_dict.keys())
#     print(keys[index])
# else:
#     print("Value not found")


# print(my_dict["grades"])


# my_list = []

# for i in range(5):
#     my_list.append("")

# my_list = [grade for grade in my_dict["grades"][:2]]

# print(my_list)

# new_dict = {}

names = ["Dave", "Peter", "Michelle"]
surnames = ["Jackson", "Smith", "Lamb"]

# for i in range(len(names)):
#     new_dict.update({i:names[i]})

new_dict = {name:surname for name, surname in zip(names, surnames)}

# print(new_dict)

names = ["Dave", "Peter", "Michelle"]

for i, name in enumerate(names, 100): # ((0, "Dave"), (1, "Peter"), (2, "Michelle"))
    print(i, name)

name, surname, age = ("Jack", "Reacher", 35)
print(name, surname, age)