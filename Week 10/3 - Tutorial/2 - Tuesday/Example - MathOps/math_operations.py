# math_operations.py

def add(a, b):
    """Addition"""
    return a + b

def subtract(a, b):
    """Subtraction"""
    return a - b

def multiply(a, b):
    """Multiplication"""
    return a * b

def divide(a, b):
    """Division"""
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

def power(a, b):
    """Exponentiation"""
    return a ** b