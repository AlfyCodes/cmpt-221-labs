'''
Parent Class Vehicle
will construct properties for vechicle type
'''
class Vehicle:
    '''
    The Constructor for all Child Clases
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
    print_data Function
    Print the complete data of the vehicle
    '''   
    def print_data(self):

        print(self.make,self.model,self.color,self.gas_capacity,self.gas_milage,self.milage)
    '''
    drive Function
    Alters ther milage and gas milage depending on how far the person drove
    '''
    def drive(self,gas_milage,milage,total_drive):
        self.milage = self.milage + total_drive
        self.gas_milage = gas_milage - total_drive
    
'''
Child Class Motorcycle
CURRENTLY TESTING THIS CLASS ONLY
'''
class Motorcycle(Vehicle):
    def __init__(self,make,model,color,gas_capacity,gas_milage,milage):
        super().__init__(make,model,color,gas_capacity,gas_milage,milage)
'''
Child Class Truck
'''        
class Truck(Vehicle):
    def __init__(self,make,model,color,gas_capacity,gas_milage,milage):
        super().__init__(make,model,color,gas_capacity,gas_milage,milage)
        
'''
Child Class Bus
'''    
class Bus(Vehicle):
    def __init__(self,make,model,color,gas_capacity,gas_milage,milage):
        super().__init__(make,model,color,gas_capacity,gas_milage,milage)
'''
Child Class Bicycle
'''
class Car(Vehicle):
    def __init__(self,make,model,color,gas_capacity,gas_milage,milage):
        super().__init__(make,model,color,gas_capacity,gas_milage,milage)


'''
Below this line the functions outside of classes will begin
'''

'''
Function get_data()
Grabs all the data about the vehicle from user
'''
def get_data():
    #Questions about the vehicle
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
Prompt user for data to store into a new vehicle variable
'''
def create_vehicle():
    #Ask the user for type of vehicle so we can properly store to the right class.
    print ('What type_vehicle of Vehicle do you have? \nCar \nTruck \nMotorcycle \nBus')
    type_vehicle = input()
    type_vehicle = type_vehicle.lower()

    #Error Handling - completed but needs adjustments to flow with the project
    if type_vehicle == 'car':
        print('you chose car')
        make,model,color,gas_capacity,gas_milage,milage = get_data()
        car = Car(make,model,color,gas_capacity,gas_milage,milage)
        return car
    elif type_vehicle == 'truck':
        print('you chose truck')
        make,model,color,gas_capacity,gas_milage,milage = get_data()
        truck = Truck(make,model,color,gas_capacity,gas_milage,milage)
        return truck
    elif type_vehicle == 'motorcycle':
        print('you chose bike')
        make,model,color,gas_capacity,gas_milage,milage = get_data()
        motorcycle = Motorcycle(make,model,color,gas_capacity,gas_milage,milage)
        return motorcycle
    elif type_vehicle == 'bus':
        print('you chose bus')
        make,model,color,gas_capacity,gas_milage,milage = get_data()
        bus = Bus(make,model,color,gas_capacity,gas_milage,milage)
        return bus
    else:
        print('Please enter a valid Vehicle type.')
        main()



'''
Main function to handle the program
'''
    
def main():
    vehicle = create_vehicle()
    vehicle.print_data()

#Start Program
main()
