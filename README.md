# Indian E-Commerce Data Quality and Engineering Project

## Project Overview

This project focuses on profiling, validating, and understanding an Indian e-commerce dataset containing nine related CSV tables.

The project uses Python and Pandas to inspect source data, identify data-quality issues, evaluate primary-key candidates, and validate relationships between tables.

The work establishes a foundation for building a scalable Bronze, Silver, and Gold data engineering pipeline.

## Dataset

The dataset contains nine tables:

| Table | Rows | Columns |
|---|---:|---:|
| orders | 100,000 | 16 |
| order_items | 254,331 | 9 |
| customers | 25,000 | 18 |
| products | 550 | 14 |
| payments | 100,000 | 8 |
| shipments | 89,681 | 11 |
| returns | 12,075 | 8 |
| customer_reviews | 77,530 | 8 |
| marketing_campaigns | 151 | 14 |

Total: 656,288 rows across the nine source tables.

## Technology Stack

- Python
- Pandas
- PySpark
- SQL
- Git
- CSV data processing

## Project Structure

```text
Azure-DE-Terraform-Pipeline/
├── config/
├── data/
│   └── raw/                  # Local source CSV files (not committed)
├── databricks/
├── docs/
│   ├── architecture.md
│   ├── data_model.md
│   ├── data_dictionary.csv
│   └── dataset_validation_report.csv
├── notebooks/
├── outputs/                  # Generated validation reports (local)
├── pipelines/
├── screenshots/
├── sql/
├── src/
│   ├── test_spark.py
│   └── validation/
│       ├── profile_data.py
│       └── validate_relationships.py
├── terraform/
├── tests/
├── .gitignore
├── requirements.txt
└── README.md
```

## Implemented Work

### 1. Data Profiling

The profiling script examines all nine CSV files and generates:

- Table-level row and column counts.
- Missing-cell counts.
- Duplicate-row counts.
- Column-level data types and null counts.
- Candidate primary-key columns.

Generated reports:

- `outputs/table_profile.csv`
- `outputs/column_profile.csv`
- `outputs/primary_key_candidates.json`

### 2. Relationship Validation

The relationship validation script checks relationships between the source tables.

Checks include:

- Missing foreign-key values.
- Orphan records.
- Duplicate parent-key values.

Output:

- `outputs/relationship_validation.csv`

### 3. Data Quality Assessment

Initial profiling identified missing values in selected tables. These are documented for further investigation rather than automatically removing potentially valid records.

### 4. Data Model Documentation

The data model documents the nine source tables, primary-key candidates, foreign-key relationships, and data-quality observations.

## Execution

Create and activate a Python virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Run data profiling:

```powershell
python .\src\validation\profile_data.py
```

Run relationship validation:

```powershell
python .\src\validation\validate_relationships.py
```

Generated reports are saved in the `outputs/` directory.

## Planned Extensions

The following are potential future extensions and should not be considered deployed components:

- Azure Data Factory orchestration.
- Azure Data Lake Storage Gen2 integration.
- Databricks Bronze, Silver, and Gold transformations.
- Terraform-based infrastructure provisioning.
- Automated incremental ingestion and scheduling.

## Project Objective

The objective is to develop reliable data engineering practices through source-data profiling, data-quality validation, relationship checks, and documented data modelling, while establishing a foundation for cloud-based analytics pipelines.