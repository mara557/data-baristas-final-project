"""The code for reading the CSV file"""
import csv

def reading_leeds_csv_files():
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

def reading_chesterfield_csv_files():
    "Reads CSV file from data folder"
    try:
        with open("data/chesterfield_25-08-2021_09-00-00.csv", 'r', encoding="UTF-8") as file:
            csv_file = csv.reader(file)
            orders_list = []
            for row in csv_file:
                orders_list.append(row)
    except FileNotFoundError:
        print("File not found")
        orders_list = []
    return orders_list
