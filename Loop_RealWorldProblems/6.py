'''
Mini Project 6: Electricity Usage Analyzer
'''
days = int(input("Enter number of days: "))

if days <= 0:
    print("Error: Number of days must be greater than 0")
else:
    total = 0
    high_days = 0
    maximum = 0

    for day in range(1, days + 1):
        units = float(input(f"Enter units consumed on day {day}: "))
        while units < 0:
            print("Units cannot be negative. Try again.")
            units = float(input(f"Enter units consumed on day {day}: "))

        total += units

        if units > 10:
            high_days += 1

        if units > maximum:
            maximum = units

    average = total / days

    if total > 300:
        status = "High Usage"
    else:
        status = "Normal Usage"

    print("\n----- USAGE REPORT -----")
    print("Total Units            :", total)
    print("Average Usage          :", round(average, 2))
    print("Days With > 10 Units   :", high_days)
    print("Maximum Daily Usage    :", maximum)
    print("Usage Status           :", status)
