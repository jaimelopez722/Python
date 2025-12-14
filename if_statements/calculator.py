# Python calculator

operator = input("Enter an operator (+ - * /): ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} is {result}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} is {result}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} is {result}")
elif operator == "/":
    result = num2 / num1
    print(f"{num2} / {num1} is {result}")
else:
    print("You entered an invalid operator")