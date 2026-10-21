'''
Mini Project 6: Hotel Room Booking System
'''
name = input("Enter guest name: ")
room_type = input("Enter room type (Standard/Deluxe/Suite): ").strip().lower()
nights = int(input("Enter number of nights: "))

if nights <= 0:
    print("Error: Number of nights must be greater than 0")
else:
    if room_type == "standard":
        rate = 2000
    elif room_type == "deluxe":
        rate = 3500
    elif room_type == "suite":
        rate = 6000
    else:
        rate = 0

    if rate == 0:
        print("Error: Invalid room type")
    else:
        room_charge = rate * nights

        if nights >= 10:
            discount_percent = 20
        elif nights >= 5:
            discount_percent = 10
        else:
            discount_percent = 0

        discount = room_charge * discount_percent / 100
        final_amount = room_charge - discount

        print("\n----- HOTEL BOOKING -----")
        print("Guest Name      :", name)
        print("Room Type       :", room_type.capitalize())
        print("Number of Nights:", nights)
        print("Room Charge     : Rs.", room_charge)
        print("Discount        : Rs.", discount, f"({discount_percent}%)")
        print("Final Amount    : Rs.", final_amount)
