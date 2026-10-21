'''
43. Calculate sum of cubes of first n numbers.
'''
n = int(input("Enter value of n: "))

total = 0

for i in range(1, n + 1):
    total += i ** 3

print("Sum of cubes of first", n, "numbers:", total)
