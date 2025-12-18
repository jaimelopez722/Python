# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA" : "Washington D.C.",
            "India" : "New Delhi",
            "China" : "Beijing",
            "Russia" : "Moscow"}


# print(capitals.get("USA")) # checks to see if key is in collection

# if capitals.get("USA"):
#     print("That capital exists!")
# else:
#     print("That capital does not exist")

# capitals.update({"Germany" : "Berlin"})
# capitals.update({"USA" : "Los Angeles"})
# capitals.pop("China")
# print(capitals.keys())
#
# for key in capitals.keys():
#     print(key)
# print()
# print(capitals.values())
# for value in capitals.values():
#     print(value)
# print()
#
# items = capitals.items()
for keys, values in capitals.items():
    print(f"{keys} : {values}")




# print(help(capitals))