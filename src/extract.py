"""The code for reading the CSV file"""
import csv

def reading_csv_files():
    "Reads CSV file from data folder"
    try:
        with open("data/leeds.csv", 'r', encoding="UTF-8") as file:
            csv_file = csv.reader(file)
            orders_list = []
            for row in csv_file:
                orders_list.append(row)
    except FileNotFoundError:
        print("File not found")
        orders_list = []
    return orders_list

leeds_orders_list = reading_csv_files()
for rows in leeds_orders_list:
    print(rows)
