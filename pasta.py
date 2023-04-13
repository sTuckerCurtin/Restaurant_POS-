from order import Order

class Pasta(Order):
    def __init__(self, name, store):
        price = 7.99
        super().__init__(name, price, store)