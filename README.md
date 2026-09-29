# Azure Data Engineering Pipeline with Terraform and ADF

## Project Overview

This project implements a fault-tolerant Azure data engineering pipeline using Azure Data Factory, Azure Data Lake Storage Gen2, Azure Databricks, Azure SQL Database, and Terraform.

The pipeline is designed to support:

- Incremental data ingestion
- Fault tolerance and retry handling
- Data quality validation
- Quarantine of invalid records
- Schema evolution
- PySpark-based transformations
- Automated Azure infrastructure provisioning using Terraform

## Technology Stack

- Azure Data Factory
- Azure Data Lake Storage Gen2
- Azure Databricks
- PySpark
- Azure SQL Database
- Terraform
- Python
- SQL
- Git

## Architecture

Source Data → ADF → ADLS Gen2 → Databricks → Azure SQL

Invalid records are routed to a quarantine zone.

Terraform is used to provision the Azure infrastructure.

## Project Status

Initial project setup completed.