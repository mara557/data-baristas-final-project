import item_separation as isep
import purchase_separation as psep
import generate_menu_items as gmi
import sql_utils as sql
import os
from connect_to_db import *

def run(event, context):
    ssm_env_var_name = 'SSM_PARAMETER_NAME'
    print('lambda_handler: starting')

    try:
        ssm_param_name = os.environ.get(ssm_env_var_name, 'NOT_SET')
        print(f'lambda_handler: ssm_param_name={ssm_param_name} from ssm_env_var_name={ssm_env_var_name}')

        # connection
        redshift_details = get_ssm_param(ssm_param_name)
        conn, cur = open_sql_database_connection_and_cursor(redshift_details)

        print(f'lambda_handler: connected to database')

    except Exception as whoopsy:
        # ...exception reporting
        print(f'lambda_handler: failure, error={whoopsy}')
        raise whoopsy

    # Define the S3 bucket name
    bucket = "data-baristas"  # Replace with your actual S3 bucket name

    # Extract and process data
    print('lambda_handler: starting item separation')
    item_data = isep.item_separation(bucket)  # Pass the bucket name
    print(f'lambda_handler: item separation complete, item_data={item_data}')

    print('lambda_handler: starting order list creation')
    order_info = psep.create_order_list(bucket)  # Pass the bucket name
    print(f'lambda_handler: order list creation complete, order_info={order_info}')

    # Get the current max item_id from the database
    print('lambda_handler: fetching current max item_id from database')
    current_max_id = sql.get_max_item_id(conn=conn) + 1
    print(f'lambda_handler: current max item_id is {current_max_id - 1}, new starting item_id is {current_max_id}')

    # Generate menu items data from the combined items
    print('lambda_handler: generating menu data')
    menu_data, _ = gmi.generate_menu([item for data in item_data.values() for item in data], current_max_id)
    print(f'lambda_handler: menu data generation complete, menu_data={menu_data}')

    # Prepare items_ordered data
    print('lambda_handler: preparing items ordered data')
    items_ordered_data = []
    for data in item_data.values():
        for row in data:
            order_id = row[0]
            item_name = row[1]
            # Find the corresponding product_id from menu_data
            for item in menu_data:
                if item[1] == item_name:
                    item_id = item[0]
                    items_ordered_data.append([order_id, item_id])
                    break
    print(f'lambda_handler: items ordered data preparation complete, items_ordered_data={items_ordered_data}')

    # Prepare purchase information data
    print('lambda_handler: preparing purchase information data')
    purchase_info_data = []
    for data in order_info.values():
        purchase_info_data.extend(data)
    print(f'lambda_handler: purchase information data preparation complete, purchase_info_data={purchase_info_data}')

    # Load data into the database
    print('lambda_handler: loading purchase information into database')
    sql.load_purchase_information(purchase_info_data, conn=conn)
    print('lambda_handler: purchase information loaded into database')

    print('lambda_handler: loading menu data into database')
    sql.load_menu_into_table(menu_data, conn=conn)
    print('lambda_handler: menu data loaded into database')

    print('lambda_handler: loading items ordered data into database')
    sql.load_items_ordered_into_table(items_ordered_data, conn=conn)
    print('lambda_handler: items ordered data loaded into database')

    conn.close()
    print('lambda_handler: all tasks completed')

if __name__ == "__main__":
    run()
