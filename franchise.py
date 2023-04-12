from logger import Logger
from orderfactory import OrderFactory

# logger = Logger()
# order = OrderFactory()

class Franchise:
    def __init__(self):
        self.location_number = 0

    def place_order(self):
        order_type = input("What would you like to order Pizza, Pasta or a Salad? ")
        price = float(input("Enter the Price of the item "))
        store = input("Enter Store Number ")

        order = OrderFactory()
        order.create_order(order_type, price)
        logger = Logger()
        logger.log_transaction(order_type, price, store)