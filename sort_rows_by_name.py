import pandas as pd
import os

csv_files = [
    "final_clean_dataset.csv",
    "same_company_same_title.csv",
    "same_first_or_last_name.csv",
    "final_after_duplicates.csv",
    "invalid_rows.csv"
]

for file in csv_files:
    if not os.path.exists(file):
        print(f"⏭️ File not found, skipping: {file}")
        continue

    df = pd.read_csv(file)

    if "Name" not in df.columns:
        print(f"⏭️ No Name column, skipping: {file}")
        continue

    # Sort lexicographically by Name (case-insensitive)
    df = df.sort_values(by="Name", key=lambda x: x.str.lower())

    df.to_csv(file, index=False)
    print(f"✅ Sorted rows in: {file}")

print("\n🎉 All datasets sorted lexicographically by Name")
