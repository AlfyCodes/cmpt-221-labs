'''
Parent Class Vehicle
will construct properties for vechicle type
'''
class Vehicle:
    def __init__(self,make,model,color,fuel_max,fuel_current,miles_current):
        self.make = make
        self.model = model 
        self.color = color
        self.fuel_max = fuel_max
        self.fuel_current = fuel_current
        self.miles_current = miles_current
       
    def print_data(self):

        print(self.make,self.model,self.color,self.fuel_max,self.fuel_current,self.miles_current)

    def drive(self,fuel_current,miles_current,total_drive):
        self.miles_current = self.miles_current + total_drive
        self.fuel_current = fuel_current - total_drive
    
'''
Child Class Motorcycle
Will handle three properties
CURRENTLY TESTING THIS CLASS ONLY
'''
class Motorcycle(Vehicle):
    def __init__(self,make,model,color,fuel_max,fuel_current,miles_current):
        super().__init__(make,model,color,fuel_max,fuel_current,miles_current)
'''
Child Class Truck
Will handle three properties
'''        
class Truck(Vehicle):
    def __init__(self,make,model,color,fuel_max,fuel_current,miles_current):
        super().__init__(make,model,color,fuel_max,fuel_current,miles_current)
        
'''
Child Class Bus
Will handle three properties
'''    
class Bus(Vehicle):
    def __init__(self,make,model,color,fuel_max,fuel_current,miles_current):
        super().__init__(make,model,color,fuel_max,fuel_current,miles_current)
'''
Child Class Bicycle
Will handle it's own property condition
'''
class Car(Vehicle):
    def __init__(self,make,model,color,fuel_max,fuel_current,miles_current):
        super().__init__(make,model,color,fuel_max,fuel_current,miles_current)

class main():
    
    def get_data()
        print ('What is the Make of your vehicle?')
        make = input()

    print('What is the Model of your vehicle?')
    model = input()

    print('What is the Color of your vehicle?')
    color = input()

'''
Asking the User the questions to store data
'''


bike = Motorcycle(make,model,color,20,10,1000)

bike.print_data()
 
#Vehicle.drive(bike)

#print(bike)
