# logical operators = evaluate multiple conditions (or, and, not)
#                or = at least one condition must be True
#               and = both conditions must be True
#               not = inverts the condition (not False, not True)

temp = 40
is_raining = False
is_sunny = True

if temp >= 30 and is_sunny:
    print("It is hot 🥵 and sunny ☀️")
else:
    print("It is cold 🥶 and sunny ☀️")