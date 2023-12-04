# Try-Except Example

def divide_numbers(a, b):
    try:
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

# Valid division
divide_numbers(10, 2)

# Division by zero
divide_numbers(5, 0)

#Invalid data type
divide_numbers("10", 2)