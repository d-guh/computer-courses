# 02-strings.py
# Data Types: Strings

# === Basics ===
name = "D-Guy"
print(name)
# Remember, print("name") is not the same!

print("Hello " + name)  # Note that the spaces outside of quotes do not get added!

print(type(name))  # <class 'str'>

# Single and double quotes are equivalent in python
print("hi" == 'hi')  # True

# === Combining Strings ===
first_name = "D"
last_name = "Guy"
full_name = first_name + " " + last_name

print("Hello", full_name)  # Note this `,` behaves differently than adding!

# === Immutability and Other Languages ===
# Strings are immutable in Python, which means they cannot be modified. This has a few performance and security benefits.
# For example, in other languages you would be able to edit the third letter in a string by doing the following:
test = "test"
#test[2] = 'm'  # This will error!
# However, you can still re-assign the string altogether:
test = "temt"
print(test)

# === Resources ===
# Intro to Python Strings - https://www.w3schools.com/python/python_strings.asp
