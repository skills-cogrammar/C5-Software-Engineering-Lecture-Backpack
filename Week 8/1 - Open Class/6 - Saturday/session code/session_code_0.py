# read in data and cleanse
poke_stat_dict = {}

def login_read():
    """
    login function
    """
    list_of_users = []
    with open("poke_users.txt", 'r+') as file:
        for line in file:
            list_of_users.append(line.strip('\n'))
    
    while True:
        user_name = input("Enter your username: ")

        if user_name in list_of_users:
            print(f"Welcome {user_name}")
            return user_name
        else:
            print("You aren't a registerd pokemon trainer. Please register")


def view_pokemon():
    """
    function to load the pokemon data and print it to screen
    """
    with open("ash_poke_stat.txt", "r+") as file:
        content = file.readlines()

        # print(content)

        for line in content:
            # print(f"current line data: {line}")
            line_split = line.split(", ")
            # print(line_split)

            # if line_split[1] == "electric":
            #     print("true it is electric")
            # else:
            #     print("naaawrrr ") 

            poke_name = line_split[0]
            poke_type = line_split[1]
            poke_math_score = line_split[2]
            poke_combat_score = line_split[3].strip()

            poke_stat_dict[poke_name] = [poke_type, poke_math_score, poke_combat_score]

    for key, value in poke_stat_dict.items():
        print(f"{key}, {value[0]}, {value[1]}, {value[2]}\n")


logged_in_user = login_read()

while True:
    if logged_in_user == "ash":
        print("1. Register your friend \n2. Add Pokemon \n3. View Pokemon \n4 Exit")
    else:
        print("1. Add Pokemon \n2. View Pokemon \n3 Exit")

    user_input = input("Enter your choice: ")

    if user_input == "1":
        pass
    elif user_input == "2":
        view_pokemon()
    elif user_input == "3":
        print("Thank for using program, bye")
        break
    else:
        print("Incorrect input entered")


# # Printing out values
# # for key, value in poke_stat_dict.items():
# #     print(key, value)

# # access a specific key
# # print(poke_stat_dict["psyduck"])

# # Editing information
# poke_stat_dict["bulbasuar"] = ["grass", 90, 1200]
# print(poke_stat_dict)


# # # adding new pokemon stat to dictionary 
# # poke_stat_dict["sunflora"] = ["grass", 45, 12]

# # print(poke_stat_dict)

with open("ash_poke_stat.txt", "w+") as file:
    for key, value in poke_stat_dict.items():
        file.write(f"{key}, {value[0]}, {value[1]}, {value[2]}\n")