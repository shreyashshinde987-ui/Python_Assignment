'''
Mini Project 8: Movie Ticket Booking
'''
name = input("Enter customer name: ")
age = int(input("Enter age: "))
show = input("Enter show type (Morning/Evening): ").strip().lower()
day = input("Enter day type (Weekday/Weekend): ").strip().lower()

if age < 0:
    print("Error: Age cannot be negative")
elif show != "morning" and show != "evening":
    print("Error: Show type must be Morning or Evening")
elif day != "weekday" and day != "weekend":
    print("Error: Day type must be Weekday or Weekend")
else:
    base_price = 200
    discount = 0

    # Age based discount
    if age < 12:
        discount = discount + base_price * 50 / 100
    elif age >= 60:
        discount = discount + base_price * 30 / 100

    # Morning show extra discount
    if show == "morning":
        discount = discount + 30

    # Weekend surcharge
    if day == "weekend":
        surcharge = 50
    else:
        surcharge = 0

    final_price = base_price - discount + surcharge

    print("\n----- MOVIE TICKET -----")
    print("Customer Name      :", name)
    print("Original Price     : Rs.", base_price)
    print("Discount           : Rs.", discount)
    print("Weekend Surcharge  : Rs.", surcharge)
    print("Final Ticket Price : Rs.", final_price)
