import csv

# Example 1 - UTF-8
content = "UTF-8 Encoded Text. This is the japanese word for pluto: 冥王星"

with open("utf_8_file.txt", 'w', encoding='utf-8') as file:
    file.write(content)

# Example 2 - Latin-1
content = "This is a french word: café"
with open("latin_1_file.txt", 'w', encoding='latin-1') as file:
    file.write(content)
    # Note - In VsCode the file can be opened with the Central European (Windows 1250) encoding

# Example 3 - Different file format 
twod_list_to_write = [
    ["name", "age", "city"],
    ["serge", "456", "pluto-metropolitan"],
    ["pika", "34", "antarctica"]
]

with open('random_utf-8_csv.csv', 'w', newline='', encoding='utf-8' ) as file:
    writer_instance = csv.writer(file)
    writer_instance.writerows(twod_list_to_write)
