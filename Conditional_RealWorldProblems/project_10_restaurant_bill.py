'''
Mini Project 10: Restaurant Bill and Service Charge
'''
name = input("Enter customer name: ")
bill = float(input("Enter food bill amount: "))
member = input("Membership (Yes/No): ").strip().lower()

if bill <= 0:
    print("Error: Bill amount must be greater than 0")
elif member != "yes" and member != "no":
    print("Error: Membership must be Yes or No")
else:
    # Discount percentage based on bill amount
    if bill >= 5000:
        discount_percent = 15
    elif bill >= 3000:
        discount_percent = 10
    elif bill >= 1000:
        discount_percent = 5
    else:
        discount_percent = 0

    # Additional member discount
    if member == "yes":
        discount_percent = discount_percent + 5

    discount = bill * discount_percent / 100
    after_discount = bill - discount

    # Service charge is 5% on the amount AFTER discount
    service_charge = after_discount * 5 / 100
    final_amount = after_discount + service_charge

    if final_amount >= 5000:
        message = "Thank you for being a valued customer"
    else:
        message = "Thank you for dining with us"

    print("\n----- RESTAURANT BILL -----")
    print("Customer Name    :", name)
    print("Original Bill    : Rs.", bill)
    print("Discount         : Rs.", round(discount, 2), f"({discount_percent}%)")
    print("Service Charge   : Rs.", round(service_charge, 2))
    print("Final Payable    : Rs.", round(final_amount, 2))
    print("Message          :", message)
