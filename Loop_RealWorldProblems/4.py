'''
Mini Project 4: Shopping Cart Total
'''
count = int(input("Enter number of products: "))

if count <= 0:
    print("Error: Number of products must be greater than 0")
else:
    subtotal = 0

    for i in range(1, count + 1):
        print(f"\n--- Product {i} ---")
        price = float(input("Enter price: Rs. "))
        while price < 0:
            print("Price cannot be negative. Try again.")
            price = float(input("Enter price: Rs. "))

        quantity = int(input("Enter quantity: "))
        while quantity < 0:
            print("Quantity cannot be negative. Try again.")
            quantity = int(input("Enter quantity: "))

        item_total = price * quantity
        print("Item subtotal: Rs.", item_total)
        subtotal += item_total

    # 10% discount when subtotal is Rs. 3000 or more
    if subtotal >= 3000:
        discount = subtotal * 10 / 100
    else:
        discount = 0

    after_discount = subtotal - discount

    # Delivery charge depends on the discounted amount
    if after_discount < 1500:
        delivery = 100
    else:
        delivery = 0

    final_amount = after_discount + delivery

    print("\n----- BILL SUMMARY -----")
    print("Subtotal         : Rs.", subtotal)
    print("Discount         : Rs.", discount)
    print("Delivery Charge  : Rs.", delivery)
    print("Final Payable    : Rs.", final_amount)
