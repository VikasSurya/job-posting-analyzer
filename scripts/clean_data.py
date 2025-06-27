import pandas as pd
import os

# 🧹 Step 0: Delete old cleaned CSV if exists
try:
    os.remove("../data/cleaned_jobs_data.csv")
except:
    pass

# Step 1: Load raw data
df = pd.read_csv("../data/raw_jobs_data.csv")
print("🔍 Raw rows before cleaning:", len(df))

# Step 2: Drop duplicates
df.drop_duplicates(subset=['title', 'company'], inplace=True)

# ✅ Step 3: Make sure skills is string (even if NaN)
df['skills'] = df['skills'].fillna('').astype(str)

# Step 4: Drop rows where skills is empty
df = df[df['skills'].str.strip() != '']

# Optional: Drop if title/company/date missing
df.dropna(subset=['title', 'company', 'date_posted'], inplace=True)

# Step 5: Reset index
df.reset_index(drop=True, inplace=True)

# Step 6: Save cleaned data
df.to_csv("../data/cleaned_jobs_data.csv", index=False)
print("✅ Cleaned CSV saved as: data/cleaned_jobs_data.csv")
print("🧮 Final cleaned rows:", len(df))
