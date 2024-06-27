import remove_sensitive as rs
import generate_uids as uids
# function to create list of lists for order information 


def create_order_list(dataset):
    expunged_data = rs.remove_pii(dataset)
    ids_list = uids.generate_hashed_ids(dataset)
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
 
        # Append the sub  list to the main list
        purchase_information.append(order_sublist)
 
    # Return the list of order information
    return purchase_information
 
 