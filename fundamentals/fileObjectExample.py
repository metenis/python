# Create a file object in write mode
with open("example.txt", "w") as file:
    # Write to the file
    file.write("This is an example file.\n")
    file.write("It has multiple lines.\n")
    file.write("And it's written using Python!")

# Create a file object in read mode
with open("example.txt", "r") as file:
    # Read the entire file
    contents = file.read()
    print("File contents:", contents)

# Create a file object in append mode
with open("example.txt", "a") as file:
    # Append to the file
    file.write("\nThis is an appended line.")

# Create a file object in read mode again
with open("example.txt", "r") as file:
    # Read the entire file again
    contents = file.read()
    print("File contents after appending:", contents)

# Using the `readline()` method to read a single line
with open("example.txt", "r") as file:
    line = file.readline()
    print("First line:", line.strip())

# Using the `readlines()` method to read all lines
with open("example.txt", "r") as file:
    lines = file.readlines()
    print("All lines:", [line.strip() for line in lines])

# Using the `write()` method to write a single line
with open("example.txt", "w") as file:
    file.write("This is a new line.\n")

# Using the `writelines()` method to write multiple lines
with open("example.txt", "w") as file:
    lines = ["This is line 1.\n", "This is line 2.\n", "This is line 3.\n"]
    file.writelines(lines)

# Using the `seek()` method to move the file pointer
with open("example.txt", "r+") as file:
    file.write("This is a new line.\n")
    file.seek(0)
    print("File contents after seeking:", file.read())

# Using the `tell()` method to get the current file pointer position
with open("example.txt", "r+") as file:
    file.write("This is a new line.\n")
    print("Current file pointer position:", file.tell())