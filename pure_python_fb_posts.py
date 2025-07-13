import csv
import statistics
from collections import defaultdict, Counter
import math

# Load dataset
FILE_PATH = '2024_fb_posts_president_scored_anon.csv'

# Columns to analyze
NUMERIC_COLUMNS = ['Likes', 'Comments', 'Shares']
CATEGORICAL_COLUMNS = ['Facebook_Id', 'post_id', 'Type']

# Containers
rows = []
with open(FILE_PATH, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        rows.append(row)

# NUMERIC SUMMARY 
print("\n--- NUMERIC SUMMARY ---\n")
for col in NUMERIC_COLUMNS:
    values = []
    for row in rows:
        val = row.get(col, "").replace(",", "").strip()
        if val:
            try:
                values.append(float(val))
            except ValueError:
                continue
    if values:
        print(f"Column: {col}")
        print(f"Count: {len(values)}")
        print(f"Mean: {round(statistics.mean(values), 2)}")
        print(f"Min: {min(values)}")
        print(f"Max: {max(values)}")
        print(f"Std Dev: {round(statistics.stdev(values), 2) if len(values) > 1 else 0.0}\n")
    else:
        print(f"Column {col} not found or contains no valid values.\n")

# CATEGORICAL SUMMARY 
print("--- CATEGORICAL SUMMARY ---\n")
for col in CATEGORICAL_COLUMNS:
    counter = Counter()
    for row in rows:
        val = row.get(col, "").strip()
        if val:
            counter[val] += 1
    if counter:
        print(f"Column: {col}")
        print(f"Unique Values: {len(counter)}")
        print(f"Most Frequent: {counter.most_common(1)}\n")
    else:
        print(f"Column {col} not found.\n")

# GROUP BY 
print("--- GROUP BY SUMMARY ---\n")
group_by_page_id = set()
group_by_page_post_id = set()
for row in rows:
    page = row.get("Facebook_Id", "").strip()
    post = row.get("post_id", "").strip()
    if page:
        group_by_page_id.add(page)
    if page and post:
        group_by_page_post_id.add((page, post))

print(f"Total groups by Facebook_Id: {len(group_by_page_id)}")
print(f"Total groups by (Facebook_Id, post_id): {len(group_by_page_post_id)}")
