'''
36. Write a program to check whether a person is eligible for a driving license.
'''
age = int(input("Enter your age: "))
passed_test = input("Have you passed the driving test? (yes/no): ").lower()

if age >= 18 and passed_test == "yes":
    print("Eligible for a driving license")
elif age < 18:
    print("Not eligible: minimum age is 18")
else:
    print("Not eligible: you must pass the driving test")
