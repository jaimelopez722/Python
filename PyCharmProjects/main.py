# Python calculator

# asks user for operation to perform
operator = input("Enter an operator (+ - * /) : ")

# asks user for 2 numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


# goes through logic of what user chose
if operator == '+':
    result = num1 + num2
    print(round(result,2))
elif operator == '-':
    result = num1 - num2
    print(abs(result))
elif operator == '*':
    result = num1 * num2
    print(round(result,2))
elif operator == '/':
    result = num1 / num2
    print(round(result,2))
else:
    print(f"{operator} is not a correct operator.")
