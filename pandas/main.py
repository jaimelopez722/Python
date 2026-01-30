import pandas as pd

# Series = A Pandas one-dimensional labeled array that can hold any data type
#          Think of it like a single column in a spreadsheet (1-dimensional)

data = [100, 102, 104, 200, 202]

series = pd.Series(data, index = ['a', 'b', 'c', 'd', 'e']) # index gives labels to rows

# series.loc['c'] = 200   # manipulate data

# print(series.loc['a'])  # returns value at label 'a'

# print(series.loc['c'])

# print(series.iloc[0]) #prints value at position

# print(help(series))

print(series[series >= 200]) # 

