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

try:
    with open(input_file, 'r') as file:
        # Load the JSON File as a dict
        data = json.load(file)
        
        # If the file is empty
        if not data:
            data = DEFAULT_SETTINGS
            json.dump(data, file, indent=4)
            print(f"Created default settings in {input_file}")
        
        app_name = (data.get("app_name") or "").strip()
        currency = (data.get("currency") or "").strip()
        low_stock_threshold = data.get("low_stock_threshold")
        show_summary = data.get("show_summary")

        if not app_name:
            app_name = DEFAULT_SETTINGS["app_name"]

        if not data.get("low_stock_threshold"):
            low_stock_threshold = DEFAULT_SETTINGS["low_stock_threshold"]
        else:
            try:
                low_stock_threshold = float(low_stock_threshold)
                if not math.isfinite(low_stock_threshold):
                    low_stock_threshold = DEFAULT_SETTINGS["low_stock_threshold"]
                elif low_stock_threshold < 0:
                    low_stock_threshold = DEFAULT_SETTINGS["low_stock_threshold"]
            except ValueError:
                low_stock_threshold = DEFAULT_SETTINGS["low_stock_threshold"]

        if not currency:
            currency = DEFAULT_SETTINGS["currency"]

        if not show_summary:
            show_summary = DEFAULT_SETTINGS["show_summary"]
        else:
            try:
                show_summary = bool(show_summary)
            except ValueError:
                show_summary = DEFAULT_SETTINGS["show_summary"]
    
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
