from order import Order

class Salas(Order):
    def __init__(self, name, price) -> None:
        super().__init__(name, price)