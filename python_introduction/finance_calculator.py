
def calculate_savings():
    """
    Calculates monthly and projected annual savings based on user input.
    Assumes a simple annual interest rate of 5%.
    """
    try:
        # User Input for Financial Details
        # Prompt the user for their monthly income and convert to a float.
        monthly_income = float(input("Enter your monthly income: "))

        # Prompt the user for their total monthly expenses and convert to a float.
        monthly_expenses = float(input("Enter your total monthly expenses: "))

        # Input validation: Ensure income and expenses are non-negative.
        if monthly_income < 0 or monthly_expenses < 0:
            print("Error: Income and expenses cannot be negative. Please enter positive values.")
            return

        # Input validation: Ensure expenses do not exceed income.
        if monthly_expenses > monthly_income:
            print("Error: Monthly expenses cannot be greater than monthly income.")
            return

        # Calculate Monthly Savings
        # Subtract monthly expenses from monthly income to get monthly savings.
        monthly_savings = monthly_income - monthly_expenses

        # Project Annual Savings
        # Assume a simple annual interest rate of 5% (0.05).
        annual_interest_rate = 0.05

        # Calculate the projected savings after one year, incorporating the interest.
        # Use the simplified formula: Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)
        projected_annual_savings = (monthly_savings * 12) + (monthly_savings * 12 * annual_interest_rate)

        # Output Results
        # Display the user’s monthly savings, formatted to two decimal places.
        print(f"Your monthly savings are ${monthly_savings:.2f}.")

        # Display the projected annual savings after including interest, formatted to two decimal places.
        print(f"Projected savings after one year, with interest, is: ${projected_annual_savings:.2f}.")

    except ValueError:
        # Handle cases where the user enters non-numeric input.
        print("Invalid input. Please enter numerical values for income and expenses.")
    except Exception as e:
        # Catch any other unexpected errors.
        print(f"An unexpected error occurred: {e}")

# Call the function to run the calculator when the script is executed.
if __name__ == "__main__":
    calculate_savings()