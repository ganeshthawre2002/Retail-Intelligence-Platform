-- ==========================================================
-- Retail Intelligence Platform
-- Table: customers
-- Description:
-- Stores customer information for the operational database.
-- ==========================================================

CREATE TABLE IF NOT EXISTS retail.customers (

    customer_id VARCHAR(50) PRIMARY KEY,

    customer_unique_id VARCHAR(50) NOT NULL,

    customer_zip_code_prefix VARCHAR(10) NOT NULL,

    customer_city VARCHAR(100) NOT NULL,

    customer_state CHAR(2) NOT NULL

);

COMMENT ON TABLE retail.customers IS
'Stores customer information.';

COMMENT ON COLUMN retail.customers.customer_id IS
'Unique identifier for a customer record.';

COMMENT ON COLUMN retail.customers.customer_unique_id IS
'Persistent identifier that can link multiple customer records belonging to the same customer.';

COMMENT ON COLUMN retail.customers.customer_zip_code_prefix IS
'Customer ZIP code prefix.';

COMMENT ON COLUMN retail.customers.customer_city IS
'Customer city.';

COMMENT ON COLUMN retail.customers.customer_state IS
'Brazilian state abbreviation.';