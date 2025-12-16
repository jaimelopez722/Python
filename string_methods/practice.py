# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter a username: ")

if len(username) < 12 and username.find(" ") and username.isalpha():
    print("Good Job!")
else:
    print("Pick another username")