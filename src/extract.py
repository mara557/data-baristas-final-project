import csv

def reading_csv_files():
    try:
        with open("leeds.csv", 'r') as file:
            csv_file = csv.DictReader(file)
            products_list = list(csv_file)
    except FileNotFoundError:
        leeds_list = []

reading_csv_files()