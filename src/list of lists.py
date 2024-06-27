import remove_sensitive as rs
import extract as ex
# function to create list of lists for order information
leeds_info = ex.reading_leeds_csv_files()
expunged_leeds = rs.remove_pii(leeds_info)
for row in expunged_leeds:
    print(row)

def create_order_list(dataset):
    # Create an empty list to store order information
    purchase_information = []

    # Create a sublist representing order details
    order_sublist = [
        list_of_ids,
        time_of_purchase,
        location,
        total_paid,
        payment_method       
    ]

    # Append the sub  list to the main list
    purchase_information.append(order_sublist)

    # Return the list of order information
    return purchase_information



