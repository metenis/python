# math_utils.py - a module for mathematical utilities

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return the quotient of a and b."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b


# main.py - a script that uses the math_utils module

import math_utils  # Import the math_utils module

# Use the functions from the math_utils module
result = math_utils.add(2, 3)
print("2 + 3 =", result)

result = math_utils.subtract(5, 2)
print("5 - 2 =", result)

result = math_utils.multiply(4, 5)
print("4 * 5 =", result)

try:
    result = math_utils.divide(10, 0)
    print("10 / 0 =", result)
except ValueError as e:
    print("Error:", e)