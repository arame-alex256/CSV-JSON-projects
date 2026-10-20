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
    print(f"Total number of products:{len(products)}")

all_products = load_products("data/products.csv")
if all_products != None:
    total_product_count(all_products)