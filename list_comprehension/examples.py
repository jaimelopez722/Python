numbers = [1, -2, 3, -4, 5, -6]

positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num % 2 == 0]

print("---Positive Numbers---")
print(positive_nums, end='\n\n')
print("---Negative Numbers---")
print(negative_nums,end='\n\n')
print("---Even Numbers---")
print(even_nums)