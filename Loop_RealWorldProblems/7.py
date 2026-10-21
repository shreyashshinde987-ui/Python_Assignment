'''
Mini Project 7: Employee Payroll Summary
'''
count = int(input("Enter number of employees: "))

if count <= 0:
    print("Error: Number of employees must be greater than 0")
else:
    total_net = 0

    for i in range(1, count + 1):
        print(f"\n--- Employee {i} ---")
        name = input("Enter employee name: ")

        basic = float(input("Enter basic salary: Rs. "))
        while basic < 0:
            print("Salary cannot be negative. Try again.")
            basic = float(input("Enter basic salary: Rs. "))

        overtime_hours = float(input("Enter overtime hours: "))
        while overtime_hours < 0:
            print("Overtime hours cannot be negative. Try again.")
            overtime_hours = float(input("Enter overtime hours: "))

        overtime_pay = overtime_hours * 200
        gross = basic + overtime_pay

        if gross >= 50000:
            deduction = gross * 10 / 100
        else:
            deduction = gross * 5 / 100

        net = gross - deduction
        total_net += net

        print("\n", name)
        print("  Gross Salary :", gross)
        print("  Deduction    :", deduction)
        print("  Net Salary   :", net)

    print("\n----- PAYROLL SUMMARY -----")
    print("Employee Count    :", count)
    print("Total Net Payroll : Rs.", total_net)
