import json
from pathlib import Path
import math

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

has_has_error = False

try:
    with open(input_file, 'r') as file:
        # Load the JSON File as a dict
        data = json.load(file)
        
        # If the file is empty
        if not data:
            data = DEFAULT_SETTINGS
            has_has_error = True
        
        # Get the individual settings
        app_name = (data.get("app_name") or "").strip()
        currency = (data.get("currency") or "").strip()
        low_stock_threshold = data.get("low_stock_threshold")
        show_summary = data.get("show_summary")

        # Check if the name is empty
        if not app_name:
            app_name = DEFAULT_SETTINGS["app_name"]
            has_has_error = True

        # Check if the low stock threshold is empty or not number or negative
        if not data.get("low_stock_threshold"):
            low_stock_threshold = DEFAULT_SETTINGS["low_stock_threshold"]
            has_has_error = True
        else:
            try:
                low_stock_threshold = float(low_stock_threshold)
                if not math.isfinite(low_stock_threshold):
                    low_stock_threshold = DEFAULT_SETTINGS["low_stock_threshold"]
                    has_error = True
                elif low_stock_threshold < 0:
                    low_stock_threshold = DEFAULT_SETTINGS["low_stock_threshold"]
                    has_error = True

            except ValueError:
                low_stock_threshold = DEFAULT_SETTINGS["low_stock_threshold"]
                has_error = True

        # Check if the currency is empty
        if not currency:
            has_error = True
            currency = DEFAULT_SETTINGS["currency"]

        # Check if the show summary is empty or not bool
        if not show_summary:
            has_error = True
            show_summary = DEFAULT_SETTINGS["show_summary"]
        else:
            try:
                show_summary = bool(show_summary)
                has_error = True
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
    if has_error == True:
        with open(input_file, 'w') as file:
            json.dump(current_settings, file, indent=4)

    # Print the settings
    print(f"Welcome to {app_name}")
    print("Current Settings")
    print(f"1- Application name: {app_name}")
    print(f"2- Currency: {currency}")
    print(f"3- low Stock Threshold: {low_stock_threshold}")
    print(f"4- Show Summary: {show_summary}")

except FileNotFoundError:
    with open(input_file, 'w') as file:
        json.dump(DEFAULT_SETTINGS, file, indent=4)
        print(f"Created default settings in {input_file}")
