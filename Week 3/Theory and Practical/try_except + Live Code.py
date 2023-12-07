# Try-Except Example

a = "5" # String
b = 5   # Integer
c = False # Boolean
d = 1.5 # Float

## Runnning without Exception Handling:
# result = a / b
# print("Result:", result)

try:
    result = a / b
    print(f"Result: {result}")
except (ZeroDivisionError, TypeError):
    print("Error: Cannot divide by zero or wrong data type.")
# except TypeError:
#     print("Error: Invalid data type for division.")
except Exception as e:
    print("An unexpected error occurred:", e)
finally:
    print("This block always executes, regardless of exceptions.")

user_input = int(input("Enter a value greater 10: "))
if user_input < 10:
    raise Exception("Please provide a value greater than 10!")
    print("Please provide a value greater than 10!")


# Raise in try-except
try:
    age = int(input("Please enter your age: "))
    if age < 0:
        # raise a ValueError with a custom error message
        raise ValueError("Age cannot be negative.")
except ValueError as error:
    # Catch the raised ValueError and print the error message
    print("An error occurred: ", error)