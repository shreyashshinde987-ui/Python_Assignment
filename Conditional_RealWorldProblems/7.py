'''
Mini Project 7: Mobile Data Plan Bill
'''
name = input("Enter customer name: ")
plan = input("Enter plan type (Basic/Standard/Premium): ").strip().lower()
extra_gb = float(input("Enter extra data used in GB: "))

if extra_gb < 0:
    print("Error: Data usage cannot be negative")
else:
    if plan == "basic":
        base_charge = 299
        included_gb = 10
    elif plan == "standard":
        base_charge = 499
        included_gb = 25
    elif plan == "premium":
        base_charge = 799
        included_gb = 50
    else:
        base_charge = 0
        included_gb = 0

    if base_charge == 0:
        print("Error: Invalid plan type")
    else:
        extra_charge = extra_gb * 20

        if extra_gb > 10:
            surcharge = 100
        else:
            surcharge = 0

        final_bill = base_charge + extra_charge + surcharge

        print("\n----- MOBILE DATA BILL -----")
        print("Customer Name      :", name)
        print("Plan Type          :", plan.capitalize(), f"({included_gb} GB included)")
        print("Base Plan Charge   : Rs.", base_charge)
        print("Extra Data Charge  : Rs.", extra_charge)
        print("Surcharge          : Rs.", surcharge)
        print("Final Bill         : Rs.", final_bill)
