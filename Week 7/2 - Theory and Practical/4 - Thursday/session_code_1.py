# Writing to files

# Example 1
with open("list_of_cats.txt", 'a') as file:
    file.write('\nMr boo')


# Example 2
lines_I_write = ["pluto", "is", "a", "planet", "let's", "remember", "that", "in", "our", "hearts"]
# with open("serge_manifesto.txt", "w+") as file:
#     new_sent = " ".join(lines_I_write)
#     file.writelines(new_sent)

# Example 3
with open("serge_manifesto.txt", "a+") as file:
    new_sent = " ".join(lines_I_write)
    file.seek(5)
    file.write(new_sent)