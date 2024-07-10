import extract as ex
import remove_sensitive as rs
import generate_uids as uids
from datetime import datetime

def create_order_list(bucket):
    # Reading all CSV files from the specified bucket
    all_files_data = ex.reading_all_csv_files(bucket)
    print(f'Read all files: {all_files_data}')  # Print the raw data read from the files
    all_order_information = {}

    for filepath, dataset in all_files_data.items():
        print(f'Processing file: {filepath}')
        
        # Remove PII from the dataset
        expunged_data = rs.remove_pii(dataset)
        print(f'Expunged data for {filepath}: {expunged_data}')  # Print the data after removing PII
        
        # Generate unique IDs for each order
        ids_list = uids.hash_ids_list(expunged_data)
        print(f'Generated IDs for {filepath}: {ids_list}')  # Print the generated IDs

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
        
        print(f'Purchase information for {filepath}: {purchase_information}')  # Print the purchase information for each file
        file_name = filepath.split('/')[-1]
        all_order_information[file_name] = purchase_information

    print(f'All order information: {all_order_information}')  # Print the final order information
    return all_order_information
