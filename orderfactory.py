from pizza import Pizza
from pasta import Pasta
from salad import Salad

class OrderFactory:
    def create_order(self, order_type, store):
        if order_type == "Pizza":
            return Pizza(order_type, store)
        elif order_type == "Pasta":
            return Pasta(order_type, store)
        elif order_type == "Salad":
            return Salad(order_type, store)
        

