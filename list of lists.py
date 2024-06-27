

# function to create list of lists for order information

def create_order_list(list_of_ids, time_of_purchase, location, total_paid, payment_method):
    
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



