# 01-variables.py
# Variables

# === Overview ===
# In some languages variables can be declares separately from their creation or "assignment"
# In python, a variables is created the moment you assign a value to it.

# variables start with the name of the variable, followed by an equals sign for assignment
# they can generally be named whatever, but have a few restrictions we won't cover right now
variable = "value"

# In other languages, you may need to declare a type for a variable.
# While Python still has types, you do not need to specify them, as they are inferred.

# When a variable is used, it is as if you placed a value directly in that position, but it can be modified or reused as well!
print(variable)  # Prints the value stored within variable
# note this is not the same as:
print("variable")  # Prints the string "variable"

# Also, note that variables are case sensitive:
a = 0
A = 1
print(a == A)  # False

# === Styling ===
# When writing variables, you want them to be concise but understandable
# There are many approaches to styling, but generally for Python variables, we use snake_case
snake_case = "This is a multi-word variable using snake case"

# === Resources ===
# Intro to Python Variables - https://www.w3schools.com/python/python_variables.asp
# Python Naming Conventions - https://pythonguides.com/python-naming-conventions/
