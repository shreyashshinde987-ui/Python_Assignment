'''
6. Write a program to compare two numbers and print the greater one.
'''
num1= int(input("Enter number 1= "))
num2= int(input("Enter number 2= "))

if num1 >  num2:
	print(f"{num1} is greater than {num2}")
elif num2 > num1:
	print(f"{num2} is greater than {num1}")
else:
	print("Both are equal")