# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                          Print or assign one of two values based on a condition
#                          syntax = return X if condition is true else return Y


#num = -5
# a = 9
# b = 15
user_role = "admin"


#print("Positive" if num > 0 else "Negative")
# max_num = a if a>b else b
# min_num = a if a<b else b
access_level = "Full Access" if user_role == "admin" else "Limited Access"

# print(max_num)
# print(min_num)
print(access_level)