from order import Order

class Salad(Order):
    def __init__(self, name, store):
        price = 5.99
        super().__init__(name, price, store)