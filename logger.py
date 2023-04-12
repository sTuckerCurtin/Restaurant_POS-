from order import Order


class Logger:
    transaction_count = 0
    daily_sales = 0


    def log_transaction(order):
        Logger.transaction_count += 1
        Logger.daily_sales += order.price
        with open("log.txt","a") as file:
            file.write(
                f"Transaction Count : {Logger.transaction_count}"
                f"Dish Ordered : {order.name}"
                f"Store {order.store}"
                f"Price : ${order.price}"
                f"Daily Income: ${Logger.daily_sales}"
            )