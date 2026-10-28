import csv

with open("data/labels.csv", mode="r", encoding="utf-8") as f:
    rows = list(csv.reader(f))

header = rows[0]
data_rows = rows[1:]

for i, row in enumerate(data_rows, start=1):
    if i <= 20:
        row[2] = f"Cold label check (Row {i})"
    else:
        row[2] = f"AI-assisted verification (Row {i})"

with open("data/labels.csv", mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data_rows)

print("Successfully updated data/labels.csv notes!")
