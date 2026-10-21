'''
Mini Project 5: Employee Performance Bonus
'''
name = input("Enter employee name: ")
salary = float(input("Enter monthly salary: "))
experience = float(input("Enter years of experience: "))
rating = int(input("Enter performance rating (1-5): "))

if rating < 1 or rating > 5:
    print("Error: Rating must be between 1 and 5")
elif salary <= 0 or experience < 0:
    print("Error: Salary must be positive and experience cannot be negative")
else:
    if experience >= 10 and rating >= 4:
        bonus_percent = 20
    elif experience >= 5 and rating >= 4:
        bonus_percent = 15
    elif experience >= 2 and rating >= 3:
        bonus_percent = 10
    else:
        bonus_percent = 0   # includes rating below 3

    bonus_amount = salary * bonus_percent / 100
    final_salary = salary + bonus_amount

    if rating == 5:
        message = "Excellent Performer"
    elif rating == 4:
        message = "Very Good Performance"
    elif rating == 3:
        message = "Satisfactory Performance"
    else:
        message = "Needs Improvement"

    print("\n----- BONUS REPORT -----")
    print("Employee Name    :", name)
    print("Bonus Percentage :", bonus_percent, "%")
    print("Bonus Amount     : Rs.", bonus_amount)
    print("Final Salary     : Rs.", final_salary)
    print("Performance      :", message)
