import dzz

class Car(dzz.Vehicle):
    def __init__(self, num_doors, num_wheels):
        self.num_doors = num_doors
        self.num_wheels = num_wheels
s = Car(dzz.Vehicle, 4,4)
s.dzz.Vehicle("lamborghini", "Gallardo Spider", 2011)