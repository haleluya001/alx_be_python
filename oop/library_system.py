
"""
library_system.py

This script defines a set of classes to model a simple library system,
demonstrating inheritance, composition, and polymorphism in Python.
"""

class Book:
    """
    A base class to represent a generic book.
    """
    def __init__(self, title: str, author: str):
        """
        Initializes a Book instance with a title and author.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        Returns a string representation of the Book object.
        """
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    """
    A derived class representing an electronic book.
    It inherits from the Book class.
    """
    def __init__(self, title: str, author: str, file_size: int):
        """
        Initializes an EBook instance, calling the base class constructor
        and adding the file_size attribute.

        Args:
            title (str): The title of the e-book.
            author (str): The author of the e-book.
            file_size (int): The size of the e-book file in KB.
        """
        # Call the base class constructor to initialize title and author
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """
        Overrides the __str__ method to include the file size.
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    """
    A derived class representing a physical print book.
    It inherits from the Book class.
    """
    def __init__(self, title: str, author: str, page_count: int):
        """
        Initializes a PrintBook instance, calling the base class constructor
        and adding the page_count attribute.

        Args:
            title (str): The title of the print book.
            author (str): The author of the print book.
            page_count (int): The number of pages in the book.
        """
        # Call the base class constructor to initialize title and author
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """
        Overrides the __str__ method to include the page count.
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    """
    A class that represents a library, using composition to manage a
    collection of book objects.
    """
    def __init__(self):
        """
        Initializes a Library instance with an empty list to hold books.
        """
        self.books = []

    def add_book(self, book: Book):
        """
        Adds a Book, EBook, or PrintBook instance to the library's collection.

        Args:
            book (Book): An instance of a book class to be added.
        """
        self.books.append(book)

    def list_books(self):
        """
        Prints the details of each book in the library's collection.
        This method now uses polymorphism by calling the __str__ method
        of each book object.
        """
        for book in self.books:
            print(book)
