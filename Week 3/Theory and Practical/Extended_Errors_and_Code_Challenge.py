# Error Types Example

# Syntax Error
# Uncomment the line below to see a syntax error
# print("Hello, World!"


# NameError
# Uncomment the line below to see a NameError
# print(first_name)


# number = "5"
# TypeError
# Uncomment the line below to see a TypeError
# result = int("5") + 3
# print(result)

# IndexError
# Uncomment the line below to see an IndexError
# numbers = [1, 2, 3]
# #          0  1  2  3
# print(numbers[2])

# FileNotFoundError
# Uncomment the line below to see a FileNotFoundError
# with open("nonexistent_file.txt", "r") as file:
#     content = file.read()



"""
START

print a the welcome text. (Use "-" as dividers)

Prompt the user for an number. (Might want to consider accounting
for events where the user enters non-numerical values such as letters
or symbols.)

Take the user's input and return it to the power of 3 (user_input ** 3)

END
"""

# Start 

# LINE = "-" * 100
# WELCOME = "Welcome to the square app!"
# END = "Goodbye"

# print(f"{LINE}\n{WELCOME}\n{LINE}")



# user_number = int(input("Please enter any number greater than ZERO (>0): "))

# while user_number <= 0:
#     user_number = int(input("Nope, please enter a value greater than zero: "))

# result = f"{user_number} to the power of 3 is: {user_number ** 3}"

# print(result)
# print(f"\n\n {LINE}\n{END}\n{LINE}")

# password = ""
# if password != "123":
#     print("Incorrect Password (Case Sensitive)")
# else:
# print("Logged in. Welcome Back!")

# for i in range(1, 10):
#     if i == 5:
#         print("Halfway :)")


string = "myMu"
new = ""
for letter in range(len(string)):
    # Swap lower to upper and vice versa    
    if string[letter] == string[letter].lower():
        new += string[letter].upper()
    else:
        new += string[letter].lower()
    
print(new)