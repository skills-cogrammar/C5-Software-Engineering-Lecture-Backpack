
# for i in range(1,6):
#     for _ in range(i):
#         print(">", end="")
#     print()

# num = 5

# for i in range(10):
#     if i == 5:
#         print("Your num is 5")
#     else:
#         print("Your num is not 5")


"""
ask the user to press enter or enter the word "stop"
while the user has not entered "stop"
    print "Hello"
    ask the user to press enter or enter the word "stop"
"""

# user_input = input("Please press enter or enter the word 'stop': ")


while user_input.upper() not in ["STOP", "EXIT", "END"]:
    print("Hello")
    user_input = input("Please press enter or enter the word 'stop': ")

print()


num1 = 10
num2 = 20

ave = (num1 + num2) / 2
print(ave)









