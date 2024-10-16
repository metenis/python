# Define a variable to hold a score
score = 85

# Print the original score
print("Score:", score)

# Use if, elif, and else to determine the grade based on the score
if score >= 90:
    # If the score is 90 or above, assign an 'A' grade
    grade = 'A'
elif score >= 80:
    # If the score is between 80 and 89, assign a 'B' grade
    grade = 'B'
elif score >= 70:
    # If the score is between 70 and 79, assign a 'C' grade
    grade = 'C'
elif score >= 60:
    # If the score is between 60 and 69, assign a 'D' grade
    grade = 'D'
else:
    # If the score is below 60, assign an 'F' grade
    grade = 'F'

# Print the determined grade
print("Grade:", grade)

# Example of using if-else for a simple condition
is_passed = score >= 60  # Determine if the score is passing

# Print whether the student has passed or failed
if is_passed:
    print("Status: Passed")
else:
    print("Status: Failed")

# Another example with multiple conditions
temperature = 30  # Define a temperature variable

# Print the temperature
print("Temperature:", temperature)

# Determine the weather condition based on the temperature
if temperature > 30:
    weather = "Hot"
elif temperature >= 20:
    weather = "Warm"
elif temperature >= 10:
    weather = "Cool"
else:
    weather = "Cold"

# Print the determined weather condition
print("Weather condition:", weather)