'''
5. Write a program to check whether a given year is a leap year or not.
'''
year= int(input("Enter year= "))
if year%4==0:
	print(f"{year} Year is leap")
else:
	print(f"{year} Year is Not a leap")  