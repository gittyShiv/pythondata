import pandas as pd

# -----------------------------
# Load cleaned dataset
# -----------------------------
df = pd.read_csv("final_clean_dataset.csv")

print("Initial clean rows:", len(df))

# -----------------------------
# 1️⃣ Same Company + Same Title
# -----------------------------
same_company_title = (
    df.groupby(["Company", "Title"])
      .filter(lambda x: len(x) > 1)
)

same_company_title.to_csv(
    "same_company_same_title.csv", index=False
)

# Remove from main df
df = df.drop(same_company_title.index)

print("After removing same company + title:", len(df))

# -----------------------------
# Helper: first & last name
# -----------------------------
def split_name(name):
    parts = name.strip().split()
    if len(parts) == 1:
        return parts[0].lower(), ""
    return parts[0].lower(), parts[-1].lower()

df["first_name"], df["last_name"] = zip(*df["Name"].apply(split_name))

# -----------------------------
# 2️⃣ Same first OR same last name
# -----------------------------
same_first_or_last = df[
    df.duplicated(subset=["first_name"], keep=False)
    | df.duplicated(subset=["last_name"], keep=False)
]

same_first_or_last.to_csv(
    "same_first_or_last_name.csv", index=False
)

# Remove from main df
df = df.drop(same_first_or_last.index)

# -----------------------------
# Final dataset
# -----------------------------
df = df.drop(columns=["first_name", "last_name"])
df.to_csv("final_after_duplicates.csv", index=False)

# -----------------------------
# Logs
# -----------------------------
print("✅ Duplicate cleanup completed")
print("Generated files:")
print("- same_company_same_title.csv")
print("- same_first_or_last_name.csv")
print("- final_after_duplicates.csv")
print("Final rows:", len(df))

