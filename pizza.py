from order import Order

class Pizza(Order):
    def __init__(self, name, store):
        price = 9.99
        super().__init__(name, price, store)
        