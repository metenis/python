# Create a dictionary called 'person' with some initial key-value pairs
person = {"name": "John", "age": 30, " occupation": "Software Engineer"}

# Print the entire dictionary
print("Original Dictionary:", person)

# Access a specific value in the dictionary by its key
print("Name:", person["name"])  # Output: John

# Add a new key-value pair to the dictionary
person["city"] = "New York"
print("Updated Dictionary:", person)

# Modify an existing value in the dictionary
person["age"] = 31
print("Updated Dictionary:", person)

# Remove a key-value pair from the dictionary
del person["occupation"]
print("Updated Dictionary:", person)

# Check if a key exists in the dictionary
if "name" in person:
    print("Key 'name' exists in the dictionary")
else:
    print("Key 'name' does not exist in the dictionary")

# Get a list of all keys in the dictionary
keys = list(person.keys())
print("Keys:", keys)

# Get a list of all values in the dictionary
values = list(person.values())
print("Values:", values)

# Get a list of all key-value pairs in the dictionary
items = list(person.items())
print("Items:", items)

# Create a new dictionary from an existing one using the dict() constructor
new_person = dict(person)
print("New Dictionary:", new_person)

# Update a dictionary with new key-value pairs from another dictionary
update_dict = {"country": "USA", "hobbies": ["reading", "hiking"]}
person.update(update_dict)
print("Updated Dictionary:", person)

# Clear all key-value pairs from the dictionary
person.clear()
print("Cleared Dictionary:", person)