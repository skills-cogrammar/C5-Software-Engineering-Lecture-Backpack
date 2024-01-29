# # read in data and cleanse

# poke_stat_dict = {}

# with open("dummy_data.txt", "r+") as file:

#     content = file.readlines()
#     print(content)
#     joined = "\n".join(content)

#     print(joined)

#     for line in content:
#         line_split = line.split(", ")
#         print(line_split)

#         poke_name = line_split[0]
#         poke_type = line_split[1]
#         poke_math_score = line_split[2]
#         poke_combat_score = line_split[3].strip()

#         poke_stat_dict[poke_name] = [poke_type, poke_math_score, poke_combat_score]

# print(poke_stat_dict)

# access a specific key
# print(poke_stat_dict["psyduck"])

# # Editing information
# poke_stat_dict["bulbasuar"] = ["grass", 90, 12]

# # adding new pokemon stat to dictionary 
# poke_stat_dict["sunflora"] = ["grass", 45, 12]

# print(poke_stat_dict)

# with open("dummy_data.txt", "w+") as file:
#     for key, value in poke_stat_dict.items():
#         file.write(f"{key}, {value[0]}, {value[1]}, {value[2]}\n")


# Best Practices:


import os 
# # Ensure path exists

# file_path = "jedi_not.txt"
# path_exists = os.path.exists(file_path)
# print(path_exists)

# if path_exists:
#     print(f'The file or directory at {file_path} exists.')
#     # with open(file_path) as txt_file:
# else:
#     print(f'The file or directory at {file_path} does not exist.')


# # # Handle Exceptions:
# try:
#     with open('file.txt', 'r') as file:
#         contents = file.read()
# except FileNotFoundError:
#     print("File not found.")


# # Path construction to improve compatibility
# file_path = os.path.join('dir', 'file.txt')
# with open(file_path, 'r+') as file:
#     contents = file.read()

# os.remove("delete_me.txt")
# print(f"\u001b[31m {os.getcwd()} \u001b[37m")


#.join() 

items = ['pika', 'electric', '12', '34']
joined = " | ".join(items)
print(joined)
