# CSV = Comma Separated Values

"""
can you give some instances when you 
can leave a function's parameter empty?
"""

# def express():
#     return "I love programming!"

# print(express())

"""
Can you show the difference between read() and readlines(), readline()
 you said earlier you were going to show us the difference
"""
path = "example.txt"
# with open(path, "w") as example_file:
#     example_file.write("This is line 1. \n")
#     example_file.write("This is line 2. \n")
#     example_file.write("This is line 3. \n")

# with open(path, 'r') as example_file:
#     print(f" read():\n{example_file.read()}\n")
#     example_file.seek(0,0)
#     print(f" readlines():\n{example_file.readlines()}\n")
#     example_file.seek(0,0)
#     print(f" readline():\n{example_file.readline()}")


"""
Iterate over a dictionary
"""
# # inventory
# inventory = {"cake" : 12,
#                 "tea" : 3,
#                 "milk" : 2 }

# # .items()
# for item in inventory.items():
#     print(item)

# for key, value in inventory.items():
#     print(f"Key: {key}\nValue: {value}")

# #.keys()
# for key in inventory.keys():
#     print(key)

# # .values()
# for value in inventory.values():
#     print(value)


"""Can I see how to call data from a file and store it in lists and then do some work on 
them like checking if some data matches there and then print a message?
"""

with open(path, 'r') as example_file:
    file_lines = example_file.readlines()
    print("text_file_line: ", file_lines)
    for item in file_lines:
        words = item.split()
        print("Words: ", words)
        for item in range(len(words)):
            print(words[3])
            break

