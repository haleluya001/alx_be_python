# Prompt the user for a number to see its multiplication table
try:
    number = int(input("Enter a number to see its multiplication table: "))
except ValueError:
    print("Invalid input. Please enter a numerical value.")
    exit() # Exit the program if input is not a number

# Generate and print the multiplication table using a for loop
print(f"Multiplication Table for {number}:")
for i in range(1, 11): # Loop from 1 to 10 (11 is exclusive)
    product = number * i
    print(f"{number} * {i} = {product}")

# End of the multiplication table program