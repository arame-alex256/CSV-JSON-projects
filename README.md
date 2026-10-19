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

## Technologies

- Python 3
- Built-in `csv` module

## Project Status

This repository is a work in progress. More CSV and JSON projects will be added as I continue learning Python and developing practical automation skills.