import csv
import math
from collections import defaultdict, Counter

file_path = "2024_fb_ads_president_scored_anon.csv"

numeric_cols = ["estimated_audience_size", "estimated_impressions", "estimated_spend"]
categorical_cols = [
    "page_id", "ad_id", "currency", "publisher_platforms",
    "advocacy_msg_type_illuminating", "attack_msg_type_illuminating"
]

# Initialize storage
data = {col: [] for col in numeric_cols}
cat_data = {col: [] for col in categorical_cols}
group_page_id = defaultdict(int)
group_page_ad = defaultdict(int)

# Read data
with open(file_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Numeric stats
        for col in numeric_cols:
            val = row.get(col, "").strip()
            if val:
                try:
                    data[col].append(float(val))
                except:
                    pass

        # Categorical stats
        for col in categorical_cols:
            val = row.get(col, "").strip()
            if val:
                cat_data[col].append(val)

        # Grouping
        page = row.get("page_id", "").strip()
        ad = row.get("ad_id", "").strip()
        if page:
            group_page_id[page] += 1
        if page and ad:
            group_page_ad[(page, ad)] += 1

# Summary Functions
def summarize_numeric(col, values):
    count = len(values)
    mean = sum(values) / count if count else 0
    min_val = min(values) if values else None
    max_val = max(values) if values else None
    std = math.sqrt(sum((x - mean) ** 2 for x in values) / count) if count else 0
    print(f"\nColumn: {col}")
    print(f"Count: {count}")
    print(f"Mean: {mean:.2f}")
    print(f"Min: {min_val}")
    print(f"Max: {max_val}")
    print(f"Std Dev: {std:.2f}")

def summarize_categorical(col, values):
    freq = Counter(values)
    most_common = freq.most_common(1)
    print(f"\nColumn: {col}")
    print(f"Unique Values: {len(freq)}")
    print(f"Most Frequent: {most_common}")

# Print summaries
print("--- NUMERIC SUMMARY ---")
for col in numeric_cols:
    summarize_numeric(col, data[col])

print("\n--- CATEGORICAL SUMMARY ---")
for col in categorical_cols:
    summarize_categorical(col, cat_data[col])

print(f"\nTotal groups by page_id: {len(group_page_id)}")
print(f"Total groups by (page_id, ad_id): {len(group_page_ad)}")
