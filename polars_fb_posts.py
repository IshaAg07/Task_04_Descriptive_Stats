import polars as pl

# Load the dataset
df = pl.read_csv("/Users/ishaagrawal/Downloads/Research analyst/2024_fb_posts_president_scored_anon.csv")


# 1. NUMERIC SUMMARY
numeric_cols = df.select(pl.selectors.numeric()).columns
numeric_summary = df.select(numeric_cols).describe()
print("\n--- NUMERIC SUMMARY ---")
print(numeric_summary)

# 2. CATEGORICAL VALUE COUNTS (fixed sort syntax)
categorical_cols = ["Page Category", "Type", "Is Video Owner?"]
print("\n--- CATEGORICAL VALUE COUNTS ---")
for col in categorical_cols:
    try:
        value_counts_df = (
            df.select([pl.col(col)])
            .group_by(col)
            .agg(pl.len().alias("count"))
            .sort("count", descending=True)
        )
        print(f"\n{col.upper()}:\n{value_counts_df}")
    except Exception as e:
        print(f"Could not summarize {col}: {e}")

# 3. UNIQUE VALUE COUNTS
print("\n--- UNIQUE VALUE COUNTS ---")
for col in categorical_cols:
    try:
        unique_count = df.select(pl.col(col).n_unique())
        print(f"{col}: {unique_count[0, 0]} unique values")
    except Exception as e:
        print(f"Could not count unique values for {col}: {e}")

# 4. GROUP BY SUMMARY
print("\n--- GROUP BY SUMMARY (Page Category) ---")
try:
    grouped = df.group_by("Page Category").agg(pl.len().alias("count"))
    print(grouped)
except Exception as e:
    print(f"Could not group by Page Category: {e}")
