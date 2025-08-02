class BankAccount:
    """
    A class to represent a bank account, handling deposits, withdrawals,
    and balance display.
    """

    def __init__(self, initial_balance=0.0):
        """
        Initializes a new BankAccount instance with an optional initial balance.

        Args:
            initial_balance (float): The starting balance for the account.
                                     Defaults to 0.0.
        """
        # Encapsulation: The balance is stored in a private attribute
        # prefixed with `__` to prevent direct external modification.
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            raise ValueError("Initial balance must be a non-negative number.")
        self.__account_balance = float(initial_balance)

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        Args:
            amount (float): The amount to deposit. Must be a positive number.
        
        Raises:
            ValueError: If the amount is not a positive number.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Deposit amount must be a positive number.")
        self.__account_balance += amount

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account if funds are sufficient.

        Args:
            amount (float): The amount to withdraw. Must be a positive number.

        Returns:
            bool: True if the withdrawal was successful, False otherwise.
        
        Raises:
            ValueError: If the amount is not a positive number.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Withdrawal amount must be a positive number.")
            
        if self.__account_balance >= amount:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """
        Prints the current account balance in a user-friendly format.
        """
        # The balance is formatted to two decimal places for currency display.
        print(f"Current Balance: ${self.__account_balance:.2f}")