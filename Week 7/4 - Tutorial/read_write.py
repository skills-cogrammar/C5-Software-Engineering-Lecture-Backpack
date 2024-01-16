# # Reading from a Text File
file_path_text = "example.txt" # Relative File Path
# alternative_path = "C:\\Users\\Liano Naidoo\\Desktop\\CodeGround\\test_file.txt"           # Absolute File Path

# w = write mode
# r = read mode
# a = append mode
# r+ = read & write (in one with block)

# Manually opening and closing
# file = open(file_path_text, 'r')
# file_content = file.read()
# file.close()

# print(file_content)


# # Reading from the text file
# with open(file_path_text, "r") as text_file: # Read only permission, NO WRITING.
#     content = text_file.read()
#     print("Content of the text file:")
#     print(content)

# with open(file_path_text, "r+") as text_file: # Opens with read and write permission.
#     content = text_file.read()
#     print("Content of the text file:")
#     print(content)

# # data = []
# # Writing sample data to the text file
# with open(file_path_text, "w") as text_file: # Write only. Overwrites existing content (Will create file if it does not exist yet)
#     # content = text_file.read()
#     # data.append(content)
#     text_file.write("Hello, this is a was a string in my python code!.\n")
#     text_file.write("Hi I'm new here.\n")


# # Appending to a file.
# with open(file_path_text, "a") as text_file: # Appends to existing data. (Does not overwrite, creates file if it does not exist) 
#     # content = text_file.read()
#     # data.append(content)
#     text_file.write("Hello, this is a was a string in my python code!.\n")
#     text_file.write("Hi I'm new here.\n")















# # Using files in Loops:
# file_path_text = "test_file.txt"

# # Writing sample data to the text file
with open(file_path_text, "w") as text_file:
    text_file.write("This is the first line.\n")
    text_file.write("Python is amazing!\n")
    text_file.write("Learning file handling is cool!.\n")

# # Reading from the text file using a loop
with open(file_path_text, "r") as text_file:
    print("Content of the text file:")
    # iteration_counter = 0
    for line_number, line_content in enumerate(text_file, 1):
        # iteration_counter += 1
        # print(f"Iteration: {iteration_counter}")
        print(f"Line {line_number}: {line_content.strip()}")
    
    # for line in text_file:
    #     print([line])

