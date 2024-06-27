import item_basket as products

items = dict(product.item_separation())

# !!default i needs to be changed to something else if called again!!
def generate_menu(list_dictionary_of_items, i=0):
    item_name = []
    prices = []
    product_ids = []
    for kvpair in list_dictionary_of_items:
        if kvpair.keys() in item_name:
            pass
        else:
            item_name.append(kvpair.keys())
            prices.append(kvpair.values())
            product_ids.append(f"P00{i}")
            i += 1

    for index in range(0, i):
        items_db = []
        row = [product_ids[index], item_name[index], prices[index]]
        items_db.append(row)
    return items_db



