def display_menu():
    """Displays the main menu options to the user."""
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """
    Manages the shopping list by allowing users to add, remove, and view items.
    """
    shopping_list = [] # Initialize an empty list to store shopping items

    while True:
        display_menu() # Display the menu
        choice = input("Enter your choice: ").strip() # Get user's choice and remove whitespace

        if choice == '1':
            # Add Item functionality
            item = input("Enter the item to add: ").strip()
            if item: # Ensure the item name is not empty
                shopping_list.append(item)
                print(f"'{item}' has been added to the list.")
            else:
                print("Item name cannot be empty.")
        elif choice == '2':
            # Remove Item functionality
            if not shopping_list: # Check if the list is empty
                print("The shopping list is empty. Nothing to remove.")
                continue # Go back to the menu
            item_to_remove = input("Enter the item to remove: ").strip()
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                print(f"'{item_to_remove}' has been removed from the list.")
            else:
                print(f"'{item_to_remove}' not found in the list.")
        elif choice == '3':
            # View List functionality
            if shopping_list:
                print("\n--- Your Shopping List ---")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
                print("--------------------------")
            else:
                print("\nYour shopping list is empty.")
        elif choice == '4':
            # Exit functionality
            print("Goodbye!")
            break # Exit the loop
        else:
            # Handle invalid choices
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
