'''
31. Write a program to check whether a number is positive and even using nested if.
'''
num= int(input("Enter number= "))
if num > 0:
    if num%2==0:
        print("Number is both positive and even")
    else:
        print("Number is positive but not an even number")
else:
    print("Number is not positive and even")