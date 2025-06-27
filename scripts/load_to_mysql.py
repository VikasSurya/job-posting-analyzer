import pandas as pd
import os

# 🧹 Optional: Remove old file
try:
    os.remove("../data/cleaned_jobs_data.csv")
except:
    pass

# Step 1: Load raw data
df = pd.read_csv("../data/raw_jobs_data.csv")
print("🔍 Raw rows before cleaning:", len(df))

# Step 2: Drop duplicates (title + company)
df.drop_duplicates(subset=['title', 'company'], inplace=True)

# Step 3: Ensure skills column is string
df['skills'] = df['skills'].astype(str)

# Step 4: Drop rows where skills is blank
df = df[df['skills'].str.strip() != '']

# Optional: Drop if title or company missing
df.dropna(subset=['title', 'company'], inplace=True)

# Final: Reset index
df.reset_index(drop=True, inplace=True)

# Save cleaned data
df.to_csv("../data/cleaned_jobs_data.csv", index=False)
print("✅ Cleaned CSV saved as: data/cleaned_jobs_data.csv")
print("🧮 Final cleaned rows:", len(df))
