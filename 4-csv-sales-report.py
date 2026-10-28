import csv
from datetime import datetime, date
from collections import defaultdict
import math
from pathlib import Path

# Correct Products
correct_products = []
correct_fieldnames = ['date', 'name', 'quantity', 'price']

# Rejected Products
incorrect_products = []
incorrect_fieldnames = ['name', 'date', 'error']

# Output dir and Input file
input_file = "data/daily-list.csv"
output_dir = Path("produced_files")
report_file = output_dir / "sales_report.txt"
rejected_rows = output_dir / "daily_rejected_rows.csv"

def load_products(file_dir):
    try:
    # open the file, read mode with the products name
        with open(file_dir, mode="r", newline="", encoding='utf-8') as products_file:
            all_products = csv.DictReader(products_file)

            # Empty CSV File
            if not all_products.fieldnames:
                raise ValueError("The input CSV is empty or has no header row.")
        
            for product in all_products:
                date_text = (product.get("date") or "").strip()
                name = (product.get("name") or "").strip()
                price_text = (product.get("price") or "").strip()
                quantity_text = (product.get("quantity") or "").strip()
                errors = []
                
                # No Name Error
                if not name:
                    errors.append("Missing product name")
                
                # No or Invalid Date Error
                if not date_text:
                    errors.append("Missing product date")
                else:
                    try:
                        input_date = datetime.strptime(date_text, "%Y-%m-%d")
                    except ValueError:
                        errors.append("Invalid date (expected YYYY-MM-DD)")
                
                # No or Invalid Price
                if not price_text:
                    errors.append("Missing price")
                else:
                    try:
                        price = float(price_text)
                        if not math.isfinite(price):
                            errors.append("Price must be a finite number")
                        elif price < 0:
                            errors.append("Price cannot be negative")
                    except ValueError:
                        errors.append("Invalid price (expected a number)")

                # No or Invalid Quantity
                if not quantity_text:
                    errors.append("Missing quantity")
                else:
                    try:
                        quantity = int(quantity_text)
                        if quantity < 0:
                            errors.append("Quantity cannot be negative")
                    except ValueError:
                        errors.append("Invalid quantity (expected a whole number)")
                
                # Save Errors in incorrect_products
                if errors:
                    incorrect_products.append(
                        {
                            "name": name or "Unknown",
                            "date": date_text or "Unknown",
                            "error": "; ".join(errors),
                        }
                    )
                    continue
                
                #Save products with correct format
                correct_products.append(
                    {'date': input_date.isoformat(), 'name':name, 'price': price,'quantity': quantity})
    
    # No File
    except FileNotFoundError:
        print (f"Error: '{file_dir}' was not found.")
        return None

    # Create the output directory if necessary
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Write the rejected rows
    write_rejected_rows(incorrect_products)
    print(f"Rejected rows saved to: {rejected_rows}")

    #Write correct sales report
    with open(f'{report_file}', mode='w', encoding='utf-8') as sales_report:
        sales_report.write("="*32)
        sales_report.write("\n" + " "*10 + "SALES REPORT")
        sales_report.write("\n" + "="*32)
    print(f"Report file created in {output_dir}")
    #Return the products
    return correct_products

def write_rejected_rows(rejected_products):
    # Write the rejected products rows
    with open(rejected_rows, mode="w", newline="", encoding="utf-8") as rejected_file:
        writer = csv.DictWriter(rejected_file, fieldnames=incorrect_fieldnames)
        writer.writeheader()
        writer.writerows(rejected_products)

# The total Revenue, Sales Records, Units Sold
def total_performance(products):
    with open(output_dir, mode='a', encoding='utf-8') as sales_report:
        if not products:
            sales_report.write("\nNo valid products to compare.")
            return
        # Reported data using sum to callculate the total revenue and unit solds
        sales_report.write("\n\nOVERALL PERFORMANCE")
        sales_report.write("\n" + "-"*32)
        sales_report.write(f"\nTotal Sales Records: {len(products)}")
        sales_report.write(f"\nTotal Units Sold: {sum(x['quantity'] for x in products)}")
        sales_report.write(f"\nTotal Revenue: ${sum(y['quantity'] * y['price'] for y in products):.2f}")
    print(f"total performance was saved in {output_dir}")

# Individual Product performance
def product_performance(products):
    with open(output_dir, mode='a', encoding='utf-8') as sales_report:
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
    print(f"individual product performances were saved in {output_dir}")
    return all_units

def top_performance(products):
    with open({output_dir}, mode='a', encoding='utf-8') as sales_report:
        if not products:
            sales_report.write("\n\nTOP PERFORMERS\nNo products available.")
            return
        # Calculate the max unit solds and revenue
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
    print(f"top performances were saved in {output_dir}")
    
def daily_revenue(products):
    with open(output_dir, mode='a', encoding='utf-8') as sales_report:
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
    print(f"daily revenue was saved in {output_dir}")
    print(f"You can check the full result in {output_dir}")


all_products = load_products(input_file)
if all_products != None:
    total_performance(all_products)
    all_units = product_performance(all_products)
    top_performance(all_units)
    daily_revenue(all_products)