# 03-expressions-statements.py
# Expressions vs Statements

# === Expressions ===
# Every expression is a statement (sometimes called "expression statements")
# Expressions are anything that can evaluate to a value
# You could, in theory, replace all expressions with their resulting values, and it would work.

# === Statements ===
# Everything in Python is a statement
# Not every statement is an expression
# Literally every line of code

x = 42  # statement
y = x + 8  # expression
print(y)  # statement

# you could, in theory, replace the expression with a statement below, and the result would be the same:
x = 42  # statement
y = 50  # statement
print(y)  # statement

# === Resources ===
# https://realpython.com/python-expression-vs-statement/
# https://docs.python.org/3/glossary.html#term-expression
# https://docs.python.org/3/glossary.html#term-statement
