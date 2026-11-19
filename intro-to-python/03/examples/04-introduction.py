# 04-introduction.py
# User Introduction v2!

print("=== User introduction program v2 ===\n")

while True:
    first_name = input("What is your first name?: ")

    # Validation Method 1 (equals/empty)
    if first_name == "":
        print("Please provide a first name.")
    else:
        break

while True:
    last_name = input("What is your last name?: ")

    # Validation Method 2 (not equals/empty)
    if last_name != "":
        break
    print("Please provide a last name.")

while True:
    try:
        age = int(input("How old are you?: "))

        if 0 < age <= 120:
            break
        else:
            print("Your age must be between 1 and 120!")
    except ValueError:
        print("Input must be a number!")

while True:
    is_robot = input("Are you a robot? (y/n): ").lower()

    if is_robot.startswith('y'):
        is_robot = True
        break
    elif is_robot.startswith('n'):
        is_robot = False
        break
    else:
        print("Please input y[es] or n[o]")

bio = input("Input your bio/description: ")

print(f"""
=== Your Introduction ===
Name : {first_name} {last_name}
Age  : {age}
Robot: {is_robot}
Bio  : {bio}
""")
