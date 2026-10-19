import csv

try:
    # open the file, read mode wiht the products name
    with open("data/products.csv", mode="r", newline="", encoding='utf-8') as products:
            reader = csv.DictReader(products, fieldnames=None, restval="N/A")
            # Reads the file and prints each row's attribute
            for row in reader:
                try: 
                    price = float(row['price']) 
                except ValueError: 
                    price = 0
                print(f"{row['name']} - ${price:.2f} - {row['quantity']}")
except FileNotFoundError:
    print("Error: products.csv was not found.")