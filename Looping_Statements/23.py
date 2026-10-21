'''
23. Find sum of odd digits in a number.
'''
num = abs(int(input("Enter a number: ")))

odd_sum = 0

while num > 0:
    digit = num % 10
    if digit % 2 != 0:
        odd_sum += digit
    num //= 10

print("Sum of odd digits:", odd_sum)
