from pizza import Pizza
from pasta import Pasta
from salad import Salad

class OrderFactory:
    def create_order(self, order_type, price):
        if order_type == "Pizza":
            return Pizza(order_type, price,)
        elif order_type == "Pasta":
            return Pasta(order_type, price)
        elif order_type == "Salad":
            return Salad(order_type, price)
        

