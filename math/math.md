    friends = 11

#### addition
    friends = friends + 1
    friends += 1 # augmented

#### subtraction
    friends = friends - 2
    friends -= 2

#### multiplication
    friends = friends * 3
    friends *= 3

#### division
    friends = friends / 2
    friends /= 2

####  exponential
    friends = friends ** 2
    friends **= 2

#### modulus = remainder of any division
    remainder = friends % 2
    
    print(friends)
    print(remainder)

-----------------------------------------------------------------------

    x = 3.14
    y = 4
    z = 5

    # rounds to nearest whole number
    # result = round(x)

    # prints out absolute value
    # result = abs(y)

    # prints out y to the power of 4
    # result = pow(y,4)

    # prints the max from the list
    # result = max(x, y, z)

    # prints the min from the list
    # result = min(x, y, z)
    
    print(result)

--------------------------------------------------------------------------

## Circumference of a circle

```python
    import math
    
    radius = float(input("Enter the radius of a circle: "))
    
    circumference = 2 * math.pi * radius
    
    print(f"The circumference of the circle with radius: {radius} is {circumference:.1f}")
```
## Area of a circle

```python
    import math
    
    radius = float(input("Enter the radius of a circle: "))
    
    area = math.pi * pow(radius,2)
    
    print(f"The area of the circle with radius: {radius} is {area:.2f}cm²")
```

## Find hypotenuse of a right triangle

```python
    import math
    
    a = float(input("Enter side A: "))
    b = float(input("Enter side B: "))
    
    c = math.sqrt(pow(a,2) + pow(b,2))
    
    print(f"The length of side C is {c} cm")
```