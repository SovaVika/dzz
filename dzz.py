class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def print(self):
        print("Виробник -", self.make)
        print("Модель -", self.model)
        print("Рік -", self.year)