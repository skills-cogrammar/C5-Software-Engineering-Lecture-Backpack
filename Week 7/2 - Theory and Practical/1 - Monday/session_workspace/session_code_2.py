# Iterating Over a file
with open("random_names.txt", 'r') as file:
    file_contents = file.readlines()
    # print(file_contents)
    for line in file.readlines():
        print(line)

# Exception Handling
# FileNotFound 
# IOError  

# The code is using exception handling to handle potential errors that may occur when opening and
# reading a file.
try:
    with open("random_names.txt", 'r') as file:
        file_contents = file.readlines()
except FileNotFoundError:
    print("File not found! ")
except IOError as e:
    print(f"Error reading the file: {e}")


# Exceptin handling with traditional approach
random_names = open("random_names.txt", 'r')
try:
    content = random_names.read()
finally:
    file.close()
