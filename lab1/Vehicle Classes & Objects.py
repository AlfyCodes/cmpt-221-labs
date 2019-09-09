'''
Parent Class Vehicle
will construct properties for vechicle type
'''
class Vehicle:
    '''
    The Constructor for all child clases
    '''
    def __init__(self,make,model,color,gas_capacity,gas_milage,milage):
        #Sets the following properties Make, Model, Color, Gas Capacity, Gas Milage, Milage
        self.make = make
        self.model = model 
        self.color = color
        self.gas_capacity = gas_capacity
        self.gas_milage = gas_milage
        self.milage = milage
    '''
    Print the complete data of the vehicle
    '''   
    def print_data(self):

        print(self.make,self.model,self.color,self.gas_capacity,self.gas_milage,self.milage)
    '''
    Alters ther milage and gas milage depending on how far the person drove
    '''
    def drive(self,gas_milage,milage,total_drive):
        self.milage = self.milage + total_drive
        self.gas_milage = gas_milage - total_drive
    
'''
Child Class Motorcycle
Will handle three properties
CURRENTLY TESTING THIS CLASS ONLY
'''
class Motorcycle(Vehicle):
    def __init__(self,make,model,color,gas_capacity,gas_milage,milage):
        super().__init__(make,model,color,gas_capacity,gas_milage,milage)
'''
Child Class Truck
Will handle three properties
'''        
class Truck(Vehicle):
    def __init__(self,make,model,color,gas_capacity,gas_milage,milage):
        super().__init__(make,model,color,gas_capacity,gas_milage,milage)
        
'''
Child Class Bus
Will handle three properties
'''    
class Bus(Vehicle):
    def __init__(self,make,model,color,gas_capacity,gas_milage,milage):
        super().__init__(make,model,color,gas_capacity,gas_milage,milage)
'''
Child Class Bicycle
Will handle it's own property condition
'''
class Car(Vehicle):
    def __init__(self,make,model,color,gas_capacity,gas_milage,milage):
        super().__init__(make,model,color,gas_capacity,gas_milage,milage)







def get_data():

        print ('What type of Vehicle do you have? \nCar \nTruck \nMotorcycle \nBus')
        type = input()
        type = type.lower()

        if type == 'car' or type == 'truck' or type == 'motorcycle' or type == 'bus':
            print('you picked the right type')
        else:
            print('Please enter a valid Vehicle type.')
            main()


        print ('What is the Make of your vehicle?')
        make = input()
        
        print('What is the Model of your vehicle?')
        model = input()

        print('What is the Color of your vehicle?')
        color = input()

        print('What is the max Gas Miles of your vehicle?')
        gas_capacity = input()

        print('What is the current Gas Miles of your vehicle?')
        gas_milage = input()

        print('What is the Milage of your vehicle?')
        milage = input()
        
        return(make,model,color,gas_capacity,gas_milage,milage)



'''
Main function to handle all user based inputs
'''
    
def main():
    get_data()
    
'''
Asking the User the questions to store data
'''

main()
 
#Vehicle.drive(bike)

#print(bike)
