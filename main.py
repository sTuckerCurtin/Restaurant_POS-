
from franchise import Franchise
from simulation import Simulation

if __name__ == "__main__":
    
    franchise1 = Franchise()
    franchise2 = Franchise()
    franchise3 = Franchise()

   
    for _ in range(3):
        franchise1.place_order()
        franchise2.place_order()
        franchise3.place_order()

    
    Simulation.run_simulation()
