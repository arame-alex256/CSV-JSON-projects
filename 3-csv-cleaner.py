import csv

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
            for product in all_products:
                name = (product.get("name") or "").strip()
                price_text = (product.get("price") or "").strip()
                quantity_text = (product.get("quantity") or "").strip()
                try:
                    if product['additional']:
                        incorrect_products.append({'name': name or 'Unknown', 'error': 'more than 3 values inserted'})
                        continue
                except:
                    pass
                try: 
                    price = float(price_text)
                    quantity = int(quantity_text)
                    #missing name
                    if not name:
                        incorrect_products.append({'name': name or 'Unknown', 'error': 'missing product name'})
                        continue

                    #Negative price or quantity
                    if price < 0 or quantity < 0 or price == -0 or quantity == -0:
                        incorrect_products.append({'name': name or 'Unknown', 'error': 'negative price or quantity'})
                        continue
                    
                    if name in [exsiting_data["name"] for exsiting_data in correct_products]:
                        incorrect_products.append({'name': name or 'Unknown', 'error': 'duplicate product name'})
                        continue

                #other errors   
                except ValueError as error:
                    incorrect_products.append({'name': name or 'Unknown', 'error': error})
                    continue
                
                #Save products with correct format
                correct_products.append(
                    {'name':name, 'price': price,'quantity': quantity})

    except FileNotFoundError:
        print (f"Error: '{file_dir}' was not found.")
        return None
    
    # Write the rejected rows
    with open('produced_files/rejected_rows.csv', mode='w', newline="", encoding='utf-8') as rejected_file:
        writer = csv.DictWriter(rejected_file, fieldnames=incorrect_fieldnames)
        
        #Write Header
        writer.writeheader()
        writer.writerows(incorrect_products)

    with open('produced_files/clean_products.csv', mode='w', newline="", encoding='utf-8') as clean_file:
        writer = csv.DictWriter(clean_file, fieldnames=correct_fieldnames)
        
        #Write Header
        writer.writeheader()
        writer.writerows(correct_products)

    #Return the files
    print("You can check the full report in produced_files/ dictionary")


all_products = filter_all_products("data/wrong-formatted-products.csv")