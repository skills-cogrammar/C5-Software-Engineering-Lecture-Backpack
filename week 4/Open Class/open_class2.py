# my_str = "Welcome"
# #         0123456

# new_str = my_str[-2:]

# print(new_str)


# my_str = "Welcome"

# my_list = ["Welcome", "to", "the", "open", "class!"]

# joined_string = " ".join([my_list[0], my_list[-1]])

# print(joined_string)

# split_string = joined_string.split()

# print(split_string)



loop_string = "This is for a loop!"
#              0123456789
# print(len(loop_string))

to_find = "o"

# for i in range(len(loop_string)): # (0,1,2,3,4,5,6,7,8)
#     if loop_string[i] == to_find:
#         index = i
#         break
# print(loop_string.find("o"))

# for i in range(0, 101, 2):
#     print(i)

# has_letter = False
# for letter in loop_string:
#     if letter == to_find:
#         has_letter = True

# if "o" in loop_string:
#     print(True)

# print(f"Index of {to_find} is {index}")
# print(loop_string[9])

# my_int = 4
# my_float = 4.1

# if my_int < my_float:
#     print("Int is smaller than float")

my_str = "This is our new string!"
my_list = ["Item1", "Item2", "Item3"]

for i, item in enumerate(my_list, 1):
    print(i, item, sep=": ")

print(str(my_list))
