# Set = { } unordered and immutable, but Add/Remove OK. No duplicates

fruits = {"apple","banana","coconut","apple","orange"}
fruits.add("mango")
fruits.pop()    # removes first element in the collection, but randomly

print(fruits)