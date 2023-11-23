# # Example 1: Basic if statement
age = 17

if age >= 18:
    print("You are eligible to vote.")
else:
    print("Sorry, you are not eligible to vote yet.")

# Example 2 [Challenge]: if-elif-else chain
grade = 84

if grade > 90:
    print("A grade")
elif grade > 70:
    print("C grade")
elif grade > 80:
    print("B grade")
else:
    print("You need improvement.")

# Example 4: Nested if statements
is_weekend = input("Is it the Weekend? (yes/no)" )
is_sunny = input("Is is sunny or rainy? (sunny/rainy) ")
good_mood = "no"


if is_weekend == "yes":
    if is_sunny == "sunny":
        if good_mood == "yes": 
            print("Visit the beach!")
        else:
            print("Take a nap")
    else:
        print("Relax at home.")
else:
    print("It's a weekday, focus on work or study.")
