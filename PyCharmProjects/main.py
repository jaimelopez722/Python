import math

# 1. calculate circumference of a circle: C = 2*pi*radius
# 2. calculate the area of a circle: A = pi * r^2
# 3. Find hypotenuse of a right triangle: c = sqrt(a^2 + b^2)

# Asks user for diameter of circle
diameter = float(input("What is the diameter of the circle: "))
side1 = float(input("What is side1: "))
side2 = float(input("What is side2: "))

# Circumference calculation
radius = diameter/2
circumference = 2 * math.pi * radius

#area calculation
area = math.pi * pow(radius,2)

#hypotenuse calculation
hypotenuse = math.sqrt(pow(side1,2) + pow(side2, 2))

# Notifies user of calculation and rounds to 2 decimal places.
print(f"1. The circumference is {round(circumference, 2)} cm.")
print(f"2. The area of the circle is {round(area,2)} cm^2.")
print(f"3. The hypotenuse of the right triangle is {round(hypotenuse,2)} cm")
