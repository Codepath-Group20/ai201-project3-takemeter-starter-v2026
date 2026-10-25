import csv

# Read and strip extra columns beyond text and label
cleaned_rows = []
with open("data/sixty-five_comments.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) >= 2:
            # Keep only the first two columns (text and label)
            cleaned_rows.append([row[0].strip(), row[1].strip()])

# Write back cleanly
with open("data/sixty-five_comments.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(cleaned_rows)

print("sixty-five_comments.csv successfully normalized to 2 columns!")
