# my_str = "Jason, Jackson, 17"

# split_string = my_str.split(", ")

# print(split_string)


# print(split_string)

# split_string[1] = "was"

# print(split_string)

# my_str = " ".join(split_string)

# print(my_str)


# my_list = ['This', 'is', 'our', 'open', 'class', 'string!']

# for i, word in enumerate(my_list, 1):
#     print(i, word, sep=": ")

# user_choice = int(input("Please select a word by index: "))-1

# if 0 <= user_choice < len(my_list):
#     print(f"You chose the word: {my_list[user_choice]}")
# else:
#     print("Invalid index!")


# lst1 = ["Hello"]

# lst1.append("Goodbye")

# print(lst1)

my_str = "Jason, Jackson, 17"

if "Jack" in my_str:
    my_str = my_str.replace("Jason", "")
    print(my_str)
