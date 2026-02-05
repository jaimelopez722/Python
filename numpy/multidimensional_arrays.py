import numpy as np

# array = np.array('A') 0 - dimensional array

# array = np.array(['A', 'B', 'C']) # 1 - dimensional array

# array = np.array([['A', 'B', 'C'],
#                  ['D', 'E', 'F'],
#                  ['G', 'H', 'I']]) # 2 - dimensional array; also referred to as a matrix

array = np.array([[['A', 'B', 'C'],['D', 'E', 'F'], ['G', 'H', 'I']],
                  [['J', 'K', 'L'],['M', 'N', 'O'], ['P', 'Q', 'R']],
                  [['S', 'T', 'U'],['V', 'W', 'X'], ['Y', 'Z', '_']]])

# print(array.ndim)   # ndim tells us dimensions of our array

word = array[0][0][0] + array[2][0][0] + array[2][0][0]
print(word)

