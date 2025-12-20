import random

# print(help(random))

# number = random.randint(1,6) # 1 - 6 to represent a dice
low = 1
high = 100
options = ("rock", "paper", "scissors")

# number = random.randint(low, high)
option = random.choice(options)

print(option)