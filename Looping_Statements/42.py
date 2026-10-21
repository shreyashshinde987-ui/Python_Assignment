'''
42. Calculate sum of squares of first n numbers.
'''
n = int(input("Enter value of n: "))

total = 0

for i in range(1, n + 1):
    total += i ** 2

print("Sum of squares of first", n, "numbers:", total)
