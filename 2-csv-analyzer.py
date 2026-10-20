import csv

#open the csv file
def load_products(file_dir):
    try:
    # open the file, read mode wiht the products name
        with open(file_dir, mode="r", newline="", encoding='utf-8') as products_file:
            products = list(csv.DictReader(products_file, restval="N/A"))
        # Returns the products
        return products
    except FileNotFoundError:
        print ("Error: products.csv was not found.")
        return None

def total_product_count(products):
    print(f"Total number of products: {len(products)}")

def calculate_inventory_value(products):
    total_value = 0
    for product in products:
        try: 
            price = float(product['price'])
            quantity = int(product['quantity']) 
        except ValueError: continue
        total_value += price * quantity
    print(f"Total inventory value: ${total_value}")

all_products = load_products("data/products.csv")
if all_products != None:
    total_product_count(all_products)
    calculate_inventory_value(all_products)