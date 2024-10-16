# Create a tuple
my_tuple = (1, 2, 3, 4, 5)

# Print the tuple
print("Original Tuple:", my_tuple)

# Convert the tuple to a list using the list() function
my_list = list(my_tuple)

# Print the list
print("Converted to List:", my_list)

# Convert the list back to a tuple using the tuple() function
my_tuple_again = tuple(my_list)

# Print the tuple again
print("Converted back to Tuple:", my_tuple_again)

# Verify that the original tuple and the converted tuple are the same
print("Are the original and converted tuples the same?", my_tuple == my_tuple_again)

# Create a list
my_list2 = [1, 2, 3, 4, 5]

# Print the list
print("Original List:", my_list2)

# Convert the list to a tuple using the tuple() function
my_tuple2 = tuple(my_list2)

# Print the tuple
print("Converted to Tuple:", my_tuple2)

# Convert the tuple back to a list using the list() function
my_list2_again = list(my_tuple2)

# Print the list again
print("Converted back to List:", my_list2_again)

# Verify that the original list and the converted list are the same
print("Are the original and converted lists the same?", my_list2 == my_list2_again)