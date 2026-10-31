# 07-introduction.py
# Activity: Personal Introduction Program

first_name = "D"  # str, string literal
last_name = "Guy"  # str, string literal
full_name = first_name + " " + last_name  # str, concatenated (added) strings
full_name = first_name, last_name  # str, smart concatenation
full_name = f"{first_name} {last_name}"  # str, f-string literal

age = 21  # int

height = 73.5  # float

human = False  # bool

description = "I am THE D-Guy"  # str, string literal

# Option 1: Addition (concatenation) with type casting
print("My name is " + full_name + " and I am " + str(age) + " years old. I am " + str(height) + " inches tall. Am I a human? " + str(human) + " About me: " + description)
# Option 2: Commas (concatenation with spaces), print handles the casting for us
print("My name is", full_name, "and I am", age, "years old. I am", height, "inches tall. Am I a human?", human, "About me:", description)
# Option 3: f-string (formatting) literal
print(f"My name is {full_name} and I am {age} years old. I am {height} inches tall. Am I a human? {human} About me: {description}")

# Bonus option: multiline f-string literal
print(f"""Introduction program!
Name  : {full_name}
Age   : {age}
height: {height}in
human : {human}
desc  : {description}""")
