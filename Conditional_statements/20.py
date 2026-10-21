'''
20. Write a program to check ticket price based on age.
'''
age= int(input("Enter age= "))
if age > 18:
    print(f"{age} age is greater than 18 so price is 400")
else:
    print(f"{age} age is less than 18 so price is 200")