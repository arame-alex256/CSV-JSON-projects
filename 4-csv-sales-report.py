import csv
from datetime import datetime
from collections import defaultdict

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
    if not products:
        print("SALES REPORT\nNo valid products to compare.")
        return
    # Reported data using sum to callculate the total revenue and unit solds
    print("SALES REPORT")
    print(f"\nTotal Sales Records: {len(products)}")
    print(f"Total Units Sold: {sum(x['quantity'] for x in products)}")
    print(f"Total Revenue: ${sum(y['quantity'] * y['price'] for y in products):.2f}")

#Individual Product performance
def product_performance(products):
    if not products:
        print("\nPRODUCT PERFORMANCE\nNo valid products to show.")
        return
    # Group items by name
    single_units = defaultdict(lambda: {'name': '', 'price': 0.0, 'quantity': 0, 'total_revenue': 0.0})
    for product in products:
        product_name = product['name']
        # Inserting the first values if there isn't
        if single_units[product_name]['name'] == '':
            single_units[product_name]['name'] = product_name
            single_units[product_name]['price'] = product['price']
        # Calculate total quantity sold and revenue
        single_units[product_name]['quantity'] += product['quantity']
        single_units[product_name]['total_revenue'] += product['price'] * product['quantity']

    all_units = list(single_units.values())
    
    print("\nPRODUCT PERFORMANCE")
    # Print all the products performance
    for unit in all_units:
        print(f"\n{unit['name']}")
        print(f"  Unit Sold: {unit['quantity']}")
        print(f"  Total Revenue: ${unit['total_revenue']:.2f}")
    return all_units

def top_performance(products):
    if not products:
        print("\nTOP PERFORMERS\nNo products available.")
        return
    #calculate the max unit solds and revenue
    most_sold = max(products, key=lambda x: x['quantity'])['quantity']
    highest_revenue = max(products, key=lambda x: x['total_revenue'])['total_revenue']

    # Get the top sold products
    top_sold_names = ", ".join([p["name"] for p in products if p["quantity"] == most_sold])
    # Get the top revenue products
    top_revenue_names = ", ".join([p["name"] for p in products if p["total_revenue"] == highest_revenue])

    # Print the outputs
    print("\nTOP PERFORMERS")
    print(f"  Most Units Sold: {top_sold_names} ({most_sold} units)")
    print(f"  Highest Revenue: {top_revenue_names} (${highest_revenue:,.2f})")
    


all_products = load_products("data/daily-list.csv")
if all_products != None:
    total_performance(all_products)
    all_units = product_performance(all_products)
    top_performance(all_units)