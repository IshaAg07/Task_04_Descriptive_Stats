#!/usr/bin/env python3
"""
pure_python_twitter.py
──────────────────────
Descriptive statistics for the Twitter dataset
(2024_tw_posts_president_scored_anon.csv) **without** Pandas/Polars.

What it prints
──────────────
1.  Numeric columns (likeCount, replyCount, …): count / mean / min / max / std-dev
2.  Categorical columns (source, derived Tweet_Type, …): unique count + top value
3.  Group summaries
      • by `source`  (≈ “Twitter handle / app”)
      • by (`source`, `id`)  – effectively unique rows
"""

import csv
import math
import statistics
from collections import Counter, defaultdict
from pathlib import Path

# helpers
NUMERIC_COLS = ["retweetCount", "replyCount", "likeCount",
                "quoteCount", "viewCount", "bookmarkCount"]

RAW_PATH = Path("2024_tw_posts_president_scored_anon.csv")

def is_number(x: str) -> bool:
    try:
        float(x)
        return True
    except ValueError:
        return False


def describe_numeric(values):
    v = [float(x) for x in values]
    return dict(
        count=len(v),
        mean=sum(v) / len(v) if v else 0,
        min=min(v) if v else 0,
        max=max(v) if v else 0,
        std=statistics.stdev(v) if len(v) > 1 else 0,
    )


def describe_categorical(values):
    cnt = Counter(values)
    top, freq = cnt.most_common(1)[0]
    return dict(unique=len(cnt), top=f"{top} ({freq})")


def print_block(title):
    print(f"\n--- {title} ---\n")


# load + light cleaning
with RAW_PATH.open(newline="", encoding="utf-8") as fh:
    reader = csv.DictReader(fh)
    rows = []

    for r in reader:
        # ▸ add friendly aliases expected by the spec
        r["Twitter_Handle"] = r["source"]            # e.g. “Twitter for iPhone”
        r["Tweet_Id"] = r["id"]

        # ▸ derive a simple “Tweet_Type”
        if r["isRetweet"] == "TRUE":
            r["Tweet_Type"] = "Retweet"
        elif r["isReply"] == "TRUE":
            r["Tweet_Type"] = "Reply"
        elif r["isQuote"] == "TRUE":
            r["Tweet_Type"] = "Quote"
        else:
            r["Tweet_Type"] = "Original"

        rows.append(r)

print_block("NUMERIC SUMMARY")
for col in NUMERIC_COLS:
    nums = [row[col] for row in rows if is_number(row[col])]
    stats = describe_numeric(nums)
    print(f"Column: {col}\n"
          f"Count: {stats['count']}\n"
          f"Mean: {stats['mean']:.2f}\n"
          f"Min: {stats['min']}\n"
          f"Max: {stats['max']}\n"
          f"Std Dev: {stats['std']:.2f}\n")

print_block("CATEGORICAL SUMMARY")
CAT_COLS = ["Twitter_Handle", "Tweet_Id", "Tweet_Type", "lang"]
for col in CAT_COLS:
    vals = [row[col] for row in rows if row[col]]
    stats = describe_categorical(vals)
    print(f"Column: {col}\n"
          f"Unique Values: {stats['unique']}\n"
          f"Most Frequent: {stats['top']}\n")

#  group summaries
print_block("GROUP BY SUMMARY")
by_handle = defaultdict(list)
by_handle_id = defaultdict(list)

for r in rows:
    by_handle[r["Twitter_Handle"]].append(r)
    by_handle_id[(r["Twitter_Handle"], r["Tweet_Id"])].append(r)

print(f"Total groups by Twitter_Handle: {len(by_handle)}")
print(f"Total groups by (Twitter_Handle, Tweet_Id): {len(by_handle_id)}")
