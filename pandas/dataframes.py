import pandas as pd

# DataFrame = A tabular data structure with rows AND columns. (2 dimensional)
#             Similar to an Excel spreadsheet

data = {
    "Name" : ["Spongebob", "Patrick", "Squidward"],
    "Age" : [30, 35, 50]
} # 2-D dictionary (key = column, value = row)

df = pd.DataFrame(data, index = ['Employee 1', 'Employee 2', 'Employee 3'])

# Add a new column
df["Job"] = ["Cook", "N/A", "Cashier"]

# Add a new rows
new_rows = pd.DataFrame([{"Name" : "Sandy", "Age" : 28, "Job" : "Engineer"},
                             {"Name" : "Eugene", "Age" : 60, "Job" : "Manager"},],
                       index = ['Employee 4', 'Employee 5'])
df = pd.concat([df, new_rows])   #concatenation or add row to existing dataframe

# print(df.loc["Employee 1"]) # to access a single row
print(df)