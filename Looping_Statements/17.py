'''
17. Find largest digit in a number.
'''
num = abs(int(input("Enter a number: ")))

largest = 0

while num > 0:
    digit = num % 10
    if digit > largest:
        largest = digit
    num //= 10

print("Largest digit:", largest)
