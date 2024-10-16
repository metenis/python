# Create a variegate tuple called 'my_tuple' with initial values
my_tuple = (1, "hello", 3.14, [4, 5, 6], "goodbye", True, None, {"name": "John", "age": 30})

# Print the initial tuple to the console
print("Initial Tuple:", my_tuple)

# Access and print individual elements of the tuple
print("First element:", my_tuple[0])  # Output: 1
print("Second element:", my_tuple[1])  # Output: "hello"
print("Third element:", my_tuple[2])  # Output: 3.14
print("Fourth element:", my_tuple[3])  # Output: [4, 5, 6]
print("Fifth element:", my_tuple[4])  # Output: "goodbye"
print("Sixth element:", my_tuple[5])  # Output: True
print("Seventh element:", my_tuple[6])  # Output: None
print("Eighth element:", my_tuple[7])  # Output: {"name": "John", "age": 30}

# Tuples are immutable, meaning their contents cannot be modified after creation
# Attempting to modify a tuple will result in a TypeError
try:
    my_tuple[0] = 10
except TypeError as e:
    print("Error:", e)

# However, if a tuple contains a mutable object (like a list or dictionary),
# that object can still be modified
my_tuple[3][0] = 10
print("Modified Tuple:", my_tuple)

# Tuples can be concatenated using the '+' operator
my_tuple2 = (1, 2, 3)
print("Concatenated Tuple:", my_tuple + my_tuple2)

# Tuples can be repeated using the '*' operator
print("Repeated Tuple:", my_tuple * 2)

# The main differences between lists and tuples are:
# 1. Immutability: Tuples are immutable, while lists are mutable.
# 2. Syntax: Tuples use parentheses '()' while lists use square brackets '[]'.
# 3. Performance: Tuples are generally faster and more memory-efficient than lists.
# 4. Use cases: Tuples are often used when the data should not be changed,
#   while lists are used when the data needs to be modified.