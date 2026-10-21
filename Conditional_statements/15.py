'''
15. Write a program to check whether a number is divisible by both 3 and 7 or not.
'''
num= int(input("Enter number= "))
if num%3==0 and num%7==0:
    print(f"{num} is divisible by both 3 and 7")
else:
    print(f"{num} is not divisible by both number 3 and 7")    