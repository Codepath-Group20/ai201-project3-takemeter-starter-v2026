import pandas as pd

# 1. Load the labels list safely from your hyphenated file
local_vars = {}
with open("comments-list.py", "r") as f:
    exec(f.read(), local_vars)

labels_50 = local_vars["labels_50"]

# 2. Read your fifty samples CSV file
df = pd.read_csv("data/fifty_sample.csv")

# 3. Verify that the row count matches your 50 labels
if len(df) != len(labels_50):
    raise ValueError(f"Length mismatch: CSV has {len(df)} rows, but comments-list.py has {len(labels_50)} labels.")

# 4. Replace the old label column with your new category labels
df["label"] = labels_50

# 5. Save the updated dataset back to CSV
df.to_csv("data/fifty_sample.csv", index=False)
print("Successfully replaced all labels in data/fifty_sample.csv!")
print(df["label"].value_counts())
