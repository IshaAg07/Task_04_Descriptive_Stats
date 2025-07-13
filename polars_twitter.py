import polars as pl
from polars.selectors import numeric

# Load dataset
df = pl.read_csv("2024_tw_posts_president_scored_anon.csv")

# --- NUMERIC SUMMARY ---
print("\n--- NUMERIC SUMMARY ---")

# Get numeric columns and describe them
numeric_cols = df.select(numeric()).columns
desc = df.select(numeric_cols).describe()
desc_rows = desc.to_dicts()

# Use appropriate key name
key_field = "statistic"
wanted_stats = ["count", "null_count", "mean", "std", "min", "25%"]
summary_by_stat = {row[key_field]: row for row in desc_rows if row[key_field] in wanted_stats}

for stat in wanted_stats:
    print(f"\n{stat.upper()}:")
    for col in numeric_cols:
        val = summary_by_stat.get(stat, {}).get(col, "NA")
        if isinstance(val, float):
            val = f"{val:,.2f}"
        print(f"  {col:<35}: {val}")

# --- CATEGORICAL SUMMARY ---
print("\n\n--- CATEGORICAL SUMMARY ---")
categorical_cols = ["source", "id", "lang"]
for col in categorical_cols:
    if col in df.columns:
        unique = df.select(pl.col(col).n_unique()).item()
        top_val = (
            df.group_by(col)
            .agg(pl.len().alias("count"))
            .sort("count", descending=True)
            .limit(1)
        )
        top_str = f"{top_val[0, col]} ({top_val[0, 'count']})"
        print(f"{col:>15}: unique={unique:<5} top={top_str}")
    else:
        print(f"{col:>15}: Column not found")

# --- GROUP BY SUMMARY ---
print("\n\n--- GROUP BY SUMMARY ---")
if "source" in df.columns and "id" in df.columns:
    group1 = df.group_by("source").len().height
    group2 = df.group_by(["source", "id"]).len().height
    print(f"Total groups by source           : {group1}")
    print(f"Total groups by (source, id)     : {group2}")
else:
    print("Columns 'source' and/or 'id' not found for group by.")
