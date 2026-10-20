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
                    correct_products.append(product)
                except ValueError:
                    print(f"{product['name']} has incorrect data!")
        # Returns the products
        return correct_products
    except FileNotFoundError:
        print ("Error: products.csv was not found.")
        return None

#The total products number
def total_product_count(products):
    print(f"Total number of products: {len(products)}")

#The total value
def calculate_inventory_value(products):
    total_value = 0
    # for product in products:
    #     #add the total value
    #     total_value += price * quantity
    print(f"Total inventory value: ${total_value}")

all_products = load_products("data/products.csv")
if all_products != None:
    total_product_count(all_products)
    calculate_inventory_value(all_products)