class Vechicle:
    def __init__(self, make,model,color):
        self.make = make
        self.model = model 
        self.color = color
       
    def drive(self,fuel_current,miles_current):
        pass
class Motorcycle(Vechicle):
    def __init__(self,fuel_max,fuel_current,miles_current):
        self.fuel_max = fuel_max
        self.fuel_current = fuel_current
        self.miles_current = miles_current        
class Truck(Vechicle):
    def __init__(self,fuel_max,fuel_current,miles_current):
        self.fuel_max = fuel_max
        self.fuel_current = fuel_current
        self.miles_current = miles_current    
class Bus(Vechicle):
    def __init__(self,fuel_max,fuel_current,miles_current):
        self.fuel_max = fuel_max
        self.fuel_current = fuel_current
        self.miles_current = miles_current
class Bicycle(Vechicle):
    def __init__(self,condition):
        self.condition = condition
