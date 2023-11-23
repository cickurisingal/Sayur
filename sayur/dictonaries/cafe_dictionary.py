
            
import re   

#initializing menu stock and sales details lists
menu = {      #contains menu available in the cafe
    "vadai" : {"price" : "10", "Stock" : "50","Sales" : "0","Profit": "4"},
    "tea" : {"price" : "12", "Stock" : "50","Sales" : "0","Profit": "5"},
    "coffee" : {"price" : "15", "Stock" : "50","Sales" : "0","Profit": "6"}
}
customer_input = []                     #empty list to append customer order

#getting order from customer and checking for the availability each time and updating the sales details each time
for customers in range(2) :
    order = input("enter your order: ")                             #getting order as input
    quantity = re.findall(r'\b(\d{2}|\d+)\b' , order)               #seperating quantity of food using RegEx
    items = re.findall(r'\b(vadai|tea|coffee)\b',order.lower())     #seperating the food item ordered using RegEx

    #for loop to check for stock for the foods in items list 
    for index,item in enumerate(items) :
        orderedQuantity = int(quantity[index])
        availableQuantity = int(menu[item]['Stock'])
        soldQuantity = int(menu[item]['Sales'])
        
        if orderedQuantity <= availableQuantity :
            availableQuantity -= orderedQuantity
            soldQuantity += orderedQuantity
            menu[item]['Stock'] = availableQuantity
            menu[item]['Sales'] = soldQuantity

        else :
            print(f"only {availableQuantity} {item} is available :" ) 
        
totalProfit = 0
totalSales = 0

for key in menu :
    #totalSold = int(menu[key]["Sales"])
    profit = int(menu[key]["Profit"]) * int(menu[key]["Sales"])
    moneyEarned = int(menu[key]["Sales"]) *int(menu[key]["price"])
    print(f"Total sales for {key} is {moneyEarned}")
    print(f"Total profit for {key} is {profit}")
    totalProfit += profit
    totalSales += moneyEarned

print(f"Total Sales  = {totalSales}")
print(f"Total profit = {totalProfit}")
     
