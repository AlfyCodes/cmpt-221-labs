#Find the total cost of the customer's items
items_cost = eval(input("What is the total cost of your items?"))

#Ask user how much money was given
money_gave = eval(input("How much money did you give?"))

#Compute the change
change_back = money_gave - items_cost

#Declarations of Coins
quarter = 25
dime = 10
nickel = 5
penny = 1