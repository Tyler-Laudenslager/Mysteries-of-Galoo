class Item:

    def __init__(self, name, price, quantity = 0):
        self._name = name
        self._quantity = quantity
        self._price = price

    def increment_quantity(self, amount):
        for i in range(amount):
            self._quantity += 1

    def zero(self):
        self._quantity = 0

    def get_price(self):
        return self._price * self._quantity

    def get_item(self):
        return {self._name: self._quantity}