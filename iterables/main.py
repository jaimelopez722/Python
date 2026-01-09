# iterables = an object/collection that can return its elements one at a time, allowing it to be iterated over in a loop

numbers = [1,2,3,4,5,6]
my_dictionary = {"A":1, "B":2, "C":3}

for number in numbers:
    print(number)

print()

for key in my_dictionary: # this only gives the key of the dictionary
    print(key)

print()

for value in my_dictionary.values(): # this only prints the value. Must use .value()
    print(value)

print()

for key, value in my_dictionary.items(): # to print both key and value
    print(f"{key} : {value}")