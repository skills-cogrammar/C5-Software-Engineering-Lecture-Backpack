# name = "Jack"
# age = 20

# my_str = f"Hello {name}, you are {age} years old!"
# other_str = "Hello {}, you are {} years old!".format(name, age)


# num = 10
# num += 5
# # print(num, end="-")

# # print("Jack")

# names = ["Jack", "Jill", "Jane", "John"]
# # for i in range(len(names)):
# #     print(i, names[i], sep=": ")


# # for i, name in enumerate(names, 1): # ((0, "Jack"), (1, "Jill"), (2, "Jane"), (3, "John"))
# #     print(i, name, sep=": ")


# our_str = "Welcome to the open class!"
# print(our_str[::-1])

# words_to_remove = ["to", "open"]
# our_str = "Welcome to the open class!"
# split_str = our_str.split()
# for word in words_to_remove:
#     split_str.remove(word)
# our_str = " ".join(split_str)
# print(our_str)

# user = "jack,35,email@gmail.com"
# user = user.split(',')
# user[2] = "new.email@gmail.com"
# user = ",".join(user)
# print(user)


# str1 = "Hello"
# str2 = "World"

# new_str = ["" for i in range(3)]
# for i in range(3):
#     for letter1, letter2 in zip(str1, str2):
#         if letter1 > letter2:
#             new_str[i] += letter1 + letter2
#         else:
#             new_str[i] += letter2 + letter1

# print(new_str)
            
str1 = "Hello"
str2 = "World@@@@"
str2 = str2.replace("@", "")

# for letter1, letter2 in zip(str1, str2):
#     print(letter1, letter2, sep=" - ") 


my_list = [3,4,2,5,3]
my_list.sort()
print(my_list)