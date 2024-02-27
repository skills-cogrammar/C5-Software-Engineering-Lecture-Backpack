from datetime import datetime

date = "2024 10 Apr"
date_obj = datetime.strptime(date, "%Y %d %b").date()
# print(date_obj)

# now = datetime.now().date()
# print(now)

# if date_obj > now:
#     print(f"{date_obj} is after {now}.")

# date_obj = datetime.strptime(t[due_date], "%Y %d %b").date()
# today > date_obj

# task_data = [t for t in task_data if t != ""]

tasks = []
with open("data.txt", "r") as file:
    for line in file:
        tasks.append(line.strip().split(", "))    

print(tasks[0])
print(", ".join(tasks[0]))

# for user in users:
    
#     for task in tasks:
#         date = datetime.strptime(task[3], "%d %b %Y").date()
#         print(date)
    

x, y, z = 3, 5, 6