# 01-naming-conventions.py
# Naming Conventions

# Naming conventions are not a concept unique to Python, as different languages use different rules.
# Utilize PEP8 for full python style guidelines

# variables use snake_case as shown below:
variable_name = "i am a string!"
# function names use snake_case too, but the standard library functions tend to stay one word
print(variable_name)

def my_function():
    pass

# Class names use PascalCase
class MyClass:
    pass

# Constant variables (constants) use SCREAMING_SNAKE_CASE (snake_case but all caps)
CONSTANT_VARIABLE = "i am a constant string!"
# Constants in python don't hold any special properties, but generally should not be changed

# Dunder refers to "double underscore" __
# certain functions/constructs use this, and it is reserved. 
# One example is "dunder main"
if __name__ == "__main__":
    print("I am main!")

# __name__ represents the name of the environment where the code is run
# __name__ will be __main__ if you are in the "top-level code environment", i.e. running the script directly
# This is used to signify that a script is meant to be run directly, and also control what is run!
# There are more dunder expressions but they will be covered later

# === Resources ===
# https://pythonguides.com/python-naming-conventions/
