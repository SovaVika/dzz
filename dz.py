import dzz

class Car(dzz.Vehicle):
    def __init__(self, num_doors, num_wheels):
        dzz.Vehicle.__init__(self, "Lamborghini", "Aventador", 2022) 
        self.num_doors = num_doors
        self.num_wheels = num_wheels
    def __str__(self):
        return f"Авто:\nКількість дверей - {self.num_doors}\nКількість коліс - {self.num_wheels}\nВиробник - {self.make}\nМодель - {self.model}\nРік - {self.year}\n"

class Motorcycle(dzz.Vehicle):
    def __init__(self, engine_size, num_wheels, color):
        dzz.Vehicle.__init__(self, "Honda", "SH 125", 2001) 
        self.engine_size = engine_size
        self.num_wheels = num_wheels
        self.color = color
    def __str__(self):
        return f"Мотоцикл:\nРозмір двигуна - {self.engine_size}\nКількість коліс - {self.num_wheels}\nКолір - {self.color}\nВиробник - {self.make}\nМодель - {self.model}\nВиробник - {self.year}"

car = Car(4, 4)
motorcycle = Motorcycle("125 см3", 2, "чорний")
print(car)
print(motorcycle)