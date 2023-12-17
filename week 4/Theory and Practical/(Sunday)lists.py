# num_list = [1,2,3,4,5]
# word_list = ["Word1", "Word2", "Word3"]
# bool_list = [False, True, True, False]
# list_2d = [[1,2,3], 
#            [4,5,6], 
#            [7,8,9]]
# mixed_list = ["Hello", 13, 87.98, True, None, tuple(), [], {}]

new_list = list()
# new_list2 = []

# num_list = [1,2,3,4,5]
# new_num_list = num_list.copy()

# new_num_list[2] = 200
# print(num_list)

# # Mutable
# num_list = [1,2,3,4,5]
# num_list[0] = 5
# print(num_list)

# # Immutable
# strings = "Piano"
# strings[0] = "L"
# print(strings)

# # Indexing



# print(my_list[0])
# print(my_list[3])
# print(my_list[-1])
# print(my_list[-3])



# Slicing
# [start:stop:step] (stop --> Up to, but not including)

# print(my_list[2:4])
# print(my_list[:3])
# print(my_list[2:])
# print(my_list[::2])

# print(my_list[-3:-1])
# print(my_list[-3:])
# print(my_list[-3:-1])
# print(my_list[::-1])


# # Item assignment

# my_list[1] = "was"
# print(my_list)

# num_list = [1,2,3,4,5]
# num_list[3] = 9
# print(num_list)


# Adding items


# # Append to the end of the list.
# my_list.append(":)")
# print(my_list)

# # Inserting at a specific index.
# my_list.insert(2, "insert")
# print(my_list)

# # Appending another list to an existing list
# my_list.extend(["This", "is", "another", "list", "."])
# print(my_list)

# my_list += ["This", "is", "another", "list", "."]
# print(my_list)


# # Removing items
# my_list.remove("list")
# print(my_list)

# my_list.pop()
# print(my_list)

# my_list.pop(3)
# print(my_list)

# my_list.clear()
# print(my_list)

# my_list = ["This", "is", "our", "list", "!"] 
# my_list = [7, 2, 4, 100, 16]

# List manipulation
# my_list.sort()
# print(my_list)
# my_list.sort(reverse=True) # Look Up ASCII Table
# print(my_list)

# my_list.reverse()
# print(my_list)

# num_list = [0,1,2,3,4,5]
# print(len(num_list))
# print(max(num_list))
# print(min(num_list))

my_list = ["This", "is", "our", "list", "!"]
# for word in my_list:
#     print(word)

# for index in range(len(my_list)):
#     my_list[index] = 0

# print(my_list)

# for i in range(len(my_list)):
#     print(my_list[i])

# my_list = ["This", "is", "our", "list", "!"]

# # enumerated_list = enumerate(my_list, 1)
# # print(list(enumerated_list))

# for i, word in enumerate(my_list, 283):
#     print(i, word)


# How to iterate over a List and a dictionary.

prices = {"Shoe": 12,
         "Dress" : 30,
         "Shirt": 20}

store_items = ["Shoe", "Dress", "Shirt"]

string = ""
count = -1
for item in prices.values():
    count += 1
    for element in range(count, count +1):
        string += f"{store_items[element]} : "
    string += str(item) + "\n"

print(string)
        
