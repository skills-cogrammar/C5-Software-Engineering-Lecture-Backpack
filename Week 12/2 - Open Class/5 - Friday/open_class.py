
from datetime import date

our_date = "2024-02-22"
our_date = our_date.split("-")
our_date = list(map(lambda x: int(x), our_date))
our_date = date(our_date[0], our_date[1], our_date[2])
# print(f"our date: {our_date}")
# print(date.today())

if our_date < date.today():
    print("This day has passed.")

tasks = []

with open("tasks.txt", "r") as file:
    for line in file:
        split_line = line.strip().split(",")
        user_dict = {"username": split_line[0],
                     "title": split_line[1],
                     "description": split_line[2],
                     "due_date": split_line[3]}
        tasks.append(user_dict)

print(tasks)

for i, task in enumerate(tasks, 1):
    # print(task)
    print(f"{i} User: {task['username']}\tTask Name: {task['title']}\t"
          + f"Due date: {task['due_date']}")
    print("-"*80)

user_choice = int("1")-1
user_task = tasks[user_choice]
user_task['due_date'] = "2024-06-06"

print(tasks)



with open("tasks.txt", "w") as file:
    for task in tasks:
        file.write(f"{task['username']},{task['title']},{task['description']},{task['due_date']}\n")


# tasks.append("User,Todo,A task,2024-03-05")
# print(tasks)

# for i, task in enumerate(tasks, 1):
#     print(i, task)

