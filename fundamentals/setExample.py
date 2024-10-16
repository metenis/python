# Create a set called 'fruits' with some initial elements
fruits = {"apple", "banana", "orange", "grape"}

# Print the entire set
print("Original Set:", fruits)

# Add a new element to the set
fruits.add("mango")
print("Updated Set:", fruits)

# Remove an element from the set
fruits.remove("banana")
print("Updated Set:", fruits)

# Check if an element exists in the set
if "orange" in fruits:
    print("Element 'orange' exists in the set")
else:
    print("Element 'orange' does not exist in the set")

# Get the length of the set (number of elements)
print("Length of Set:", len(fruits))

# Create a new set from an existing one using the set() constructor
new_fruits = set(fruits)
print("New Set:", new_fruits)

# Update a set with new elements from another set
update_set = {"pear", "peach"}
fruits.update(update_set)
print("Updated Set:", fruits)

# Get the union of two sets (all elements from both sets)
union_set = fruits.union({"kiwi", "strawberry"})
print("Union Set:", union_set)

# Get the intersection of two sets (elements common to both sets)
intersection_set = fruits.intersection({"orange", "grape", "kiwi"})
print("Intersection Set:", intersection_set)

# Get the difference of two sets (elements in the first set but not the second)
difference_set = fruits.difference({"orange", "grape"})
print("Difference Set:", difference_set)

# Clear all elements from the set
fruits.clear()
print("Cleared Set:", fruits)