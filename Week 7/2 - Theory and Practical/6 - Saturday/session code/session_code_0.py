# File Paths 

# open() - read in file content as file object 

# Absolute Path
# C:\Users\smugh\Desktop\HypeDev Lecture Backpack\Week 7\sat_session_workspace\list_of_cats.txt

# Relative Path
# subFolder\list_of_cats.txt

# Open up files

# Approach 1
file_object = open("sub_folder\list_of_birds.txt", 'r')

# return reference in memory
print(file_object)

# read file
print(file_object.read())

# closing the file
file_object.close()

# Approach 2 - Best Practice
with open("list_of_cats.txt", 'r') as file_object:
    print(file_object.read())