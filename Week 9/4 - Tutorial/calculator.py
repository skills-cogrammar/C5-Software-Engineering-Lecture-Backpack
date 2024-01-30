print("***** BASIC CALCULATOR *****")

while True:
    while True:
        num1 = input("Please enter a number: ")
        if num1.isnumeric():
            num1 = int(num1)
            break
        print("Please use numbers only!")
    while True:
        num2 = input("Please enter another number: ")
        if num2.isnumeric():
            num2 = int(num2)
            break
        print("Please use numbers only!")    
    while True:
        operator = input("Please select an operation(+,-,*,/): ")
        if operator in ["+", "-", "*", "/"]:
            break
        print("The only available operators are +, -, *, /.")

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2

    print(f"{num1} {operator} {num2} = {result}")

    if input("Press enter to do another equation or type anything to quit."):
        break
