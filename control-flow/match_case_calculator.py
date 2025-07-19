# Prompt the user for the first number
try:
    num1 = float(input("Enter the first number: "))
except ValueError:
    print("Invalid input for the first number. Please enter a numerical value.")
    exit() # Exit the program if input is not a number

# Prompt the user for the second number
try:
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input for the second number. Please enter a numerical value.")
    exit() # Exit the program if input is not a number

# Ask for the type of operation
operation = input("Choose the operation (+, -, *, /): ")

# Perform the calculation using if-elif-else statements
if operation == '+':
    result = num1 + num2
    print(f"The result is {result}.")
elif operation == '-':
    result = num1 - num2
    print(f"The result is {result}.")
elif operation == '*':
    result = num1 * num2
    print(f"The result is {result}.")
elif operation == '/':
    if num2 == 0:
        print("Cannot divide by zero.")
    else:
        result = num1 / num2
        print(f"The result is {result}.")
else: # Handles unexpected input
    print("Invalid operation. Please choose from +, -, *, /.")