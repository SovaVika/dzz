class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def print(self):
        veh_inf = f"Vehicle:\nВиробник - {self.make}\nМодель - {self.model}"
        print(veh_inf)
        return veh_inf