# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end(exclusive: not including) : step]

credit_number = "1234-5678-9012-4567"
last_digits = credit_number[-4::]

print(credit_number[4])
print(credit_number[0:4])
print(credit_number[5:9])
print(credit_number[0::2])
print(last_digits)