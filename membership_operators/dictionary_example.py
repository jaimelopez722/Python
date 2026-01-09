grades = {"Sandy" : "A",
          "Squidward" : "B",
          "Spongebob" : "C",
          "Patrick" : "D"}

student = input("Enter the name of a student: ").capitalize()

if student in grades:
    print(f"{student}'s grade is a {grades[student]}")
else:
    print(f"{student} not found")