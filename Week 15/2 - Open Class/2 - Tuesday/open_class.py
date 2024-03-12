# num_list = []

# with open("data.txt", "r") as file:
#     for line in file:
#         num_list.append(line.strip())

# print(num_list)

# with open("new_data.txt", "w") as file:
#     for i in range(1, 7):
#         file.write(f"{i}\n")
 
# with open("new_data.txt", "a") as file:
#     for i in range(7, 11):
#         file.write(f"{i}\n")

# users = []

# with open("data/data.txt", "r") as file:
#     file.readline()
#     for line in file:
#         users.append(line.strip().split(", "))
#     # users = file.readlines()[1:]

# print(users)

# print("Name\tSurname\tAge\tID")
# for user in users:
#     print(f"{user[0]}\t{user[1]}\t{user[2]}\t{user[3]}")

# users[0][1] = "Brown"

# with open("new_data.txt", "w") as file:
#     file.write("Name,Surname,Age,ID\n")
#     user_string = ""
#     for user in users:
#         user_string += ",".join(user) + "\n"
#     file.write(user_string)


# my_list = [1,2,3]
# my_list.append(4)
# new_list = [5,6,7,8]
# my_list.extend(new_list)
# print(my_list)

i = 0
while i < 10:
    if i%2 == 0:
        i += 1
        continue
    print(i)
    i += 1

# for i in range(10):
#     if i%2 == 0:
#         continue
#     print(i)


i = 0
while i < 10:
    if i == 10:
        i += 1
    elif i == 5:
        i += 5
    break


my_str = "1-2-3-4-5-6-7"
my_str += "-8"
split_str = my_str.split("-")
print(split_str)

joined_str = " ".join(split_str)
print(joined_str)



