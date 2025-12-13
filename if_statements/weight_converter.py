# Python weight converter
import math

weight = float(input("Enter your weight: "))
unit = input("Kilogram or Pounds? (k or l): ")

if unit == 'k':
    conversion = weight * 2.205
    print(f"You are {weight} kgs and in pounds that is {round(conversion,2)} lbs")
elif unit == 'l':
    conversion = weight / 2.205
    print(f"You are {weight} lbs and in kilograms that is {round(conversion,2)} kgs")
else:
    print("You entered wrong unit")
