"""
We want to divide two numbers

Get 2 numbers from user.(validate input)

divide the first number with the second

output result

"""
while True:
    num1 = input("Please enter the first number: ")
    if not num1.replace("-", "", 1).isnumeric():
        print("Non numerical values entered!")
    else:
        break

while True:
    num2 = input("Please enter the second number: ")
    if not num2.replace("-", "", 1).isnumeric():
        print("Non numerical values entered!")
    elif num2 == "0":
        print("Cannot divide by ZERO!")
    else:
        break

num1 = int(num1)
num2 = int(num2)
result = num1/num2

print(f"The result of {num1}/{num2} is {result}")


my_str = "-54"
new_str = my_str.replace("-", "", 1)

# if my_str.isnumeric():
print(my_str)
print(new_str)
