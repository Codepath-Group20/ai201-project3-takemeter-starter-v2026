import csv

# Open the sixty-five comments CSV file in read mode
with open("data/sixty-five_comments.csv", mode="r", encoding="utf-8") as f:
    rows = list(csv.reader(f))

# Extract the header and data rows
header = rows[0]
data_rows = rows[1:]

# Append a new column name to the header
header.append("notes")

# Loop through each row and pad it with an extra value for the new column
for i, row in enumerate(data_rows, start=1):
    if i <= 20:
        row.append(f"Batch A check (Row {i})")
    else:
        row.append(f"Batch B verification (Row {i})")

# Write the updated header and rows back to the CSV file
with open("data/sixty-five_comments.csv", mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data_rows)

print("Successfully added a new column to sixty-five_comments.csv!")
