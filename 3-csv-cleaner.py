import csv

#open the csv file
def load_products(file_dir):
    correct_products = []
    try:
    # open the file, read mode wiht the products name
        with open(file_dir, mode="r", newline="", encoding='utf-8') as products_file:
            all_products = csv.DictReader(products_file, restval="N/A", restkey="additional")
            #Check if the price and quantity are in the correct format
            for product in all_products:
                name = (product.get("name") or "").strip()
                price_text = (product.get("price") or "").strip()
                quantity_text = (product.get("quantity") or "").strip()
                try:
                    if product['additional']:
                        print(f"product '{name or 'Unknown'}' has more than 3 values inserted")
                        continue
                except:
                    pass
                try: 
                    price = float(price_text)
                    quantity = int(quantity_text)
                    #missing name
                    if not name:
                        raise ValueError("missing product name")

                    #Negative price or quantity
                    if price < 0 or quantity < 0 or price == -0 or quantity == -0:
                        raise ValueError("negative price or quantity")

                #other errors   
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
    print(correct_products)
    return correct_products

all_products = load_products("data/wrong-formatted-products.csv")