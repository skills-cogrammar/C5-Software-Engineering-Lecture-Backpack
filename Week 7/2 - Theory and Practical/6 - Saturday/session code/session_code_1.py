import os
# Opening File

# file_path = "random_names.txt"

# file_object = open("list_of_cats.txt", 'r')
with open("list_of_cats.txt", 'r') as file_object:
    # process our logic within this body
    pass

# Read Methods
with open("random_names.txt", 'r') as file:
    # Read() - read the entire file
    print("Read Output: ")
    file_content = file.read()
    print(file_content)

    file.seek(0)

    # Readline() - read in the first line only
    print("\nReadline Output: ")
    file_content = file.readline()
    print(file_content)

    file.seek(0)

    # Readlines() - read all lines as items within a list
    print("\nReadlines Output: ")
    file_content = file.readlines()
    print(file_content)

# Iterating over files
with open("random_names.txt", 'r') as file:
    file_content = file.readlines()
    print(file_content)

    for line in file_content:
        jedi_name = line.strip()
        # print(f"Jedi Name: {jedi_name}")

        if jedi_name == "r2d2":
            print(f"{jedi_name} is an imposter. They aren't a Jedi YET!")
        else:
            print(f"{jedi_name} is a Jedi!")

# Exception Handling
# with() approach 
try:
    with open("random_dance_session.txt", 'r') as file:
        file_content = file.read()
except (FileNotFoundError, IOError) as e:
    print(f"Error encountered: {e}")

# tradional approach
file_object = open("random_names.txt", 'r')
try:
    file_content = file_object.read()
    print(file_content)
except (FileNotFoundError, IOError) as e:
    print(f"Error encountered: {e}")
finally:
    file_object.close()

# Dynamic File Paths
# approach 1
file_path = "random_names.txt"
with open(file_path, 'r') as file:
    file_content = file.readlines()

# approach 2
# sat_session_workspace\random_names.txt
file_path = os.path.join("your directory", "random_names.txt")

# Encoding 
with open("random_names.txt", 'r', encoding='utf-8') as file:
    file_content = file.readlines()
    print(file_content)
