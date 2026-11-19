# 02-strings.py
# String operations, indexing/slicing, and string methods

print("=== Strings ===")

# === Recap/Overview ===
print("\n=== Recap/Overview ===")
# Strings store a series of characters, and they are IMMUTABLE
# Strings are defined with single or double quotes, and can be multiline
'single quote string'
"double quote string"
'''
multiline
single quote string
'''

# Strings can be combined and manipulated with certain operators
print("hello" + " " + "world")
print("guh??" * 5)

# === Indexing and Slicing ===
print("\n=== Indexing and Slicing ===")
# Strings are indexed sequences, which means you can access a part of a string using index notation
# Positive indices start at 0 and count up
# Negative indices start at -1 and count down
my_string = "I am a very cool string!"
print(my_string[0])   # I
print(my_string[1])   #  
print(my_string[10])  # y
print(my_string[-1])  # !
print()
# Slicing lets you take a range of indices in the format start:end, where end is exclusive
print(my_string[0:4])   # I am
print(my_string[5:11])  # a very
print(my_string[17:-1]) # string

# === Functions/Methods ===
print("\n=== Functions/Methods ===")
# There are many functions/methods for manipulating strings!
# len() gets the length of the current string
my_string = "   Wasting  Space   "
print(my_string)
print(len(my_string))  # function, not specific to strings but useful for getting the length of an object/container
print(my_string.strip())  # method
print(my_string.upper())  # method
print(my_string.lower())  # method
# You can even combine them!
print(my_string.strip().lower())  # chained methods, evaluated left to right (or inner to outer)

# === Escape Characters ===
print("\n=== Escape Characters ===")
# Escape characters are how you get python to represent special characters that are not normally typeable or would break syntax
# Remember that print automatically appends a newline '\n' by default!
print("hi1\nhi2")  # newline, moves the cursor to the next line
print("hi1\thi2")  # tab, adds a horizontal tab (NOT always 4 spaces!)
print("hi1\\hi2")  # backslash
print("hi1\'hi2")  # single quote
print("hi1\"hi2")  # double quote
print("hi1\rhi2")  # carriage return, moves cursor to start of line
print("hi1\bhi2")  # backspace
print("\x67")      # hexadecimal, in this case within a string, auto converted to ASCII text, 0x67 = 103 = g
print("\x48\x65\x6C\x6C\x6F")  # hexadecimal ASCII "Hello"

# BONUS: ANSI codes! 
# https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797
# https://gist.github.com/JBlond/2fea43a3049b38287e5e9cefc87b2124
# Used for cursor manipulation, color (when supported), and more!
# Begins with the escape sequence: \x1B
print("\x1b[1;32mI'm so green...")
print("guh??")
print("\x1b[1;39mI'm normal again!")
# Note that these are not specific to python, but your TERMINAL

# === Formatted Strings / f-strings ===
print("\n=== Formatted Strings / f-strings ===")
# THE GOAT
# f-strings let you use variables/expressions/statements directly within the string
# much easier to edit, read, and understand
# simply a normal string but prefixed with f
name = "D-Guy"
print(f"My name is {name}, 6 + 7 = {6 + 7}")

# Originally, the format() function was used, and f-strings do the same but simpler.
# For example, if you wanted to print 2 decimal places ($6.00 for example), you can do so with the use of format specifiers:
price = 6

print("f-string   ->", f"{price:.2f}")  # Modern standard
print("format()   ->", format(price, ".2f"))  # OG method
print("% operator ->", "%.2f" % price)  # Nobody does this lol

# === Resources ===
# https://www.geeksforgeeks.org/python/python-string/
# https://docs.python.org/3/library/string.html
# https://www.w3schools.com/python/python_ref_string.asp
# https://www.geeksforgeeks.org/python/python-escape-characters/
