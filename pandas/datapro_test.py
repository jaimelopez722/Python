import pandas as pd

df = pd.read_csv("2026_01_30 14_44_Event Number 01_UNF.csv")

# Convert columns to numeric (header rows become NaN)
df["time"] = pd.to_numeric(df["Headers"], errors="coerce")
df["value"] = pd.to_numeric(df["Unnamed: 1"], errors="coerce")

# Keep only real data rows
data = df.dropna(subset=["time", "value"])

min_val = data["value"].min()
max_val = data["value"].max()
avg_val = data["value"].mean()
std_val = data["value"].std()

print(min_val, max_val, avg_val, std_val)
