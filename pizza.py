from order import Order

class Pizza(Order):
    def __init__(self, name, price):
        super().__init__(name, price)