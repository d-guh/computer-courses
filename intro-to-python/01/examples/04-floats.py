# 04-floats.py
# Data Types: Floats

# === Basics ===
height = 73.5
print(height)
print(type(height))  # <class 'float'>

# === Combining Floats ===
# Float math is... weird
# Computers kinda suck at it
# For example:
total = 0.1 + 0.2
print(total)  # Should be 0.3 right?

# You can use rounding:
print(round(total, 2))

# In general, precise calculations should be done using integers, or fixed precision decimal numbers

# === Combining Floats and Strings ===
# This is pretty similar to integers
# You cannot combine str and float!
#print("I'm D-Guy and I'm " + height + "in tall!")  # Error!
# We can fix this with type casting!
print("I'm D-Guy and I'm " + str(height) + "in tall!")

# === Resources ===
# Intro to Python Numbers - https://www.w3schools.com/python/python_numbers.asp
# Floating Point Error in Python - https://www.geeksforgeeks.org/python/floating-point-error-in-python/
# Floating Point Arithmetic - https://en.wikipedia.org/wiki/Floating-point_arithmetic
# Floating Point Errors - https://en.wikipedia.org/wiki/Floating-point_error_mitigation
