# 05-invoice.py
# Invoice generator program

INPUT_VALIDATION = True

if INPUT_VALIDATION:
    print("=== Invoice Generator (WITH VALIDATION) ===")
    while True:
        title = input("Invoice Title: ")
        if title == '':
            print("Please supply a title.")
        else:
            break

    while True:
        item_name = input("Item Name: ")
        if item_name != '':
            break
        print("Please supply an item name.")

    while True:
        try:
            item_count = int(input("Item Count: "))
            break
        except ValueError:
            print("Item count must be a whole number!")

    while True:
        try:
            item_price = float(input("Item Price: "))
            break
        except ValueError:
            print("Item price must be a number!")

    total = item_count * item_price

    print(f"""
    === INVOICE: {title} ===
    {item_name}: ${item_price:.2f} x {item_count}ct
    TOTAL: ${total:.2f}
    """)

else:
    print("=== Invoice Generator (NO VALIDATION) ===")
    title = input("Invoice Title: ")
    item_name = input("Item Name: ")
    item_count = int(input("Item Count: "))
    item_price = float(input("Item Price: "))
    total = item_count * item_price

    print(f"""
    === INVOICE: {title} ===
    {item_name}: ${item_price:.2f} x {item_count}ct
    TOTAL: ${total:.2f}
    """)
