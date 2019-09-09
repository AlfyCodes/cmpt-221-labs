'''
Parent Class Vehicle
will construct properties for vechicle type
'''
class Vehicle:
    '''
    The Constructor for all Child Clases
    '''
    def __init__(self,make,model,color,gas_capacity,gas_mileage,mileage):
        #Sets the following properties Make, Model, Color, Gas Capacity, Gas Milage, Milage
        self.make = make
        self.model = model 
        self.color = color
        self.gas_capacity = gas_capacity
        self.gas_mileage = gas_mileage
        self.mileage = mileage
    '''
    Function Menu
    Interacitve function that the user can use
    to calculate various situations depending on
    vehicle type
    '''
    def menu(self):
        #Menu Text
        print('\n\nWelcome to the Menu\n1. Calculate Drive\n2. Your Gas Capacity\n3. Current Gas Milage\n4. Current Milage\n5. Special Features\n6. Exit Program')
        choice = input()

        #Upon user choice, step into one of the if statements.
        if choice == '1':
            #Start drive function
            self.drive() 
        elif choice == '2':
            #Display Gas Capacity
            print('\nYour '+self.make+' ' +str(self.model)+' Gas Capacity is ' +str(self.gas_capacity))
            self.menu()
        elif choice == '3':
            #Display Current Gas Mileage
            print('\nCurrent Gas Mileage: '+str(self.gas_mileage))
            self.menu()
        elif choice == '4':
            #Display Current mileage
            print('\nCurrent Car Mileage: '+str(self.mileage))
            self.menu()
        elif choice == '5':
            #Figure out how to call a child class dependant on vehicle type.
            print('Woopie Specail stuff')
            special_menu(self)
            self.menu()
        elif choice == '6':
            #Exit Program
            print('Exiting Program')
            SystemExit
        else:
            #Error handaling
            print('\nPlease enter a numberic value 1-6')
            self.menu()


    '''
    print_data Function
    Print the complete data of the vehicle
    '''   
    def print_data(self):
        #Display back the data that was given
        print('\nVehicle created with the following data:\n\nMake: '+self.make,'\nModel: '+self.model, '\nColor: '+self.color,'\nCar Total Gas Milage: '+self.gas_capacity,'\nCurrent Gas Milage: '+self.gas_mileage, '\nTotal Milage: '+self.mileage)
    '''
    drive Function
    Alters ther mileage and gas mileage depending on how far the person drove
    '''
    def drive(self):
        #Get the miles driven
        print ('How many miles will/did you drive?')
        total_drive = input()
        int_total_drive = int(total_drive)
        #Error handling (not full proof) 
        if int_total_drive > 0:
            #Concatanate variables for adding
            self.mileage = int(self.mileage)
            self.gas_mileage = int(self.gas_mileage)
            #Update the Milage and Gas Milage
            self.mileage = self.mileage + int_total_drive
            self.gas_mileage = self.gas_mileage - int_total_drive
            #Display updated results
            print('\nUpdated Gas Milage: '+str(self.gas_mileage)+ '\nUpdated Milage: '+str(self.mileage))
            #Bring user back to main menu
            self.menu()
        else:
            print('Please enter a postive numeric value')
            self.drive()
    
'''
Child Class Motorcycle: Parent Class is Vehicle 
'''
class Motorcycle(Vehicle):
    def __init__(self,make,model,color,gas_capacity,gas_mileage,mileage):
        super().__init__(make,model,color,gas_capacity,gas_mileage,mileage)
    def special_menu(self):
        print('\n\nWelcome to the Motorcycle special menu!')
'''
Child Class Truck: Parent Class is Vehicle
'''        
class Truck(Vehicle):
    def __init__(self,make,model,color,gas_capacity,gas_mileage,mileage):
        super().__init__(make,model,color,gas_capacity,gas_mileage,mileage)
    def special_menu(self):
        print('\n\nWelcome to the Truck special menu!')
        
'''
Child Class Bus: Parent Class is Vehicle
'''    
class Bus(Vehicle):
    def __init__(self,make,model,color,gas_capacity,gas_mileage,mileage):
        super().__init__(make,model,color,gas_capacity,gas_mileage,mileage)
    def special_menu(self):
        
        print('\n\nWelcome to the Bus special menu!')
        
'''
Child Class Car: Parent Class is Vehicle
'''
class Car(Vehicle):
    def __init__(self,make,model,color,gas_capacity,gas_mileage,mileage):
        super().__init__(make,model,color,gas_capacity,gas_mileage,mileage)
    def special_menu(self):
        print('\n\nWelcome to the Car special menu!')
        #Menu Text
        print('\n1. Order the babe magnet special! (no refunds) \n2. Vroom your car! \n3. Return to main menu')
        choice = input()

        #Upon user choice, step into one of the if statements.
        if choice == '1':
            #Order the babe magnet
            print('Well, well, well... Player One just entered the building!\n(your babe magnet special has been ordered)')
            self.special_menu()
        elif choice == '2':
            #Vroom vroom?
            print('choice 2')
            print('\n(vroom... vroom!...) Listen... I am crunching for time here, what did you expect?')
            self.special_menu()
        elif choice == '3':
            #Return to Main Menu
            self.menu()


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
    gas_mileage = input()

    print('What is the Milage of your vehicle?')
    mileage = input()

    return(make,model,color,gas_capacity,gas_mileage,mileage)

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
        make,model,color,gas_capacity,gas_mileage,mileage = get_data()
        car = Car(make,model,color,gas_capacity,gas_mileage,mileage)
        return car
    elif type_vehicle == 'truck':
        print('you chose truck')
        make,model,color,gas_capacity,gas_mileage,mileage = get_data()
        truck = Truck(make,model,color,gas_capacity,gas_mileage,mileage)
        return truck
    elif type_vehicle == 'motorcycle':
        print('you chose bike')
        make,model,color,gas_capacity,gas_mileage,mileage = get_data()
        motorcycle = Motorcycle(make,model,color,gas_capacity,gas_mileage,mileage)
        return motorcycle
    elif type_vehicle == 'bus':
        print('you chose bus')
        make,model,color,gas_capacity,gas_mileage,mileage = get_data()
        bus = Bus(make,model,color,gas_capacity,gas_mileage,mileage)
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
