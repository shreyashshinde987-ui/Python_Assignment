'''
31. Generate first n odd numbers.
'''
n = int(input("Enter value of n: "))

for i in range(1, n + 1):
    print(2 * i - 1, end=" ")
print()
