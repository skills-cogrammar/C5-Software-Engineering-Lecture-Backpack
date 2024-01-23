"""
Can you please explain about seek() in file handling?
"""

# Seek()
# with open("test.txt", "r+") as text_file:
#     text_file.write("This is line 1 of seek.txt\nThis is line 2\nAnd this is line 3")
#     text_file.seek(0)
#     contents = text_file.read()
#     print(contents)

"""
2 tehings I would like to go through tonight.
the def function and how to open a file rearrange 
the contnts in the order you need.
"""

with open("test.txt", "r+") as text_file:
    # Read in the file contents (as string)
    file_content = text_file.readlines()
    print(file_content)

    # Manipulate the string to our needs/requirements
    
    counter = 0
    new_line = ""
    for line in file_content:
        counter += 1
        if counter >= 2: 
            new_line += line.replace("\n", "") + " of seek.txt\n"
            print(new_line)
        else:
            new_line += "This is line 1 of seek.txt\n"

    # # Write these changes back to the text file (Overwriting the old content)
    text_file.seek(0)
    text_file.write(new_line)


"""
Could you show me/us how 
to store values in a dictionary from a function, please?
"""

# dictionary = {}
# print(dictionary)

# def filler(key, value):
#     dictionary[key] = value
#     print(dictionary)

# filler("Liano","Pasta")
