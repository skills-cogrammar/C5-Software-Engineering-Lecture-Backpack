num_list = [1,2,3,4,5]
word_list = ["Word1", "Word2", "Word3"]
bool_list = [False, True, True, False]
list_2d = [[1,2,3], [4,5,6], [7,8,9]]
mixed_list = ["Hello", 13, 87.98, True, [], {}]

# Indexing
# 
# print(my_list[0])
# word = my_list[3]
# print(word)
# print(my_list[-1])
# print(my_list[-3])

# Slicing

# new_list = my_list[2:4]
# print(new_list[0])
# print(my_list[:3])
# print(my_list[2:])
# print(my_list[::2])

# print(my_list[-3:-1])
# print(my_list[-3:])
# print(my_list[:-2])
# print(my_list[::-1])


# Item assignment
my_list = ["We", "are", "working", "with", "lists!"] 
# my_list[1] = "were"
# print(my_list)


# num_list = [1,2,3,4,5]
# num_list[3] = 9
# print(num_list)

# # Lists are mutable
# list1 = [1,2,3,4,5]
# list2 = list1.copy()
# list2[2] = 500
# print(list2)
# print(list1)




# # Adding items
# my_list.append(":)")
# print(my_list)

# my_list.insert(2, "insert")
# print(my_list)

# my_list.extend(["This", "is", "another", "list", "."])
# print(my_list)

# my_list += ["This", "is", "another", "list", "."]
# print(my_list)

# Removing items
# my_list.remove("lists!")
# print(my_list)

# my_list.pop(3)
# print(my_list)

# my_list.clear()
# print(my_list)

# List manipulation
# print(my_list)
# my_list.sort()
# print(my_list)

# print("\n", my_list)
# my_list.reverse()
# print(my_list)

# num_list = [-1000,2,3,4,10]
# print(len(num_list))
# print(max(num_list))
# print(min(num_list))



my_list = ["We", "are", "working", "with", "lists!"] 
# for i in range(len(my_list)):
#     print(my_list[i])

# for word in my_list:
#     print(word)

# for i, word in enumerate(my_list, 30):
#     print(i, word)


"""
could you please explain how to loop through a list to
check if the list item is equal to a dictionary value?
"""

names = ["Liano", "Caroline", "Jax"]

surnames = {"Vivek" : "Tee",
            "Tim" : "Cook",
            "Phil" : "Jax"}

# Cross Check whether a item in a list is equal to a value in a dictionary:
for i in range(len(names)):
    for key, value in surnames.items():
        if names[i] == value:
            print(f"Fun fact {names[i]}! Your name is {key}'s surname :)")



# 
