# Try-Except

# '+'  '-' '*' '/'
# Arithmetic Errors
# ZeroDivisionError



# operation = input("What would you like to do with these values?\
#                   '+'  '-' '*' '/' ")

# error = True
# while error:
#     num_1 = input("Enter a number: ")
#     num_2 = input("Enter another number: ")
#     try:
#         result = int(num_1) / int(num_2)
#         print(f"Result: {result}")
#         error = False
#     except ZeroDivisionError:
#         print("Oops, you cannot divide by 0.")
#     finally:
#         print("Thank you for using our calculator.")

# While there is an error:
#    run the code again

# counter = 10
# while True:
#     counter -= 1
#     if counter == 0:
#         break
#     else:
#         print(counter)


age =  int(input("Enter your age: "))
if age < 0:
    # Manually raising an exception:
    raise Exception("Your age can't be less than 0! ")
