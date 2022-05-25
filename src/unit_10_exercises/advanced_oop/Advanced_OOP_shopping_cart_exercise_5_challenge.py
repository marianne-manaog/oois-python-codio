class ShoppingCart:
    """
    This class defines a shopping cart.

    Attributes: item, total (0 by default)
    """

    def __init__(self):
        self.items = []
        self.total: float = 0

    def __str__(self):
        return f"The cart has {len(self.items)} items for a total of {self.total}"

    def add_item(self, item):
        self.items.append(item)
        self.calculate_total()

    def calculate_total(self):
        list_of_totals = []
        for i in range(len(self.items)):
            list_of_totals.append(self.items[i].price * self.items[i].quantity)
        self.total = sum(list_of_totals)

    def get_total(self):
        return self.total

    def get_num_items(self):
        num_items = len(self.items)
        return num_items

    def get_items(self):
        return self.items
