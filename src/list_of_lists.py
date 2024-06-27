import extract as ex
import remove_sensitive as rs
import generate_uids as uids

# function to create list of lists for order information 
def create_order_list(directory="data"):
    all_files_data = ex.reading_all_csv_files(directory)
    all_order_information = {}

    for filepath, dataset in all_files_data.items():
        expunged_data = rs.remove_pii(dataset)
        ids_list = uids.hash_ids_list(dataset)
        print(ids_list)
        # Create an empty list to store order information
        purchase_information = []
        i = 0
        for row in expunged_data:
            order_id = ids_list[i]
            time_of_purchase = row[0]
            location = row[1]
            total_paid = row[3]
            payment_method = row[4]
            order_sublist = [
                order_id,
                time_of_purchase,
                location,
                total_paid,
                payment_method      
            ]
            i += 1

            # Append the sub list to the main list
            purchase_information.append(order_sublist)
        
        file_name = filepath.split('/')[-1]
        all_order_information[file_name] = purchase_information

    # Return the dictionary of order information for all files
    return all_order_information

if __name__ == "__main__":
    orders = create_order_list()
    for city, city_orders in orders.items():
        print(f"City: {city}")
        for order in city_orders:
            print(order)
 
 