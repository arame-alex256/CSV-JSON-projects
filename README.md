# CSV-JSON-Projects

A collection of Python projects focused on learning CSV and JSON processing, handling structured data, and building simple automation tools.

## CSV Projects

These projects cover the basics of working with CSV files, starting with simple data structures and progressing toward file reading and data analysis.

### Project 0: Sales List

Uses a list of dictionaries to store and display product information.

- Displays product names and prices.
- Formats floating-point prices to two decimal places while keeping integer prices unchanged.
- Calculates the total price of all products.

### Project 1: CSV Reader

Reads product information from a CSV file in the `data/` directory using Python's built-in `csv.DictReader`.

- Reads product names, prices, and quantities.
- Handles missing column values by displaying `"N/A"`.
- Converts prices from strings to floating-point numbers.
- Uses `0` as a fallback when a price cannot be converted.
- Handles missing files with basic exception handling.
- Formats prices to two decimal places.

### Project 2: CSV Analyzer

orginizes the data from the CSV file using different Python's built-in functions and gives a structured output.

- Filter the products, and skip products with issues such as missing a name value, negative or non-number value.
- Stores the products into a list where name is a `str`, price is a `float` and quantity is an `int`.
- Calculates the total number of products after the filter.
- Calculates the total inventory value using price x quantity.
- Calculates the highest price with `max()` function and match it with the products with the same price if there are products.
- Calculates the average price of the all products if there are products.
- Finds products that have lower qunatities than a chosen threshold value and returns a message if there was no such product.
- Prevents from running the other functions in case of any error.

### Project 3: CSV Cleaner

A Python script that cleans and validates messy CSV product data, separating valid products from rows that contain errors.

- Reads product data from a CSV file using `csv.DictReader`.
- Removes unnecessary whitespace from product names, prices, and quantities.
- Detects rows containing more than the expected number of values.
- Identifies products with missing or empty names.
- Validates prices and quantities by converting them to numeric types.
- Rejects rows with non-numeric or invalid price and quantity values.
- Rejects products with negative prices or quantities while allowing zero values.
- Detects duplicate product names and keeps the first valid occurrence.
- Separates valid products from rejected rows with explanations for each error.
- Saves cleaned product data to `produced_files/clean_products.csv` using `csv.DictWriter`.
- Saves rejected rows and their error messages to `produced_files/rejected_rows.csv`using `csv.DictWriter`.
- Creates the output directory automatically with `path` and reports the number of accepted and rejected products.

## Technologies

- Python 3
- Built-in `csv` module
- Built-in `path` module

## Project Status

This repository is a work in progress. More CSV and JSON projects will be added as I continue learning Python and developing practical automation skills.