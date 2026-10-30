import json

# read the json file

input_file = "data/config.json"

try:
    with open(input_file, 'r') as file:
        data = json.load(file)
        print(f"Welcome to {data['app_name']}")
        print("Current Settings")
        print(f"1- Application name: {data['app_name']}")
        print(f"2- Currency: {data['currency']}")
        print(f"3- Stock Threshold: {data['low_stock_threshold']}")
        print(f"4- Show Summary: {data['show_summary']}")
except FileNotFoundError:
    print (f"Error: '{input_file}' was not found.")
