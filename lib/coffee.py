class Coffee:
    """
    A class to represent a coffee product in a bookstore.
    
    Attributes:
        name (str): The name of the coffee
        roast_level (str): The roast level (light, medium, dark)
        price (float): The price of the coffee
        quantity (int): The quantity of coffee packs in stock
        origin (str): The origin/source of the coffee beans
    """
    
    def __init__(self, name, roast_level, price, quantity=0, origin="Unknown"):
        """
        Initialize a Coffee object.
        
        Args:
            name (str): The name of the coffee
            roast_level (str): The roast level (light, medium, dark)
            price (float): The price of the coffee
            quantity (int): The quantity of coffee packs in stock (default: 0)
            origin (str): The origin/source of the coffee beans (default: "Unknown")
        """
        self.name = name
        self.roast_level = roast_level
        self.price = price
        self.quantity = quantity
        self.origin = origin
    
    def get_name(self):
        """Return the name of the coffee."""
        return self.name
    
    def get_roast_level(self):
        """Return the roast level of the coffee."""
        return self.roast_level
    
    def get_price(self):
        """Return the price of the coffee."""
        return self.price
    
    def get_quantity(self):
        """Return the quantity of coffee in stock."""
        return self.quantity
    
    def get_origin(self):
        """Return the origin of the coffee beans."""
        return self.origin
    
    def set_price(self, new_price):
        """
        Set a new price for the coffee.
        
        Args:
            new_price (float): The new price
        """
        if new_price >= 0:
            self.price = new_price
        else:
            raise ValueError("Price cannot be negative")
    
    def set_quantity(self, new_quantity):
        """
        Set a new quantity for the coffee.
        
        Args:
            new_quantity (int): The new quantity
        """
        if new_quantity >= 0:
            self.quantity = new_quantity
        else:
            raise ValueError("Quantity cannot be negative")
    
    def set_origin(self, new_origin):
        """
        Set a new origin for the coffee.
        
        Args:
            new_origin (str): The new origin
        """
        self.origin = new_origin
    
    def add_stock(self, amount):
        """
        Add coffee packs to stock.
        
        Args:
            amount (int): The number of packs to add
        """
        if amount < 0:
            raise ValueError("Amount to add cannot be negative")
        self.quantity += amount
    
    def remove_stock(self, amount):
        """
        Remove coffee packs from stock.
        
        Args:
            amount (int): The number of packs to remove
        
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
        """Return a string representation of the coffee."""
        return f"Coffee: {self.name} ({self.roast_level} roast) - ${self.price} (Origin: {self.origin}, Stock: {self.quantity})"
    
    def __repr__(self):
        """Return a detailed string representation of the coffee."""
        return f"Coffee(name='{self.name}', roast_level='{self.roast_level}', price={self.price}, quantity={self.quantity}, origin='{self.origin}')"