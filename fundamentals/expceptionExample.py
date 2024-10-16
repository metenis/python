# Example of handling exceptions with try and except

# Define a function to divide two numbers
def divide(a, b):
    """Return the result of dividing a by b."""
    try:
        result = a / b  # Attempt to perform the division
    except ZeroDivisionError:  # Handle division by zero
        return "Error: Cannot divide by zero."  # Return an error message
    except TypeError:  # Handle incorrect types
        return "Error: Invalid input types. Please provide numbers."  # Return an error message
    else:
        return result  # Return the result if no exceptions occurred

# Call the divide function with valid inputs
print("10 divided by 2:", divide(10, 2))

# Call the divide function with a zero denominator
print("10 divided by 0:", divide(10, 0))

# Call the divide function with invalid input types
print("10 divided by 'a':", divide(10, 'a'))

# Example of using finally
def read_file(file_path):
    """Read the contents of a file and return them."""
    try:
        file = open(file_path, 'r')  # Attempt to open the file
        content = file.read()  # Read the file content
        return content  # Return the content
    except FileNotFoundError:  # Handle file not found error
        return "Error: File not found."  # Return an error message
    finally:
        # This block will execute regardless of whether an exception occurred
        print("Execution of read_file completed.")  # Indicate completion

# Call the read_file function with a non-existent file
print(read_file("non_existent_file.txt"))

# Call the read_file function with an existing file (ensure the file exists)
# print(read_file("existing_file.txt"))  # Uncomment to test with an actual file