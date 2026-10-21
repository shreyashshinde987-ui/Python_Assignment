'''
30. Write a program to check the type of number (single, double, or three digit).
'''
num = int(input("Enter a number: "))

if num >= -9 and num <= 9:
    print("Single-digit number")
elif num >= -99 and num <= 99:
    print("Double-digit number")
elif num >= -999 and num <= 999:
    print("Three-digit number")
else:
    print("More than three-digit number")