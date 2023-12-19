# # Loop for 5 iterations and append each number (in this range) to the list.

# num_list = []
# for i in range(1, 6):
#     num_list.append(i)

# # print(num_list)

# # Same result as above, using List Comp

# num_list = [i for i in range(1,6)]
# print(num_list)

str_number = ["1", "2", "3"]
str_number[0]

for i in range(len(str_number)):
    print(i)


# integer_num = []
# for i in range(len(str_number)):
#     integer_num.append(int(str_number[i]))

# print(integer_num)
# integer_num.clear()

# integer_num = [int(str_number[i]) for i in range(len(str_number))]
# print(integer_num)


# Complex List Comprehension:
complex_squares = [x**2 if x % 2 == 0 else 0 for x in range(10) if x > 2 and x < 8]

# # # if x % 2 == 0:
# # #     x**2
# # # else:
# # #     0

# # print(len(animals))
# # print(complex_squares)

# # Conditional Expression (Ternary Operator)
# x = 4
# if (x == 5):
#     print("Because the condition is true")
# else:
#     print("Because the condition is false")

#             # True                          | condition     | False
# result = ["Because the condition is true" if x == 5 else "Because the condition is false"]

