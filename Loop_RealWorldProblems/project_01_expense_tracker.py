'''
Mini Project 1: Daily Expense Tracker
'''
days = int(input("Enter number of days: "))

if days <= 0:
    print("Error: Number of days must be greater than 0")
else:
    total = 0
    highest = 0

    for day in range(1, days + 1):
        expense = float(input(f"Enter expense for day {day}: Rs. "))

        # Re-ask until a valid (non-negative) expense is entered
        while expense < 0:
            print("Expense cannot be negative. Try again.")
            expense = float(input(f"Enter expense for day {day}: Rs. "))

        total += expense
        if expense > highest:
            highest = expense

    average = total / days

    if total > 5000:
        status = "Budget Alert"
    else:
        status = "Within Budget"

    print("\n----- EXPENSE SUMMARY -----")
    print("Total Expense          : Rs.", total)
    print("Average Daily Expense  : Rs.", round(average, 2))
    print("Highest Daily Expense  : Rs.", highest)
    print("Budget Status          :", status)
