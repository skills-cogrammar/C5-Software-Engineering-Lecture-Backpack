import os
from math_operations import *

def clear_screen():
    # Clear the console screen
    os.system("cls||clear")

def display_menu():
    """Display the menu"""
    print(f"{'=' * 6} Math Calculator {'=' * 6}")
    print("\nMath Operations Menu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Quit")

def get_user_choice():
    """Get user's choice"""
    try:
        choice = input("Enter your choice (1 - 6): ")
        int_choice = int(choice)
        if 1 <= int_choice <= 6:
            return str(int_choice)
        else:
            raise ValueError("Invalid choice. Try again:")
    except ValueError as err_msg:
        print(f"Error: {err_msg}")
        return get_user_choice()

def get_user_input():
    """Get user input for operands"""
    try:
        a = float(input("Enter your first number: "))
        b = float(input("Enter your second number: "))
        return a, b
    except ValueError as err_msg:
        print(f"Error: {err_msg}")
        return get_user_input()
    
def log_operation(operation, a, b, result):
    operation_symbols = {
        "add": '+', 
        "subtract": '-',
        "multiply": '*',
        "divide": '/', 
        "power": '^'
    }

    symbol = operation_symbols.get(operation.__name__, 'UNKNOWN')
    log_message = f"{a} {symbol} {b} = {result}\n"

    with open("operation_log.txt", "a") as log_file:
        log_file.write(log_message)

def main():
    clear_screen()
    choice = ''
    while choice != '6':
        display_menu()
        choice = get_user_choice()

        if choice in ['1','2','3','4','5']:
            a, b = get_user_input()

            try:
                if choice == '1':
                    result = add(a, b)
                    operation = add
                elif choice == '2':
                    result = subtract(a, b)
                    operation = subtract
                elif choice == '3':
                    result = multiply(a, b)
                    operation = multiply
                elif choice == '4':
                    result = divide(a, b)
                    operation = divide
                elif choice == '5':
                    result = power(a, b)
                    operation = power

                print(f"{operation.__name__.capitalize()} Result: {result}")
                log_operation(operation, a, b, result)
                input("-- Press enter to return to the main menu. > ")
                clear_screen()
            
            except Exception as err_msg:
                print(f"Error during operation: {err_msg}")

        elif choice == '6':
            print("Exiting the Program. Bye for now!")

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()