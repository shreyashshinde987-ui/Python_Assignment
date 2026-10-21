'''
22. Find sum of even digits in a number.
'''
num = abs(int(input("Enter a number: ")))

even_sum = 0

while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        even_sum += digit
    num //= 10

print("Sum of even digits:", even_sum)
