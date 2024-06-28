import extract as ex
import remove_sensitive as rs
import generate_uids as uids
from datetime import datetime


def create_order_list(directory="data"):
    all_files_data = ex.reading_all_csv_files(directory)
    all_order_information = {}

    for filepath, dataset in all_files_data.items():
        expunged_data = rs.remove_pii(dataset)
        ids_list = uids.hash_ids_list(dataset)


        purchase_information = []
        i = 0
        for row in expunged_data:
            order_id = ids_list[i]
            time_of_purchase = row[0]
            location = row[1]
            total_paid = row[3]
            payment_method = row[4]
            

            try:
                time_of_purchase = datetime.strptime(time_of_purchase, "%d/%m/%Y %H:%M").strftime("%Y-%m-%d %H:%M:%S")
            except ValueError as e:
                print(f"Error parsing date '{time_of_purchase}': {e}")
                continue
            
            order_sublist = [
                order_id,
                time_of_purchase,
                location,
                total_paid,
                payment_method      
            ]
            i += 1


            purchase_information.append(order_sublist)
        
        file_name = filepath.split('/')[-1]
        all_order_information[file_name] = purchase_information


    return all_order_information
