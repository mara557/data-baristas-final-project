DROP DATABASE IF EXISTS DB;

CREATE TABLE items (
    item_id VARCHAR(50) PRIMARY KEY,
    item_name VARCHAR(255) NOT NULL,
    price NUMERIC NOT NULL
);

CREATE TABLE purchase_information (
    order_id VARCHAR(50) PRIMARY KEY,
    time_of_purchase TIMESTAMP NOT NULL,
    location VARCHAR(255) NOT NULL,
    total_paid NUMERIC NOT NULL,
    payment_method VARCHAR(50) NOT NULL
);

CREATE TABLE items_ordered (
    order_id VARCHAR(50),
    item_id VARCHAR(50),
    PRIMARY KEY (order_id, item_id),
    FOREIGN KEY (order_id) REFERENCES purchase_information(order_id),
    FOREIGN KEY (item_id) REFERENCES items(item_id)
);




"""
        Copy these tables and insert them into your database
        SQL command
        DB: DB
        Copy these tables, insert into SQL command
        Execute
"""