import csv
import pandas as pd

valid_rows = []
extra_column_rows = []
invalid_rows = []

# Expected header
final_header = ["Name", "Title", "Company", "Youtube URL"]

with open("input.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)  # skip header

    for row in reader:
        # 1️⃣ Rows with more than 4 columns
        if len(row) > 4:
            extra_column_rows.append(row)
            continue

        # 2️⃣ Rows with less than 4 columns
        if len(row) < 4:
            invalid_rows.append(row)
            continue

        name, title, company, youtube = [x.strip() for x in row]

        # 3️⃣ Invalid placeholders
        if (
            name in ["", "—", "-","–"]
            or title in ["", "—", "-","–","(Title not stated)"]
            or company in ["", "—", "-","–"]
        ):
            invalid_rows.append(row)
            continue

        # 4️⃣ Clean row → keep
        valid_rows.append(row)

# -----------------------------
# Save outputs
# -----------------------------

pd.DataFrame(extra_column_rows).to_csv(
    "rows_with_extra_columns.csv",
    index=False,
    header=False
)

pd.DataFrame(invalid_rows, columns=final_header[:len(invalid_rows[0])] if invalid_rows else None)\
  .to_csv("invalid_rows.csv", index=False)

pd.DataFrame(valid_rows, columns=final_header)\
  .to_csv("final_clean_dataset.csv", index=False)

print(" Strict cleanup completed")
print("Generated files:")
print("- rows_with_extra_columns.csv  (rows with >3 commas)")
print("- invalid_rows.csv             (— / empty fields)")
print("- final_clean_dataset.csv      (ONLY clean rows)")
