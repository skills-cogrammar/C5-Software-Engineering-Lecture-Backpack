# File Reading

# Traditional Method
# cat_names_object = open("randomOtherFolder\cat_names.txt", 'r')
cat_names_object = open("list_of_cats.txt", 'r')
# print(cat_names_object)

# Read Method
# `cat_names_read = cat_names_object.read()` is reading the entire contents of the file
# `cat_names_object` and storing it in the variable `cat_names_read`.
cat_names_read = cat_names_object.read()
print(cat_names_read)

# Readline Method
# `cat_names_readline = cat_names_object.readline()` is reading a single line from the file object
# `cat_names_object` and storing it in the variable `cat_names_readline`.
cat_names_readline = cat_names_object.readline()
print(cat_names_readline)

# Readlines Method
# `cat_names_readlines = cat_names_object.readlines()` is using the `readlines()` method to read all
# the lines of the file object `cat_names_object` and store them in the variable
# `cat_names_readlines`. The `readlines()` method returns a list where each element is a line from the
# file.
cat_names_readlines = cat_names_object.readlines()
print(cat_names_readlines)

# `cat_names_object.close()` is closing the file object `cat_names_object`. This is important to do
# after reading or writing to a file, as it frees up system resources and ensures that the file is
# properly closed.
cat_names_object.close()

# Best Practice Approach 
with open("list_of_cats.txt", 'r') as cat_names_object:

    # print(cat_names_object)

    # Read Method
    cat_names_read = cat_names_object.read()
    print("\n Read Output: ")
    print(cat_names_read)

    # `cat_names_object.seek(0)` is used to move the file pointer to the beginning of the file. This
    # allows you to read the file from the start again, even if you have already read it once before.
    # In the given code, it is used to reset the file pointer before using the `readline()` and
    # `readlines()` methods to read the file again.
    cat_names_object.seek(0)

    # Readline Method
    cat_names_readline = cat_names_object.readline()
    print("\n Readline Output: ")
    print(cat_names_readline)
    
    cat_names_object.seek(0)

    # Readlines Method
    cat_names_readlines = cat_names_object.readlines()
    print("\n Readlines Output: ")
    print(cat_names_readlines)
