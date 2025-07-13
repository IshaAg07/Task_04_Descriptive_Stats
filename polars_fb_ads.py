import polars as pl

# Load the dataset
file_path = "2024_fb_ads_president_scored_anon.csv"
df = pl.read_csv(file_path)

# SCHEMA
print("SCHEMA:")
print(df.schema)

# NUMERIC SUMMARY
numeric_cols = [col for col, dtype in df.schema.items() if dtype in [pl.Int64, pl.Float64]]
if numeric_cols:
    print("\n NUMERIC SUMMARY:")
    print(df.select(numeric_cols).describe())
else:
    print("No numeric columns found for summary.")

# NULL VALUE COUNTS
print("\n NULL VALUE COUNTS:")
nulls = df.select([pl.col(col).is_null().sum().alias(col) for col in df.columns])
print(nulls)

# TOP 10 VALUES FOR SELECTED CATEGORICAL FIELDS
def print_top_10(df, col):
    print(f"\n TOP 10 VALUES IN '{col}':")
    print(
        df.group_by(col)
          .agg(pl.len().alias("count"))
          .sort("count", descending=True)
          .head(10)
    )

for col in ["page_id", "currency", "publisher_platforms", "bylines"]:
    if col in df.columns:
        print_top_10(df, col)

# SPEND BUCKETS
if "estimated_spend" in df.columns:
    df = df.with_columns(
        pl.when(pl.col("estimated_spend") < 100).then(pl.lit("<$100"))
        .when((pl.col("estimated_spend") >= 100) & (pl.col("estimated_spend") < 1000)).then(pl.lit("$100–$999"))
        .when((pl.col("estimated_spend") >= 1000) & (pl.col("estimated_spend") < 10000)).then(pl.lit("$1K–$9.9K"))
        .when(pl.col("estimated_spend") >= 10000).then(pl.lit("≥$10K"))
        .otherwise(pl.lit("Unknown"))
        .alias("spend_bucket")
    )

    print("\n SPEND BUCKET DISTRIBUTION:")
    print(
        df.group_by("spend_bucket")
          .agg(pl.len().alias("count"))
          .sort("count", descending=True)
    )
else:
    print("Column 'estimated_spend' not found.")
