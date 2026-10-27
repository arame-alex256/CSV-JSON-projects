import csv
from datetime import datetime, date
from collections import defaultdict
from pathlib import Path

def load_products(file_dir):
    correct_products = []
    
    incorrect_products = []
    incorrect_fieldnames = ['name', 'date', 'error']
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
                    datetime.strptime(date_text, "%Y-%m-%d")
                    #Lists of Different Errors
                    if not name:
                        incorrect_products.append({'date': date_text or 'Unkown','name':'Unknown', 'error': 'Missing product name'})
                        continue
                    
                    if not date_text:
                        incorrect_products.append({'date': date_text or 'Unkown', 'name': name, 'error': 'Missing product date'})
                        continue

                    if price < 0 or quantity < 0:
                        incorrect_products.append({'date': date_text, 'name': name, 'error': 'negative price or quantity'})
                        continue
                    
                except ValueError as error:
                    incorrect_products.append({'date': date_text or 'unkown', 'name': name or 'unkown', 'error': error})
                    continue
                
                #Save products with correct format
                correct_products.append(
                    {'date': date_text, 'name':name, 'price': price,'quantity': quantity})

    except FileNotFoundError:
        print (f"Error: '{file_dir}' was not found.")
        return None

    # Create the output directory if necessary
    output_dir = Path("produced_files")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Write the rejected rows
    with open(f'{output_dir}/daily_rejected_rows.csv', mode='w', newline="", encoding='utf-8') as rejected_file:
        writer = csv.DictWriter(rejected_file, fieldnames=incorrect_fieldnames)
        
        #Write Header
        writer.writeheader()
        writer.writerows(incorrect_products)

    #Write correct sales report
    with open(f'{output_dir}/sales_report.txt', mode='w', encoding='utf-8') as sales_report:
        sales_report.write("="*32)
        sales_report.write("\n" + " "*10 + "SALES REPORT")
        sales_report.write("\n" + "="*32)
    print(f"Report file created in {output_dir}")
    #Return the products
    return correct_products

#The total Revenue, Sales Records, Units Sold
def total_performance(products):
    with open('produced_files/sales_report.txt', mode='a', encoding='utf-8') as sales_report:
        if not products:
            sales_report.write("\nNo valid products to compare.")
            return
        # Reported data using sum to callculate the total revenue and unit solds
        sales_report.write("\n\nOVERALL PERFORMANCE")
        sales_report.write("\n" + "-"*32)
        sales_report.write(f"\nTotal Sales Records: {len(products)}")
        sales_report.write(f"\nTotal Units Sold: {sum(x['quantity'] for x in products)}")
        sales_report.write(f"\nTotal Revenue: ${sum(y['quantity'] * y['price'] for y in products):.2f}")
    print("total performance was saved in sales_report.txt")

#Individual Product performance
def product_performance(products):
    with open('produced_files/sales_report.txt', mode='a', encoding='utf-8') as sales_report:
        if not products:
            sales_report.write("\n\nPRODUCT PERFORMANCE\nNo valid products to show.")
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
        
        sales_report.write("\n\nPRODUCT PERFORMANCE")
        sales_report.write("\n" + "-"*32)
        # Print all the products performance
        for unit in all_units:
            sales_report.write(f"\n\n{unit['name']}")
            sales_report.write(f"\n  Unit Sold: {unit['quantity']}")
            sales_report.write(f"\n  Total Revenue: ${unit['total_revenue']:.2f}")
    print("individual product performances were saved in sales_report.txt")
    return all_units

def top_performance(products):
    with open('produced_files/sales_report.txt', mode='a', encoding='utf-8') as sales_report:
        if not products:
            sales_report.write("\n\nTOP PERFORMERS\nNo products available.")
            return
        #calculate the max unit solds and revenue
        most_sold = max(products, key=lambda x: x['quantity'])['quantity']
        highest_revenue = max(products, key=lambda x: x['total_revenue'])['total_revenue']

        # Get the top sold products
        top_sold_names = ", ".join([p["name"] for p in products if p["quantity"] == most_sold])
        # Get the top revenue products
        top_revenue_names = ", ".join([p["name"] for p in products if p["total_revenue"] == highest_revenue])

        # Print the outputs
        sales_report.write("\n\nTOP PERFORMERS")
        sales_report.write("\n" + "-"*32)
        sales_report.write(f"\n  Most Units Sold: {top_sold_names} ({most_sold} units)")
        sales_report.write(f"\n  Highest Revenue: {top_revenue_names} (${highest_revenue:,.2f})")
    print("top performances were saved in sales_report.txt")
    
def daily_revenue(products):
    with open('produced_files/sales_report.txt', mode='a', encoding='utf-8') as sales_report:
        if not products:
            sales_report.write("\n\nDAILY REVENUE\nNo valid products to show.")
            return
        # Group items by name
        single_day = defaultdict(lambda: {'date': '', 'total_revenue': 0.0})
        for product in products:
            list_day = product['date']
            # Inserting the first values if there isn't
            if single_day[list_day]['date'] == '':
                single_day[list_day]['date'] = list_day
            # Calculate total quantity sold and revenue
            single_day[list_day]['total_revenue'] += product['price'] * product['quantity']

        daily_performance = list(single_day.values())
        
        sales_report.write("\n\nDAILY REVENUE")
        sales_report.write("\n" + "-"*32)
        # Print all the daily performances
        for day in daily_performance:
            sales_report.write(f"\n{day['date']}: ${day['total_revenue']:.2f}")

        sales_report.write("\n\n" + "="*32)
        sales_report.write(f"\nReport generated successfully on {date.today().isoformat()}")
    print("daily revenue was saved in sales_report.txt")
    print("You can check the full result in sales_report.txt")


all_products = load_products("data/daily-list.csv")
if all_products != None:
    total_performance(all_products)
    all_units = product_performance(all_products)
    top_performance(all_units)
    daily_revenue(all_products)