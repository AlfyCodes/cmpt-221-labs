
''' 
get_info() Function 
Will ask and grab the Total Cost of the customer's Items
and how much Money was given then return those values in items_cost and money_gave
'''
def get_info():

    #Find the total cost of the customer's items
    items_cost = eval(input("What is the total cost of your items? "))

    #Ask user how much money was given
    money_gave = eval(input("How much money did you give? "))

    #Return values
    return items_cost, money_gave
'''
get_change Function
Takes in two Parameters then computes the change that 
the user should get back
'''    
def get_change(items_cost, money_gave):
    #Compute the change
    change = money_gave - items_cost

    #Gets rid of the decimal by mulitplaying by 100 so we can just deal with whole numbers
    change = change * 100
    return change
'''
get_coins Function
Takes in change as a parameter then computes
how many of each coin the user will get back 
adn the total of coins.
'''
def get_coins(change):
    '''
    get_new_change() Inner Function
    To update the change so we can properly find
    how much of each coin the user will get back
    '''
    def get_new_change(change,coin_amount,coin):
        change = change - (coin_amount * coin)
        return change
    
    #Declarations of Coins
    quarter = 25
    dime = 10
    nickel = 5
    penny = 1

    #Find the amount of Quarters we need
    amount_of_quarters = int(change // quarter)

    #Update change
    change = get_new_change(change,amount_of_quarters,quarter)

    #Find the amount of Dimes to return
    amount_of_dimes = int(change // dime)

    #Update change
    change = get_new_change(change,amount_of_dimes,dime)

    #Find the amount of Nickels to return
    amount_of_nickels = int(change // nickel)

    #Update change
    change = get_new_change(change,amount_of_nickels,nickel)

    #Find the amount of pennies to return
    amount_of_pennies = int(change // penny)

    #Update change
    change = get_new_change(change,amount_of_pennies,penny)

    #The sum of coins from each type of coin
    total_coins = amount_of_quarters + amount_of_dimes + amount_of_nickels + amount_of_pennies

    return amount_of_quarters,amount_of_dimes,amount_of_nickels,amount_of_pennies,total_coins

def display_info(items_cost,money_gave,change,amount_of_quarters,amount_of_dimes,amount_of_nickels,amount_of_pennies,total_coins):
 #Print out details for display
    print('Your total cost of items: '+str(items_cost))

    print('You gave: '+str(money_gave))

    print('You should receive the following change:')

    #Show amount of Quarters
    print('Quarters: ' +str(amount_of_quarters))
    
    #Show amount of Dimes
    print('Dimes: ' +str(amount_of_dimes))

    #Show amount of Nickels
    print('Nickels: ' +str(amount_of_nickels))

    #Show amount of Pennies
    print('Pennies: ' +str(amount_of_pennies))

    print('Total number of coins: ' +str(total_coins))
#Start Loop

'''
Main part of the program that will call the functions
'''

#Boolean type for loop
calculate = True

while calculate == True:

    items_cost, money_gave = get_info()

    change = get_change(items_cost, money_gave)

    amount_of_quarters,amount_of_dimes,amount_of_nickels,amount_of_pennies,total_coins = get_coins(change)

    display_info(items_cost,money_gave,change,amount_of_quarters,amount_of_dimes,amount_of_nickels,amount_of_pennies,total_coins)
    
    #Ask User if they want to calculate again
    print('Would you like to make another calculation? [y/n] ')
    choice = input()

    #if statement, if User choices other than 'y' then stop loop and end program. 
    if choice != 'y':
        calculate = False
