'''
38. Find smallest digit in a number.
'''
num = abs(int(input("Enter a number: ")))

if num == 0:
    smallest = 0
else:
    smallest = 9
    while num > 0:
        digit = num % 10
        if digit < smallest:
            smallest = digit
        num //= 10

print("Smallest digit:", smallest)
