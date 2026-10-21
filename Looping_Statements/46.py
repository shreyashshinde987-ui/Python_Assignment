'''
46. Print first n multiples of a number.
'''
num = int(input("Enter a number: "))
n = int(input("Enter how many multiples to print: "))

print("First", n, "multiples of", num, "are:")
for i in range(1, n + 1):
    print(num * i, end=" ")
print()
