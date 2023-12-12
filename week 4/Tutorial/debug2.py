# # Calculate average of 2 numbers
# num1 = 10
# num2 = 5
# average = (num1 + num2) /2
# print(average)












# # Sum numbers within a given range
# total = 0
# for i in range(10):
#     total += i
# print("Debug print on line 22: ", total)







# # # # Retrieve number from user and print numbers 1 up to user number
# user_num = input("Please enter a number: ")
# if user_num.replace(".", "", 1).isnumeric(): # Removing "." to include float values
#     user_num = int(user_num)
#     print(type(user_num))
#     for i in range(user_num):
#         print(i)
# else:
#     print("You did not enter a number!")

# print("12312.12".replace(".", "", 1).isnumeric())




# Divide a given number with each number in a range
# given_num = 10

# for i in range(1, 11):
#     if i > 0:
#         print(given_num/i)


# even = []
# odd = []
# for i in range(21):
#     if i%2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)

    

# print("Even numbers: ", even)
# print("Odd numbers: ", odd)

def my_print(text):
    print(text)

def sum_all_values(values):
    my_print()
    total = 0 
    for num in values:
        total += num
    return total

my_print("Hello")
numbers = [2,3,4,5,6,3,4,5]

result = sum_all_values(numbers)
print(result)

# "Hello".replace("l", "@")





