





# for i in range(5):
#     if i == 3:
#         break
#     else:
#         print(i)

# print("After for loop")
# print(i)


# range_limit = input("Please enter a number: ")

# range_limit = int(range_limit)

# for num in range(range_limit):
#     print(num)


# base = 2
# power = 3
# total = base

# for i in range(power-1):
#     total *= base

# print(total)

"""
define a list numbers
define a total variable

loop over each number in list
    if number is even add to total

print total
"""

numbers = [1, 2, 3, 4, 5, 6]   
total = 0

# for i in numbers:
#     if i % 2 == 0:
#         total += i

# print(total)




"""
define a string to reverse
define a variable to store reversed string

get the length of string

loop over string starting from last index
    add each letter to new reversed string variable

print reversed string to user
"""

my_string = "Hello"
reversed_string = ""

max_index = len(my_string)-1
for i in range(max_index, -1, -1):
    reversed_string += my_string[i]

print(my_string[4])




