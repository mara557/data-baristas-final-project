import csv
import glob

def reading_all_csv_files(directory="data"):
    """Reads all CSV files from the specified directory"""
    all_files_data = {}
    for filepath in glob.glob(f"{directory}/*.csv"):
        try:
            with open(filepath, 'r', encoding="UTF-8") as file:
                csv_file = csv.reader(file)
                all_files_data[filepath] = list(csv_file)
        except FileNotFoundError:
            print(f"File not found: {filepath}")
    return all_files_data

