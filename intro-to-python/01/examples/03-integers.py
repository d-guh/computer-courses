# 03-integers.py
# Data Types: Integers

# === Basics ===
age = 21
age += 1  # += updates AND assigns, same as age = age + 1
# Note some langs have the ++ (increment) operator, Python does NOT
print(age)
print(type(age))  # <class 'int'>

# You cannot perform integer operations on a str!
age_str = "21"
#age_str += 1  # Error!
print(age_str)

# === Combining Integers ===
total = 6 + 7
print(total)

# === Combining Integer and Strings ===
# You cannot combine str and int!
#print("I'm D-Guy and I'm " + age + " years old!")  # Error!
# We can fix this with type casting!
print("I'm D-Guy and I'm " + str(age) + " years old!")

# === Mutability and Other Languages ===
# Unlike strings, integers are mutable, which means they can be updated. (they can still also be re-assigned completely)
# We won't cover allocation/memory management of these numbers at this moment, but it is much more important in other languages like C or Rust
# Other languages use set sizes for integers, like i32 (32-bit signed integer). Python just has the type int for all.

# === Resources ===
# Intro to Python Numbers - https://www.w3schools.com/python/python_numbers.asp
