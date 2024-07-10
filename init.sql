DROP DATABASE IF EXISTS DB;

CREATE TABLE items (
    item_id VARCHAR(255) PRIMARY KEY,
    item_name VARCHAR(255),
    price DECIMAL(10,2)
);

CREATE TABLE purchase_information (
    order_id VARCHAR(255) PRIMARY KEY,
    time_of_purchase TIMESTAMP,
    location VARCHAR(255),
    total_paid DECIMAL(10,2),
    payment_method VARCHAR(255)
);

CREATE TABLE items_ordered (
    row_id INTEGER IDENTITY(1,1) PRIMARY KEY,
    order_id VARCHAR(255),
    item_id VARCHAR(255),
    FOREIGN KEY (order_id) REFERENCES purchase_information(order_id),
    FOREIGN KEY (item_id) REFERENCES items(item_id)
);



GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE items_ordered TO data_baristas_user;
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE purchase_information TO data_baristas_user;
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE items TO data_baristas_user;



"""
        Copy these tables and insert them into your database
        SQL command
        DB: DB
        Copy these tables, insert into SQL command
        Execute
"""