<<<<<<< HEAD
# !!default i needs to be changed to something else if called again!!


def generate_menu(list_items, start_id=0):
    items_name = []
    items_db = []
    i = start_id
    for each_row in list_items:
        if each_row[1] in items_name:
            pass
        else:
            items_name.append(each_row[1])
            item_name = each_row[1]
            price = each_row[2]
            product_id = f"P{str(i).zfill(3)}"
            i += 1
            row = [product_id, item_name, price]
            items_db.append(row)
    return items_db, i

=======
# !!default i needs to be changed to something else if called again!!


def generate_menu(list_items, start_id=0):
    items_name = []
    items_db = []
    i = start_id
    for each_row in list_items:
        # Check if the item name and price combination already exists
        duplicate_found = False
        for item in items_db:
            if item[1] == each_row[1] and item[2] == each_row[2]:
                duplicate_found = True
                break
        
        if duplicate_found:
            continue
        
        items_name.append(each_row[1])
        item_name = each_row[1]
        price = each_row[2]
        product_id = f"P{str(i).zfill(3)}"
        i += 1
        row = [product_id, item_name, price]
        items_db.append(row)
    return items_db, i


>>>>>>> faf0513afec6090b5f97c7f892ddad23f5175d7e
