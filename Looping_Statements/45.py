'''
45. Print numbers skipping multiples of 3.
'''
n = int(input("Enter the last number: "))

for i in range(1, n + 1):
    if i % 3 == 0:
        continue
    print(i, end=" ")
print()
