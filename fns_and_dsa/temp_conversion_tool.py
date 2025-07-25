# Define Global Conversion Factors
# Factor to convert Fahrenheit to Celsius: (F - 32) * 5/9
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9 # Changed to remove spaces around /
# Factor to convert Celsius to Fahrenheit: (C * 9/5) + 32
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5 # Changed to remove spaces around /

def convert_to_celsius(fahrenheit: float) -> float:
    """
    Converts a temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit (float): The temperature in Fahrenheit.

    Returns:
        float: The temperature converted to Celsius.
    """
    # Use the global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius: float) -> float:
    """
    Converts a temperature from Celsius to Fahrenheit.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The temperature converted to Fahrenheit.
    """
    # Use the global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    """
    Main function to handle user interaction for temperature conversion.
    """
    print("Temperature Conversion Tool")
    while True:
        try:
            # Prompt the user for the temperature
            temp_str = input("Enter the temperature to convert: ").strip()
            temperature = float(temp_str) # Convert input to float

            # Prompt the user for the unit (C/F)
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

            if unit == 'C':
                # Convert Celsius to Fahrenheit
                converted_temp = convert_to_fahrenheit(temperature)
                print(f"{temperature}°C is {converted_temp}°F")
            elif unit == 'F':
                # Convert Fahrenheit to Celsius
                converted_temp = convert_to_celsius(temperature)
                print(f"{temperature}°F is {converted_temp}°C")
            else:
                print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
            break # Exit loop after successful conversion

        except ValueError:
            # Handle non-numeric input for temperature
            print("Invalid temperature. Please enter a numeric value.")
        except Exception as e:
            # Catch any other unexpected errors
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
