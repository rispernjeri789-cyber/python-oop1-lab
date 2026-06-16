class Book:
    """
    A class to represent a book in a bookstore.
    
    Attributes:
        title (str): The title of the book
        author (str): The author of the book
        price (float): The price of the book
        isbn (str): The ISBN number of the book
        quantity (int): The quantity of books in stock
    """
    
    def __init__(self, title, author, price, isbn, quantity=0):
        """
        Initialize a Book object.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            price (float): The price of the book
            isbn (str): The ISBN number of the book
            quantity (int): The quantity of books in stock (default: 0)
        """
        self.title = title
        self.author = author
        self.price = price
        self.isbn = isbn
        self.quantity = quantity
    
    def get_title(self):
        """Return the title of the book."""
        return self.title
    
    def get_author(self):
        """Return the author of the book."""
        return self.author
    
    def get_price(self):
        """Return the price of the book."""
        return self.price
    
    def get_isbn(self):
        """Return the ISBN of the book."""
        return self.isbn
    
    def get_quantity(self):
        """Return the quantity of books in stock."""
        return self.quantity
    
    def set_price(self, new_price):
        """
        Set a new price for the book.
        
        Args:
            new_price (float): The new price
        """
        if new_price >= 0:
            self.price = new_price
        else:
            raise ValueError("Price cannot be negative")
    
    def set_quantity(self, new_quantity):
        """
        Set a new quantity for the book.
        
        Args:
            new_quantity (int): The new quantity
        """
        if new_quantity >= 0:
            self.quantity = new_quantity
        else:
            raise ValueError("Quantity cannot be negative")
    
    def add_stock(self, amount):
        """
        Add books to stock.
        
        Args:
            amount (int): The number of books to add
        """
        if amount < 0:
            raise ValueError("Amount to add cannot be negative")
        self.quantity += amount
    
    def remove_stock(self, amount):
        """
        Remove books from stock.
        
        Args:
            amount (int): The number of books to remove
        
        Returns:
            bool: True if successful, False if insufficient stock
        """
        if amount < 0:
            raise ValueError("Amount to remove cannot be negative")
        if amount > self.quantity:
            return False
        self.quantity -= amount
        return True
    
    def __str__(self):
        """Return a string representation of the book."""
        return f"Book: {self.title} by {self.author} - ${self.price} (ISBN: {self.isbn}, Stock: {self.quantity})"
    
    def __repr__(self):
        """Return a detailed string representation of the book."""
        return f"Book(title='{self.title}', author='{self.author}', price={self.price}, isbn='{self.isbn}', quantity={self.quantity})"