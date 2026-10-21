'''
12. Reverse a number using while loop.
'''
num = int(input("Enter a number: "))

temp = abs(num)
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

if num < 0:
    reverse = -reverse

print("Reversed number:", reverse)
