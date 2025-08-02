def safe_divide(numerator, denominator):
    """
    Performs division while handling ZeroDivisionError and ValueError.

    Args:
        numerator (str): The numerator as a string from command line arguments.
        denominator (str): The denominator as a string from command line arguments.

    Returns:
        str: A message indicating the result or an error.
    """
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        den = float(denominator)

        # Attempt to perform division
        result = num / den
        return f"The result of the division is {result}"
    except ValueError:
        # Handle cases where inputs are not valid numbers
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        # Handle division by zero
        return "Error: Cannot divide by zero."