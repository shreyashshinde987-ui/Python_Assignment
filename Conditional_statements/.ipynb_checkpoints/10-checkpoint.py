'''
10. Write a program to check whether a number is a single-digit number or not
'''
num= int(input("Enter number= "))
if num<10 and num>-10:
    print("Number is single-digit")
else:
    print("Number is double-digit")