"""WHILE LOOPS"""

# while True:
#     print("I'm a loop")
#     question = input("Continue? (y/n)").lower()

#     if question == 'y':
#         print("Back to the beginning!")
#         continue

#     else:
#         print("I shall cease")
#         break




# # Example 1: Print numbers from 1 to 5 using a while loop
# counter = 1
# while counter <= 5: 
#     print(counter)
#     counter += 1



# Example 2: Calculate the sum of numbers until a certain condition is met
# total = 0
# num = 1
# while total < 10:
#     total += num
#     print("Total: ", total)
#     num += 1
#     print("Num: ", num)


# print("Sum:", total)


# Example 3: Repeatedly prompt the user until valid input is received
# user_input = ''
# while user_input.lower() != 'yes':
#     user_input = input("Do you want to break? (yes/no): ")

# Check if the user has entered a valid password:
# password = input("Please enter your password:\t")
# while password != "User_B@d_P@ss_123":
#     password = input("Incorrect! \n Please re-enter your password (Case Sensitive):\t")

# print("Valid Password, welcome!")

# while True:
#     user_input = input("Do you want to break out? (yes/no): ")

#     if user_input == "yes":
#         print("Breaking out :)")
#         break




# Example 4: Repeatedly prompt the user to input a menu option
# user_input = ''
# while True:
#     menu = """Please select an option below:
# 1: Option 1
# 2: Option 2
# 3: Option 3
# 4: Quit
# """
#     user_input = input(menu)
#     if user_input == "1":
#         print("Option 1 chosen")
#     elif user_input == "2":
#         print("Option 2 chosen")
#     elif user_input == "3":
#         print("Option 3 chosen")
#     elif user_input == "4":
#         print("Goodbye.")
#         break


# Example 5: Number guessing game
import random

random_number = random.randint(1, 100)
guess = None
attempts = 0

while guess != random_number:
    guess = int(input("Guess the number (between 1 and 100): "))
    attempts += 1
    if guess < random_number:
        print("Too low! Try again.")
    elif guess > random_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
