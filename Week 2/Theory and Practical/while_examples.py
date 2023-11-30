"""WHILE LOOPS"""

# Example 1: Print numbers from 1 to 5 using a while loop
count = 1
while count <= 5:
    print(count)
    count += 1


# Example 2: Calculate the sum of numbers until a certain condition is met
total = 0
num = 1
while total < 10:
    total += num
    num += 1
print("Sum:", total)


# Example 3: Repeatedly prompt the user until valid input is received
user_input = ''
while user_input.lower() != 'yes':
    user_input = input("Do you want to continue? (yes/no): ")


# Example 4: Repeatedly prompt the user to input a menu option
user_input = ''
while True:
    menu = """Please select an option below:
1: Option 1
2: Option 2
3: Option 3
4: Quit
"""
    user_input = input(menu)
    if user_input == "1":
        print("Option 1 chosen")
    elif user_input == "2":
        print("Option 2 chosen")
    elif user_input == "3":
        print("Option 3 chosen")
    elif user_input == "4":
        print("Goodbye.")
        break


# Example 5: Number guessing game
import random

target_number = random.randint(1, 100)
guess = None
attempts = 0

while guess != target_number:
    guess = int(input("Guess the number (between 1 and 100): "))
    attempts += 1
    if guess < target_number:
        print("Too low! Try again.")
    elif guess > target_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
