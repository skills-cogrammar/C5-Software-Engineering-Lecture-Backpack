# # Reading from a sub-folder
# with open("sub-folder/cat_names.txt", 'r+') as cat_file_obj:
#     print(cat_file_obj.read())

# # Pass example
# # with open("jedi.txt", "w+") as file_obj:
# #     pass    # skips this body of code

# # File Opening for writing
# with open("sub-folder/jedi_new.txt", "w+") as jedi_file_obj:
#     jedi_file_obj.write("Monty")

# # File opening for appending
# with open("jedi.txt", "a+") as file_obj:
#     file_obj.write("\nbeans")

# # Write Data from input
# with open("sub-folder/cat_names.txt", "a+") as file_obj:
#     user_prompt = input("What is your cats name ? ")
#     file_obj.write(f"\n{user_prompt} is a tabby cat")

# """
# write() - write the contents to the file
# writelines() - writes a list of strings to a file 
# """

# # File Opening for writing
# with open("sub-folder/jedi_new.txt", "w+") as jedi_file_obj:
#     jedi_file_obj.writelines(["Monty", "Serge", "Pluto", "Beans"])

# Overwrting data to text file
new_clean_list = []
with open("jedi.txt", "r+") as file_obj:
    content = file_obj.readlines()

    print(content)
    for line in content:
        new_clean_list.append(line.strip())

print(new_clean_list)

none_duplicate_list = list(set(new_clean_list))

print(none_duplicate_list)

# What if i want to create a new file everytime it runs
# with open("secret_secret_secret_pokemon.txt", "x") as file_obj:
#     pass

"""
x - create an empty file to avoid accidentally overwriting the current file.
"""

# whenever we use readlines should we just put .seek in?
# yes

# with open("secret_secret_pokemon.txt", "r+") as file_obj:
#     content = file_obj.readlines()
#     print(content)

#     file_obj.write("Raikou")

# use seek(-1) - we get a valueError
# with open("jedi.txt", 'r+') as file:
#     file.seek(-1)
#     file.readline()


with open("planets.txt", 'w') as planet_file_object:
    print("MVEMJSUNP")
    print("Mercury", file=planet_file_object)
    print("Venus", file=planet_file_object)
    print("Earth", file=planet_file_object)
    print("Mars", file=planet_file_object)
    print("Jupiter", file=planet_file_object)
    print("Saturn", file=planet_file_object)
    print("Uranus", file=planet_file_object)
    print("Neptune", file=planet_file_object)
    print("PLUTO", file=planet_file_object)