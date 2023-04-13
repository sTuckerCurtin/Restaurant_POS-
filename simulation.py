from franchise import Franchise


class Simulation:
    def run_simulation(self):
        franchise1 = Franchise(1)
        franchise2 = Franchise(2)
        franchise3 = Franchise(3)


        for i in range(3):
            franchise1.place_order()
            franchise2.place_order()
            franchise3.place_order()

