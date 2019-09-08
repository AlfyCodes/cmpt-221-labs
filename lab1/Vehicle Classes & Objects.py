'''
Parent Class Vechicle
will construct properties for vechicle type
'''
class Vechicle:
    def __init__(self, make,model,color):
        self.make = make
        self.model = model 
        self.color = color
       
    def drive(self,fuel_current,miles_current,total_drive):
        self.miles_current = self.miles_current + total_drive
        self.fuel_current = fuel_current - total_drive
    
'''
Child Class Motorcycle
Will handle three properties
'''
class Motorcycle(Vechicle):
    def __init__(self,fuel_max,fuel_current,miles_current):
        super()__init__(self,make,model,color)
        self.fuel_max = fuel_max
        self.fuel_current = fuel_current
        self.miles_current = miles_current
'''
Child Class Truck
Will handle three properties
'''        
class Truck(Vechicle):
    def __init__(self,fuel_max,fuel_current,miles_current):
        self.fuel_max = fuel_max
        self.fuel_current = fuel_current
        self.miles_current = miles_current
'''
Child Class Bus
Will handle three properties
'''    
class Bus(Vechicle):
    def __init__(self,fuel_max,fuel_current,miles_current):
        self.fuel_max = fuel_max
        self.fuel_current = fuel_current
        self.miles_current = miles_current
'''
Child Class Bicycle
Will handle it's own property condition
'''
class Bicycle(Vechicle):
    def __init__(self,condition):
        self.condition = condition

bike = Motorcycle(20,10,100)

