-- ==========================================================
-- Retail Intelligence Platform
--- Table: category _translation 
--- Description:
--- Maps Portuguese product category names to English names.
--- =====


CREATE TABLE IF NOT EXISTS retail.category_translation (

    product_category_name VARCHAR(255) PRIMARY KEY,
    product_category_name_english VARCHAR(255) NOT NULL

);


COMMENT ON TABLE retail.category_translation IS
'Lookup table that translates Portuguese product category names into English.';

COMMENT ON COLUMN retail.category_translation.product_category_name IS
'Original product category name in Portuguese.';

COMMENT ON COLUMN retail.category_translation.product_category_name_english IS
'English translation of the product category.';