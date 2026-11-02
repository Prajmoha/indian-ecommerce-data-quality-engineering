# Indian E-Commerce Data Platform — Data Model

## 1. Project Overview

This document defines the source data model for the Indian E-Commerce Data Engineering Platform.

The dataset contains nine CSV tables covering orders, customers, products, payments, shipments, returns, customer reviews, and marketing campaigns.

The model will be used to build the Bronze, Silver, and Gold data layers.

## 2. Source Tables

| Table | Rows | Columns | Primary Key |
|---|---:|---:|---|
| orders | 100,000 | 16 | order_id |
| order_items | 254,331 | 9 | order_item_id |
| customers | 25,000 | 18 | customer_id |
| products | 550 | 14 | product_id |
| payments | 100,000 | 8 | payment_id |
| shipments | 89,681 | 11 | shipment_id |
| returns | 12,075 | 8 | return_id |
| customer_reviews | 77,530 | 8 | review_id |
| marketing_campaigns | 151 | 14 | campaign_id |

## 3. Primary Keys

The following columns were identified as unique, non-null primary-key candidates:

- orders: order_id
- order_items: order_item_id
- customers: customer_id
- products: product_id
- payments: payment_id
- shipments: shipment_id
- returns: return_id
- customer_reviews: review_id
- marketing_campaigns: campaign_id

## 4. Foreign-Key Relationships

The following 12 relationships were validated against the source data.

| Child Table | Foreign Key | Parent Table | Parent Key |
|---|---|---|---|
| orders | customer_id | customers | customer_id |
| orders | campaign_id | marketing_campaigns | campaign_id |
| order_items | order_id | orders | order_id |
| order_items | product_id | products | product_id |
| payments | order_id | orders | order_id |
| shipments | order_id | orders | order_id |
| returns | order_id | orders | order_id |
| returns | customer_id | customers | customer_id |
| returns | product_id | products | product_id |
| customer_reviews | order_id | orders | order_id |
| customer_reviews | customer_id | customers | customer_id |
| customer_reviews | product_id | products | product_id |

## 5. Relationship Validation Results

Validation was performed using Python and pandas.

| Validation Check | Result |
|---|---:|
| Total relationships checked | 12 |
| Relationships passed | 12 |
| Orphan records | 0 |
| Duplicate parent keys | 0 |
| Unexpected null foreign keys | 0 |

All 12 relationships passed validation.

Note: orders.campaign_id contains 82,821 null values. These are treated as optional campaign references, not orphan records.

## 6. Source Data Quality Observations

Initial profiling identified missing values in the following tables:

| Table | Missing Cells |
|---|---:|
| orders | 116,532 |
| customers | 2,675 |
| products | 4 |
| shipments | 4,642 |
| customer_reviews | 233 |

No duplicate complete rows were detected in any of the nine source tables.

Missing values will be investigated during the Silver-layer transformation. Nullable business fields will not be removed without understanding their meaning.

## 7. Planned Data Architecture

### Bronze Layer
- Ingest all nine source CSV files.
- Preserve the original source data.
- Add ingestion metadata.
- Maintain traceability to source files.

### Silver Layer
- Clean and standardize source data.
- Apply appropriate data types.
- Handle missing and invalid values.
- Validate primary and foreign keys.
- Separate invalid records for further investigation.

### Gold Layer
- Build analytics-ready tables.
- Create business-level aggregations.
- Support sales, customer, product, payment, shipment, and campaign analysis.

## 8. Validation Artifacts

The following validation outputs are maintained in the project:

- outputs/table_profile.csv
- outputs/column_profile.csv
- outputs/primary_key_candidates.json
- outputs/relationship_validation.csv

