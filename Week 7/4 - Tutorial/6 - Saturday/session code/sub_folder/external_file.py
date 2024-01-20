# accessing from an external file

with open("list_of_cats.txt", 'r') as file:
    content = file.read()
    print(content)