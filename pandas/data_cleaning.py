from cProfile import label

import pandas as pd

# Data cleaning = the process of fixing/removing:
#                 incomplete, incorrect, or irrelevant data.
#                 ~ 75% of work done with Pandas is data cleaning

df = pd.read_csv("data.csv", index_col = "No")

# 1. Drop irrelevant columns
# df = df.drop(columns = ["Legendary", "No"]) # reassign to new dataframe

# 2. Handle missing data
# df = df.dropna(subset = ["Type2"])  # this drops any ROWS that are missing any values ("NaN")
# df = df.fillna({"Type2" : "None"})    # Fills any ("NaN") rows with new value of ("None") only for column key

# 3. Fix inconsistent values
# df["Type1"] = df["Type1"].replace({"Grass": "GRASS", "Water" : "WATER", "Fire" : "FIRE"})

# 4. Standardize text
# df["Name"] = df["Name"].str.lower()

# 5. Fix data types
# df["Legendary"] = df["Legendary"].astype(bool)      # this took numeric values of 0/1 to a bool data type True/False

# 6. Remove duplicate values
df = df.drop_duplicates()


print(df.to_string())