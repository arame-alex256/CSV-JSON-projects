import csv

#open the csv file
def load_products(file_dir):
    correct_products = []
    try:
    # open the file, read mode wiht the products name
        with open(file_dir, mode="r", newline="", encoding='utf-8') as products_file:
            all_products = csv.DictReader(products_file, restval="N/A")
            #Check if the price and quantity are in the correct format
            for product in all_products:
                name = (product.get("name") or "").strip()
                price_text = (product.get("price") or "").strip()
                quantity_text = (product.get("quantity") or "").strip()
                try: 
                    price = float(price_text)
                    quantity = int(quantity_text)
                    #Lists of Different Errors
                    if not name:
                        raise ValueError("missing product name")

                    if price < 0 or quantity < 0:
                        raise ValueError("negative price or quantity")
                    
                except ValueError as error:
                    print(f"product '{name or 'Unknown'}' has error: {error}")
                    continue
                
                #Save products with correct format
                correct_products.append(
                    {'name':name, 'price': price,'quantity': quantity})

    except FileNotFoundError:
        print (f"Error: '{file_dir}' was not found.")
        return None

    #Return the products
    return correct_products

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
    if not products:
        print("\nNo valid products to compare.")
        return
    #calculate the max price
    highest_price = max(products, key=lambda x: x["price"])['price']
    #line breaker
    print("\nThe most expensive product(s) is/are")
    for product in products:
        if product['price'] == highest_price:
            print(f"{product['name']} : ${highest_price:.2f}")


#The Average price of all products
def average_product_price(products):
    if not products:
        print("\nCannot calculate the average: no valid products.")
        return
    average_price = 0
    for product in products:
        average_price += product['price']
    average_price = average_price / len(products)
    print(f"\nThe average product price is ${average_price:.2f}")

#find products lower than a chosen threshold
def find_low_stock(products, threshold):
    print(f"\nProducts with quantity below {threshold}:")
    found_products = False

    for product in products:
        #find the products
        if product['quantity'] < threshold:
            print(f'{product['name']} - Current quantity: {product['quantity']}')
            found_products = True

    if not found_products:
        print("No products below the threshold.")

#run the functions
all_products = load_products("data/products.csv")
if all_products != None:
    total_product_count(all_products)
    calculate_inventory_value(all_products)
    average_product_price(all_products)
    most_expensive_product(all_products)
    find_low_stock(products=all_products, threshold=3)