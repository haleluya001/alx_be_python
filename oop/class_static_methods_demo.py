
"""
class_static_methods_demo.py

This script defines a Calculator class to illustrate the use of class methods
and static methods in Python, highlighting their differences and use cases.
"""

class Calculator:
    """
    A simple Calculator class that provides both a static method and a
    class method to perform arithmetic operations.
    """
    # A class attribute that can be accessed by class methods.
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        A static method to add two numbers.
        
        Static methods do not have access to the class or instance.
        They behave like regular functions but are namespaced within the class.

        Args:
            a (int or float): The first number.
            b (int or float): The second number.

        Returns:
            int or float: The sum of the two numbers.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        A class method to multiply two numbers.
        
        Class methods receive the class itself as the first argument ('cls'),
        giving them access to class attributes like calculation_type.

        Args:
            cls: The class itself (automatically passed).
            a (int or float): The first number.
            b (int or float): The second number.

        Returns:
            int or float: The product of the two numbers.
        """
        # Accessing the class attribute via the 'cls' parameter.
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

# The main execution block from main.py is not included here, as this file
# is intended to be imported by main.py.
