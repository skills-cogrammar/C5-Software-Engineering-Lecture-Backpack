# hello = "Hello"
# world = "world"

# new_string = "{},{},{},{}!".format(h=hello, w=world)

# print(new_string)






# my_str = "Armand"

# my_str = my_str.replace("d", "t")

# print(my_str)

# num_str = ["Hello", "World"]
# num_str = int(num_str)

# print(type([{"this"}]))

# [{"this"}]

# "Hello world"

# products = [["Dog food", 15, 3], ["Cat food", 20, 2]]

# print(products[0][0])



"""
Count vowels and consonants

create constant with vowels
create constant with consonants

get string from the user
create a variable to count vowels
create a variable to count consonants

iterate over string using a for loop
    if the letter is a vowel 
        increment vowel count
    if the letter is a consonants 
        increment consonants count

output total amount of vowels and consonant to the user

"""

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwqxyz"

user_input = input("Please enter some text to count the vowels and consonants:\n")
vowel_count = 0
consonant_count = 0

for letter in user_input.lower():
    if letter in VOWELS:
        vowel_count += 1
    elif letter in CONSONANTS:
        consonant_count += 1

print(f"The total number of vowels is {vowel_count} and the total"
      + f" number of consonants is {consonant_count}.")



