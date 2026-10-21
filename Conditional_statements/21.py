'''
21. Write a program to find the smallest of three numbers.
'''
num1= int(input("Enter number 1= "))
num2= int(input("Enter number 2= "))
num3= int(input("Enter number 3= "))
if num2 > num1 < num3:
    print(f"{num1} is Smallest")
elif num1 > num2 < num3:
    print(f"{num2} is Smallest")
else:
    print(f"{num3} is Smallest")        