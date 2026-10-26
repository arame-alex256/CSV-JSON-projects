import csv
from datetime import datetime
from math import prod

def load_products(file_dir):
    correct_products = []
    try:
    # open the file, read mode wiht the products name
        with open(file_dir, mode="r", newline="", encoding='utf-8') as products_file:
            all_products = csv.DictReader(products_file, restval="N/A")
            #Check if the price and quantity are in the correct format
            for product in all_products:
                date_text = (product.get("date") or "").strip()
                name = (product.get("name") or "").strip()
                price_text = (product.get("price") or "").strip()
                quantity_text = (product.get("quantity") or "").strip()
                try: 
                    price = float(price_text)
                    quantity = int(quantity_text)
                    date = datetime.strptime(date_text, "%Y-%m-%d")
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
                    {'date': date, 'name':name, 'price': price,'quantity': quantity})

    except FileNotFoundError:
        print (f"Error: '{file_dir}' was not found.")
        return None

    #Return the products
    return correct_products

#The total Revenue, Sales Records, Units Sold
def total_performance(products):
    # Reported data using sum to callculate the total revenue and unit solds
    print(f"\nTotal Sales Records: {len(products)}")
    print(f"Total Units Sold: {sum(x["quantity"] for x in products)}")
    print(f"Total Revenue: ${sum(y["quantity"] * y["price"] for y in products):.2f}")


all_products = load_products("data/daily-list.csv")
if all_products != None:
    total_performance(all_products)