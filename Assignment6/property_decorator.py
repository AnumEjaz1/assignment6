class Product:
    def __init__(self, price):
        self._price = price  # private attribute

    # Getter method
    @property
    def price(self):
        return self._price

    # Setter method
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative!")
        self._price = value

    # Deleter method
    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price


# Example usage
p = Product(100)
print(p.price)      # Get price: 100

p.price = 150       # Update price
print(p.price)      # Get price: 150

del p.price         # Delete price

# Accessing after deletion will raise an AttributeError
# print(p.price)    # Uncommenting this line will cause an error
