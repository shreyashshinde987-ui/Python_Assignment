'''
47. Find product of digits of a number.
'''
num = abs(int(input("Enter a number: ")))

if num == 0:
    product = 0
else:
    product = 1
    while num > 0:
        product *= num % 10
        num //= 10

print("Product of digits:", product)
