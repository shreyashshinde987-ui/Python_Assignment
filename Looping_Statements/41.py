'''
41. Print numbers which are perfect cubes between 1 and 100.
'''
print("Perfect cubes between 1 and 100:")

for num in range(1, 101):
    root = round(num ** (1 / 3))
    if root * root * root == num:
        print(num, end=" ")
print()
