import os
import psycopg2 as psy
from dotenv import load_dotenv

load_dotenv()

host_name = os.environ.get("POSTGRES_HOST")
user_name = os.environ.get("POSTGRES_USER")
user_password = os.environ.get("POSTGRES_PASSWORD")
database_name = os.environ.get("POSTGRES_DB")

def load_menu_into_table(list_input):
    for item in list_input:
        product_id = item[0]
        name = item[1]
        price = item[2]
        
        with psy.connect(
            host = host_name,
            user = user_name,
            password = user_password,
            database = database_name,
            
        ) as connection:
            with connection.cursor() as cursor:
                add_sql = """
                UPDATE items
                SET item_id = %s
                SET item_name = %s
                SET price = %s
                """
                values = (product_id, name, price)
                cursor.execute(add_sql, values)

def load_items_ordered_into_table(list_input):
    for item in list_input:
        order_id = item[0]
        item_id = item[1]
        
        with psy.connect(
            host = host_name,
            user = user_name,
            password = user_password,
            database = database_name,
            
        ) as connection:
            with connection.cursor() as cursor:
                add_sql = """
                UPDATE items_ordered
                SET order_id = %s
                SET item_id = %s
                """
                values = (order_id, item_id)
                cursor.execute(add_sql, values)

def load_purchase_information(list_input):
    for item in list_input:
        order_id = item[0]
        time_of_purchase = item[1]
        location = item[2]
        total_paid = item[3]
        payment_method = item[4]
        
        with psy.connect(
            host = host_name,
            user = user_name,
            password = user_password,
            database = database_name,
            
        ) as connection:
            with connection.cursor() as cursor:
                add_sql = """
                UPDATE order_information
                SET order_id = %s
                SET time_of_purchase = %s
                SET location = %s
                SET total_paid = %s
                SET payment_method = %s
                """
                values = (order_id, time_of_purchase, location, total_paid, payment_method)
                cursor.execute(add_sql, values)
          