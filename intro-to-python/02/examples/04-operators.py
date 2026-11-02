# 04-operators.py
# Operators
print("=== Operators ===")

# === Arithmetic Operators ===
print("\n=== Arithmetic Operators ===")
# Arithmetic operators are the core math operations
# They generally operate on numbers (integers and floats) but can also have some niche uses outside of this!
# Note the difference between division and floor division. 
a = 60
b = 7

print("Addition:", a + b)         # 60 + 7  = 67
print("Subtraction:", a - b)      # 60 - 7  = 53
print("Multiplication:", a * b)   # 60 * 7  = 420
print("Division:", a / b)         # 60 / 7  = 8.571428571428571
print("Floor Division:", a // b)  # 60 // 7 = 8
print("Modulus:", a % b)          # 60 % 7  = 4
print("Exponentiation:", a ** b)  # 60 ^ 7  = 2799360000000

# === Relational "Comparison" Operators ===
print("\n=== Relational \"Comparison\" Operators ===")
# Relational (or comparison) operators compare values. They either return True or False based on the condition
a = 60
b = 7

print(a > b)   # 60 > 7  = True
print(a < b)   # 60 < 7  = False
print(a == b)  # 60 == 7 = False
print(a != b)  # 60 != 7 = True
print(a >= b)  # 60 >= 7 = True
print(a <= b)  # 60 <= 7 = False

# === Logical "Boolean" Operators ===
print("\n=== Logical \"Boolean\" Operators ===")
# Logical (or Boolean) operators perform logical operations. They are used to combine conditional statements (flow control).
a = True
b = False

print(a and b)  # True and False = False
print(a or b)   # True or False  = True
print(not a)    # not True       = False

# === Bitwise "Binary" Operators ===
print("\n=== Bitwise \"Binary\" Operators ===")
# Bitwise (or Binary) operators perform bit-by-bit (bitwise) operations. They are used to operate on binary numbers or edit memory directly etc.
a = 10
b = 3

print(a & b)  # 00001010 & 00000011 = 00000010 (2)
print(a | b)  # 00001010 | 00000011 = 00001011 (11)
print(~a)     # ~00001010           = 11110101 (-11)* note this is tricky due to how negative integers are handled, we will not cover this for now.
print(a ^ b)  # 00001010 ^ 00000011 = 00001001 (9)
print(a << 2) # 00001010 << 2       = 00101000 (40)*
print(a >> 2) # 00001010 >> 2       = 00000010 (2)*  note shifts can occasionally be more complicated while handling negative integers, we will not cover that for now.

# Note: computers are actually pretty bad at multiplication! They follow the old school rule of adding something many times, with a few exceptions.
# If a number is multiplied by a power of two, you can simply bitshift, making excellent use of binary numbers, and is very fast/efficient
# If it's not, you can either do the addition method, or use a neat trick.
# Break down the multiplication problem into its factors, and find the powers of two, perform that operation, and then addition the rest of the way (saves a lot!)
# For example: 10*35
# Rather than doing: 10+10+10+10...(35 times in total)
# The computer does: 10 << 5 (since 2^5=32) and then adds the remaining amount +10+10+10 (equivalent to 35 times in total, but with only 4 operations made!)
# This is the binary (base 2) equivalent of only computing the important parts on paper (base 10) that you may have learned!

# === Assignment Operators ===
print("\n=== Assignment Operators ===")
# Assignment operators are used to assign values to variables. The value of the right is assigned to the left.

a = 10
b = a     # Regular assignment
print(b)  # 10 = 10
b += a    # Additive assignment (same as b = b + a)
print(b)  # 20 = 10 + 10
b -= a    # Subtractive assignment (same as b = b - a)
print(b)  # 10 = 20 - 10
b *= a    # Multiplicative assignment (same as b = b * a)
print(b)  # 100 = 10 * 10
b <<= a   # Left shift assignment (same as b = b << a)
print(b)  # 102400 = 100 << 10

# === Identity Operators ===
print("\n=== Identity Operators ===")
# Identity operators check if two values are located in the same spot in memory (i.e. identical). Note this is NOT the same as checking if two values are EQUAL
a = 10
b = 20
c = a

print(a is c)      # 10 is 10     = True*
print(a is not b)  # 10 is not 20 = True*
# note that the values here are irrelevant, what matters is if are the objects (in memory) are THE SAME
# since c is assigned from a and it points to the same low value in this case, it is identical
# also note that integers in python may share the same object in memory (as an optimization)
# Don't worry if you don't understand this for now, it will make more sense once we get into objects
a = [1, 2]
b = [1, 2]
print(a == b)  # 1 == 1, 2 == 2 = True
print(a is b)  # a is b         = False
# note that in this case, even though the values are EQUAL, the objects are not IDENTICAL

# === Membership Operators ===
print("\n=== Membership Operators ===")
# Membership operators test whether a value or variable is present in a sequence/object.
a = 24
b = 20
my_list = [10, 20, 30, 40, 50]

print(a in my_list)      # 24 in [10, 20, 30, 40, 50]     = False
print(a not in my_list)  # 24 not in [10, 20, 30, 40, 50] = True
print(b in my_list)      # 20 in [10, 20, 30, 40, 50]     = True
print(b not in my_list)  # 20 not in [10, 20, 30, 40, 50] = False

# === Ternary Operator ===
print("\n=== Ternary Operator ===")
# Ternary operators as essentially an if/else statement squished onto one line. They evaluate something based on a condition being true or false.
# note they kind of read like english
a, b = 10, 20
min = a if a < b else b

print(min)  # 10

# === Order of Operations ===
print("\n=== Order of Operations ===")
# The order of operations determines the order in which operators are evaluated (in expressions with more than one operator).
# Note this is more or less the same as math order of operations
# == Operator Precedence ==
print("== Operator Precedence ==")
# Operator precedence is used in expressions with more than one operator, when the operators have different precedence.
expr = 10 + 20 * 30
print(expr)
name = "Alex"
age = 0

if name == "Alex" or name == "John" and age >= 2:
    print("Hello! Welcome.")
else:
    print("Good Bye!!")

# == Operator Associativity ==
print("== Operator Associativity ==")
# Operator associativity is used in expressions with more than one operator, when the operators have the same precedence.
# Generally this is left to right, or right to left, but the order would have no impact on the result.
print(100 / 10 * 10)
print(5 - 2 + 3)
print(5 - (2 + 3))
print(2 ** 3 ** 2)

# === Resources ===
# https://www.geeksforgeeks.org/python/python-operators/
# https://www.geeksforgeeks.org/python/python-arithmetic-operators/
# https://www.geeksforgeeks.org/python/python-object-comparison-is-vs/
# https://www.geeksforgeeks.org/python/python-logical-operators/
# https://www.geeksforgeeks.org/python/python-bitwise-operators/
# https://www.geeksforgeeks.org/python/assignment-operators-in-python/
# https://www.geeksforgeeks.org/python/python-membership-identity-operators-not-not/
# https://www.geeksforgeeks.org/python/ternary-operator-in-python/
# https://www.geeksforgeeks.org/python/precedence-and-associativity-of-operators-in-python/
