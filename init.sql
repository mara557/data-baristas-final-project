<<<<<<< HEAD
DROP DATABASE IF EXISTS DB;
-- Create the items table
CREATE TABLE items (
    item_id VARCHAR(255) PRIMARY KEY,
    item_name VARCHAR(255),
    price DECIMAL(10,2)
);

-- Create the purchase_information table
CREATE TABLE purchase_information (
    order_id VARCHAR(255) PRIMARY KEY,
    time_of_purchase TIMESTAMP,
    location VARCHAR(255),
    total_paid DECIMAL(10,2),
    payment_method VARCHAR(255)
);

-- Create the items_ordered table using SERIAL to simulate AUTO_INCREMENT
CREATE TABLE items_ordered (
    row_id SERIAL PRIMARY KEY,
    order_id VARCHAR(255),
    item_id VARCHAR(255),
    FOREIGN KEY (order_id) REFERENCES purchase_information(order_id),
    FOREIGN KEY (item_id) REFERENCES items(item_id)
);


"""
        Copy these tables and insert them into your database
        SQL command
        DB: DB
        Copy these tables, insert into SQL command
        Execute
=======
DROP DATABASE IF EXISTS DB;
-- Create the items table
CREATE TABLE items (
    item_id VARCHAR(255) PRIMARY KEY,
    item_name VARCHAR(255),
    price DECIMAL(10,2)
);

-- Create the purchase_information table
CREATE TABLE purchase_information (
    order_id VARCHAR(255) PRIMARY KEY,
    time_of_purchase TIMESTAMP,
    location VARCHAR(255),
    total_paid DECIMAL(10,2),
    payment_method VARCHAR(255)
);

-- Create the items_ordered table using SERIAL to simulate AUTO_INCREMENT
CREATE TABLE items_ordered (
    row_id SERIAL PRIMARY KEY,
    order_id VARCHAR(255),
    item_id VARCHAR(255),
    FOREIGN KEY (order_id) REFERENCES purchase_information(order_id),
    FOREIGN KEY (item_id) REFERENCES items(item_id)
);







"""
        Copy these tables and insert them into your database
        SQL command
        DB: DB
        Copy these tables, insert into SQL command
        Execute
>>>>>>> faf0513afec6090b5f97c7f892ddad23f5175d7e
"""