<<<<<<< HEAD
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

=======
import csv
import glob
import os

def reading_all_csv_files(directory="data"):
    """Reads all CSV files from the specified directory and groups them by location, appending data from files with the same location."""
    all_files_data = {}
    
    for filepath in glob.glob(f"{directory}/*.csv"):
        try:
            filename = os.path.basename(filepath)
            location = filename.split('_')[0]  # Assuming the location is the first part of the filename
            
            if location not in all_files_data:
                all_files_data[location] = []
            
            with open(filepath, 'r', encoding="UTF-8") as file:
                csv_file = csv.reader(file)
                data = list(csv_file)
                all_files_data[location].extend(data)
        except FileNotFoundError:
            print(f"File not found: {filepath}")
    
    return all_files_data
>>>>>>> faf0513afec6090b5f97c7f892ddad23f5175d7e
