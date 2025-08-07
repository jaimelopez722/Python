# Python weight converter

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ").upper()

if unit == 'K':
    weight = round((weight * 2.205),2)
    unit = "Pounds"
    print(f"Your weight in {unit} is {weight}")
elif unit == 'L':
    unit = "Kilograms"
    weight = round((weight / 2.205),2)
    print(f"Your weight in {unit} is {weight}")
else:
    print("Please enter a valid unit.")

