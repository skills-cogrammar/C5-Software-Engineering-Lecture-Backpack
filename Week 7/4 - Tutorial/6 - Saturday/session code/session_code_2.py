# Reading and Writing

# Writing Recap

# W - opening file for writing

try:
    with open('list_of_planets.txt', 'x') as file:
        # process the logic
        pass
except FileExistsError:
    print("oops, file does exist 😓")
# Modes when writing to file
"""
w - open file for writing and create if it doesn't exist, or overwrite if it does
a - open for writing and appending to existing file. create if it doesn't exist
x - open for creation only, it will fail if the file does exist.
"""

# Write Methods
"""
write() - it is used to write content to the file
writelines() - write list of characters from iterable (list, dictionary) to the file
"""
# write() method example

random_string = "Pluto is a planet NASA, stop being mean"

with open('message_to_NASA', 'w') as file:
    file.write(random_string)

# writelines() method example
lines_to_file = ["thor", "hulk", "wonder woman", "deadpool", "professor x", "barney the dinosaur"]

with open('comic_char.txt', 'w') as file:
    for line in lines_to_file:
        file.writelines(line + "\n")

# Append to file
with open("comic_char.txt", "a") as file:
    file.write("aang\n")
    file.write("cabbage man")
