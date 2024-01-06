

# Using user input in dictionary as value
# user_dict = {"name": "",
#              "surname": ""}

# name = input("Please enter your name: ")
# surname = input("Please enter your surname: ")

# user_dict["name"] = name
# user_dict["surname"] = surname

# user_dict.update(name=name, surname=surname)

# print(user_dict)






# Using user input in dictionary as key
# user_dict = {}

# name = input("Please enter your name: ")
# surname = input("Please enter your surname: ")

# # user_dict[name] = surname
# user_dict.update({name : surname})

# print(user_dict)







# sounds = {"Dog": "Woof",
#           "Cat": "Meow",
#           "Bird": "Tweet",
#           "Mouse": "Squeek",
#           "Cow": "Moo",
#           "Frog": "Croak",
#           "Elephant": "Toot",
#           "Duck": "Quack",
#           "Fish": "Blub",
#           "Seal": "Ow Ow Ow"}

# while True:
#     print("Please enter the name of an animal below:\n")
#     for animal in sounds:
#         print(f"--{animal}--")
        
#     user_animal = input(": ").capitalize()
#     sound_list = ["Fish", "Seal", "Cow"]
#     for sound in sound_list:
#         if user_animal not in sounds:
#             print("Animal not in list.")
#             continue

#     print(f"Animal: {user_animal} Sound: {sounds[user_animal]}")
#     break


# sound_list = ["Fish", "Seal", "Cow", "Lizard"]
# for sound in sound_list:
#     if sound in sounds:
#         print(f"Animal: {sound} Sound: {sounds[sound]}")

# print(len(sounds))









input_grid = [
    ["-", "#", "-", "#", "#"], # [0][0] 
    ["#", "-", "-", "#", "#"], # [x+1][2]
    ["-", "#", "-", "-", "-"],
    ["-", "-", "-", "-", "#"],
    ["#", "#", "-", "-", "-"]
]

rows = len(input_grid)
cols = len(input_grid[0])

output_grid = [['' for _ in range(cols)] for _ in range(rows)]
# print(output_grid)

for i in range(rows):  
    for j in range(cols):
        # If current cell = "#" send to output grid.
        if input_grid[i][j] == '#':
            output_grid[i][j] = '#'
        else:
            # Count mines surrounfing this spot (incl diagonals)
            mine_counter = 0
            for x in range(max(0, i - 1), min(rows, i+2)):
                for y in range(max(0, j -1), min(cols, j+2)):
                    if input_grid[x][y] == '#':
                        mine_counter += 1

            # send to output grid.       
            output_grid[i][j] = mine_counter