from order import Order

class Salad(Order):
    def __init__(self, name, price):
        super().__init__(name, price)