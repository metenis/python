# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Print the original list
print("Original list:", numbers)

# Use a for loop to iterate over the list
for number in numbers:
    # Print each number in the list
    print("Number:", number)

# Example of using a for loop with a string
message = "Hello, World!"

# Print the original message
print("Original message:", message)

# Use a for loop to iterate over the characters in the string
for char in message:
    # Print each character in the string
    print("Character:", char)

# Example of using a for loop with a dictionary
person = {"name": "John", "age": 30, "city": "New York"}

# Print the original dictionary
print("Original dictionary:", person)

# Use a for loop to iterate over the key-value pairs in the dictionary
for key, value in person.items():
    # Print each key-value pair in the dictionary
    print(f"{key}: {value}")

# Example of using a for loop with a range
for i in range(1, 6):
    # Print each number in the range
    print("Number:", i)

# Example of using a for loop with enumerate
fruits = ["apple", "banana", "cherry"]

# Use a for loop with enumerate to iterate over the list with indices
for index, fruit in enumerate(fruits):
    # Print each fruit with its index
    print(f"Fruit at index {index}: {fruit}")

# Example of using a for loop with zip
names = ["John", "Mary", "David"]
ages = [25, 31, 42]

# Use a for loop with zip to iterate over two lists simultaneously
for name, age in zip(names, ages):
    # Print each name with its corresponding age
    print(f"{name} is {age} years old.")