#Find the total cost of the customer's items
items_cost = eval(input("What is the total cost of your items?"))

#Ask user how much money was given
money_gave = eval(input("How much money did you give?"))

#Compute the change
change_back = money_gave - items_cost

#Get rid of the decimal
chancge_back = change_back * 100

#Declarations of Coins
quarter = .25
dime = .10
nickel = .5
penny = .01

#Find the amount of Quarters we need
amount_of_quarters = int(change_back // quarter)



print('Quarters' +str(amount_of_quarters))