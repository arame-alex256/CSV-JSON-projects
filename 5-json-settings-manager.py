import json
from pathlib import Path

# read the json file

input_dir = Path("data")
input_file = input_dir / "config.json"

DEFAULT_SETTINGS = {
    "app_name": "My App",
    "currency": "USD",
    "low_stock_threshold": 10,
    "show_summary": True
}

current_settings = {}

has_error = False

def update():
    with open(input_file, 'w') as file:
        json.dump(current_settings, file, indent=4)

try:
    with open(input_file, 'r') as file:
        # Load the JSON File as a dict
        try:
            file_data = json.load(file)
        except ValueError:
            file_data = DEFAULT_SETTINGS
            has_error = True

        
        # Get the individual settings
        if type(file_data.get("app_name")) != str:
            app_name = (str(file_data.get("app_name")) or "").strip()
            has_error = True
        else:
            app_name = (file_data.get("app_name") or "").strip()
        
        if type(file_data.get("currency")) != str:
            currency = (str(file_data.get("currency")) or "").strip()
            has_error = True
        else:
            currency = (file_data.get("currency") or "").strip()
       
        low_stock_threshold = file_data.get("low_stock_threshold")
        show_summary = file_data.get("show_summary")

        # Check if the name is empty
        if not app_name:
            app_name = DEFAULT_SETTINGS["app_name"]
            has_error = True

        # Check if the low stock threshold is empty or not number or negative
        try:
            low_stock_threshold = int(low_stock_threshold)
            if low_stock_threshold < 0:
                low_stock_threshold = DEFAULT_SETTINGS["low_stock_threshold"]
                has_error = True

        except ValueError:
            low_stock_threshold = DEFAULT_SETTINGS["low_stock_threshold"]
            has_error = True

        # Check if the currency is empty
        if not currency:
            has_error = True
            currency = DEFAULT_SETTINGS["currency"]
        else:
            if type(currency) != str:
                currency = str(currency)
                has_error = True

        # Check if the show summary is empty or not bool
        try:
            show_summary = bool(show_summary)
        except ValueError:
            has_error = True
            show_summary = DEFAULT_SETTINGS["show_summary"]

        # Save the current data in the dict
        current_settings = {
            "app_name": app_name,
            "currency": currency,
            "low_stock_threshold": low_stock_threshold,
            "show_summary": show_summary
        }
    
    # Update the file with new settings
    if has_error:
        with open(input_file, 'w') as file:
            json.dump(current_settings, file, indent=4)

    while True:
        # Print the settings
        print(f"\nWelcome to {current_settings['app_name']}")
        print("Current Settings")
        print(f"\n1- Application name: {current_settings['app_name']}")
        print(f"2- Currency: {current_settings['currency']}")
        print(f"3- low Stock Threshold: {current_settings['low_stock_threshold']}")
        print(f"4- Show Summary: {current_settings['show_summary']}")
        print("5- Quit")

        user_input = input("\nEnter choice number: ")
        # App Name settings inputs
        if user_input == '1':
            while True:
                app_input = input("\nEnter an app name: ")
                if not app_input or not app_input.strip():
                    print("Please enter a valid app name")
                else:
                    current_settings["app_name"] = str(app_input).strip()
                    update()
                    break

        # Currency settings inputs
        elif user_input == '2':
            while True:
                cur_input = input("\nEnter a currency: ")
                if not cur_input or not cur_input.strip():
                    print("Please enter a valid currency")
                else:
                    current_settings["currency"] = str(cur_input).strip()
                    update()
                    break
                
        # Low stock threshold settings inputs
        elif user_input == '3':
            while True:
                lst_input = input("\nEnter the low stock threshold: ")
                if not lst_input:
                    print("Please enter a valid number low stock threshold")
                else:
                    try:
                        lst_input = int(lst_input)
                        if int(lst_input) < 0:
                            print("Please enter a positive number for low stock threshold")
                        else:
                            current_settings["low_stock_threshold"] = int(lst_input)
                            update()
                            break
                    except ValueError:
                        print("Please enter a whole number low stock threshold")

        # Show summary settings input
        elif user_input == '4':
            while True:
                yesno = input("\nEnter yes/no for showing summary: ")
                if not yesno:
                    print("Please enter an input")
                else:
                    if yesno.strip().lower() == "yes":
                        current_settings["show_summary"] = True
                        update()
                        break
                    elif yesno.strip().lower() == "no":
                        current_settings["show_summary"] = False
                        update()
                        break
                    else:
                        print("Please enter either yes or no")

        # Quie
        elif user_input == '5':
            print("Good bye!")
            break
        else:
            print("Please enter a number between 1 and 5!")


except FileNotFoundError:
    with open(input_file, 'w') as file:
        json.dump(DEFAULT_SETTINGS, file, indent=4)
        print(f"Created default settings in {input_file}")
