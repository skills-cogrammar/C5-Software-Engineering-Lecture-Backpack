# Output

# print("Hello World")
# print('This is how we can produce output through our console.')
# print("""We can use this as a tool to comunicate with our users.""")





# Input
# name = input("Please enter your name: ")
# print(name)
# input("Would you like to continue? (y/n)\n")







# Storing data

name = "Jacob"
surname = 'Brown'
age = 25
height = 176.5
has_license = True

# print(name, surname, age, height, has_license)

# output_str = f"Name:\t\t\t {name}\n"
# output_str += f"Surname:\t\t {surname}\n"
# output_str += f"Age:\t\t\t {age}\n"
# output_str += f"Height:\t\t\t {height}\n"
# output_str += f"Drivers License:\t {has_license}\n"
# print("Hello!\t\t:")
# print("Welcome!\t:")













# Conditions
# Equal
same_num = 5 == 5
same_word = "Welcome" == "welcome"

# Not Equal
not_same_num = 4 != 2
not_same_word = "Hello" != "World"

# Greater/Less than
# is_larger = "Yes" if 10 > 5 else "no"
# is_smaller = 3 < 9

# is_larger_alpha = "z" > "z"
# is_smaller_alpha = "b" < "d"


# #Greater/Less than or Equal
# is_larger_equal = 9 >= 10
# is_smaller_equal = 6 >= 6

# is_larger_alpha = "z" >= "z"
# is_smaller_alpha = "d" <= "d"









# if-elif-else

# num = 5
# if num >= 5:
#     print(num)



# question = 'Which planet is known as the "Red Planet" in our solar system?'
# choices = "A - Venus\t\tB - Mars\nC - Jupiter\t\tD - Saturn"
# answer = input(f"{question}\n{choices}\n: ")

# if answer.lower() == "b":
#     print("You are correct!") 
# else:
#     print("Unfortunately you are incorrect.")


# age = int(input("Please enter your age: "))

# if age < 13:
#     print("You are a child.")
# elif age < 18:
#     print("You are a teenager.")
# elif age < 100:
#     print("You are an adult.")
# else:
#     print("You have reached the age of wisdom.")









# Loops
# num = 10
# while num > 5:
#     print(num)
#     num -= 1



# user_choice = "y"
# while user_choice == "y":
#     print("Looping!")
#     user_choice = input("Would you like to loop again?")
#     print("Hello")


num = 10
# while True:
#     print(num)
#     num -= 1
#     if num == 5:
#         break


# menu = "Please select an option below:\n1 - Option A\n2 - Option B\n3 - Option C\n0 - Quit"
# while True:
#     user_choice = input(menu)
#     if user_choice == "1":
#         print("Option A selected!")
#     elif user_choice == "2":
#         print("Option B selected!")
#     elif user_choice == "3":
#         print("Option C selected!")
#     elif user_choice == "0":
#         break
#     else:
#         print("No option selected.")










# For loops

# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# print(7)
# print(8)
# print(9)
# print(10)

# for i in range(1, 11): # (1,2,3,4,5,6,7,8,9,10)
#     print(i)


# total = 0
# for _ in range(5):
#     user_num = input("Please enter a number: ")
#     user_num = int(user_num)
#     total += user_num

# print(f"The average of the numbers entered is {total//5}")


text = "This is a sentence."
# print(f"Text: {text}")
# user_letter = input("Please enter the letter you are looking for: ")
# for i, letter in enumerate(text):
#     if user_letter == letter:
#         print(f"Text contains the letter '{user_letter}' at index {i}!")
#         break
print(text[12])