import pandas as pd

df = pd.read_csv("data.csv")

# Filtering = Keeping the rows that match a condition

# Create a program where the program will only return rows where Height > 2.0m
#tall_pokemon = df[df["Height"] >= 2].to_string()
#heavy_pokemon = df[df["Weight"] >= 100].to_string()
#is_legendary = df[df["Legendary"] == 1].to_string()
# same as line above
#is_legendary = df[df["Legendary"] == True].to_string()

# Or operator
#water_pokemon = df[(df["Type1"] == "Water") | (df["Type2"] == "Water")]

# And operator
ff_pokemon = df[(df["Type1"] == "Water") & (df["Type2"] == "Flying")]


#print(tall_pokemon)
#print(heavy_pokemon)
#print(is_legendary)
print(ff_pokemon)
