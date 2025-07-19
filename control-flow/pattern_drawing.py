
try:
    size = int(input("Enter the size of the pattern: "))
    if size <= 0:
        print("Please enter a positive integer for the pattern size.")
        exit()
except ValueError:
    print("Invalid input. Please enter an integer.")
    exit()

# Generate a square pattern of asterisks
row_count = 0
while row_count < size:
    # Inner for loop to print asterisks for the current row
    for _ in range(size):
        print("*", end="") # Print asterisk without a newline
    print() # Print a newline character after each row is complete
    row_count += 1

