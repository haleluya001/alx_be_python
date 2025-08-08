
"""
book_class.py

This script defines a Book class that demonstrates the use of Python's
magic methods for initialization, deletion, and object representation.
"""

class Book:
    """
    A class to model a book with a title, author, and publication year.
    It includes magic methods for constructor, destructor, and string
    representations.
    """

    def __init__(self, title, author, year):
        """
        Constructor (__init__) to initialize a Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year.
        """
        self.title = title
        self.author = author
        self.year = year
        print(f"Book '{self.title}' created.")

    def __del__(self):
        """
        Destructor (__del__) to print a message when the object is deleted.
        Note: The timing of this method's execution can be non-deterministic.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        String Representation (__str__) for a human-readable format.
        This is used by functions like print().

        Returns:
            str: A formatted string: "(title) by (author), published in (year)".
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official Representation (__repr__) for an unambiguous format.
        This string can be used to recreate the object.

        Returns:
            str: A formatted string: f"Book('{self.title}', '{self.author}', {self.year})".
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"

# The main execution block from main.py is not included here, as this file
# is intended to be imported by main.py.
