# Can we show an error message if 
# there is a white space line in the text file?

with open("secret_secret_pokemon.txt", 'r') as file:
    content = file.readlines()

    print(content)


