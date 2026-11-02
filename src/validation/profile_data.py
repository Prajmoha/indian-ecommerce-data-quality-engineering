
from pathlib import Path
import pandas as pd
import json

# Project directories
PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = PROJECT_ROOT / "data" / "raw"
OUTPUT_DIR = PROJECT_ROOT / "outputs"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Expected source tables
EXPECTED_FILES = [
    "orders.csv",
    "order_items.csv",
    "customers.csv",
    "products.csv",
    "payments.csv",
    "shipments.csv",
    "returns.csv",
    "customer_reviews.csv",
    "marketing_campaigns.csv"
]

table_profiles = []
column_profiles = []
primary_key_candidates = {}

print("=" * 65)
print("E-COMMERCE DATA PROFILING")
print("=" * 65)

for filename in EXPECTED_FILES:

    file_path = RAW_DIR / filename

    if not file_path.exists():
        print(f"\nMISSING FILE: {filename}")
        continue

    print(f"\nProcessing: {filename}")

    # Read CSV
    try:
        df = pd.read_csv(file_path, low_memory=False)
    except UnicodeDecodeError:
        df = pd.read_csv(
            file_path,
            encoding="latin-1",
            low_memory=False
        )

    row_count, column_count = df.shape

    # Table-level statistics
    missing_cells = int(df.isnull().sum().sum())
    duplicate_rows = int(df.duplicated().sum())

    table_profiles.append({
        "table_name": filename,
        "row_count": row_count,
        "column_count": column_count,
        "missing_cells": missing_cells,
        "duplicate_rows": duplicate_rows
    })

    # Column-level statistics
    for column in df.columns:
        column_profiles.append({
            "table_name": filename,
            "column_name": column,
            "data_type": str(df[column].dtype),
            "null_count": int(df[column].isnull().sum()),
            "null_percentage": round(
                df[column].isnull().mean() * 100, 2
            ),
            "distinct_values": int(df[column].nunique())
        })

    # Identify columns that may be primary keys
    candidates = []

    for column in df.columns:
        if (
            column.lower().endswith("_id")
            and df[column].notna().all()
            and df[column].is_unique
        ):
            candidates.append(column)

    primary_key_candidates[filename] = candidates

    print(f"Rows: {row_count:,}")
    print(f"Columns: {column_count}")
    print(f"Missing cells: {missing_cells:,}")
    print(f"Duplicate rows: {duplicate_rows:,}")
    print(f"Unique ID candidates: {candidates}")

    print("\nColumn names:")
    print(list(df.columns))

# Save table-level profile
table_profile_df = pd.DataFrame(table_profiles)
table_profile_df.to_csv(
    OUTPUT_DIR / "table_profile.csv",
    index=False
)

# Save column-level profile
column_profile_df = pd.DataFrame(column_profiles)
column_profile_df.to_csv(
    OUTPUT_DIR / "column_profile.csv",
    index=False
)

# Save candidate ID information
with open(
    OUTPUT_DIR / "primary_key_candidates.json",
    "w",
    encoding="utf-8"
) as file:
    json.dump(primary_key_candidates, file, indent=4)

print("\n" + "=" * 65)
print("DATA PROFILING COMPLETED")
print("=" * 65)

print(f"Tables profiled: {len(table_profiles)}")
print(f"Outputs saved in: {OUTPUT_DIR}")
