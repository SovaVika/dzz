import dzz

class Car(dzz.Vehicle):
    def __init__(self, num_doors, num_wheels):
        self.num_doors = num_doors
        self.num_wheels = num_wheels
        

car = Car("Toyota", "Corolla", 2022, 4, 4)