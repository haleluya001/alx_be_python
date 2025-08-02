import sys
from bank_account import BankAccount

def main():
    """
    Parses command-line arguments to perform banking operations on a
    BankAccount instance.
    """
    # Create a single BankAccount instance with a starting balance for this session.
    # This balance will be modified by the commands.
    account = BankAccount(100.0)

    # Check for the correct number of command-line arguments.
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>[:<amount>]")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Split the first argument at the colon to get the command and amount.
    command_parts = sys.argv[1].split(':', 1)
    command = command_parts[0]
    
    amount = None
    # If a second part exists, try to convert it to a float.
    if len(command_parts) > 1:
        try:
            amount = float(command_parts[1])
        except ValueError:
            print(f"Error: Invalid amount provided for '{command}' operation. Amount must be a number.")
            sys.exit(1)

    # Process the command and call the corresponding method.
    if command == "deposit":
        if amount is not None:
            try:
                account.deposit(amount)
                print(f"Deposited: ${amount:.2f}")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Error: The 'deposit' command requires an amount. Usage: deposit:<amount>")
    elif command == "withdraw":
        if amount is not None:
            try:
                if account.withdraw(amount):
                    print(f"Withdrew: ${amount:.2f}")
                else:
                    print("Insufficient funds.")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Error: The 'withdraw' command requires an amount. Usage: withdraw:<amount>")
    elif command == "display":
        # The 'display' command does not require an amount.
        account.display_balance()
    else:
        print(f"Invalid command: '{command}'. Available commands: deposit, withdraw, display.")
        sys.exit(1)

if __name__ == "__main__":
    main()
