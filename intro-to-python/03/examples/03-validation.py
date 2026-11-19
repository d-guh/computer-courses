# 03-validation.py
# Validating Input
# Validating input is important because you never know what the user will input!
# Some may be typos, some may be actively malicious!

# What could happen WITHOUT proper validation:
num = int(input("Enter a number: "))
# if a user enters a non-number, the program will crash!
num += 1
print(f"Your new number is: {num}")

# WITH proper validation:
while True:
    try:
        num = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid Input!")
num += 1
print(f"Your new number is: {num}")

# Another example for a specific range
while True:
    try:
        age = int(input("Enter your age: "))

        if 0 < age < 120:
            break
        else:
            print("Your age must be between 0 and 120!")
    except ValueError:
        print("Invalid Input!")
print(f"You are {age} years old!")

if age > 18:
    print("LMAO UNC!!!!!")

# We will cover this more once we get into flow, loops, and more!

# === Resources ===
# https://www.geeksforgeeks.org/python/input-validation-in-python/
