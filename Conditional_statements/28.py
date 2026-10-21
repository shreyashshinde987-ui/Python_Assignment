'''
28. Write a program to calculate discounts based on total shopping amount.
'''
amount = float(input("Enter total shopping amount: "))

if amount >= 5000:
    discount = amount * 0.20
elif amount >= 3000:
    discount = amount * 0.15
elif amount >= 1000:
    discount = amount * 0.10
else:
    discount = 0

final_amount = amount - discount

print("Shopping Amount: ₹", amount)
print("Discount: ₹", discount)
print("Final Amount: ₹", final_amount)