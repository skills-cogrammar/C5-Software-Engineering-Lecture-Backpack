"""FOR LOOPS"""

# Example 1: Print numbers from 1 to 5
for i in range(1, 6):
    print(i)

# Example 2: Iterate over elements in a list
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# Example 3: Calculate the sum of numbers in a range
total = 0
for num in range(1, 6):
    total += num
print("Sum:", total)

# Example 4: Iterate over characters in a string.
my_str = "Hello, world!"
for letter in my_str:
    print(letter)

# Example 5: Stop a for loop early using 'break'
for i in range(1, 6):
    if i == 4:
        break
    print(i)


# Example 6: Start next iteration using 'continue'
for i in range(1,6):
    if i == 4:
        continue
    print(i)

# Example 7: Asking a user to enter a value mulitple times
for i in range(3):
    user_input = input("Please enter a number")
    print(user_input)