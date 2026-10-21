'''
4. Write a program to check whether a number is greater than 100 or not.
'''
num= int(input("Enter number= "))
if num > 100:
	print(f"{num} is greater than 100")
elif num == 100:
	print(f"{num} is equal to 100")
else:
	print(f"{num} is less than 100")