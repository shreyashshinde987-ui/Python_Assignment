'''
11. Count number of digits in a number.
'''
num = abs(int(input("Enter a number: ")))

if num == 0:
    count = 1
else:
    count = 0
    while num > 0:
        count += 1
        num //= 10

print("Number of digits:", count)
