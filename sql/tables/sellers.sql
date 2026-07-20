-- ==========================================================
-- Retail Intelligence Platform
-- Table: sellers
-- Description:
-- Stores marketplace seller information.
-- ==========================================================

CREATE TABLE IF NOT EXISTS retail.sellers (

    seller_id VARCHAR(50) PRIMARY KEY,

    seller_zip_code_prefix VARCHAR(10) NOT NULL,

    seller_city VARCHAR(100) NOT NULL,

    seller_state CHAR(2) NOT NULL

);

COMMENT ON TABLE retail.sellers IS
'Stores seller information for the marketplace.';

COMMENT ON COLUMN retail.sellers.seller_id IS
'Unique identifier for each seller.';

COMMENT ON COLUMN retail.sellers.seller_zip_code_prefix IS
'Seller ZIP code prefix.';

COMMENT ON COLUMN retail.sellers.seller_city IS
'Seller city.';

COMMENT ON COLUMN retail.sellers.seller_state IS
'Brazilian state abbreviation.';