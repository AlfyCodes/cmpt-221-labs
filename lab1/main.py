

def get_cost():
    items_cost = eval(input("What is the total cost of your items? "))
    return items_cost



#Start Loop

#Boolean type for loop
calculate = True

while calculate == True:
    #Find the total cost of the customer's items
    items_cost = get_cost()

    #Ask user how much money was given
    money_gave = eval(input("How much money did you give? "))

    #Compute the change
    change_back = money_gave - items_cost

    #Get rid of the decimal
    change_back = change_back * 100

    #Declarations of Coins
    quarter = 25
    dime = 10
    nickel = 5
    penny = 1

    #Print out details for display
    print('Your total cost of items: '+str(items_cost))

    print('You gave: '+str(money_gave))

    print('You should receive the following change:')

    #Find the amount of Quarters we need
    amount_of_quarters = int(change_back // quarter)

    #Show amount of Quarters
    print('Quarters: ' +str(amount_of_quarters))

    #Update change_back 
    change_back = change_back - (amount_of_quarters * quarter)

    #Find the amount of Dimes to return
    amount_of_dimes = int(change_back // dime)

    #Show amount of Dimes
    print('Dimes: ' +str(amount_of_dimes))

    #Update change_back 
    change_back = change_back - (amount_of_dimes * dime)

    #Find the amount of Nickels to return
    amount_of_nickels = int(change_back // nickel)

    #Show amount of Nickels
    print('Nickels: ' +str(amount_of_nickels))

    #Update change_back 
    change_back = change_back - (amount_of_nickels * nickel)

    #Find the amount of pennies to return
    amount_of_pennies = int(change_back // penny)

    #Show amount of Pennies
    print('Pennies: ' +str(amount_of_pennies))

    #Update change_back 
    change_back = change_back - (amount_of_pennies * penny)

    #Total coins
    total_coins = amount_of_quarters + amount_of_dimes + amount_of_nickels + amount_of_pennies

    print('Total number of coins: ' +str(total_coins))
    
    #Ask User if they want to calculate again
    print('Would you like to make another calculation? [y/n] ')
    choice = input()

    #if statement, if User choices other than 'y' then stop loop and end program. 
    if choice != 'y':
        calculate = False
