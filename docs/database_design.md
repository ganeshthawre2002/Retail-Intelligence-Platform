# Retail Intelligence Platform - Database Design

## Objective

Design the operational PostgreSQL database for the Retail Intelligence Platform.

The schema is based on the Olist Brazilian E-Commerce dataset and is designed to support:

- Transactional storage
- Analytics
- ETL pipelines
- Data warehouse modeling
- AI-powered insights

---

# Business Entities

| Entity | Description |
|---------|-------------|
| Customers | Customer information |
| Orders | Customer orders |
| Order Items | Products purchased in each order |
| Products | Product catalog |
| Sellers | Seller information |
| Payments | Payment details |
| Reviews | Customer reviews |
| Geolocation | Geographic reference data |
| Category Translation | Portuguese to English product categories |

---

# Candidate Primary Keys

| Table | Primary Key |
|---------|-------------|
| customers | customer_id |
| orders | order_id |
| products | product_id |
| sellers | seller_id |
| category_translation | product_category_name |
| order_items | (order_id, order_item_id) |
| order_payments | (order_id, payment_sequential) |
| order_reviews | Investigation Required |
| geolocation | No Primary Key |

---

# Candidate Foreign Keys

| Child Table | Foreign Key | Parent Table |
|--------------|-------------|--------------|
| orders | customer_id | customers |
| order_items | order_id | orders |
| order_items | product_id | products |
| order_items | seller_id | sellers |
| order_payments | order_id | orders |
| order_reviews | order_id | orders |
| products | product_category_name | category_translation |

---

# Notes

- Primary keys were identified using the profiling engine.
- Composite keys were identified through unique value analysis.
- Relationships will be validated before implementing the PostgreSQL schema.