import re

menu_card = ["tea", "vadai", "coffee", "biscuit"]
price = [20, 5, 20, 10]
item_quantity = [100, 150, 100, 50]
remaining_quantity = []


order = input("What you need:")
# Use regular expression to extract numbers
numbers = re.findall(r'\d+.\d+|\d+', order)
items = re.findall(r'(coffee?s|tea|vadai|biscuit)', order)
print(numbers)
print(items)   

for i in range(items[i]):
    index=index.menucard(item[i])
    print(index)