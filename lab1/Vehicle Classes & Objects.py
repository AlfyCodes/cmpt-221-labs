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
    Function Menu
    Interacitve function that the user can use
    to calculate various situations depending on
    vehicle type
    '''
    def menu(self):

        print('\n\nWelcome to the Menu\n1. Calculate Drive\n2. Your Gas Capacity\n3. Current Gas Milage\n4. Current Milage\n5. Special Features\n6. Exit Program')
        choice = input()

        if choice == '1':
            self.drive() 
        elif choice == '2':
            print('choice 2')
            print('\nYour '+self.make+' ' +self.model+' Gas Capacity is ' +self.gas_capacity)
            self.menu()
        elif choice == '3':
            print('\nCurrent Gas Milage: '+self.gas_milage)
            self.menu()
        elif choice == '4':
            print('\nCurrent Car Milage: '+self.milage)
            self.menu()
        elif choice == '5':
            #Figure out how to call a child class dependant on vehicle type.
            print('Woopie Specail stuff')
            special_menu(self)
            self.menu()
        elif choice == '6':
            print('Exiting Program')
            SystemExit
        else:
            print('\nPlease enter a numberic value 1-6')
            self.menu()


    '''
    print_data Function
    Print the complete data of the vehicle
    '''   
    def print_data(self):

        print('\nVehicle created with the following data:\n\nMake: '+self.make,'\nModel: '+self.model, '\nColor: '+self.color,'\nCar Total Gas Milage: '+self.gas_capacity,'\nCurrent Gas Milage: '+self.gas_milage, '\nTotal Milage: '+self.milage)
    '''
    drive Function
    Alters ther milage and gas milage depending on how far the person drove
    '''
    def drive(self):
        
        print ('How many miles will/did you drive?')
        total_drive = input()
        int_total_drive = int(total_drive)
        if int_total_drive > 0:
            #Problem adding together ints. TypeError: can only concatenate str (not "int") to str
            
            self.milage = int(self.milage + int_total_drive)
            self.gas_milage = self.gas_milage - int_total_drive
            print('\nUpdated Gas Milage: '+self.gas_milage+ '\nUpdated Milage: '+self.milage)
        else:
            print('Please enter a postive numeric value')
            self.drive()
    
'''
Child Class Motorcycle
CURRENTLY TESTING THIS CLASS ONLY
'''
class Motorcycle(Vehicle):
    def __init__(self,make,model,color,gas_capacity,gas_milage,milage):
        super().__init__(make,model,color,gas_capacity,gas_milage,milage)
    def special_menu(self):
        print('\n\nWelcome to the special Menu! Motorcycle')
'''
Child Class Truck
'''        
class Truck(Vehicle):
    def __init__(self,make,model,color,gas_capacity,gas_milage,milage):
        super().__init__(make,model,color,gas_capacity,gas_milage,milage)
    def special_menu(self):
        print('\n\nWelcome to the special Menu! Truck')
        
'''
Child Class Bus
'''    
class Bus(Vehicle):
    def __init__(self,make,model,color,gas_capacity,gas_milage,milage):
        super().__init__(make,model,color,gas_capacity,gas_milage,milage)
    def special_menu(self):
        print('\n\nWelcome to the special Menu! Bus')
'''
Child Class Car
'''
class Car(Vehicle):
    def __init__(self,make,model,color,gas_capacity,gas_milage,milage):
        super().__init__(make,model,color,gas_capacity,gas_milage,milage)
    def special_menu(self):
        print('\n\nWelcome to the Car special Menu!')


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

    #Error Handling and the creation of Class varible depending on user's car
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

def special_menu(self):
    self.special_menu()

def main():
    #Create the vehicle, also can call functions from classes by just using 'vehicle' variable.
    vehicle = create_vehicle()
    vehicle.print_data()
    vehicle.menu()

    special_menu(vehicle)
#Start Program
main()
