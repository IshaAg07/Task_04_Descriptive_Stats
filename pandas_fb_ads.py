
import sys
import pandas as pd
import textwrap as tw

CSV = sys.argv[1] if len(sys.argv) > 1 else "2024_fb_ads_president_scored_anon.csv"


# 1) LOAD

df = pd.read_csv(
    CSV,
    low_memory=False,            # let pandas infer dtypes first
    dtype_backend="pyarrow"      # lighter memory + nullable dtypes
)

print("\n SCHEMA:")
schema = {c: str(df.dtypes[c]) for c in df.columns}
print(schema)


# 2) NUMERIC SUMMARY

numeric_cols = df.select_dtypes("number").columns
print("\n NUMERIC SUMMARY:")
print(df[numeric_cols].describe().T)      # .T ⇒ rows = columns, cols = stats


# 3) NULL COUNTS

print("\n NULL VALUE COUNTS:")
print(df.isna().sum().to_frame("nulls").T)


# 4) CATEGORICAL VALUE COUNTS

cat_cols = [
    "page_id",
    "currency",
    "publisher_platforms",
    "bylines"
]

for col in cat_cols:
    print(f"\n TOP 10 VALUES IN '{col}':")
    vc = (
        df[col]
        .value_counts(dropna=False)   # keep NaNs separate
        .head(10)
        .reset_index(name="count")
        .rename(columns={"index": col})
    )
    print(vc)


# 5) SIMPLE BUCKETING EXAMPLE

bins  = [-1,  99,    999,  9_999, df["estimated_spend"].max()]
labels = ["<$100", "$100–$999", "$1K–$9.9K", "≥$10K"]
df["spend_bucket"] = pd.cut(df["estimated_spend"], bins=bins, labels=labels)

print("\n SPEND BUCKET DISTRIBUTION:")
print(df["spend_bucket"].value_counts().to_frame("count"))


# 6) (OPTIONAL) GROUP-BY EXAMPLE

group_count = df.groupby("page_id", observed=True).size().reset_index(name="ads_per_page")
print("\n NUMBER OF ADS PER PAGE_ID  (first 5 rows):")
print(group_count.head())

# friendly footer
print(
    tw.dedent("""
    ------------------------------------------------------------------
    ✔ Descriptive statistics complete (pandas version).
    ------------------------------------------------------------------
    """)
)
