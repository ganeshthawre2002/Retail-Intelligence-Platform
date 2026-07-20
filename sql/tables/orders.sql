-- ==========================================================
-- Retail Intelligence Platform
-- Table: orders
-- Description:
-- Stores customer orders and their lifecycle timestamps.
-- ==========================================================

CREATE TABLE IF NOT EXISTS retail.orders (

    order_id VARCHAR(50) PRIMARY KEY,

    customer_id VARCHAR(50) NOT NULL,

    order_status VARCHAR(50) NOT NULL,

    order_purchase_timestamp TIMESTAMP NOT NULL,

    order_approved_at TIMESTAMP,

    order_delivered_carrier_date TIMESTAMP,

    order_delivered_customer_date TIMESTAMP,

    order_estimated_delivery_date TIMESTAMP NOT NULL,

    CONSTRAINT fk_orders_customer
        FOREIGN KEY (customer_id)
        REFERENCES retail.customers(customer_id)

);

COMMENT ON TABLE retail.orders IS
'Stores customer orders and important lifecycle timestamps.';

COMMENT ON COLUMN retail.orders.order_id IS
'Unique identifier for each order.';

COMMENT ON COLUMN retail.orders.customer_id IS
'References the customer who placed the order.';

COMMENT ON COLUMN retail.orders.order_status IS
'Current status of the order.';

COMMENT ON COLUMN retail.orders.order_purchase_timestamp IS
'Timestamp when the customer placed the order.';

COMMENT ON COLUMN retail.orders.order_approved_at IS
'Timestamp when the payment was approved.';

COMMENT ON COLUMN retail.orders.order_delivered_carrier_date IS
'Timestamp when the order was handed over to the carrier.';

COMMENT ON COLUMN retail.orders.order_delivered_customer_date IS
'Timestamp when the customer received the order.';

COMMENT ON COLUMN retail.orders.order_estimated_delivery_date IS
'Estimated delivery date for the order.';