# Example of using with statements for file management

# Define a function to read a file using with
def read_file_with(file_path):
    """Read the contents of a file and return them."""
    try:
        with open(file_path, 'r') as file:  # Open the file using with
            content = file.read()  # Read the file content
            return content  # Return the content
    except FileNotFoundError:  # Handle file not found error
        return "Error: File not found."  # Return an error message

# Call the read_file_with function with an existing file (ensure the file exists)
# print(read_file_with("existing_file.txt"))  # Uncomment to test with an actual file

# Define a function to write to a file using with
def write_file_with(file_path, content):
    """Write content to a file."""
    try:
        with open(file_path, 'w') as file:  # Open the file using with
            file.write(content)  # Write the content to the file
    except Exception as e:  # Handle any exceptions
        print(f"Error: {e}")  # Print the error message

# Call the write_file_with function to write to a file
write_file_with("example_file.txt", "This is an example file.")

# Example of using with statements for multiple resources

# Define a function to read and write files using with
def read_and_write_files(file_path_read, file_path_write):
    """Read from one file and write to another."""
    try:
        with open(file_path_read, 'r') as file_read, open(file_path_write, 'w') as file_write:
            content = file_read.read()  # Read the content from the first file
            file_write.write(content)  # Write the content to the second file
    except Exception as e:  # Handle any exceptions
        print(f"Error: {e}")  # Print the error message

# Call the read_and_write_files function to read and write files
read_and_write_files("example_file.txt", "copied_file.txt")

# Example of using with statements for context managers

# Define a class that acts as a context manager
class ManagedFile:
    def __init__(self, file_path):
        self.file_path = file_path

    def __enter__(self):
        self.file = open(self.file_path, 'r')  # Open the file
        return self.file  # Return the file object

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()  # Close the file

# Define a function to read a file using the ManagedFile context manager
def read_file_with_context_manager(file_path):
    """Read the contents of a file and return them."""
    try:
        with ManagedFile(file_path) as file:  # Use the ManagedFile context manager
            content = file.read()  # Read the file content
            return content  # Return the content
    except FileNotFoundError:  # Handle file not found error
        return "Error: File not found."  # Return an error message

# Call the read_file_with_context_manager function with an existing file (ensure the file exists)
# print(read_file_with_context_manager("existing_file.txt"))  # Uncomment to test with an actual file