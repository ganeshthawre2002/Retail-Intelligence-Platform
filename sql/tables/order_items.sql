-- ==========================================================
-- Retail Intelligence Platform
-- Table: order_items
-- Description:
-- Stores individual products within each customer order.
-- ==========================================================

CREATE TABLE IF NOT EXISTS retail.order_items (

    order_id VARCHAR(50) NOT NULL,

    order_item_id INTEGER NOT NULL,

    product_id VARCHAR(50) NOT NULL,

    seller_id VARCHAR(50) NOT NULL,

    shipping_limit_date TIMESTAMP NOT NULL,

    price NUMERIC(10,2) NOT NULL,

    freight_value NUMERIC(10,2) NOT NULL,

    CONSTRAINT pk_order_items
        PRIMARY KEY (order_id, order_item_id),

    CONSTRAINT fk_order_items_order
        FOREIGN KEY (order_id)
        REFERENCES retail.orders(order_id),

    CONSTRAINT fk_order_items_product
        FOREIGN KEY (product_id)
        REFERENCES retail.products(product_id),

    CONSTRAINT fk_order_items_seller
        FOREIGN KEY (seller_id)
        REFERENCES retail.sellers(seller_id)

);

COMMENT ON TABLE retail.order_items IS
'Stores individual products included in customer orders.';

COMMENT ON COLUMN retail.order_items.order_id IS
'References the order that contains this item.';

COMMENT ON COLUMN retail.order_items.order_item_id IS
'Sequential item number within an order.';

COMMENT ON COLUMN retail.order_items.product_id IS
'References the purchased product.';

COMMENT ON COLUMN retail.order_items.seller_id IS
'References the seller responsible for the item.';

COMMENT ON COLUMN retail.order_items.shipping_limit_date IS
'Deadline for the seller to ship the item.';

COMMENT ON COLUMN retail.order_items.price IS
'Sale price of the product.';

COMMENT ON COLUMN retail.order_items.freight_value IS
'Shipping cost charged for the item.';