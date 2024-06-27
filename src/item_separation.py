import extract as ex
import remove_sensitive as rm

"""This is separating each item name and price in each order into a list of dictionaries from data folder."""
def item_separation():
    all_files_data = ex.reading_all_csv_files()
    
    all_results = {}
    for filepath, data in all_files_data.items():
        file_name = filepath.split('/')[-1]
        all_data = rm.remove_pii(data)
        
        result = [
            ["item_id", "item_name", "price"]
        ]

        for item_id, row in enumerate(all_data):
            if len(row) > 2:  # Ensure the row has the items column
                items = row[2].split(", ")
                for item in items:
                    name, price = item.rsplit(" - ", 1)
                    result.append([item_id, name.strip(), float(price.strip())])
        
        all_results[file_name] = result

    return all_results

if __name__ == "__main__":
    items = item_separation()
    for city, city_items in items.items():
        if city == "headers":
            continue
        print(f"City: {city}")
        for item in city_items:
            print(item)