# List comprehension = A concise way to create lists in Python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

doubles = []

for x in range(1,11):
    doubles.append(x * 2)
print(doubles)

# vs.

twice = [x * 2 for x in range(1,11)] # [expression for value in iterable if condition].... less blocks of code

print()
print(twice)