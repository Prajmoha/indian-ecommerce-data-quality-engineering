
from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = PROJECT_ROOT / "data" / "raw"
OUTPUT_DIR = PROJECT_ROOT / "outputs"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Child table, child column, parent table, parent column
RELATIONSHIPS = [
    ("orders.csv", "customer_id", "customers.csv", "customer_id"),
    ("orders.csv", "campaign_id", "marketing_campaigns.csv", "campaign_id"),
    ("order_items.csv", "order_id", "orders.csv", "order_id"),
    ("order_items.csv", "product_id", "products.csv", "product_id"),
    ("payments.csv", "order_id", "orders.csv", "order_id"),
    ("shipments.csv", "order_id", "orders.csv", "order_id"),
    ("returns.csv", "order_id", "orders.csv", "order_id"),
    ("returns.csv", "customer_id", "customers.csv", "customer_id"),
    ("returns.csv", "product_id", "products.csv", "product_id"),
    ("customer_reviews.csv", "order_id", "orders.csv", "order_id"),
    ("customer_reviews.csv", "customer_id", "customers.csv", "customer_id"),
    ("customer_reviews.csv", "product_id", "products.csv", "product_id"),
]

# Read each source table once
tables = {}

for filename in set(
    [r[0] for r in RELATIONSHIPS] +
    [r[2] for r in RELATIONSHIPS]
):
    tables[filename] = pd.read_csv(
        RAW_DIR / filename,
        dtype="string"
    )

results = []

print("=" * 75)
print("FOREIGN KEY / RELATIONSHIP VALIDATION")
print("=" * 75)

for child_table, child_col, parent_table, parent_col in RELATIONSHIPS:

    child_df = tables[child_table]
    parent_df = tables[parent_table]

    child_values = child_df[child_col].dropna()
    parent_values = parent_df[parent_col].dropna()

    parent_set = set(parent_values)

    orphan_mask = ~child_values.isin(parent_set)
    orphan_count = int(orphan_mask.sum())

    null_count = int(child_df[child_col].isna().sum())
    parent_duplicates = int(parent_values.duplicated().sum())

    result = {
        "child_table": child_table,
        "child_column": child_col,
        "parent_table": parent_table,
        "parent_column": parent_col,
        "child_rows": len(child_df),
        "null_foreign_keys": null_count,
        "orphan_records": orphan_count,
        "distinct_child_keys": int(child_values.nunique()),
        "parent_duplicate_keys": parent_duplicates,
        "status": "PASS" if orphan_count == 0
                  and parent_duplicates == 0 else "REVIEW"
    }

    results.append(result)

    print(
        f"\n{child_table}.{child_col} -> "
        f"{parent_table}.{parent_col}"
    )
    print(f"Null foreign keys: {null_count}")
    print(f"Orphan records: {orphan_count}")
    print(f"Parent duplicate keys: {parent_duplicates}")
    print(f"Status: {result['status']}")

# Save results
report = pd.DataFrame(results)

report.to_csv(
    OUTPUT_DIR / "relationship_validation.csv",
    index=False
)

print("\n" + "=" * 75)
print("RELATIONSHIP VALIDATION COMPLETED")
print("=" * 75)

print(report["status"].value_counts())
print("\nReport saved to outputs/relationship_validation.csv")
