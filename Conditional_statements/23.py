'''
23. Write a program to calculate electricity bill based on units consumed.
'''

units = int(input("Enter electricity units consumed: "))
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7
elif units <= 300:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10
else:
    bill = (100 * 5) + (100 * 7) + (100 * 10) + (units - 300) * 15

print("Total Electricity Bill: ₹", bill)
