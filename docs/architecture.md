# Indian E-Commerce Data Engineering Architecture

## Project Overview

The project currently focuses on local data profiling and validation of nine Indian e-commerce CSV datasets.

## Implemented Architecture

```text
Source CSV Files
       |
       v
Python / Pandas
       |
       v
Data Profiling
       |
       v
Data Quality Checks
       |
       v
Relationship Validation
       |
       v
Validation Reports
```

## Implemented Components

1. Source CSV dataset containing nine related tables.
2. Python-based data profiling.
3. Missing-value and duplicate-row analysis.
4. Primary-key candidate identification.
5. Foreign-key relationship validation.
6. CSV and JSON validation reports.

## Future Architecture

The following cloud architecture is a planned extension, not yet deployed as part of this repository:

```text
Source Data
    |
    v
Azure Data Factory
    |
    v
Azure Data Lake Storage Gen2
    |
    v
Azure Databricks
    |
    v
Bronze -> Silver -> Gold
    |
    v
Analytics and Reporting
```

Terraform infrastructure provisioning and automated cloud orchestration are also planned extensions.