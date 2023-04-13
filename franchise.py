from logger import Logger
from orderfactory import OrderFactory
# from pizza import Pizza
# from pasta import Pasta
# from salad import Salad


price = float
class Franchise:
    def __init__(self, location_number):
        self.location_number = location_number

    def place_order(self):
        order_type = input(f"From store {self.location_number } What would you like to order? Pizza, Pasta or a Salad? ")
        if order_type == "Pizza":
            order_price = 25
        elif order_type == "Pasta":
            order_price = 10.00
        elif order_type == "Salad":
            order_price = 5.00
        

        order = OrderFactory()
        order.create_order(order_type, self.location_number)
        logger = Logger()
        logger.log_transaction(order_type, order_price, self.location_number )