# Concession stand program

# dictionary {key:value}

menu = {"Pizza" : 3.00,
        "Nachos" : 4.50,
        "Popcorn" : 6.00,
        "Fries" : 2.50,
        "Chips" : 1.00,
        "Pretzel" : 3.50,
        "Soda" : 3.00,
        "Lemonade" : 4.25}

cart = []
total = 0

print("-------MENU-------")
for key, value in menu.items():
    print(f"{key:10} : ${value:.2f}")
print("------------------")
print()
while True:
    food = input("Select an item (q to quit): ")
    if food.lower() == 'q':
        break
    elif menu.get(food) is not None:
        cart.append()