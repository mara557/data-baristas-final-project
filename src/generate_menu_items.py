

# !!default i needs to be changed to something else if called again!!
def generate_menu(list_dictionary_of_items, i=0):
    items_name = []
    items_db = []
    for each_dictionary in list_dictionary_of_items:
        if each_dictionary["item_name"] in items_name:
            pass
        else:
            items_name.append(each_dictionary["item_name"])
            item_name = (each_dictionary["item_name"])
            price = (each_dictionary["price"])
            product_id = (f"P00{i}")
            i += 1
            row = [product_id, item_name, price]
            items_db.append(row)
    return items_db



