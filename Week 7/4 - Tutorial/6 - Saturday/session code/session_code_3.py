import csv
import json
from tabulate import tabulate

# # Writing to CSV
# poke_grade_list = [
#     ["Name", "Field Work Score", "Combat Score", "Mathematics Score"],
#     ["Pikachu", 85, 83, 56],
#     ["Squirtle", 90, 75, 70],
#     ["Psyduck", 70, 50, 97]
# ]

with open('poke_stats.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(poke_grade_list)


# Writing to JSON
psy_poke_stat = {
    "name": "Psyduck",
    "Field Work Score": 70,
    "Combat Score": 50,
    "Mathematics Score": 97
}

with open('psyduck.json', 'w') as file:
    json.dump(psy_poke_stat, file, indent=2)

# updating JSON file

pika_poke_stat = {
    "name": "Pikachu",
    "Field Work Score": 85,
    "Combat Score": 83,
    "Mathematics Score": 56
}

# append mode to new file
with open('pika.json', 'a') as file:
    json.dump(pika_poke_stat, file, indent=2)

# Reading CSV and JSON file
csv_file_path = 'poke_stats.csv'

with open(csv_file_path, 'r') as csv_file_object:
    csv_file_object_reader = csv.reader(csv_file_object)

    # tabulate approach
    table_data = tabulate(csv_file_object_reader, headers='firstrow', tablefmt="fancy_grid")
    print(table_data)

    # for-loop approach
    # for row in csv_file_object_reader:
    #     print(row)


# Reading JSON
json_file_path = 'pika.json'

with open(json_file_path, 'r') as json_file:
    pika_data = json.load(json_file)
    # print(pika_data)

    pika_table = tabulate(pika_data.items(), headers=['Key', 'Value'] )
    print(pika_table)
