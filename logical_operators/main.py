# logical operators = evaluate multiple conditions (or, and, not)
#                     or - at least one condition must be true
#                     and - both conditions must be true
#                     not - inverts the condition (not False, not True)

temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")

