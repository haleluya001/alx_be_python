class Book:
    """
    Represents a book in the library.
    
    Attributes:
        title (str): The title of the book (public).
        author (str): The author of the book (public).
        _is_checked_out (bool): A private attribute to track if the book is
                                currently checked out.
    """
    def __init__(self, title, author):
        """
        Initializes a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """
        Marks the book as checked out.
        """
        self._is_checked_out = True

    def return_book(self):
        """
        Marks the book as returned and available.
        """
        self._is_checked_out = False

    def is_available(self):
        """
        Returns the availability status of the book.
        
        Returns:
            bool: True if the book is available, False otherwise.
        """
        return not self._is_checked_out

class Library:
    """
    Manages a collection of books.
    
    Attributes:
        _books (list): A private list to store Book objects.
    """
    def __init__(self):
        """
        Initializes a new Library instance with an empty list of books.
        """
        self._books = []

    def add_book(self, book):
        """
        Adds a Book object to the library's collection.

        Args:
            book (Book): The Book instance to add.
        """
        self._books.append(book)
        print(f"Book '{book.title}' by {book.author} has been added to the library.")

    def check_out_book(self, title):
        """
        Finds a book by its title and checks it out if available.

        Args:
            title (str): The title of the book to check out.
        """
        found = False
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"Successfully checked out '{title}'.")
                found = True
                break
        if not found:
            print(f"Book '{title}' is not available for checkout.")

    def return_book(self, title):
        """
        Finds a book by its title and marks it as returned.

        Args:
            title (str): The title of the book to return.
        """
        found = False
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"Successfully returned '{title}'.")
                found = True
                break
        if not found:
            print(f"Book '{title}' was not found or was not checked out.")

    def list_available_books(self):
        """
        Prints the title and author of all books that are currently available.
        """
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")