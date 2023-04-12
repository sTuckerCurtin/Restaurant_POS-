from logger import Logger
from orderfactory import OrderFactory


class Franchise:
    def __init__(self) -> None:
        self.location_number = 0

    def place_order(self):
        order_type = input("What would you like to order? ")
        price = float(input("Enter the Price of the item"))
        store = input("Enter Store Number")


        order = OrderFactory.create_order(order_type, price, store)
        Logger.log_transaction(order)