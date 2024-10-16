# Create a string
my_string = "Hello, World! This is a test string."

# Print the string
print("Original String:", my_string)

# Accessing individual characters in the string
print("First character:", my_string[0])  # Output: H
print("Last character:", my_string[-1])  # Output: .

# Slicing the string
print("First 5 characters:", my_string[:5])  # Output: Hello
print("Last 5 characters:", my_string[-5:])  # Output: string

# String concatenation
greeting = "Hello, "
name = "John"
print("Concatenated string:", greeting + name)  # Output: Hello, John

# String formatting
age = 30
print("Formatted string:", "My name is {} and I am {} years old.".format(name, age))
print("Formatted string (f-string):", f"My name is {name} and I am {age} years old.")

# String modification
print("Original string:", my_string)
print("String in uppercase:", my_string.upper())
print("String in lowercase:", my_string.lower())
print("String with first letter capitalized:", my_string.capitalize())
print("String with all letters capitalized:", my_string.title())

# Using the re module for regular expressions
import re

# Searching for a pattern in the string
pattern = "test"
if re.search(pattern, my_string):
    print("Pattern found in string")
else:
    print("Pattern not found in string")

# Replacing a pattern in the string
new_string = re.sub(pattern, "example", my_string)
print("String after replacement:", new_string)

# Splitting the string into substrings
substrings = re.split("\s+", my_string)
print("Substrings:", substrings)

# Finding all occurrences of a pattern in the string
matches = re.findall(pattern, my_string)
print("Matches:", matches)

# String modification using the re module
print("Original string:", my_string)
print("String with all digits removed:", re.sub("\d", "", my_string))
print("String with all punctuation removed:", re.sub("[^\w\s]", "", my_string))