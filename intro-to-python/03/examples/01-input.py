# 01-input.py
# The input() function
# input() is like the opposite of print, rather than outputting, it reads input!
import sys

# === Reading Input ===
# To read input, simply create a variable to store the input into, and optionally provide a message:
val = input("Prompt message: ")
print(val)

# === Casting Input ===
# Let's say you want the user to input a number
# The info they enter is always treated as a string, but we can cast it!
number = input("Enter a number: ")
number = int(number)
print(f"{number} + {7} = {number + 7}")
# or more concisely:
number = int(input("Enter a number: "))
print(f"{number} + {7} = {number + 7}")

# === The Input Stream ===
# The OS has an input stream too!
# Standard Input (stdin, fd 0)
# Imported via sys, lets you interact with the input stream directly!

# === Low(er) Level ===
print("Type something: ", end='', flush=True)  # note we needed to flush here so that our message shows up before readline() blocks!
val2 = sys.stdin.readline()  # note this can break your terminal a bit, the reason print and input are used is to perform proper clean-up and niceties!
print(val2)

# === Resources ===
# https://www.geeksforgeeks.org/python/taking-input-in-python/
# LINUX/BASH: https://www.geeksforgeeks.org/linux-unix/input-output-redirection-in-linux/
# POWERSHELL: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_redirection?view=powershell-7.6
