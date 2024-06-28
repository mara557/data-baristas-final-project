import extract as ex
import remove_sensitive as rm
import generate_uids as uids  # Import the uids module to access hash_ids_list function

"""This is separating each item name and price in each order into a list of dictionaries from data folder."""
def item_separation():
    all_files_data = ex.reading_all_csv_files()
    
    all_results = {}
    for filepath, data in all_files_data.items():
        file_name = filepath.split('/')[-1]
        all_data = rm.remove_pii(data)
        
        dataset = []
        for row in all_data:
            if len(row) > 2:  # Ensure the row has the items column
                dataset.append(row)

        ids_list = uids.hash_ids_list(dataset)

        result = []
        for order_index, row in zip(ids_list, dataset):
            items = row[2].split(", ")
            for item in items:
                name, price = item.rsplit(" - ", 1)
                result.append([order_index, name.strip(), float(price.strip())])

        all_results[file_name] = result
    
    return all_results

