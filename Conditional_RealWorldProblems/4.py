'''
Mini Project 4: Student Scholarship Eligibility
'''
name = input("Enter student name: ")
percentage = float(input("Enter percentage: "))
income = float(input("Enter annual family income: "))
attendance = float(input("Enter attendance percentage: "))

if percentage < 0 or percentage > 100 or attendance < 0 or attendance > 100 or income < 0:
    print("Error: Invalid input values")
else:
    marks_ok = percentage >= 75
    income_ok = income <= 400000
    attendance_ok = attendance >= 75

    print("\n----- SCHOLARSHIP RESULT -----")
    print("Student Name :", name)

    if marks_ok and income_ok and attendance_ok:
        print("Eligibility  : Eligible")
        if percentage >= 90:
            print("Category     : Full Scholarship")
        else:
            print("Category     : Partial Scholarship")
    else:
        print("Eligibility  : Not Eligible")
        print("Category     : Not Eligible")
        print("Reason(s)    :")
        if not marks_ok:
            print("  - Percentage is below 75%")
        if not income_ok:
            print("  - Annual family income is above Rs. 4,00,000")
        if not attendance_ok:
            print("  - Attendance is below 75%")
