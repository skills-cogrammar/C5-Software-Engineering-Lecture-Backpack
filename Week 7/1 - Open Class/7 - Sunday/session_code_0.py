# Example 1
# with open("temp_text.txt", 'r') as file:
#     content = file.readlines()
#     print(content)

#     for pos, line in enumerate(content, 1):
#         print(pos, line)


# Example 2
# poke_list = ["pika", "squirtle", "psyduck"]

# poke_combat = {"pika": 78, "squirtle": 87, "psyduck": 66} # stock 
# poke_field = {"pika": 45, "squirtle": 56, "psyduck": 68}  # price

# for poke in poke_list:
#     print(f"{poke} has a combined strength of about: {poke_combat[poke] * poke_field[poke]} xp")
#     # print(poke_combat[poke] * poke_field[poke])

poke_combat = {}
poke_field = {}

# Example 3 - Exercise (populate the data back into the dictionaries accurately)
with open("temp_text_1.txt", 'r') as file:
    content = file.readlines()
    print(content)
    for pos, line in enumerate(content):
        # print(line)
        combat_values = line.split(", ")
        # print(combat_values)
        for stat in combat_values:
            # print(stat)
            if pos == 0:
                stat_split = stat.split(": ")
                print(stat_split[0])
                poke_combat.update({stat_split[0].strip():stat_split[1].strip()})

print(poke_combat)