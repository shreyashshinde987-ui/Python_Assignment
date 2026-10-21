'''
Mini Project 2: Online Shopping Checkout
'''
name = input("Enter customer name: ")
amount = float(input("Enter purchase amount: "))
cust_type = input("Enter customer type (Regular/Premium): ").strip().lower()

if amount <= 0:
    print("Error: Purchase amount must be greater than 0")
elif cust_type != "regular" and cust_type != "premium":
    print("Error: Customer type must be Regular or Premium")
else:
    # Discount percentage based on purchase amount
    if amount >= 5000:
        discount_percent = 20
    elif amount >= 3000 and amount < 5000:
        discount_percent = 10
    elif amount >= 1000 and amount < 3000:
        discount_percent = 5
    else:
        discount_percent = 0

    # Additional benefit for premium customers
    if cust_type == "premium":
        discount_percent = discount_percent + 5

    discount_amount = amount * discount_percent / 100
    amount_after_discount = amount - discount_amount

    # Delivery charge
    if amount_after_discount >= 2000:
        delivery_charge = 0
    else:
        delivery_charge = 100

    final_amount = amount_after_discount + delivery_charge

    print("\n----- CHECKOUT SUMMARY -----")
    print("Customer Name    :", name)
    print("Customer Type    :", cust_type.capitalize())
    print("Purchase Amount  : Rs.", amount)
    print("Discount Amount  : Rs.", round(discount_amount, 2), f"({discount_percent}%)")
    print("Delivery Charge  : Rs.", delivery_charge)
    print("Final Payable    : Rs.", round(final_amount, 2))
