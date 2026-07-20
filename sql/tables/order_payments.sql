-- ==========================================================
-- Retail Intelligence Platform
-- Table: order_payments
-- Description:
-- Stores payment information for customer orders.
-- ==========================================================

CREATE TABLE IF NOT EXISTS retail.order_payments (

    order_id VARCHAR(50) NOT NULL,

    payment_sequential INTEGER NOT NULL,

    payment_type VARCHAR(30) NOT NULL,

    payment_installments INTEGER NOT NULL,

    payment_value NUMERIC(10,2) NOT NULL,

    CONSTRAINT pk_order_payments
        PRIMARY KEY (order_id, payment_sequential),

    CONSTRAINT fk_order_payments_order
        FOREIGN KEY (order_id)
        REFERENCES retail.orders(order_id)

);

COMMENT ON TABLE retail.order_payments IS
'Stores payment information for customer orders.';

COMMENT ON COLUMN retail.order_payments.order_id IS
'References the order associated with the payment.';

COMMENT ON COLUMN retail.order_payments.payment_sequential IS
'Sequence number for multiple payments within the same order.';

COMMENT ON COLUMN retail.order_payments.payment_type IS
'Payment method used by the customer.';

COMMENT ON COLUMN retail.order_payments.payment_installments IS
'Number of installments used for the payment.';

COMMENT ON COLUMN retail.order_payments.payment_value IS
'Payment amount.';