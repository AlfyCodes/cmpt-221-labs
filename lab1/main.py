#Find the total cost of the customer's items
items_cost = eval(input("What is the total cost of your items?"))

#Ask user how much money was given
money_gave = eval(input("How much money did you give?"))

#Compute the change
change_back = money_gave - items_cost

#Get rid of the decimal
change_back = change_back * 100

#Declarations of Coins
quarter = 25
dime = 10
nickel = 5
penny = 1

#Find the amount of Quarters we need
amount_of_quarters = int(change_back // quarter)

print('You should receive')

#Test Quarters
print('Quarters: ' +str(amount_of_quarters))

#Update change_back 
change_back = change_back - (amount_of_quarters * quarter)

#Find the amount of Dimes to return
amount_of_dimes = int(change_back // dime)

#Test Dimes
print('Dimes: ' +str(amount_of_dimes))

#Update change_back 
change_back = change_back - (amount_of_dimes * dime)

#Find the amount of Nickels to return
amount_of_nickels = int(change_back // nickel)

#Test Nickels
print('Nickels: ' +str(amount_of_nickels))

#Update change_back 
change_back = change_back - (amount_of_nickels * nickel)

#Find the amount of pennies to return
amount_of_pennies = int(change_back // penny)

#Test Pennies
print('Pennies: ' +str(amount_of_pennies))

#Update change_back 
change_back = change_back - (amount_of_pennies * penny)