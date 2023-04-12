from pizza import Pizza
from pasta import Pasta
from salad import Salad

class OrderFactory:
    def create_order(self, order_type, price, store):
        if order_type == "Pizza":
            return Pizza(price, store)
        elif order_type == "Pasta":
            return Pasta(price, store)
        elif order_type == "Salad":
            return Salad(price, store)
        

        