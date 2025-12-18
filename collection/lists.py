# collection = single "variable" used to store multiple values
#   List = [] ordered and changeable. Duplicates OK
#   Set = {} unordered and immutable, but Add/Remove OK. No duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. Faster

fruits = ["apple","orange","banana","apple"]
# fruits[0] = "pineapple"
fruits.append("Kiwi")
fruits.remove("apple")
fruits.insert(2,"mango")
fruits.sort()
fruits.reverse()

for fruit in fruits:
     print(fruit)

# print(help(fruits))
