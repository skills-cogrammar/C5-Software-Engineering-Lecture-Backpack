file_path_cats = "list_of_cats.txt"
file_path_birds = "sub_folder/list_of_birds.txt"

# Example 1 - iterating over file
with open(file_path_cats, 'r') as file:
    file_content = file.readlines()
    for line in file_content:
        print(line.strip())


# Example 2 - cat count
with open(file_path_cats, 'r') as file:
    file_content = file.readlines()
    cat_count = len(file_content)

print(f"Number of cats: {cat_count}")

# Example 3
with open(file_path_cats, 'r') as file:
    file_content = file.readlines()

    for pos, line in enumerate(file_content, 1):
        print(pos, line.strip())

# Example 4
with open(file_path_cats, 'r') as cat_file, open(file_path_birds, 'r') as bird_file:
    print("Cats in daycare: ")
    for line in cat_file.readlines():
        print(line.strip())

    print("\nBirds in daycare: ")
    for line in bird_file.readlines():
        print(line.strip())
