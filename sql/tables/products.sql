-- ==========================================================
-- Retail Intelligence Platform
-- Table: products
-- Description:
-- Stores product information available in the marketplace.
-- ==========================================================

CREATE TABLE IF NOT EXISTS retail.products (

    product_id VARCHAR(50) PRIMARY KEY,

    product_category_name VARCHAR(255),

    product_name_length INTEGER,

    product_description_length INTEGER,

    product_photos_qty INTEGER,

    product_weight_g INTEGER,

    product_length_cm NUMERIC(10,2),

    product_height_cm NUMERIC(10,2),

    product_width_cm NUMERIC(10,2),

    CONSTRAINT fk_products_category
        FOREIGN KEY (product_category_name)
        REFERENCES retail.category_translation(product_category_name)

);

COMMENT ON TABLE retail.products IS
'Stores product information available in the marketplace.';

COMMENT ON COLUMN retail.products.product_id IS
'Unique identifier for each product.';

COMMENT ON COLUMN retail.products.product_category_name IS
'Portuguese product category. References category_translation.';

COMMENT ON COLUMN retail.products.product_name_length IS
'Length of the product name in characters.';

COMMENT ON COLUMN retail.products.product_description_length IS
'Length of the product description in characters.';

COMMENT ON COLUMN retail.products.product_photos_qty IS
'Number of product photos available.';

COMMENT ON COLUMN retail.products.product_weight_g IS
'Product weight in grams.';

COMMENT ON COLUMN retail.products.product_length_cm IS
'Product length in centimeters.';

COMMENT ON COLUMN retail.products.product_height_cm IS
'Product height in centimeters.';

COMMENT ON COLUMN retail.products.product_width_cm IS
'Product width in centimeters.';