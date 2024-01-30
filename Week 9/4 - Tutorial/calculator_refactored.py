def add(num1, num2):
    """Adds num1 and num2 together and returns the answer."""
    return num1 + num2

def subtract(num1, num2):
    """Subtracts num1 from num2 and returns the answer."""
    return num1 - num2

def multiply(num1, num2):
    """Multiplies num1 by num2 and returns the answer."""
    return num1 * num2

def divide(num1, num2):
    """Divides num1 by num2 and returns the answer."""
    return num1 / num2

def calculate(num1, num2, operator):
    """Determines which function should be applied to the provided numbers. """
    if operator == "+":
        result = add(num1, num2)
    elif operator == "-":
        result = subtract(num1, num2)
    elif operator == "*":
        result = multiply(num1, num2)
    elif operator == "/":
        result = divide(num1, num2)

    return result

def get_num_input(prompt):
    """
    Receives input from the user using the given prompt and 
    determines if the value entered is numeric. If the value
    is not numeric user will be prompted again.
    """
    while True:
        user_input = input(prompt)
        if user_input.isnumeric():
            user_input = int(user_input)
            break
        print("Please use numbers only!")
    return user_input


def main():
    """Main function for file execution."""
    print("***** BASIC CALCULATOR *****")
    while True:
        num1 = get_num_input("Please enter a number: ")
        num2 = get_num_input("Please enter another number: ")

        while True:
            operator = input("Please select an operation(+,-,*,/): ")
            if operator in ["+", "-", "*", "/"]:
                break
            print("The only available operators are +, -, *, /.")

        result = calculate(num1, num2, operator)

        print(f"{num1} {operator} {num2} = {result}")

        if input("Press enter to do another equation or type anything to quit: "):
            break

if __name__ == "__main__":
    main()
