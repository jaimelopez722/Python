# format specifiers = {value:flags} format a value based on what flags are inserted

price1 = 3000.141945
price2 = -9870.65
price3 = 1200.34

# .(number)f = round to that many decimal places (fixed point)
print(f"Price 1 is ${price1:.2f}")
print(f"Price 2 is ${price2:.2f}")
print(f"Price 3 is ${price3:.2f}")

# :(number) = allocate that many spaces
print(f"Price 1 is ${price1:10}")
print(f"Price 2 is ${price2:10}")
print(f"Price 3 is ${price3:10}")

# :03 = allocate and zero pad that many spaces
print(f"Price 1 is ${price1:010}")
print(f"Price 2 is ${price2:010}")
print(f"Price 3 is ${price3:010}")

# :< = left justify
print(f"Price 1 is ${price1:<10}")
print(f"Price 2 is ${price2:<10}")
print(f"Price 3 is ${price3:<10}")

# :> = right justify
print(f"Price 1 is ${price1:>20}")
print(f"Price 2 is ${price2:>20}")
print(f"Price 3 is ${price3:>20}")

# :^ = center align
print(f"Price 1 is ${price1:^20}")
print(f"Price 2 is ${price2:^20}")
print(f"Price 3 is ${price3:^20}")

# :+ = use a plus sign to indicate positive value
print(f"Price 1 is ${price1:+}")
print(f"Price 2 is ${price2:+}")
print(f"Price 3 is ${price3:+}")

# := = place sign to leftmost position
print(f"Price 1 is ${price1:=}")
print(f"Price 2 is ${price2:=}")
print(f"Price 3 is ${price3:=}")

# :  = insert a space before positive numbers
print(f"Price 1 is ${price1: }")
print(f"Price 2 is ${price2: }")
print(f"Price 3 is ${price3: }")

# :, = comma separator
print(f"Price 1 is ${price1:,}")
print(f"Price 2 is ${price2:,}")
print(f"Price 3 is ${price3:,}")










