class Vechicle:
    def __init__(self, make,model,color,fuel_max,fuel_current,miles_current):
        self.make = make
        self.model = model 
        self.color = color
        self.fuel_max = fuel_max
        self.fuel_current = fuel_current
        self.miles_current = miles_current
class Motorcycle(Vechicle):
    pass        
class Truck(Vechicle):
    pass
class Bicycle(Vechicle):
    pass
class Bus(Vechicle):
    pass
