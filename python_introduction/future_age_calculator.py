# Prompt the user to input their current age
# The input() function reads a line from input, and returns it as a string.
# int() converts the string to an integer.
current_age = int(input("How old are you? "))

# Calculate how many years are between the current assumed year (2023) and 2050
years_to_add = 2050 - 2023

# Calculate the user's age in 2050
future_age = current_age + years_to_add

# Print the user's age in 2050 in the specified format
print(f"In 2050, you will be {future_age} years old.")