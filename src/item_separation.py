import extract as ex
import remove_sensitive as rm

def item_separation():
    all_data = rm.remove_pii(ex.reading_all_csv_files())
    
    item_list = []

    for row in all_data:
        if len(row) > 2:  # Ensure the row has the items column
            items = row[2].split(", ")
            for item in items:
                name, price = item.rsplit(" - ", 1)
                item_dict = {
                    "item_name": name.strip(),
                    "price": float(price.strip())
                }
                item_list.append(item_dict)
    
    return item_list


"""This is separating each item name and price in each order into a list of dictionaries from data folder."""

