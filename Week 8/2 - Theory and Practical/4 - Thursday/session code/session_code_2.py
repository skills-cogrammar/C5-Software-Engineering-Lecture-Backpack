# read in data and cleanse

poke_stat_dict = {}

with open("dummy_data.txt", "r+") as file:
    content = file.readlines()

    print(content)

    for line in content:
        line_split = line.split(", ")
        print(line_split)

        poke_name = line_split[0]
        poke_type = line_split[1]
        poke_math_score = line_split[2]
        poke_combat_score = line_split[3].strip()

        poke_stat_dict[poke_name] = [poke_type, poke_math_score, poke_combat_score]

print(poke_stat_dict)

# access a specific key
# print(poke_stat_dict["psyduck"])

# Editing information
poke_stat_dict["bulbasuar"] = ["grass", 90, 12]

# adding new pokemon stat to dictionary 
poke_stat_dict["sunflora"] = ["grass", 45, 12]

print(poke_stat_dict)

with open("dummy_data.txt", "w+") as file:
    for key, value in poke_stat_dict.items():
        file.write(f"{key}, {value[0]}, {value[1]}, {value[2]}\n")