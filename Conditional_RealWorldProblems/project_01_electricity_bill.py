'''
Mini Project 1: Smart Electricity Bill Calculator
'''
name = input("Enter customer name: ")
units = int(input("Enter units consumed: "))

if units < 0:
    print("Error: Units consumed cannot be negative")
else:
    # Slab-wise energy charge
    if units <= 100:
        energy_charge = units * 3
    elif units <= 200:
        energy_charge = (100 * 3) + (units - 100) * 5
    else:
        energy_charge = (100 * 3) + (100 * 5) + (units - 200) * 7

    service_charge = 150
    final_bill = energy_charge + service_charge

    if final_bill > 5000:
        message = "High Usage Bill"
    else:
        message = "Normal Usage Bill"

    print("\n----- ELECTRICITY BILL -----")
    print("Customer Name   :", name)
    print("Units Consumed  :", units)
    print("Energy Charge   : Rs.", energy_charge)
    print("Service Charge  : Rs.", service_charge)
    print("Final Bill      : Rs.", final_bill)
    print("Usage Message   :", message)
