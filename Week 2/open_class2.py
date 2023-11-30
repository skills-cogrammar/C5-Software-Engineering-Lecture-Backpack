# # print("Hello")
# # print("Hello")
# # print("Hello")
# # print("Hello")
# # print("Hello")

# # for i in range(5):
# #     print("Hello")

# # new_string = "Hello world!"

# # for letter in new_string:
# #     if letter == "l":
# #         continue
# #     print(letter)



# # my_string = "Hello"
# # new_string = ""
# # end_index = len(my_string)-1

# # for i in range(end_index, -1, -1):
# #     new_string += my_string[i]

# # print(new_string)




# my_string = "Hello"
# new_string = ""

# for letter in my_string:
#     if letter == 'l':
#         new_string += letter.upper()
#         continue
#     new_string += letter

# print(new_string)


# # for i in range(5):
# #     for j in range(3):
# #         print(i, j)


# # for i in range(1, 6):
# #     print("@"*i)


# for i in range(5):
#     print(i)

for i in range(5):
    if i == 3:
        continue
    print(i)

print("done")

counter = 0

for i in range(10):
    if counter == 5:
        break
    print(counter)
    counter += 1

