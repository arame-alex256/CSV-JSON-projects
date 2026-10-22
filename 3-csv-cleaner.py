import csv
from pathlib import Path

#open the csv file
def filter_all_products(file_dir):
    correct_products = []
    incorrect_products = []
    correct_fieldnames = ['name', 'price', 'quantity']
    incorrect_fieldnames = ['name', 'error']

    try:
    # open the file, read mode wiht the products name
        with open(file_dir, mode="r", newline="", encoding='utf-8') as products_file:
            all_products = csv.DictReader(products_file,restval="N/A", restkey="additional")
            #Check if the price and quantity are in the correct format

            # Track accepted names to detect duplicates
            existing_names = set()

            for product in all_products:
                name = (product.get("name") or "").strip()
                price_text = (product.get("price") or "").strip()
                quantity_text = (product.get("quantity") or "").strip()
                
                # Reject rows with extra columns
                if product.get("additional"):
                    incorrect_products.append({
                        "name": name or "Unknown",
                        "error": "More than 3 values inserted"
                    })
                    continue
                
                #missing name
                if not name:
                    incorrect_products.append({'name':'Unknown', 'error': 'Missing product name'})
                    continue

                try: 
                    price = float(price_text)
                    quantity = int(quantity_text)

                    #Negative price or quantity
                    if price < 0 or quantity < 0:
                        incorrect_products.append({'name': name, 'error': 'negative price or quantity'})
                        continue
                    
                    #Duplicate product name
                    if name in existing_names:
                        incorrect_products.append({'name': name, 'error': 'duplicate product name'})
                        continue

                #other errors   
                except ValueError as error:
                    incorrect_products.append({'name': name, 'error': error})
                    continue
                
                #Save products with correct format
                correct_products.append(
                    {'name':name, 'price': price,'quantity': quantity})
                existing_names.add(name)

    except FileNotFoundError:
        print (f"Error: '{file_dir}' was not found.")
        return None

    # Create the output directory if necessary
    output_dir = Path("produced_files")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Write the rejected rows
    with open(f'{output_dir}/rejected_rows.csv', mode='w', newline="", encoding='utf-8') as rejected_file:
        writer = csv.DictWriter(rejected_file, fieldnames=incorrect_fieldnames)
        
        #Write Header
        writer.writeheader()
        writer.writerows(incorrect_products)

    with open(f'{output_dir}/clean_products.csv', mode='w', newline="", encoding='utf-8') as clean_file:
        writer = csv.DictWriter(clean_file, fieldnames=correct_fieldnames)
        
        #Write Header
        writer.writeheader()
        writer.writerows(correct_products)

    #Return the files
    print(f"Cleaning complete!")
    print(f"Accepted products: {len(correct_products)}")
    print(f"Rejected rows: {len(incorrect_products)}")
    print(f"Reports saved in '{output_dir}/'.")

    return correct_products, incorrect_products


filter_all_products("data/wrong-formatted-products.csv")