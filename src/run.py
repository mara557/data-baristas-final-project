import item_separation as isep
import purchase_separation as psep
import generate_menu_items as gmi
import sql_utils as sql

def run():
    # Extract and process data
    item_data = isep.item_separation()
    order_info = psep.create_order_list()
    
    # Combine all items from all files
    combined_items = []
    for data in item_data.values():
        combined_items.extend(data)

    # Get the current max item_id from the database
    current_max_id = sql.get_max_item_id() + 1

    # Generate menu items data from the combined items
    menu_data, _ = gmi.generate_menu(combined_items, current_max_id)

    # Prepare items_ordered data
    items_ordered_data = []
    for row in combined_items:
        order_id = row[0]
        item_name = row[1]
        # Find the corresponding product_id from menu_data
        for item in menu_data:
            if item[1] == item_name:
                item_id = item[0]
                items_ordered_data.append([order_id, item_id])
                break
    
    # Prepare purchase information data
    purchase_info_data = []
    for data in order_info.values():
        purchase_info_data.extend(data)
    
    # Load data into the database
    sql.load_purchase_information(purchase_info_data)
    sql.load_menu_into_table(menu_data)
    sql.load_items_ordered_into_table(items_ordered_data)

if __name__ == "__main__":
    run()
