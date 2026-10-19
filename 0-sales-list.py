sales = [
    {"item": "Book", "price": 12.5},
    {"item": "Pen", "price": 2.0},
    {"item": "Notebook", "price": 5.5},
    {"item": "Pencil", "price": 1.0},
] #list of dictionaries

#loop through the list and print the item and price
total_price = 0


for sale in sales:
    #calculate the total price of the sales
    total_price += sale['price']

    #print the item and price in a formatted way
    if sale['price'].is_integer():
        print(f"{sale['item']}: ${int(sale['price'])}")
    else:
        print(f"{sale['item']}: ${sale['price']:.2f}")

    
print(f"Total price: ${total_price:.2f}")