from order import Order

class Pasta(Order):
    def __init__(self, name, price):
        super().__init__(name, price)