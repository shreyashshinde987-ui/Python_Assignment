'''
33. Write a program to check whether a person can apply for a loan.
'''
age = int(input("Enter your age: "))
salary = float(input("Enter your monthly salary: "))

if age >= 21 and salary >= 25000:
    print("Eligible to apply for a loan")
else:
    print("Not eligible to apply for a loan")