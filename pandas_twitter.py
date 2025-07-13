import pandas as pd

# Load the dataset
df = pd.read_csv("2024_tw_posts_president_scored_anon.csv")

# Display schema (column names and types)
print("SCHEMA:")
print(df.dtypes)

# Summary of numeric columns
print("\n NUMERIC SUMMARY:")
print(df.describe(include='number'))

# Null value count
print("\n NULL VALUE COUNTS:")
print(df.isnull().sum())

# Top 10 values in selected categorical fields (if they exist)
categorical_cols = ["author_id", "tweet_type", "author_country", "lang"]
for col in categorical_cols:
    if col in df.columns:
        print(f"\nTOP 10 VALUES IN '{col}':")
        print(df[col].value_counts().head(10))

# Distinct count of selected categorical fields
print("\n DISTINCT COUNTS FOR CATEGORICAL FIELDS:")
for col in categorical_cols:
    if col in df.columns:
        print(f"{col}: {df[col].nunique()} unique values")
