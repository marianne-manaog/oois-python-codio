class Item:
    """
    This class defines an item.

    Attributes, name, price, quantity, subtotal (0 by default)
    """

    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.subtotal: float = 0.

    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.quantity}, {self.price * self.quantity})"

    def calculate_subtotal(self):
        self.subtotal = self.price * self.quantity

    def get_subtotal(self):
        return self.subtotal
