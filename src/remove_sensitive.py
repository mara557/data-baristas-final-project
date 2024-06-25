import extract as ex

leeds_info = ex.reading_leeds_csv_files()
chesterfield_info = ex.reading_chesterfield_csv_files()

def remove_pii(dataset):
    expunged_data = []
    for row in dataset:
        row.pop(2)
        row.pop(5)
        expunged_data.append(row)
    return expunged_data



