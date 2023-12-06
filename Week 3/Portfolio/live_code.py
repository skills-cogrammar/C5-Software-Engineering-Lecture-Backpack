"""
Start 

Display a menu with options related to shopping cart
Implement While loop to keep the menu running (after user has selcted options)
Provide the user with the option to end the program (Break out of while)

End
"""

# print("Welcome to my shop!\n")
# while True:
#     menu = input(" Select one of the following:\n\
#              1. Add Item \n\
#              2. Remove Item \n\
#              3. Update Item \n\
#              4. Exit Cart\n\
#              :\t")
    
#     if menu == "1":
#         print("Added Item")
#     elif menu == "2":
#         print("Item removed")
#     elif menu == "3":
#         print("Item updated")
#     elif menu == "4":
#         print("Have a good day!")
#         break
#     else:
#         print("Invalid option")


# Add 1 to this variable for every iteration (Increment by 1)
counter = 0

# Looping 3 times (Iterating 3 times)
for i in range(3):
    # Incrementing counter variable by 1
    counter += 1

# Printing updated counter variable
print(counter)