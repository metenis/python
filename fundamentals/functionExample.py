# Define a function to calculate the square of a number
def square(number):
    """Return the square of the given number."""
    return number ** 2  # Calculate and return the square

# Call the square function and print the result
result = square(5)
print("Square of 5:", result)

# Define a function to greet a user
def greet(name):
    """Print a greeting message for the given name."""
    print(f"Hello, {name}!")  # Print a greeting message

# Call the greet function with a name
greet("Alice")

# Define a function to calculate the average of a list of numbers
def average(numbers):
    """Return the average of a list of numbers."""
    if not numbers:  # Check if the list is empty
        return 0  # Return 0 if the list is empty
    return sum(numbers) / len(numbers)  # Calculate and return the average

# Call the average function and print the result
numbers_list = [10, 20, 30, 40, 50]
avg_result = average(numbers_list)
print("Average of the list:", avg_result)

# Define a function with default parameters
def power(base, exponent=2):
    """Return the base raised to the power of exponent (default is 2)."""
    return base ** exponent  # Calculate and return the power

# Call the power function with and without the exponent parameter
print("2 raised to the power of 3:", power(2, 3))  # Custom exponent
print("3 raised to the power of 2 (default):", power(3))  # Default exponent

# Define a function that accepts variable number of arguments
def concatenate(*args):
    """Return a concatenated string of all arguments."""
    return " ".join(args)  # Join all arguments into a single string

# Call the concatenate function with multiple arguments
concatenated_result = concatenate("Hello", "world!", "How", "are", "you?")
print("Concatenated string:", concatenated_result)