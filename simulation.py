from franchise import Franchise


class Simulation:
    def run_simulation(self):
        franchise1 = Franchise()
        franchise2 = Franchise()
        franchise3 = Franchise()


        for i in range(3):
            franchise1.place_order()
            franchise2.place_order()
            franchise3.place_order()


        if __name__ == "__main__":

            Simulation.run_simulation