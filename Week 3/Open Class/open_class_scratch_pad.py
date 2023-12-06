# Control: Loop -> While Loop :)

# total = 0 # Sum of the values
# counter = 0 # The amount of values entered by user

# for i in range(5):
#     user_input = int(input("Please enter a number: \ "))
#     counter += 1
#     total += user_input


# print(total)

# password = "LianO_123"


# if user_input.upper() != password.upper():
#     print("Password Invalid.")
# else:
#     print("Welcome")



# print("He said: \"This is how it looks\" ")





user_input = input("Enter a password: ")
print(user_input != "123")

while user_input != "123":
    user_input = input("Enter a password: ")

print("Welcome")

while True:
    # Within the scope of the while loop. (Local Scope)
    if user_input == "exit":
        break

# Global Scope
if user_input == "123":
    print("Valid")
