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

