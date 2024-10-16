# Create a variegate list called 'my_list' with initial values
my_list = [1, "hello", 3.14, [4, 5, 6], "goodbye", True, None, {"name": "John", "age": 30}]  

# Print the initial list to the console
print("Initial List:", my_list)  

# Access and print individual elements of the list
print("First element:", my_list[0])  # Output: 1
print("Second element:", my_list[1])  # Output: "hello"
print("Third element:", my_list[2])  # Output: 3.14
print("Fourth element:", my_list[3])  # Output: [4, 5, 6]
print("Fifth element:", my_list[4])  # Output: "goodbye"
print("Sixth element:", my_list[5])  # Output: True
print("Seventh element:", my_list[6])  # Output: None
print("Eighth element:", my_list[7])  # Output: {"name": "John", "age": 30}

# Modify the list by appending a new element
my_list.append("new element")  

# Print the list after appending the new element
print("List after appending new element:", my_list)  

# Modify the list by updating the third element
my_list[2] = "pi"  

# Print the list after updating the third element
print("List after updating third element:", my_list)  

# Delete the fifth element from the list
del my_list[4]  

# Print the list after deleting the fifth element
print("List after deleting fifth element:", my_list)  