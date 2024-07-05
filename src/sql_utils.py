<<<<<<< HEAD
import os
import psycopg2 as psy
from dotenv import load_dotenv

load_dotenv()

host_name = os.environ.get("POSTGRES_HOST")
user_name = os.environ.get("POSTGRES_USER")
user_password = os.environ.get("POSTGRES_PASSWORD")
database_name = os.environ.get("POSTGRES_DB")

def get_max_item_id():
    with psy.connect(
        host=host_name,
        user=user_name,
        password=user_password,
        database=database_name,
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT MAX(item_id) FROM items")
            result = cursor.fetchone()
            max_id = result[0] if result[0] else "P-001"
            max_id_num = int(max_id[1:])
            return max_id_num

def load_menu_into_table(list_input):
    for item in list_input:
        product_id = item[0]
        name = item[1]
        price = item[2]
        print(f"Inserting into items: {product_id}, {name}, {price}")

        with psy.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=database_name,
        ) as connection:
            with connection.cursor() as cursor:
                add_sql = """
                INSERT INTO items(item_id, item_name, price)
                VALUES (%s, %s, %s)
                """
                values = (product_id, name, price)
                cursor.execute(add_sql, values)

def load_items_ordered_into_table(list_input):
    for item in list_input:
        order_id = item[0]
        item_id = item[1]
        print(f"Inserting into items_ordered: {order_id}, {item_id}")

        with psy.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=database_name,
        ) as connection:
            with connection.cursor() as cursor:
                add_sql = """
                INSERT INTO items_ordered(order_id, item_id)
                VALUES (%s, %s)
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
        print(f"Inserting into purchase_information: {order_id}, {time_of_purchase}, {location}, {total_paid}, {payment_method}")

        with psy.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=database_name,
        ) as connection:
            with connection.cursor() as cursor:
                add_sql = """
                INSERT INTO purchase_information(order_id, time_of_purchase, location, total_paid, payment_method)
                VALUES (%s, %s, %s, %s, %s)
                """
                values = (order_id, time_of_purchase, location, total_paid, payment_method)
                cursor.execute(add_sql, values)
=======
import os
import psycopg2 as psy

from connect_to_db import *
import os

# Name of the environment variable which has the SSM parameter name as its value.
# The SSM parameter name will be "<team name>_redshift_settings".

def get_max_item_id(conn):
    with conn.cursor() as cursor:
        cursor.execute("SELECT MAX(item_id) FROM items")
        result = cursor.fetchone()
        max_id = result[0] if result[0] else "P-001"
        max_id_num = int(max_id[1:])
        return max_id_num

def load_menu_into_table(list_input, conn):
    for item in list_input:
        product_id = item[0]
        name = item[1]
        price = item[2]
        print(f"Inserting into items: {product_id}, {name}, {price}")

        with conn.cursor() as cursor:
            # Check if item already exists
            cursor.execute("SELECT COUNT(*) FROM items WHERE item_name = %s AND price = %s", (name, price))
            result = cursor.fetchone()
            if result[0] == 0:
                add_sql = """
                INSERT INTO items(item_id, item_name, price)
                VALUES (%s, %s, %s)
                """
                values = (product_id, name, price)
                cursor.execute(add_sql, values)

def load_items_ordered_into_table(list_input, conn):
    for item in list_input:
        order_id = item[0]
        item_id = item[1]
        print(f"Inserting into items_ordered: {order_id}, {item_id}")
        
        with conn.cursor() as cursor:
            add_sql = """
            INSERT INTO items_ordered(order_id, item_id)
            VALUES (%s, %s)
            """
            values = (order_id, item_id)
            cursor.execute(add_sql, values)

def load_purchase_information(list_input, conn):
    for item in list_input:
        order_id = item[0]
        time_of_purchase = item[1]
        location = item[2]
        total_paid = item[3]
        payment_method = item[4]
        print(f"Inserting into purchase_information: {order_id}, {time_of_purchase}, {location}, {total_paid}, {payment_method}")

<<<<<<< HEAD
        with psy.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=database_name,
        ) as connection:
            with connection.cursor() as cursor:
                add_sql = """
                INSERT INTO purchase_information(order_id, time_of_purchase, location, total_paid, payment_method)
                VALUES (%s, %s, %s, %s, %s)
                """
                values = (order_id, time_of_purchase, location, total_paid, payment_method)
                cursor.execute(add_sql, values)
>>>>>>> faf0513afec6090b5f97c7f892ddad23f5175d7e
=======
        with conn.cursor() as cursor:
            add_sql = """
            INSERT INTO purchase_information(order_id, time_of_purchase, location, total_paid, payment_method)
            VALUES (%s, %s, %s, %s, %s)
            """
            values = (order_id, time_of_purchase, location, total_paid, payment_method)
            cursor.execute(add_sql, values)
>>>>>>> 88f2e03ed22a7bcac6ba18987a9798e62d06e752
