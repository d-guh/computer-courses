# 02-type-casting-conversion.py
# Type Casting/Conversion

# Type casting is the act of converting a variable's data type into a certain other type to perform a required operation.

# === Implicit Conversion ===
# Implicit type conversion is what Python does automatically for us.
# For example:
a = 7
print(type(a))
print(a)  # still works!

# === Explicit Conversion ===
# Explicit type conversion is what we do by manually specifying a type, also known as "Type Casting"
a = 5
n = float(a)
print(type(n))
print(n)

# Float to Int example
a = 5.9
n = int(a)

print(type(n))
print(n)

# Int to String example
a = 5
n = str(a)

print(type(n))
print(n)

# Note that this has to be compatible to be converted/cast
# String to Int example
a = "5"
b = "t"
n = int(a)

print(n)
print(type(n))

#print(int(b))  # This errors since "t" cannot be converted to an integer!
print(type(b))

# === Resources ===
# https://www.geeksforgeeks.org/python/type-casting-in-python/
