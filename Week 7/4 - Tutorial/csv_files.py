import csv
import pandas # terminal: python -m pip install pandas
from csv import writer
from csv import reader

# Example 2: Reading from a CSV File
csv_path = "example.csv"

# Writing sample data to the CSV file
with open(csv_path, "w", newline="") as csv_file:
    csv_writer = writer(csv_file)                   # Create a writer object (before actually writing to file)
    csv_writer.writerow(["Name", "Age", "City"])
    csv_writer.writerow(["Alice", 25, "London"])
    csv_writer.writerow(["Bob", 30, "Manchester"])
    csv_writer.writerow(["Charlie", 22, "Edinburgh"])

# Reading from the CSV file
with open(csv_path, "r") as csv_file:
    csv_reader = reader(csv_file)
    print("Content of the CSV file:")
    for row in csv_reader:
        print(row[2])



















# Using Loops:


# # Writing sample data to the CSV file
# with open(file_path_csv, "w", newline="") as csv_file:
#     csv_writer = csv.writer(csv_file)
#     csv_writer.writerow(["Name", "Age", "City"])
#     csv_writer.writerow(["Agreb", 25, "London"])
#     csv_writer.writerow(["Bob", 30, "Manchester"])
#     csv_writer.writerow(["Cassandra", 22, "Edinburgh"])

# # Reading from the CSV file using a loop
with open(csv_path, "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    print("Content of the CSV file:")
    for row_number, row in enumerate(csv_reader, 1):
        print(f"Row {row_number}: {'      '.join(row)}")