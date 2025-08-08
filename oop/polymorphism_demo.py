
"""
polymorphism_demo.py

This script demonstrates polymorphism and method overriding in Python.
It defines a base Shape class and two derived classes, Rectangle and Circle,
each with its own implementation of the area() method.
"""

import math

class Shape:
    """
    A base class for geometric shapes.
    It defines an area() method that must be overridden by subclasses.
    """
    def area(self):
        """
        Calculates the area of the shape. This is a placeholder method that
        will be overridden by derived classes.
        """
        raise NotImplementedError("Subclasses must implement this method")

class Rectangle(Shape):
    """
    A derived class representing a rectangle.
    It inherits from Shape and overrides the area() method.
    """
    def __init__(self, length: float, width: float):
        """
        Initializes a Rectangle instance.

        Args:
            length (float): The length of the rectangle.
            width (float): The width of the rectangle.
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Overrides the area() method to calculate the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.length * self.width

class Circle(Shape):
    """
    A derived class representing a circle.
    It inherits from Shape and overrides the area() method.
    """
    def __init__(self, radius: float):
        """
        Initializes a Circle instance.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Overrides the area() method to calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * (self.radius ** 2)

# The main execution block from main.py is not included here, as this file
# is intended to be imported by main.py.
