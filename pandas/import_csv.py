import pandas as pd

df = pd.read_csv("data.csv", index_col= "Name")

# print(df) # prints 1st 5 rows, and last 5 rows
# print(df.to_string()) # prints entire list

# Selection by Column
# print(df["Name"])
print(df[["Height", "Weight"]].to_string()) # multiple column selections, YOU MUST PASS IN A LIST

# Selection by Row/s
# print(df.loc["Pikachu"])