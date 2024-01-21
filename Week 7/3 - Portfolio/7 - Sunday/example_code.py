log_string = "11/12/2023 12:30 | Order Placed | 512458 | London | Electronics"

# The line `file_path = "dummy_data.txt"` is assigning the string value "dummy_data.txt" to the
# variable `file_path`. This variable is used to store the path of the file that will be opened and
# read later in the code.
file_path = "dummy_data.txt"

# The line `with open(file_path, 'r') as log_file_object:` is opening the file specified by
# `file_path` in read mode. It creates a file object named `log_file_object` that can be used to read
# the contents of the file. The `with` statement ensures that the file is automatically closed after
# it is no longer needed, even if an exception occurs.
with open(file_path, 'r') as log_file_object:
    # `file_content = log_file_object.readlines()` is reading all the lines from the `log_file_object`
    # file and storing them as a list in the `file_content` variable. Each line in the file becomes an
    # element in the list.
    file_content = log_file_object.readlines()
    print(file_content)

    # The code `for line in file_content: print(line.split(" ; "))` is iterating over each line in the
    # `file_content` list and splitting each line using the delimiter " ; ". It then prints the
    # resulting list of substrings for each line.
    for line in file_content:
        print(line.split(" ; "))
