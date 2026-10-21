'''
22. Write a program to check salary bonus based on years of service.
'''
e_years= int(input("Enter year of service= "))
if e_years >= 5:
    print("Your Salary bonus is 10000")
elif e_years >= 2 and e_years < 5:
    print("Your salary bonus is 5000")
else:
    print("Your salary bonus is 1000")