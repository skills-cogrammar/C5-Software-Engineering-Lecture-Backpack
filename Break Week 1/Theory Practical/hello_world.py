my_int = 5
my_float = 34.65
my_str = 'Hello World'
my_bool = True


# Operators
add_num = my_int + 20 + my_float
subtract_num = 40 - my_int
multiply_num = my_int * 5
divide = 20/4

add_str = my_str + "!"
new_str = "We can concatenate strings together" + " using the '+' oeprator."
multiply_str = "Hello"*20





# Output
# print("This is how we print to the terminal.")
# print(my_str)
# print(my_str, my_int, my_float, my_bool, sep="-")


# User Input
# name = input("Please enter your name: ")
# num = input("Please enter a number: ")
# num = int(num)
# print(type(num))


# # Comparison operators
# same_word = "Hello" == "Hello"
# same_num = 5 == 5.0

# not_same_word = "Hello" != "World"
# not_same_num = 10 != 30

# is_greater = 11 >= 10
# is_lesser = 15 <= 15

# has_substring = "ell" in "Hello"
# print(has_substring)









# # If-statements
# age = 19
# if age < 18:
#     print("You are not old enough to drive!")
# else:
#     print("You are old enough to drive.")


# user_input = input("Which do you prefer?\n1. Burgers\n2. Pizza\n")
# if user_input == "1":
#     print("Burgers all day every day!")
# elif user_input == "2":
#     print("Eight slices of greatness!")
# else:
#     print("No option selected")


# grade = 95
# if grade >= 90:
#     print("A grade")
# elif grade >= 80:
#     print("B grade")
# elif grade >= 70:
#     print("C grade")
# else:
#     print("You need improvement.")






# good_mood = "yes"

# is_weekend = input("Is it the Weekend? (yes/no)" )

# if is_weekend == "yes":
#     is_sunny = input("Is is sunny or rainy? (sunny/rainy) ")
#     if is_sunny == "sunny":
#         if good_mood == "yes": 
#             print("Visit the beach!")
#         else:
#             print("Take a nap")
#     else:
#         print("Relax at home.")
# else:
#     print("It's a weekday, focus on work or study.")


# num = 20
# if num > 10 and num < 30:
#     print(f"{num} is between 10 and 30")

# if num < 5 or num > 15:
#     print(f"{num} is smaller than 5 or larger than 15")


# user_choice = input("Do you like milkshakes? ")
# if user_choice == "yes" or user_choice == "y":
#     print("Milkshakes are great!")


# num1 = 10
# num2 = 0
# if num2 != 0 and (num1/num2)%2 == 0:
#     even_odd = "even"
# else:
#     even_odd = "odd"
# print(f"{num1} divided by {num2} produces and {even_odd} number!")

# my_str = "Hello"
# if not "World" in my_str:
#     print("'World' is not present in string.")

# if 10 != 10:
#     print("Condition is false.")


num = 11
# if num %2 == 0:
#     even_odd = "Even"
# else:
#     even_odd = "Odd"

even_odd = "Even" if num %2 == 0 else "Odd"
print(even_odd)