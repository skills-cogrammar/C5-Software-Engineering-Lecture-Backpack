import os
# Best Practices

# 1. Always use the with() statement
with open("random_names.txt", 'r') as file_object:
    content = file_object.read()
    # print(content)

# 2. Handle exceptions try/except
## Error Handling
try:
    with open("random_names.txt", 'r') as file_object:
        content = file_object.read()
except FileNotFoundError:
    print("File not found!")
except IOError as e:
    print(f"Error encountered: {e}")

## File Existence using OS library
file_path = "random.txt"

if os.path.exists(file_path):
    with open("random_names.txt", 'r') as file_object:
        content = file_object.read()
else:
    print(f"File '{file_path}' does not exist!")

# 3. Specify Encoding
with open("sub_folder/list_of_birds.txt", 'r', encoding='utf-8') as file_object:
    content = file_object.read()
    print(content)

# 4. Dynamic Paths
file_path = "sub_folder/list_of_birds.txt"

with open(file_path, 'r', encoding='utf-8') as file_object:
    content = file_object.read()
    print(content)

# using the os library
file_path = os.path.join("your directory", "name of the file")
