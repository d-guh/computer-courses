# 00-print.py
# The print() function
# We've been using print for a while now, but let's actually take an in depth look
import sys

# === Syntax ===
# The print() syntax is as follows:
# print(*objects, sep=' ', end='\n', file=None, flush=False)
# Note that *objects are positional arguments that accept one or more values to print
# sep, end, file, and flush are other parameters that have default values, so you may not normally see them
print("Default")  # Default print behavior, prints string and appends newline
print("No newline", end='')  # Prints string and adds nothing (stays on same line)
print("Hi", "Hello", "guh?", sep='')  # Prints string without the space separator between arguments
# all of these options can be very useful for handling loops and lists etc.

# === Output Streams ===
# The OS has 2 main output streams:
# Standard Output (stdout, fd 1)
# Standard Error (stderr, fd 2)
# Imported via sys, print lets you specify a stream to print to!
print("Standard output message!")
print("Standard error message!", file=sys.stderr)

# === Low(er) Level ===
sys.stdout.write("LARP")  # this is roughly equivalent to using print(), as it writes the data directly to stdout.

# === Resources ===
# https://www.geeksforgeeks.org/python/python-print-function/
# LINUX/BASH: https://www.geeksforgeeks.org/linux-unix/input-output-redirection-in-linux/
# POWERSHELL: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_redirection?view=powershell-7.6
