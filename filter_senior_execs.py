import pandas as pd

# -----------------------------
# Load dataset
# -----------------------------
df = pd.read_csv("final_after_duplicates.csv")
print("Initial rows:", len(df))

# -----------------------------
# Keywords
# -----------------------------
senior_keywords = [
    "chief",
    "ceo", "coo", "cfo", "cto", "cmo", "cio", "cro",
    "president",
    "founder", "co-founder",
    "svp", "senior vice president",
    "evp", "executive vice president"
]

# Explicit exclusions
excluded_keywords = [
    "director",
    "leader"
]

def is_senior_exec(title):
    title = str(title).lower()

    # Remove if any excluded keyword appears
    if any(word in title for word in excluded_keywords):
        return False

    # Keep only if senior keyword appears
    return any(word in title for word in senior_keywords)

# -----------------------------
# Apply filter
# -----------------------------
senior_df = df[df["Title"].apply(is_senior_exec)]
removed_df = df[~df["Title"].apply(is_senior_exec)]

# -----------------------------
# Save outputs
# -----------------------------
senior_df.to_csv("final_senior_execs.csv", index=False)
removed_df.to_csv("removed_non_senior_execs.csv", index=False)

# -----------------------------
# Logs
# -----------------------------
print("Senior execs kept:", len(senior_df))
print("Removed non-senior execs:", len(removed_df))
print("✅ Senior exec filtering (Director removed) completed")

