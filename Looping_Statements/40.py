'''
40. Print numbers which are perfect squares between 1 and 100.
'''
print("Perfect squares between 1 and 100:")

for num in range(1, 101):
    root = int(num ** 0.5)
    if root * root == num:
        print(num, end=" ")
print()
