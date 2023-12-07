# Try-Except Example

a = 0
b = 0

try: # Try this:
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except TypeError:
    print("Error: Invalid data type for division.")
except Exception as e:
    print("An unexpected error occurred:", e)
finally:
    print("This block always executes, regardless of exceptions.")


# Raise in try-except
try:
    age = int(input("Please enter your age: "))
    if age < 0:
        # raise a ValueError with a custom error message
        raise ValueError("Age cannot be negative.")
except ValueError as raised_error:
    # Catch the raised ValueError and print the error message
    print("An error occurred: ", raised_error)