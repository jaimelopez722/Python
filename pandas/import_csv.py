import pandas as pd

df = pd.read_csv("data.csv", index_col= "Name")

# print(df) # prints 1st 5 rows, and last 5 rows
# print(df.to_string()) # prints entire list

# Selection by Column
# print(df["Name"])
# print(df[["Height", "Weight"]].to_string()) # multiple column selections, YOU MUST PASS IN A LIST

# Selection by Row/s

#print(df.loc["Pikachu"])

#if I only want certain criteria, pass in a list
#print(df.loc["Pikachu", ["Height", "Weight"]])

# Slicing
# print(df.loc["Charizard": "Blastoise", ["Height", "Weight"]])

# Slicing by integer location, second argument is like slicing above but must pass in indices
print(df.iloc[0 : 11, 3 : 5])