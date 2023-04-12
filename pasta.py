from order import Order

class Pasta(Order):
    def __init__(self, name, price, store) -> None:
        super().__init__(name, price, store)