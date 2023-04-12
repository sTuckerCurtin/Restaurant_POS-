from orderfactory import OrderFactory

class Logger:
    def __init__(self) -> None:
        
        self.transaction_count = 0
        self.daily_sales = 0


    def log_transaction(self, order_name, order_price, order_store):
        self.transaction_count += 1
        self.daily_sales += order_price
        
        with open("log.txt","a") as file:
            file.write(
                f"Transaction Count : {self.transaction_count}\n"
                f"Dish Ordered : {order_name}\n"
                f"Store {order_store}\n"
                f"Price : ${order_price}\n"
                f"Daily Income: ${self.daily_sales}\n"
            )



