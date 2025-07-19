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

# Perform the calculation using a match-case statement
match operation:
    case '+':
        result = num1 + num2
        print(f"The result is {result}.")
    case '-':
        result = num1 - num2
        print(f"The result is {result}.")
    case '*':
        result = num1 * num2
        print(f"The result is {result}.")
    case '/':
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}.")
    case _: # Default case for unexpected input
        print("Invalid operation. Please choose from +, -, *, /.")

