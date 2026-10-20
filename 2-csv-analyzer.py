import csv

#open the csv file
def load_products(file_dir):
    try:
    # open the file, read mode wiht the products name
        with open(file_dir, mode="r", newline="", encoding='utf-8') as products_file:
            all_products = csv.DictReader(products_file, restval="N/A")
            correct_products = []
            #Check if the price and quantity are in the correct format
            for product in all_products:
                try: 
                    float(product['price']) and int(product['quantity'])
                    #Save products with correct format
                    correct_products.append(
                        {'name': product['name'], 'price': float(product['price']),'quantity': int(product['quantity'])})
                except ValueError:
                    print(f"{product['name']} has incorrect data!")
        # Returns the products
        return correct_products
    except FileNotFoundError:
        print ("Error: products.csv was not found.")
        return None

#The total products number
def total_product_count(products):
    print(f"\nTotal number of products: {len(products)}")

#The total value
def calculate_inventory_value(products):
    total_value = 0
    for product in products:
        #add the total value
        total_value += product['price'] * product['quantity']
    print(f"\nTotal inventory value: ${total_value:.2f}")

#The Most Expensive Product
def most_expensive_product(products):
    #calculate the max price
    highest_price = max(products, key=lambda x: x["price"])['price']
    #line breaker
    print("\n")
    for product in products:
        if product['price'] >= highest_price:
            print(f"The most expensive product is {product['name']} with the price of ${product['price']:.2f}")


#The Average price of all products
def average_product_price(products):
    average_price = 0
    for product in products:
        average_price += product['price']
    average_price = average_price / len(products)
    print(f"\nThe average product price is ${average_price:.2f}")

#run the functions
all_products = load_products("data/products.csv")
if all_products != None:
    total_product_count(all_products)
    calculate_inventory_value(all_products)
    average_product_price(all_products)
    most_expensive_product(all_products)