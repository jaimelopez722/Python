for_sale = True
response = input("Would you like food? (Y/N): ").upper()
name = input("Enter your name: ")

if response == "Y":
    print("Have some food!")
else:
    print("No food for you")


if name == "":
    print("You did not type in your name!!!!!!!!!!!")
else:
    print(f"Hello {name}!")

if for_sale:
    print("This item is for sale")
else:
    print("This item is not for sale")