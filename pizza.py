from order import Order

class Pizza(Order):
    def __init__(self, name, price, store) -> None:
        super().__init__(name, price, store)