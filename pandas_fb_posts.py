import pandas as pd

# Load the dataset
df = pd.read_csv("2024_fb_posts_president_scored_anon.csv")

# SCHEMA 
print("\n SCHEMA:")
print(df.dtypes)

#  NUMERIC SUMMARY 
print("\n NUMERIC SUMMARY:")
print(df.describe(include='number'))

# NULL VALUE COUNTS 
print("\n NULL VALUE COUNTS:")
print(df.isnull().sum())

# TOP 10 VALUES IN CATEGORICAL COLUMNS 
categorical_columns = ['Facebook_Id', 'Page Category', 'Page Admin Top Country', 'Type']
for col in categorical_columns:
    if col in df.columns:
        print(f"\n TOP 10 VALUES IN '{col}':")
        print(df[col].value_counts().head(10))

# DISTINCT COUNTS FOR CATEGORICAL FIELDS 
print("\n DISTINCT COUNTS FOR CATEGORICAL FIELDS:")
for col in categorical_columns:
    if col in df.columns:
        print(f"{col}: {df[col].nunique()} unique values")
