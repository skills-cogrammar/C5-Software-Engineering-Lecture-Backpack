# for i in range(10):
#     print(i)






# total = 0
# start = 1
# stop = 20
# for num in range(start, stop):
#     total += num
# print("Sum:", total)


# for _ in range(3):
#     user_input = input("Please enter a number: ")
#     print(user_input)


# my_str = "Hello, world!"
# for letter in my_str:
#     print(letter, end=" ")


# fruits = ['apple', 'banana', 'cherry', "Pear"]
# for fruit in fruits:
#     if fruit in ["apple", "banana"]:
#         print(fruit)


# fruits = ['apple', 'banana', 'cherry']
# for i, fruit in enumerate(fruits, 1):  # ((1, "apple"), (2, "banana"), (3, "cherry"))
#     print(i, fruit)


# for i in range(1, 6):
#     if i == 4:
#         break
#     print(i)


for i in range(1,6):
    if i == 4:
        continue
    print(i)
else:
    print("Loop ended")
