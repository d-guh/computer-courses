# 06-multi-assign.py
# Multiple Assignment

# name = "D-Guy"
# age = 21
# height = 73.5
# human = True

# Multiple assignment of different values
name, age, height, human = "D-Guy", 21, 73.5, True

#print(name + age + height + human)  # Error!
print(name + str(age) + str(height) + str(human))
print(name, age, height, human)

# a (usually) better way, f-strings! (format strings)
print(f"My name is {name} and i am {age}. I am {height}in tall. Am I human?: {human}")

# Multiple assignment of the same value
value1 = value2 = value3 = value4 = 42

# === Resources ===
# https://www.w3schools.com/python/python_variables_multiple.asp
